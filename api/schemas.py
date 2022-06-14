from typing import Optional, Union
from pydantic import BaseModel, Field, EmailStr, conint
from datetime import datetime

class WordcloudBase(BaseModel):
    text: str = Field(example="Hello World this is the Word Cloud Generator.")
    # font = bytes
    width: int
    height: int
    prefer_horizontal: float
    # mask: bytes
    contour_width: float
    contour_color: str
    scale: float
    min_font_size: int
    font_step: int
    max_words: int
    # stopwords: Optional[str]
    background_color: str
    max_font_size: Optional[int]
    mode: str
    relative_scaling: float = Field(description="Vaule = 0-1 or -1 for auto")
    color_func: Optional[str]
    regexp: Optional[str]
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