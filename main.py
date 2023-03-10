from fastapi import FastAPI
from database import  engine,Base
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from routers import video
from services import get_youtube_data

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/swagger-ui/', port=8000)

app.include_router(video.router)
# for Cors control
# enable support for ors
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
This function will run at the start of the project , for scapping from the youtube API .
"""
@app.on_event("startup")
@repeat_every(seconds=30,wait_first=True)
async def start():
    await get_youtube_data()

if __name__ == "__main__":
    
    uvicorn.run(app, host="localhost", port=8000)
