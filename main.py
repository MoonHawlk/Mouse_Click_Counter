import csv
import datetime
from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if pressed:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        click_data = [current_time, x, y]
        save_to_csv(click_data)

def save_to_csv(click_data):
    with open('click_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(click_data)

with Listener(on_click=on_click) as listener:
    listener.join()
