from typing import Optional

from pydantic import BaseModel, Field


class SourceModel(BaseModel):
    """
    Модель для описания источника новостей.
    """

    id: Optional[str] = Field(title="Идентификатор источника")
    name: Optional[str] = Field(title="Наименование источника")
