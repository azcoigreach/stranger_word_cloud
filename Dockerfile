FROM python:3.10.4

WORKDIR /usr/src/app

COPY ./* ./

RUN pip install --no-cache-dir -r requirements.txt -r requirements-api.txt

COPY ./wordcloud/* ./wordcloud/

RUN python setup.py build_ext --inplace

RUN pip install wordcloud

COPY ./api/* ./api/

CMD ["uvicorn", " api.main.:api", "--host", "0.0.0.0", "--port", "8000"]