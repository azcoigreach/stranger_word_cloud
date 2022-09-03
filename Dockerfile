FROM python:3.10.5

WORKDIR /usr/src/app

COPY ./* ./

COPY ./wordcloud/* ./wordcloud/

COPY ./api/* ./api/

RUN pip install --no-cache-dir -r requirements.txt -r requirements-api.txt

RUN python setup.py build_ext --inplace

RUN pip install . --no-cache-dir

CMD ["uvicorn", " api.main.:api", "--host", "0.0.0.0", "--port", "8000"]