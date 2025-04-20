from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Молоко")

class CategoryBase(BaseModel):
    id: int = Field(None, gt=0, example=1)
    name: str = Field(..., max_length=255, example='Еда')
    description: str = Field(None, max_length=255, example='То что можно скушать')

class BaseGame(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Mайнкрафт")
    description: str = Field(example="Веселая песочница") 
    rating: int = Field(example= 10)

