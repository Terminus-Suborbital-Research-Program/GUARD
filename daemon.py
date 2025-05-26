#!/usr/bin/env python3
import os, time, datetime

from radiacode import RadiaCode

# 1) Read the boot ID so filenames collide only between boots
with open("/proc/sys/kernel/random/boot_id") as f:
    boot_id = f.read().strip()

# 2) Prepare log directory
log_dir = "/var/log/radiacode"
os.makedirs(log_dir, exist_ok=True)

# 3) Open one file per data type
ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
data_f    = open(f"{log_dir}/data_{boot_id}_{ts}.log",    "a", buffering=1)
spectrum_f= open(f"{log_dir}/spectrum_{boot_id}_{ts}.log","a", buffering=1)
accum_f   = open(f"{log_dir}/accum_{boot_id}_{ts}.log",   "a", buffering=1)

device = RadiaCode()

while True:
    now = time.time()
    data     = device.data_buf()
    spectrum = device.spectrum()
    accum    = device.spectrum_accum()

    # write raw lists or numbers with timestamps
    for d in data:
        data_f.write(f"{now} {d}\n")
    spectrum_f.write(f"{now} {spectrum}\n")
    accum_f.write(f"{now} {accum}\n")

    time.sleep(1)

