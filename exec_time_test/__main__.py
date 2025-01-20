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
import json
import sys
import argparse
from .load_info_collector import getLoadInfo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='python -m exec_time_test',
                    description='get the current load of a linux system',
                    epilog='Copyright (C) 2025 IoTmaxx GmbH',
                    formatter_class=lambda prog: argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=37)
    )
    parser.add_argument('-i', '--iterations', type=int, default=1,  metavar='<num>', help='# of iterations')
    parser.add_argument('-s', '--sleep', type=float, default=0.1, metavar='<s>', help='time(s) between iterations')

    args = parser.parse_args()
    print(json.dumps(getLoadInfo(iterations=args.iterations, sleep=args.sleep),indent=4))
