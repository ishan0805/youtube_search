from datetime import datetime
from pydantic import BaseModel


class ShowThumbnail(BaseModel):
    default_url= str
    default_width=int
    default_height=int

    class Config:
        orm_mode = True



class ShowVideo(BaseModel):
    etag= str
    title = str
    description = str
    publishTime = datetime
    thumbnail = ShowThumbnail




    
class Thumbnail(ShowThumbnail):
    id =int
    class Config:
        orm_mode = True

class Video(ShowVideo):
    id = str
    thumbnail =Thumbnail
    class Config:
        orm_mode = True

   

  


