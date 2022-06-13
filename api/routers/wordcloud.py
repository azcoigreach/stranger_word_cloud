from typing import List
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from numpy import array, reshape
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, random_color_func, get_single_color_func
import matplotlib.pyplot as plt

# from io import BytesIO

router = APIRouter(
    prefix="/wordcloud",
    tags=['Word Cloud'],
)

test_text = "Hello World this is the Word Cloud Generator."

@router.put("/")
async def extended(text: str = test_text,
                    width: int = 500,
                    height: int = 500,
                    prefer_horizontal: float = 0.90,
                    contour_width: float = 0,
                    contour_color: str = "black",
                    scale: float = 1,
                    min_font_size: int = 4,
                    font_step: int = 1,
                    max_words: int = 200,
                    stopwords: str = None,
                    background_color: str = "#00000000",
                    max_font_size: int = None,
                    mode: str = "RGBA",
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

    # if mask is not None:
    #     mask = reshape(array(mask))
    #     width = None
    #     height = None
        

    wordcloud: bytes = WordCloud(width=width,
                        height=height,
                        prefer_horizontal=prefer_horizontal,
                        # mask=mask,
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
                        ).generate(text).to_file("wordcloud.png")
                        
    # wordcloud_file = "wordcloud.png"

    return FileResponse("wordcloud.png")