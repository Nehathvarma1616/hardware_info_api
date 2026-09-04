import psutil # type: ignore
import json




# cpu

# print(psutil.cpu_percent())
# print(psutil.cpu_percent(percpu=True))

# cpu_count() give how many logical cpu's in a machine
# Hyper_Threading(intel) and SMT(AMD) allows a single core to act as 2 logical cpu's virtually
# if we do explicit logical as False we get actually physical cores
# print(psutil.cpu_count(logical= False)) 

# psutil.cpu_percent(interval=5)
# we can also do explicit things it wil calculate over next 5 seconds

# print(psutil.cpu_freq())
# What does frequency actually mean?
# Frequency is basically:
# How fast the CPU's clock is currently operating.
    # cpu_freq() output: scpufreq(
    # current=3192.0, here 3192 MHz ~ /1000 ~ 3.192 GHz
    # min=400.0, 400 MHz ~ 0.4 GHz
    # max=4200.0 4200 MHz ~ 4.2 GHz
    #)
    

# print(psutil.cpu_stats())
    # output something like this
        # scpustats(
        #     ctx_switches=123456789, context switch = CPU changes from one task to another , the number is since boot
        #     interrupts=9876543, through hardware or system -> signals the CPU that something needs attention,
        #                                                       a cumulative count, not "interrupts per second."
        #     soft_interrupts=3456789, These are software-generated interrupts/events handled by the OS.
        #     syscalls=456789 A system call happens when a user-space program 
        #                     asks the operating system kernel to perform some privileged operation.
        # )


# print(psutil.cpu_times())
# print(psutil.cpu_times(percpu = True)) 
# psutil.cpu_percent(percpu=True) # gives 
# times is strictly in seconds cummulative count
    # output look something like this
    #     scputimes(
    #       user=12543.2, Time spent running normal programs in user-space (like your web browser, Python scripts, or games, basically all applications)  
    #       system=4521.7, Time spent executing kernel-level operations (like handling hardware requests, system drivers, or allocating memory).
    #       idle=98765.4 CPUs have collectively spent approximately 98,765.4 seconds idle.
    # )

# print(psutil.cpu_times_percent()) # just percentage version of cpu_times()





# memory, RAM

# for reference 
    # 1 Byte = 8 bits
    # 1 Kilobyte (KB) = 1,024 Bytes
    # 1 Megabyte (MB) = 1,024 Kilobytes
    # 1 Gigabyte (GB) = 1,024 Megabytes
    # 1 Terabyte (TB) = 1,024 Gigabytes

# memory = psutil.virtual_memory() # gives you a snapshot of the machine's memory state.
    # output looks like
    # svmem(
    #     total=16777216000, 
    #     available=6543210000,
    #     percent=61.0,
    #     used=10234000000,
    #     free=654320000,
    #     active=...
    #     inactive=...
    #     buffers=...
    #     cached=...
    #     shared=...
    # )
    # the number you see are byte's to convert into Megabytes divide by (1024**2), into GigaBytes by (1024***3)

# here swap means the amount of storage taken extra from SSD/HDD, inorder to run an application which requires more memory
# typically swap located in SSD/HDD
# ususally swap memory is of 4gb

# swap = psutil.swap_memory()
# print(swap)
    # output looks like
        # sswap(
        #     total=4294967296, The system has approximately 4 GiB of swap space available.
        #     used=1073741824,
        #     free=3221225472,
        #     percent=25.0, 25% of swap space is currently being used.
        #     sin=123456789,  sin = swapin. The cumulative amount of data moved into swap from memory.
        #     sout=987654321 sout = swapout. This represents the cumulative amount of data moved out of swap.
        # ) here the the bytes are not like moved in seconds 
        # these are the bytes is like total batch bytes moved into swap memory

# process = psutil.Process() # using this method you will understand how much memory or cpu etc.. is utilized by particular process
# print(process.memory_percent())
# print(process.memory_info())
# print(process.memory_full_info())

# process = psutil.Process(23093) # example: psutil.Process(pid=23093, name='Google Chrome Helper (Renderer)', status='running')
# print(process.cpu_times())





# disk usage

# print(psutil.disk_usage("/")) On Linux/macOS, / generally represents the root filesystem. generally it not represent physical ssd just file system
# on windows: psutil.disk_usage("C:\\")
# print(psutil.disk_io_counters()) it gives disk I/O 
    # output looks like 
        # sdiskio(
        #     read_count=123456,
        #     write_count=78901,
        #     read_bytes=1234567890,
        #     write_bytes=987654321,
        #     read_time=54321, accumulated time spent to read
        #     write_time=12345 accumulated time spent to write
        # )





# network

# print(psutil.net_io_counters())
    # output looks like 
        # snetio(
        #     bytes_sent=123456789, here byte_sent means how much data is sent over internet. the number here is bytes
        #     bytes_recv=987654321,
        #     packets_sent=123456, here packet_sent means, ususally the data divided into chuncks called packetes and here the 
        #                          here the number is cummulative count of packets that were created and sent
        #     packets_recv=234567,
        #     errin=0, This represents the number of incoming network errors recorded by the relevant interface/system counters. its a count
        #     errout=0, same here outgoing network errors. its a count not bytes
        #     dropin=0, This represents incoming packets that were dropped according to the OS/interface counters.
        #               A dropped packet means it arrived at the interface/system but wasn't accepted/processed normally.
        #     dropout=0 This represents outgoing packets that were dropped.
        # )

# print(psutil.net_io_counters(pernic=True)) # can get information per network interface.
    # Network interfaces
    #     Wi-Fi
    #     Ethernet
    #     Bluetooth
    #     VPN
    #     Loopback



# process
# lets put this info in text file

# with open("info.txt", "w", encoding="utf-8") as file:
#     for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
#         file.writelines(f"{process.info}\n")

# writing same info into json

# with open("info.json", "w", encoding="utf-8") as file:
#     data = []
#     for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
#         data.append(process.info)

#     json.dump(data,file,indent=4)


