from fastapi import FastAPI, Query, HTTPException, Response
import requests
from io import BytesIO
from PIL import Image

app = FastAPI()

API_KEY = "ch9ayfa"  # غير المفتاح ديالك هنا

@app.get("/banner-image")
def get_banner(uid: str = Query(...), region: str = Query(...), key: str = Query(None)):
    if key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API key")

    url = f"https://aditya-banner-v5op.onrender.com/banner-image?uid={uid}&region={region}"

    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200 or not res.headers.get("content-type", "").startswith("image"):
            raise HTTPException(status_code=400, detail="Image not found or invalid response")

        # فقط نردها كما هي بلا تعديل
        return Response(content=res.content, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
