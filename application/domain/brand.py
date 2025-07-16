from pydantic import Field

from .base import Base


class Brand(Base):
    id: int = Field(ge=1)
    name: str = Field(max_length=20)
    name_en: str = Field(max_length=20)
    slug: str = Field(max_length=20)
    description: str = Field(max_length=5000)
