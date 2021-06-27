import requests
from bs4 import BeautifulSoup


def train(a, b, c):
    url = f'https://pass.rw.by/ru/route/?from={a}&from_exp=&from_esr=&to={b}&to_exp=&to_esr=&front_date=%D0%B7%D0%B0' \
          f'%D0%B2%D1%82%D1%80%D0%B0&date={c} '
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='sch-table__cell-top')
    start_station = []
    finish_station = []
    travel_time = []
    start_time = []
    trains = []
    for i in items:
        time = i.find('div', class_='sch-table__time train-from-time').text
        station = i.find('div', class_='sch-table__station train-from-name').text
        time_road = i.find('span', class_='duration').text
        end_station = i.find('div', class_='sch-table__station train-to-name').text
        start_time.append(time)
        start_station.append(station)
        travel_time.append(time_road)
        finish_station.append(end_station)
    for i in range(len(start_station)):
        list_train = {'start_station': start_station[i], 'finish_station': finish_station[i],
                      'start_time': start_time[i], 'travel_time': travel_time[i]}
        trains.append(list_train)
    return trains
