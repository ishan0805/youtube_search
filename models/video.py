from sqlalchemy import Column, ForeignKey, Integer,String,DateTime
from sqlalchemy.orm import relationship

from database import Base

class Thumbnails(Base):
    __tablename__ = "thumbnails"

    id = Column(Integer, primary_key=True, index=True)
    default_url=Column(String)
    default_width=Column(Integer)
    default_height=Column(Integer)


class Videos(Base):
    __tablename__ = "video"

    id = Column(String, primary_key=True)
    etag= Column(String)
    title = Column(String)
    description = Column(String)
    publishedAt = Column(DateTime)
    thumbnail_id=Column(Integer, ForeignKey("thumbnails.id",ondelete="CASCADE"))
    thumbnail = relationship("Thumbnails")


    

   
    