import requests
from random import randrange
from telegram import Update

from api_token import api_token_na
from .service import log


async def sendAPOD(update, context):
    log(update.effective_chat.id, '/apod')
    apod_url = 'https://api.nasa.gov/planetary/apod/'

    params = {
        'api_key': api_token_na,
        'count': int(1)
    }

    response = await get_response(apod_url, params)

    picture = response[0]['url']
    caption = f'***{response[0]["title"]}***'
    discription = response[0]['explanation']
    await update.message.reply_photo(picture)
    log(update.effective_chat.id, f'{picture}')
    await update.message.reply_text(f'{caption} \n{discription}', parse_mode='Markdown')
    log(update.effective_chat.id, f'{caption} \n {discription}')


async def sendRPFM(update, context):  # SEND RANDOM PICTURE FROM THE MARS
    log(update.effective_chat.id, '/rpfm')
    epic_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    params = {
        'api_key': api_token_na,
        'sol': 1000,
    }

    response = await get_response(epic_url, params)
    array_len = len(response['photos'])

    randomPicture = randrange(array_len + 1)

    picture = response['photos'][randomPicture]['img_src']

    await update.message.reply_photo(picture)
    log(update.effective_chat.id, f'{picture}')


async def get_response(url, params):
    response = requests.get(url, params)
    json_response = response.json()
    return json_response
