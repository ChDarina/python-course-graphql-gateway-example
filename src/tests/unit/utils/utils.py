import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class TestUtils:
    @staticmethod
    def assert_fields(actual, expected, fields) -> None:
        for field in fields:
            assert getattr(actual, field) == expected[field]
