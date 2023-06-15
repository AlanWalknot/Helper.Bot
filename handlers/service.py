from datetime import datetime


def log(user_id, msg):
    currentTime = datetime.now()
    with open(f'C:\logs\{user_id}.log', 'a+') as file:
        file.write(f'{currentTime} : {msg}\n')

