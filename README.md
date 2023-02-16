# fastAPI-chatGPT-experiment
This app was created using the ChatGPT prompt: `show me the code for a fastAPI app which presents a single page web app to take an email and save it to a sqlite database` and also `Write a README markdown file for this code`. The only correction required was the additon of `python-multipart` and `jinja2` in the requirements. Pretty impressive! I also did the initial test using a Github Codespace without issue.

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

## Local Development
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- uvicorn main:app --reload