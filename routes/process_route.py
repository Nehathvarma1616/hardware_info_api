from fastapi import APIRouter
import psutil
process_router = APIRouter()

# get method to get system process info
@process_router.get(
        "/info",
        status_code = 200
        )
def get_process_info():
    data = []
    api_sample_data = []
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        data.append(process.info)

    for i in range(3):
        api_sample_data.append(data[i])

    return {
        "process_info": api_sample_data
    }