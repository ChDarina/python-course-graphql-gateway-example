import json
import os

from tests.unit.utils.utils import TestUtils


class NewsUtils:
    fields = ["author", "source", "title", "description", "url"]
    codes = [
        os.path.splitext(fixture)[0]
        for fixture in os.listdir("fixtures/news/")
        if fixture.endswith(".json")
    ]

    def get_news_for_all(self) -> dict[str, dict]:
        news = {}
        for name in self.codes:
            with open("fixtures/news/" + name + ".json", encoding="utf-8") as file:
                news[name] = json.load(file)["articles"]
        return news

    def get_news_for_one(self, code: str) -> dict:
        return self.get_news_for_all()[code.lower()]

    def assert_news(self, actual, expected):
        TestUtils.assert_fields(actual, expected, self.fields)
