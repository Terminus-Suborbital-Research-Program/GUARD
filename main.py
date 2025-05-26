from radiacode import RadiaCode, RealTimeData
import time

device = RadiaCode()

# Write stuff
while True:
    data = device.data_buf()
    spectrum = device.spectrum()
    accum  = device.spectrum_accum()

    if len(data) != 0:
        for datum in data:
            print(datum)

    print(spectrum)
    print(accum)
    time.sleep(1)
