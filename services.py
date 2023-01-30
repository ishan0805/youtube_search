import httpx
from constants import get_youtube_url ,YOUTUBE_APP_KEY
from database import get_db
from models.api_key import ApiKey
from models.video import Thumbnails, Videos
from datetime import datetime

async def get_youtube_data():
    async with httpx.AsyncClient() as client:
        api_key=get_active_apikey()
        url=get_youtube_url(api_key)
        resp: httpx.Response = await client.get(url)
        data = resp.json()
        if resp.status_code==200:
            add_to_db(data)
        elif resp.status_code==403:
     
            if "error" in data:
                for error in data['error']['errors']:
                    if error['reason']=='quotaExceeded':
                        deactivate_apikey(api_key)
                        

        
        

def add_to_db(data):
    try:
        db=next(get_db())
        results = data['items']
        if results:
            for data in results:
                have_data=db.query(Videos).filter(Videos.etag==data["etag"]).first()
                if have_data==None:
                    if "snippet" in  data:
                        thumbnail=None
                        if "thumbnails" in data["snippet"]:
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
                        save_video["thumbnail_id"]=thumbnail.id if thumbnail !=None else None
                        date_format="%Y-%m-%dT%H:%M:%S"
                        save_video["publishedAt"]=datetime.strptime(save_video["publishedAt"],date_format)
                        video=Videos(**save_video)
                        db.add(video)

                        db.commit()
    except Exception as ex:
        print(ex)




def get_active_apikey():
    try:
        db=next(get_db())
        data=db.query(ApiKey).filter(ApiKey.active==True).first()
        if data:
            return data.api_key
        time=datetime.now()
        modified_date = time.replace(day=time.day-1)
   

        data=db.query(ApiKey).filter(ApiKey.active==False,ApiKey.create_time<=modified_date).first()
        if data:
            return data.api_key
        
        for key in YOUTUBE_APP_KEY:
            data=db.query(ApiKey).filter(ApiKey.api_key==key).first()
            if not data:
                to_save={}
                to_save["api_key"]=key
                to_save["create_time"]=datetime.now()
                to_save["active"]=True
                db.add(ApiKey(**to_save))
                db.commit()
    except Exception as ex:
        print(ex)


    
def deactivate_apikey(key):
    try:
        db=next(get_db())
        data=db.query(ApiKey).filter(ApiKey.api_key==key).first()
        if data!=None:
            data.active=False
            data.create_time=datetime.now()
            db.commit()
    except Exception as ex:
        print(ex)