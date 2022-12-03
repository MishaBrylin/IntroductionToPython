from datetime import datetime as dt


def logger(action):
    time = dt.now().strftime('%m/%d/%Y, %H:%M:%S')
    with open('log.txt', 'a') as file:
        file.write(f' {action} - {time}\n')
