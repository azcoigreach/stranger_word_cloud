from typing import List, Union
from .. import schemas
from fastapi import APIRouter, HTTPException, Response, status, File, UploadFile, Depends
from fastapi.responses import StreamingResponse, FileResponse
from numpy import array, ndarray, reshape
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, random_color_func, get_single_color_func
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

router = APIRouter(
    prefix="/wordcloud",
    tags=['Word Cloud'],
)

test_text = "Hello World this is the Word Cloud Generator."

@router.put("/", status_code=status.HTTP_201_CREATED , response_model=schemas.WordcloudBase)
async def extended(text: str = test_text,
                    font: Union[bytes, None] = File(default=None),
                    width: int = 400,
                    height: int = 200,
                    prefer_horizontal: float = 0.90,
                    mask: Union[bytes, None] = File(default=None),
                    contour_width: float = 0,
                    contour_color: str = "black",
                    scale: float = 1,
                    min_font_size: int = 4,
                    font_step: int = 1,
                    max_words: int = 200,
                    stopwords: Union[bytes, None] = File(default=None),
                    background_color: str = "black",
                    max_font_size: int = None,
                    mode: str = "RGB",
                    relative_scaling: float = -1,
                    # color_func: str = None,
                    regexp: str = None,
                    collocations: bool = True,
                    colormap: str = "viridis",
                    normalize_plurals: bool = True,
                    repeat: bool = False,
                    include_numbers: bool = False,
                    min_word_length: int = 0,
                    collocation_threshold: int = 30
                    ):

    if relative_scaling == -1:
        relative_scaling = "auto"

    if font is not None:
        font = bytes(font)
        
    if mask is not None:
        mask_img = Image.open(BytesIO(mask))
        mask = array(mask_img)

    if stopwords is not None:
        pass
    else:
        stopwords = STOPWORDS
        

    wordcloud_arr = WordCloud(font_path=font,
                        width=width,
                        height=height,
                        prefer_horizontal=prefer_horizontal,
                        mask=mask,
                        contour_width=contour_width,
                        contour_color=contour_color,
                        scale=scale,
                        min_font_size=min_font_size,
                        font_step=font_step,
                        max_words=max_words,
                        stopwords=stopwords,
                        background_color=background_color,
                        max_font_size=max_font_size,
                        mode=mode,
                        relative_scaling=relative_scaling,
                        # color_func=color_func,
                        regexp=regexp,
                        collocations=collocations,
                        colormap=colormap,
                        normalize_plurals=normalize_plurals,
                        repeat=repeat,
                        include_numbers=include_numbers,
                        min_word_length=min_word_length,
                        collocation_threshold=collocation_threshold
                        ).generate(text).to_array()
                        
    wordcloud_img = Image.fromarray(wordcloud_arr)

    wordcloud_buf = BytesIO()
    wordcloud_img.save(wordcloud_buf, format='PNG')
    wordcloud_buf.seek(0)

    headers = {'Content-Disposition': 'inline; filename="wordcloud.png"'}
    
    return StreamingResponse(wordcloud_buf, headers=headers, media_type='image/png')