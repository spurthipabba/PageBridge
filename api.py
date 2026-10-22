
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pagebridge.reader import read_website

app = FastAPI(title="PageBridge API")


class ReadRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "Welcome to PageBridge API!"}


@app.post("/read")
def read_page(request: ReadRequest):
    try:
        result = read_website(request.url)

        return {
            "url": result.url,
            "title": result.title,
            "content": result.content,
            "method": result.method
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
