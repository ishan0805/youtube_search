from datetime import datetime
YOUTUBE_APP_KEY=["AIzaSyDBgLGXJIdUUwoU1E9fXlAOn68z_6yNBBo","AIzaSyCguFwuJpkcTH3CoSmsB-rzqU9Ftwlq81g",]

YOUTUBE_URL=f"https://youtube.googleapis.com/youtube/v3/search?part=id,snippet&maxResults=25&order=date&q=krishna&type=video"

def get_youtube_url(appKey:str):
    time=datetime.now()
    time=time.isoformat('T')+"Z"
    url=f"{YOUTUBE_URL}&publishedAfter={time}&key={appKey}"
    return url
