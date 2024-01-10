import json
from typing import Any, Dict, List, Union

from app.db import get_db, client
from app.models import PDUData
from app.schema import DataParse
from datetime import datetime
from sqlalchemy.orm import Session

from fastapi import Depends, FastAPI, HTTPException, status


app = FastAPI()


@app.post("/smpp/interception/mt", status_code=status.HTTP_201_CREATED)
def post_data(
    data: list[DataParse],
    session: Session = Depends(get_db),
):
    # service_type = str(model.service_type)
    # model.service_type = service_type
    try:
        for datas in data:
            models = PDUData(**datas.model_dump())
            session.add(models)
        session.commit()
        session.refresh(models)
        data_dict_list = [item.dict() for item in data]

        def datetime_handler(x):
            if isinstance(x, datetime):
                return x.isoformat()

        client.set("redis data", json.dumps(data_dict_list, default=datetime_handler))
        return models
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@app.get("/smpp/interception/mts")
def get_datas():
    cached = client.get("redis data")
    if cached is not None:
        data = cached.decode("utf-8")
        data_cached = json.loads(data)
        return {
            "message": "data fetched successfully from redis!!!",
            "data": data_cached,
        }


@app.get("/smpp/getdata/db")
def get_data_db(
    session: Session = Depends(get_db),
):
    db = session.query(PDUData).all()
    return db
