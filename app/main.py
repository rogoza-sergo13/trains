from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from parsing import train
from microblog.models import TableTrain
from core.database import SessionLocal


session = SessionLocal()
app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/items/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.get("/trains/", response_class=HTMLResponse)
async def read_train(request: Request, start_station: str, finish_station: str, date: str):
    trains = train(start_station, finish_station, date)
    ed_user = TableTrain(start_station=start_station, finish_station=finish_station, date=date)
    session.add(ed_user)
    session.commit()
    return templates.TemplateResponse("trains.html", {"request": request, "trains": trains})
