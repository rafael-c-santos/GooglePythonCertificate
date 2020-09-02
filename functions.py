#!/usr/bin/env python3

import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    print(f"Current free disk space is {free:.2f}")
    return free > 20


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print(f"Current CPU usage is {usage}")
    return usage < 75


def check_system():
    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    else:
        print("Everything is ok!")


def time_to_automate(automate_time, perform_time, number_of_times):
    total_time = perform_time * number_of_times
    if automate_time < total_time:
        return f"Total time of this task is {total_time}. It's worth it!"
    else:
        return f"Total time of this task is {total_time}. It's not worth it."
