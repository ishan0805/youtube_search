# RUN IN LOCAL DOCKER:
  ## STEPS
  
- docker build  -t youtube_search .
- docker run -d -p 8000:8000 youtube_search
- check out docs at -> http://localhost:8000/swagger-ui


# RUN IN LOCAL:
  ## STEPS
  
- pip install -r requirments.txt
- python -m uvicorn main:app 
- check out docs at -> http://localhost:8000/swagger-ui
