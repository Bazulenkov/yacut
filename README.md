# YaCut

YaCut — This is the reference shortening service (associate a long user link with the short, which the user himself offers or provides the service). 2 interfaces are available: web, api.

### How to start the project on a local machine:

Clone the repository and enter into directory:
```
git clone 
cd yacut
```

Create and activate virtual environment:
```
python3 -m venv venv
```

* On Linux/macOS:
    ```
    source venv/bin/activate
    ```

* On Windows:
    ```
    source venv/scripts/activate
    ```

Install requirements from requirements.txt:
```
pip install -r requirements.txt
```

Create `.env` and fill it like in `.env.example`

Apply migrations to the DB of the project:
```
flask db upgrade
```

Run the project:
```
flask run
```
