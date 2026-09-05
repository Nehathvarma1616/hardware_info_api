from fastapi import APIRouter
import psutil

memory_router = APIRouter()

@memory_router.get(
    "/info",
    status_code = 200
)
def memory_utilization():
    memory = psutil.virtual_memory()
    total = (memory.total)/(1024**3)

    return {
        "Total Memory" : f"{total} GB"
    }