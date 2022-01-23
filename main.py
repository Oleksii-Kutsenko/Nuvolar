from fastapi import FastAPI

application = FastAPI()


@application.get("/")
async def root():
    return {"name": "Fleet API 0.0.1"}
