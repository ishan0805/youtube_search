from typing import List, Optional
from fastapi import APIRouter, Depends
from database import SessionLocal, get_db
from models.video import Videos
from schemas.video import ShowVideo

router = APIRouter(
    prefix="/video",
    tags=['video'],
)

@router.get('/')  # instead of app.get use router.get
async def get(page:int=1,limit:int=10,title:Optional[str]=None,description:Optional[str]=None,db: SessionLocal = Depends(get_db)):

    if title and description:
        data=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.title.contains(title),Videos.description.contains(description)).all()
    elif title:
        data=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.title.contains(title)).all()
    elif description:
        data=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.description.contains(description)).all()
    else:
        data=db.query(Videos).order_by(Videos.publishedAt.desc()).all()
    
    if data:
        count=len(data)
        return {"count":count, "data":data,"success":True}

    return {"success":False}