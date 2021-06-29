import functools
from http import HTTPStatus
from typing import Callable, Optional, Type

from flask import Response, json, request
from pydantic import ValidationError
from pydantic.main import BaseModel

from exceptions import HttpError


def validate_request(
        request_validator: Optional[Type[BaseModel]] = None,
        query_model: Optional[Type[BaseModel]] = None,
):
    def validate(f) -> Callable:
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs) -> Response:
            status_code = HTTPStatus.OK
            body = None
            validated_query = None
            validated_data = None
            copy_kwargs = kwargs.copy()

            try:
                if request_validator:
                    validated_data = request_validator(**request.get_json())  # type: ignore

                if query_model:
                    validated_query = query_model(**request.args)

                copy_kwargs["validated_data"] = validated_data
                copy_kwargs["validated_query"] = validated_query

                body = f(self, *args, **copy_kwargs)

            except ValidationError as exc:
                body = exc.errors()
                status_code = HTTPStatus.BAD_REQUEST
            except HttpError as exc:
                body = exc.response
                status_code = exc.status_code

            if isinstance(body, BaseModel):
                response = body.json()
            else:
                response = json.dumps(body)

            return Response(
                response=response,
                status=status_code,
                content_type="application/json"
            )

        return wrapper

    return validate
