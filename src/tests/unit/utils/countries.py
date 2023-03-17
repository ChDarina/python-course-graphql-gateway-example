import json

from tests.unit.utils.utils import TestUtils


class CountryUtils:
    fields = [
        "name",
        "alpha2code",
        "alpha3code",
        "capital",
        "region",
        "subregion",
        "population",
        "latitude",
        "longitude",
        "demonym",
        "area",
        "numeric_code",
        "flag",
        "currencies",
        "languages",
    ]

    @staticmethod
    def get_countries() -> list[dict]:
        with open("fixtures/countries.json", encoding="utf-8") as file:
            countries = json.load(file)
        return countries

    def get_country(self, code: str):
        countries = self.get_countries()
        return [
            country
            for country in countries
            if country["alpha2code"].lower() == code.lower()
        ][0]

    def assert_country(self, actual, expected):
        TestUtils.assert_fields(actual, expected, self.fields)
