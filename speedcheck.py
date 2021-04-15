import speedtest
import pandas as pd
import time
import matplotlib as matplot
import numpy as np


def get_data():
    res = {'download': [],
           'upload': [],
           'ping': [],
           'timestamp': []}

    print("Começando: " + time.strftime("%H:%M:%S", time.localtime()))
    print("Aperte Ctrl+C para parar ")
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
            res['timestamp'].append(time.strftime("%H:%M", time.localtime()))
            time.sleep(60)
        except KeyboardInterrupt:
            print('Encerrando...')
            break
    return res


def graphs():
    df = pd.read_csv('log.csv')
    print(df)


if __name__ == "__main__":
    result = get_data()
    df = pd.DataFrame({'Download': result['download'],
                       'Upload': result['upload'],
                       'Ping': result['ping'],
                       'Timestamp': result['timestamp']})

    df.to_csv('log.csv', encoding='utf-8', index=False)

    # graphs()
