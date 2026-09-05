from fastapi import FastAPI # type: ignore
from routes.process_route import process_router
from routes.cpu_route import cpu_router
from routes.memory_route import memory_router
app = FastAPI()

# route to get info about process id's
app.include_router(process_router, prefix="/process")
app.include_router(cpu_router, prefix="/cpu")
app.include_router(memory_router, prefix="/memory")
@app.get(
        "/",
        status_code = 200
    )
def home():
    return {
        "message" : "This is HomePage API"
    }