import json

from tests.unit.utils.utils import TestUtils


class PlacesUtils:
    fields = [
        "id",
        "city",
        "country",
        "latitude",
        "longitude",
        "locality",
        "description",
    ]

    @staticmethod
    def get_places() -> list[dict]:
        with open("fixtures/places.json", encoding="utf-8") as file:
            places = json.load(file)["data"]
        return places

    def get_place(self, place_id: int) -> dict:
        places = self.get_places()
        return [place for place in places if place["id"] == place_id][0]

    def assert_place(self, actual, expected):
        TestUtils.assert_fields(actual, expected, self.fields)
