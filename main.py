from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
templates = Jinja2Templates(directory="templates")
Base = declarative_base()

engine = create_engine('sqlite:///./emails.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255), unique=True, index=True)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
def save_email(request: Request, email: str = Form(...)):
    db_email = Email(address=email)
    session.add(db_email)
    session.commit()
    return templates.TemplateResponse("index.html", {"request": request, "message": "Email saved successfully."})
