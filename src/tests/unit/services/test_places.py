import pytest

from services.places import PlacesService
from tests.unit.utils.places import PlacesUtils


@pytest.fixture
def utils() -> PlacesUtils:
    return PlacesUtils()


def test_read_places(utils: PlacesUtils) -> None:
    """
    Тестирование получения всех мест
    """
    places = PlacesService().get_places()
    file_places = utils.get_places()
    assert len(places) == len(file_places)
    for actual, expected in zip(places, file_places):
        utils.assert_place(actual, expected)


def test_read_place(utils: PlacesUtils) -> None:
    """
    Тестирование получения одного места
    """
    actual = PlacesService().get_place(1)
    expected = utils.get_place(1)
    utils.assert_place(actual, expected)
