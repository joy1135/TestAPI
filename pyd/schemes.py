from .base_models import *
from typing import List

class CategorySchema(CategoryBase):
    products: List[BaseProduct]


class ProductSchema(BaseProduct):
    categories: List[CategoryBase]