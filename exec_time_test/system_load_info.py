'''
    exec-time-test is a software to get the current load of a linux system.

    Copyright (C) 2025  IoTmaxx GmbH <info@iotmaxx.de>

    This file is part of exec-time-test.

    exec-time-test is free software: you can redistribute it and/or modify it under the terms of 
    the version 3 of the GNU General Public License as published by the Free Software Foundation.

    exec-time-test is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Foobar. If 
    not, see <https://www.gnu.org/licenses/>. 
'''
import psutil

def getSystemLoadInfo(**kwargs):
    curValues = {
        "NumCPUs":          psutil.cpu_count(),
        "CpuLoadPercent":   psutil.cpu_percent(),
        "VirtualMemory":    psutil.virtual_memory()._asdict(),
        "Processes":        []
    }
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_num', 'cpu_percent', 'create_time', 'status', 'memory_percent']):
        curValues["Processes"].append(proc.info)
    return curValues

