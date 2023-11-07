import pandas as pd
import time
from flowcontainer.extractor import extract

stime = time.time()

pcap = extract(r"1592993485_noise.pcap",
               filter='ip',
               extension=[],
               split_flag=False,
               verbose=True
               )

i = 0

for key in pcap:
    value = pcap[key]
    ip_packets_length = pd.Series(value.ip_lengths, index=range(len(value.ip_lengths)), name='ip_packets_length')

    ip_packets_length.to_csv('./csv/{}.csv'.format(i), index=False)
    i = i + 1