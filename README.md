start the services using `pipenv`:

```
pipenv run python3 ./src/water_bucket_challenge/main.py
```

# Contribution

Clone repository and create environment with pipenv:

```
python -m pip install --upgrade pipenv wheel
pipenv install --deploy --dev
```

# UI

For the visual presentation of the interface was chosen swagger UI which presented on /apidocs path

# Tests

For running tests use command:
 
```
PYTHONPATH=src/water_bucket_challenge/ pytest 
```
