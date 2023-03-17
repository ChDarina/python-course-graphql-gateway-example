import pytest

from services.news import NewsService
from tests.unit.utils.news import NewsUtils


@pytest.fixture
def utils() -> NewsUtils:
    return NewsUtils()


def test_read_news_for_all(utils: NewsUtils) -> None:
    """
    Тестирование получения новостей
    """
    news = NewsService().get_news()
    assert len(news) == 4
    assert news.keys() == {"ru", "ie", "rs", "us"}
    file_news = utils.get_news_for_all()
    for name in news.keys():
        expected_news = file_news[name]
        actual_news = news[name]
        assert len(actual_news) == len(expected_news)
        for actual, expected in zip(actual_news, expected_news):
            utils.assert_news(actual, expected)
