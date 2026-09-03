import psutil # type: ignore
import json
# cpu

# print(psutil.cpu_percent())
# print(psutil.cpu_percent(percpu=True))
# print(psutil.cpu_count())
# print(psutil.cpu_freq())
# print(psutil.cpu_stats())
# print(psutil.cpu_times())
# print(psutil.cpu_times_percent())

# memory

# memory = psutil.virtual_memory()
# print(psutil.virtual_memory().total)

# need to learn about swap_memory()

# swap = psutil.swap_memory()
# print(swap)

# disk usage

# print(psutil.disk_usage("/"))
# print(psutil.disk_io_counters())

# network

# print(psutil.net_io_counters())

# process
# lets put this info in text file

# with open("info.txt", "w", encoding="utf-8") as file:
#     for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
#         file.writelines(f"{process.info}\n")

# writing same info into json

with open("info.json", "w", encoding="utf-8") as file:
    data = []
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        data.append(process.info)

    json.dump(data,file,indent=4)