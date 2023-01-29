import httpx
from constants import get_youtube_url ,YOUTUBE_APP_KEY
from database import get_db
from models.video import Thumbnails, Videos
from datetime import datetime

async def get_youtube_data():
    async with httpx.AsyncClient() as client:
        url=get_youtube_url(YOUTUBE_APP_KEY)
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()
        
        data = resp.json()
        
        
    db=next(get_db())
    results = data['items']
    if results:
        for data in results:
            have_data=db.query(Videos).filter(Videos.etag==data["etag"]).first()
            if have_data==None:
                save_thumbnail={}
                save_thumbnail["default_url"]=data["snippet"]["thumbnails"]["default"]["url"]
                save_thumbnail["default_width"]=data["snippet"]["thumbnails"]["default"]["width"]
                save_thumbnail["default_height"]=data["snippet"]["thumbnails"]["default"]["height"]

                thumbnail=Thumbnails(**save_thumbnail)
                db.add(thumbnail)
                db.commit()
                save_video={}
                save_video["id"]=data["id"]["kind"]+data["id"]["videoId"]
                save_video["etag"]=data["etag"]
                save_video["title"]=data["snippet"]["title"]
                save_video["description"]=data["snippet"]["description"]
                save_video["publishedAt"]=data["snippet"]["publishedAt"][:-1]
                save_video["thumbnail_id"]=thumbnail.id
                date_format="%Y-%m-%dT%H:%M:%S"
                save_video["publishedAt"]=datetime.strptime(save_video["publishedAt"],date_format)
                video=Videos(**save_video)
                db.add(video)

                db.commit()






    
