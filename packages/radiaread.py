#!/usr/bin/env python3
import os, time

from radiacode import RadiaCode

# —— 1. bump the counter —————————————————————————————
ctr_file = "/var/lib/radiacode/counter.txt"
os.makedirs(os.path.dirname(ctr_file), exist_ok=True)

try:
    with open(ctr_file, "r") as f:
        counter = int(f.read().strip())
except FileNotFoundError:
    counter = 0

counter += 1
with open(ctr_file, "w") as f:
    f.write(str(counter))

# —— 2. open per-run logs —————————————————————————————
log_dir = "/var/log/radiacode"
os.makedirs(log_dir, exist_ok=True)

data_f     = open(f"{log_dir}/data_{counter}.log",     "a", buffering=1)
spectrum_f = open(f"{log_dir}/spectrum_{counter}.log", "a", buffering=1)
accum_f    = open(f"{log_dir}/accum_{counter}.log",    "a", buffering=1)

# —— 3. your main loop ——————————————————————————————
device = RadiaCode()
while True:
    now = time.time()

    for d in device.data_buf():
        data_f.write(f"{now} {d}\n")
    spectrum_f.write(f"{now} {device.spectrum()}\n")
    accum_f.write(f"{now} {device.spectrum_accum()}\n")

    time.sleep(1)

