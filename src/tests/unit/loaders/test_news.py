import pytest

from dataloaders import NewsLoader
from tests.unit.utils.news import NewsUtils


@pytest.fixture
def loader():
    return NewsLoader()


@pytest.fixture
def utils():
    return NewsUtils()


def test_load_news_for_one(loader: NewsLoader, utils: NewsUtils) -> None:
    actual_news = loader.load("RU").get()
    expected_news = utils.get_news_for_one("RU")
    assert len(actual_news) == len(expected_news)
    for actual, expected in zip(actual_news, expected_news):
        utils.assert_news(actual, expected)


def test_load_news_for_all(loader: NewsLoader, utils: NewsUtils) -> None:
    country_keys = ["IE", "RS", "RU", "US"]
    actual_news = loader.load_many(country_keys).get()
    expected_news = utils.get_news_for_all()
    assert len(actual_news) == len(expected_news.keys())
    for i, key in enumerate(country_keys):
        actual_collection = actual_news[i]
        expected_collection = expected_news[key.lower()]
        for actual, expected in zip(actual_collection, expected_collection):
            utils.assert_news(actual, expected)
