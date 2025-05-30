#!/usr/bin/env python3
import os
import sys
import time

from radiacode import RadiaCode

def main():
    device = RadiaCode()
    device.set_device_on(True)
    device.spectrum_reset()
    device.dose_reset()
    
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <log_directory>")
        sys.exit(1)

    log_dir = sys.argv[1]
    os.makedirs(log_dir, exist_ok=True)

    # —— 1. bump the counter —————————————————————————————
    ctr_file = os.path.join(log_dir, "counter.txt")
    try:
        with open(ctr_file, "r") as f:
            counter = int(f.read().strip())
    except FileNotFoundError:
        counter = 0

    counter += 1
    with open(ctr_file, "w") as f:
        f.write(str(counter))

    # —— 2. open per-run logs —————————————————————————————
    data_path     = os.path.join(log_dir, f"data_{counter}.log")
    spectrum_path = os.path.join(log_dir, f"spectrum_{counter}.log")
    accum_path    = os.path.join(log_dir, f"accum_{counter}.log")

    data_f     = open(data_path,     "a", buffering=1)
    spectrum_f = open(spectrum_path, "a", buffering=1)
    accum_f    = open(accum_path,    "a", buffering=1)

    # —— 3. your main loop ——————————————————————————————

    while True:
        now = time.time()

        for d in device.data_buf():
            data_f.write(f"{now} {d}\n")
        spectrum_f.write(f"{now} {device.spectrum()}\n")
        accum_f.write(f"{now} {device.spectrum_accum()}\n")

        time.sleep(1)

if __name__ == "__main__":
    main()
