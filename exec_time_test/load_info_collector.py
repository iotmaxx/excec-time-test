'''
    exec-time-test is a software to get the current load of a linux system.

    Copyright (C) 2025  IoTmaxx GmbH

    This file is part of exec-time-test.

    exec-time-test is free software: you can redistribute it and/or modify it under the terms of 
    the version 3 of the GNU General Public License as published by the Free Software Foundation.

    exec-time-test is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
    without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Foobar. If 
    not, see <https://www.gnu.org/licenses/>. 
'''
import time
from .system_load_info import getSystemLoadInfo

def with_time_measure(func):
    def inner(**kwargs):
        perfStart = time.perf_counter()
        procStart = time.process_time()
        resultDict = {
            "function": func.__name__,
            "result": func(**kwargs),
            "processTime":  str(time.process_time() - procStart),
            "runTime":      str(time.perf_counter() - perfStart)
        }
        return resultDict
    return inner        

@with_time_measure
def getLoadInfo(**kwargs):
    if not "iterations" in kwargs:
        kwargs["iterations"] = 1
    if not "sleep" in kwargs:
        kwargs["sleep"] = 0.1
    resultDict = {
        "iterations":   kwargs["iterations"],
        "sleep":        kwargs["sleep"],
        "results":      []
    }
    for x in range(kwargs["iterations"]):
        resultDict["results"].append(with_time_measure(getSystemLoadInfo)())
        time.sleep(kwargs["sleep"])
    return resultDict
