from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NewsModel(BaseModel):
    """
    Модель для описания новостей.
    """

    id: Optional[int] = Field(title="Идентификатор")
    title: str = Field(title="Название")
    author: Optional[str] = Field(title="Автор")
    description: Optional[str] = Field(title="Описание")
    url: Optional[str] = Field(title="Ссылка")
    image_url: Optional[str] = Field(title="Ссылка на изображение")
    source: Optional[str] = Field(title="Источник")
    published_at: datetime = Field(title="Дата публикации")
    content: Optional[str] = Field(title="Содержание новости")
