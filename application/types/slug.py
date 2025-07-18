from typing import Annotated

from pydantic import AfterValidator

from application.utils import slugify

Slug = Annotated[str, AfterValidator(lambda value: slugify(value=value))]
