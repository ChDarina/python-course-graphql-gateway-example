import pytest

from dataloaders import CountryLoader
from tests.unit.utils.countries import CountryUtils


@pytest.fixture
def loader() -> CountryLoader:
    return CountryLoader()


@pytest.fixture
def utils() -> CountryUtils:
    return CountryUtils()


def test_load_country(utils: CountryUtils, loader: CountryLoader) -> None:
    actual = loader.load("RU").get()
    expected = utils.get_country("RU")
    utils.assert_country(actual, expected)


def test_load_countries(utils: CountryUtils, loader: CountryLoader) -> None:
    actual_countries = loader.load_many(["IE", "RU", "RS", "US"]).get()
    expected_countries = utils.get_countries()
    assert len(actual_countries) == len(expected_countries)
    for actual, expected in zip(actual_countries, expected_countries):
        utils.assert_country(actual, expected)
