from pydantic import BaseModel, Field

class CreateProduct(BaseModel):
    name: str = Field(min_length=3,max_length=255)
    
    
class CreateGame(BaseModel):
    name: str = Field(min_length=3,max_length=255)
    description: str = Field(min_length=3,max_length=255)
    rating: int = Field(min_length=3,max_length=10)