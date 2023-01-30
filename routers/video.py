from typing import List, Optional
from fastapi import APIRouter, Depends
from database import SessionLocal, get_db
from models.video import Videos
from schemas.video import ShowVideo
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/video",
    tags=['video'],
)

@router.get('/')  # instead of app.get use router.get
async def get(page:int=1,limit:int=10,title:Optional[str]=None,description:Optional[str]=None,db: SessionLocal = Depends(get_db)):
    try:
        start=(page-1)*limit
        end=start+limit

        if title and description:
            count=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.title.contains(title),Videos.description.contains(description)).count()
            data=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.title.contains(title),Videos.description.contains(description))[start:end]
        elif title:
            count=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.title.contains(title)).count()
            data=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.title.contains(title))[start:end]
        elif description:
            count=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.description.contains(description)).count()
            data=db.query(Videos).order_by(Videos.publishedAt.desc()).filter(Videos.description.contains(description))[start:end]
        else:
            count=db.query(Videos).order_by(Videos.publishedAt.desc()).count()
            data=db.query(Videos).order_by(Videos.publishedAt.desc())[start:end]
        
        if data and count:
            return {"count":count, "data":data,"success":True}
        

        return  JSONResponse(status_code=404,content={"success":False,"message":"NO DATA FOUND"})
    except Exception as ex:
        print(ex)
        return  JSONResponse(status_code=400,content={"success":False,"message":str(ex)})
