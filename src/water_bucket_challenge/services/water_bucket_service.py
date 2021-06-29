import typing
from exceptions import HttpError
from http import HTTPStatus


class WaterBucketService:
    """ Service for Water Bucket Challenge """

    @classmethod
    def run_water_bucket_challenge(cls, x_gallon: int, y_gallon: int, target: int):
        try:
            min_path = cls._get_min_path(x_gallon, y_gallon, target)
        except ValueError:
            raise HttpError(
                response={'detail': 'Not Solvable'},
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY
            )
        return min_path

    @classmethod
    def _get_min_path(cls, x_gallon: int, y_gallon: int, target: int) -> typing.List[typing.Tuple[int, int]]:
        """ get minimal path class method """
        if y_gallon > x_gallon:
            temp = y_gallon
            y_gallon = x_gallon
            x_gallon = temp

        if target % (cls._get_greatest_common_divisor(x_gallon, y_gallon)) != 0:
            raise ValueError('No solution')

        results = {}
        for case in ((x_gallon, y_gallon), (y_gallon, x_gallon)):
            key, path = cls._pour(case[0], case[1], target)
            results[key] = path

        return results[min(results)]

    @classmethod
    def _get_greatest_common_divisor(cls, a: int, b: int):
        if b == 0:
            return a
        return cls._get_greatest_common_divisor(b, a % b)

    @staticmethod
    def _pour(from_: int, to: int, target: int):
        from_gallon = from_
        to_gallon = 0

        step = 1
        path = []

        while (from_gallon is not target) and (to_gallon is not target):

            path.append((from_gallon, to_gallon))

            temp = min(from_gallon, to - to_gallon)

            to_gallon = to_gallon + temp
            from_gallon = from_gallon - temp

            path.append((from_gallon, to_gallon))

            step = step + 1
            if (from_gallon == target) or (to_gallon == target):
                break

            # If first gallon becomes empty, fill it
            if from_gallon == 0:
                from_gallon = from_
                step = step + 1

            # If second gallon becomes full, empty it
            if to_gallon == to:
                to_gallon = 0
                step = step + 1

        return step, path
