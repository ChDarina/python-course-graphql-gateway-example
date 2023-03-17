import json
from typing import Optional

from models.places import PlaceModel


class PlacesService:
    """
    Сервис для работы с данными о любимых местах.
    """

    def get_places(self) -> list[PlaceModel]:
        """
        Получение списка любимых мест.

        :return:
        """

        result = []
        with open("fixtures/places.json", encoding="utf-8") as file:
            if data := json.load(file):
                result = [self.build_model(place) for place in data.get("data", [])]

        return result

    def get_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Получение любимого места по идентификатору.
        param place_id: Идентификатор любимого места.

        :return:
        """

        with open("fixtures/places.json", encoding="utf-8") as file:
            if data := json.load(file):
                result = [
                    self.build_model(place)
                    for place in data.get("data", [])
                    if place["id"] == place_id
                ]
                if len(result) > 0:
                    return result[0]
                return None

        return None

    @staticmethod
    def build_model(place: dict) -> PlaceModel:
        """
        Создание модели любимого места по даным.
        param place: данные о любимом месте.

        :return:
        """

        return PlaceModel(
            id=place.get("id"),
            latitude=place.get("latitude"),
            longitude=place.get("longitude"),
            description=place.get("description"),
            country=place.get("country"),
            city=place.get("city"),
            locality=place.get("locality"),
            created_at=place.get("created_at"),
            updated_at=place.get("updated_at"),
        )
