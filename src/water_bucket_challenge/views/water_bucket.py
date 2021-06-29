from flask.app import Flask
from flask.views import MethodView

from app import application
from schemas import WaterBucketInputSchema, WaterBucketResultListSchema
from services import WaterBucketService
from utils import validate_request

__all__ = [
    'WaterBucketView'
]


class WaterBucketView(MethodView):
    def __init__(self, app: Flask = application) -> None:
        self.app = app

    @validate_request(request_validator=WaterBucketInputSchema)
    def post(self, validated_data: WaterBucketInputSchema, *args, **kwargs) -> dict:
        x_gallon = validated_data.x_gallon
        y_gallon = validated_data.y_gallon
        target = validated_data.target

        result = WaterBucketService.run_water_bucket_challenge(x_gallon, y_gallon, target)

        data = WaterBucketResultListSchema.parse_obj(result)

        return data.dict()['__root__']
