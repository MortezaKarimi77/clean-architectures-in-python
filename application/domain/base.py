from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        str_strip_whitespace=True,
    )
