import csv
import datetime
from pynput.mouse import Listener
import os

def on_click(x, y, button, pressed):
    if pressed:
        current_time = datetime.datetime.now()
        formatted_time = current_time.time().strftime("%H:%M:%S.%f")[:-3]
        click_data = [current_time.date(), formatted_time, x, y]
        save_to_csv(click_data)

def save_to_csv(click_data):
    file_path = 'click_data.csv'
    is_file_exist = os.path.isfile(file_path)

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')

        if not is_file_exist:
            writer.writerow(['Data', 'Hora', 'Posição X', 'Posição Y'])

        writer.writerow(click_data)

with Listener(on_click=on_click) as listener:
    listener.join()
