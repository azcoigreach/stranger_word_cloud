wordcloud-api
=============
A FastAPI implentation of [amueller/wordcloud][forked_from]

## Build and Install
Build cython
```
python setup.py build_ext --inplace
```
Install wordcloud
```
pip install . --use-feature=in-tree-build --no-cache-dir -r requirements.txt
```
Install FastAPI
```
pip install --no-cache-dir -r requirements-api.txt
```
Run FastAPI
```
uvicorn api.main:app --host 0.0.0.0 --port 8080 --reload
```


[forked_from] https://github.com/amueller/word_cloud