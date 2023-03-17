import json
import os

from models.news import NewsModel


class NewsService:
    """
    Сервис для работы с данными о новостях.
    """

    def get_news(self) -> dict[str, list[NewsModel]]:
        """
        Получение списка новостей.
        :return:
        """

        base_directory = "fixtures/news/"
        fixtures = os.listdir(base_directory)
        json_news = [fixture for fixture in fixtures if fixture.endswith(".json")]
        mapped_news = {}
        for file in json_news:
            country_code = file.split(".")[0]
            with open(base_directory + file, encoding="utf-8") as news_file:
                if data := json.load(news_file):
                    mapped_news[country_code] = [
                        self.build_model(news) for news in data.get("articles", [])
                    ]
        return mapped_news

    @staticmethod
    def build_model(news: dict) -> NewsModel:
        """
        Создание модели новости по входным данным.

        :param: news: Данные о новости.

        :return:
        """
        return NewsModel(
            id=news.get("id"),
            title=news.get("title"),
            author=news.get("author"),
            description=news.get("description"),
            url=news.get("url"),
            image_url=news.get("urlToImage"),
            source=news.get("source"),
            content=news.get("content"),
            published_at=news.get("publishedAt"),
        )
