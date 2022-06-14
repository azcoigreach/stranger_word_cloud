from typing import Optional, Union
from pydantic import BaseModel, Field, EmailStr, conint
from datetime import datetime

class WordcloudBase(BaseModel):
    text: str = Field(example="Hello World this is the Word Cloud Generator.")
    width: int
    height: int
    prefer_horizontal: float
    contour_width: float
    contour_color: str
    scale: float
    min_font_size: int
    font_step: int
    max_words: int
    stopwords: str
    background_color: str
    max_font_size: Union[int, None]
    mode: str
    relative_scaling: float
    color_func: str
    regexp: str
    collocations: bool
    colormap: str
    normalize_plurals: bool
    repeat: bool
    include_numbers: bool
    min_word_length: int
    collocation_threshold: int


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)