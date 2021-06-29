import schemas

schema = {
    "definitions": {
        "WaterBucketInputSchema": schemas.WaterBucketInputSchema.schema(),
        "WaterBucketResultListSchema": schemas.WaterBucketResultListSchema.schema(),
        "WaterBucketState": schemas.WaterBucketState.schema(),
    },
    "info": {
        "description": "powered by Flasgger",
        "termsOfService": "/tos",
        "title": "A swagger API",
        "version": "0.0.1",
    },
    "paths": {
        "/water-bucket": {
            "post": {
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/WaterBucketInputSchema"
                        },
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/WaterBucketResultListSchema"
                        }
                    },
                    "400": {"description": "Bad Request"},
                    "422": {"description": "Unprocessable Entity"}
                },
            }
        },
    },
    "swagger": "2.0",
}
