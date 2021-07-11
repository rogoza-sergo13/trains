from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from copy import copy
from fastapi.templating import Jinja2Templates
from parsing import get_trains
from microblog.models import TableTrain, TableFavoriteTrains
from core.database import SessionLocal
from pydantic import BaseModel


class TrainFavouriteRequest(BaseModel):
    train_id: int


session = SessionLocal()
app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

all_trains = {}


@app.get("/items/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})


@app.post("/mark-favourite/", response_class=HTMLResponse)
async def favorites_train(request: Request, train_id: int = Form(...)):
    global all_trains
    best_train = copy(all_trains[train_id])
    del best_train['id']
    session.add(TableFavoriteTrains(**best_train))
    session.commit()
    return templates.TemplateResponse("mark-favourite.html", {"request": request, 'best_train': best_train})


@app.get("/trains/", response_class=HTMLResponse)
async def read_train(request: Request, start_station: str, finish_station: str, date: str):
    global all_trains
    trains = get_trains(start_station, finish_station, date)
    for idx, train in enumerate(trains):
        train['id'] = idx
        all_trains[idx] = train
    ed_user = TableTrain(start_station=start_station, finish_station=finish_station, date=date)
    session.add(ed_user)
    session.commit()
    return templates.TemplateResponse("trains.html", {"request": request, "trains": trains})
