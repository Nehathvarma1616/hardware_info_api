from fastapi import FastAPI # type: ignore
from routes.process_route import process_router
app = FastAPI()

# route to get info about process id's
app.include_router(process_router, prefix="/process")

@app.get("/")
def home(status_code = 200):
    return {
        "message" : "This is HomePage API"
    }