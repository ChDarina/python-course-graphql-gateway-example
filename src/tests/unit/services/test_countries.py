import pytest

from services.countries import CountriesService
from tests.unit.utils.countries import CountryUtils


@pytest.fixture
def utils() -> CountryUtils:
    return CountryUtils()


def test_read_countries(utils: CountryUtils) -> None:
    """
    Тестирование получения стран
    """
    countries = CountriesService().get_countries()
    file_countries = utils.get_countries()
    assert len(countries) == len(file_countries)
    for actual, expected in zip(countries, file_countries):
        utils.assert_country(actual, expected)
