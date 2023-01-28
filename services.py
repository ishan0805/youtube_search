import httpx
from constants import get_youtube_url ,YOUTUBE_APP_KEY



async def get_youtube_data():
    async with httpx.AsyncClient() as client:
        url=get_youtube_url(YOUTUBE_APP_KEY)
        resp: httpx.Response = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    results = data['items']
    if results:
        print(results)



    
