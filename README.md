## FastAPI Email Saver
This is a simple FastAPI app that presents a single page web app to take an email address and save it to a SQLite database.

Installation
To install the necessary dependencies, run the following command:

```
pip install fastapi uvicorn sqlalchemy
```

To start the app, run the following command:

```
uvicorn main:app --reload
```
This will start the app on http://localhost:8000. If you open this URL in a web browser, you should see a page with a form for entering an email address. When you submit the form, the email will be saved to the SQLite database.

