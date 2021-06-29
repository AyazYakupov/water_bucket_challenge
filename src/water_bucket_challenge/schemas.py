from typing import List, Tuple

from pydantic import BaseModel


class WaterBucketInputSchema(BaseModel):
    x_gallon: int
    y_gallon: int
    target: int


class WaterBucketState(BaseModel):
    __root__: Tuple[int, int]


class WaterBucketResultListSchema(BaseModel):
    __root__: List[WaterBucketState]
