import psutil

def getSystemLoadInfo():
    curValues = {
        "CpuLoadPercent": psutil.cpu_percent(),

    }
    print(curValues)
    print(dict(psutil.virtual_memory())
    