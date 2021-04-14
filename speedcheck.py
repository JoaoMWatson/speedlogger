import speedtest
import time
import pandas as pd
import matplotlib as matplot
from datetime import datetime


def prepare():
    res = {'download': [],
           'upload': [],
           'ping': [],
           'timestamp': []}
    while True:
        try:
            st = speedtest.Speedtest()
            st.get_servers()
            st.get_best_server()
            st.download()
            st.upload()
            result_raw = st.results.dict()
            res['download'].append(
                round(result_raw['download']/1024/1024, 2))
            res['upload'].append(round(result_raw['upload']/1024/1024, 2))
            res['ping'].append(round(result_raw['ping'], 2))
            res['timestamp'].append(str(datetime.now()))
        except KeyboardInterrupt:
            break
    return res


if __name__ == "__main__":
    result = prepare()

    df = pd.DataFrame({'Download': result['download'],
                       'Upload': result['upload'],
                       'Ping': result['ping'],
                       'Timestamp': result['timestamp']})

    df.to_csv('log.xlsx', sep='\t', encoding='utf-8')
