import json
from http import HTTPStatus
from typing import Dict


class HttpError(Exception):
    def __init__(self, response: Dict, status_code: HTTPStatus):
        self.response = response
        self.status_code = status_code

    def json(self):
        return json.dumps(self.response)
