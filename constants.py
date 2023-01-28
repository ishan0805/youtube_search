YOUTUBE_APP_KEY="AIzaSyDBgLGXJIdUUwoU1E9fXlAOn68z_6yNBBo"

YOUTUBE_URL=f"https://youtube.googleapis.com/youtube/v3/search?part=id,snippet&maxResults=25&order=date&q=krishna&type=video&key="

def get_youtube_url(appKey:str):
    url=f"{YOUTUBE_URL}{appKey}"
    return url
