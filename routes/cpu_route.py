from fastapi import APIRouter
import psutil
cpu_router = APIRouter()

@cpu_router.get(
        "/info",
        status_code = 200
    )
def cpu_utilization():
    count = psutil.cpu_count(logical = True)
    individual_percentage = psutil.cpu_percent(percpu = True)
    stats = psutil.cpu_stats()

    return {
        "message" : "cpu-utilization api",
        "Total Logical CPU's" : count,
        "individual cpu utilization" : individual_percentage,
        "CPU Stats" : [stats.ctx_switches, stats.interrupts, stats.soft_interrupts, stats.syscalls], 
        "CPU stats" : [ {
            "context_switches" : stats.ctx_switches
        },
        {
            "cpu interrupts" : stats.interrupts
        } ]
    }