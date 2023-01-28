from fastapi import FastAPI
from database import  engine,Base
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/swagger-ui/', port=8000)

#app.include_router(.router)
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


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)