from application.domain import Brand
from application.utils import slugify


def test_brand_model_init() -> None:
    brand_id: int = 1
    name: str = "دیجی کالا"
    name_en: str = "digi kala"
    slug: str = slugify(name_en)
    description: str = "digikala description"

    brand: Brand = Brand(
        id=brand_id,
        name=name,
        name_en=name_en,
        slug=slug,
        description=description,
    )

    assert brand.id == brand_id
    assert brand.name == name
    assert brand.name_en == name_en
    assert brand.slug == slug
    assert brand.description == description


def test_brand_model_init_defaults() -> None:
    brand_id: int = 1
    name: str = "دیجی کالا"
    name_en: str = "digi kala"
    slug: str = slugify(name_en)
    description: str = "digikala description"

    brand: Brand = Brand(
        id=brand_id,
        name=name,
        name_en=name_en,
        description=description,
    )

    assert brand.id == brand_id
    assert brand.name == name
    assert brand.name_en == name_en
    assert brand.slug == slug
    assert brand.description == description
