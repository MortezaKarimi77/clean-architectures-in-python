from advanced_alchemy.utils.text import slugify as advanced_slugify


def slugify(value: str, allow_unicode: bool = False, separator: str | None = None) -> str:
    return advanced_slugify(value=value, allow_unicode=allow_unicode, separator=separator)
