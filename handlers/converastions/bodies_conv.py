from telegram import Update
from telegram.ext import ConversationHandler
import requests
from bs4 import BeautifulSoup

from ..service import log



async def showBodies(update, context):
    log(update.effective_chat.id, '/bodies')
    await update.message.reply_text(
        "Хотите узнать больше о космосе?\n"
        "Весьма похвально! Тяга к знаниям\n"
        "о космосе это почти то же самое, \n"
        "что и любовь к прекрасному! \n"
        "Напишите /stop, если не хотите продолжать. \n"
        "В противном случае, напишите всё, что душе угодно!"
    )
    return 1


async def pf_first(update, context):
    bodies = await get_bodies()
    await update.message.reply_text(
        "У нас на примете короткая, но интересная и обширная информация "
        "о разных космических телах! Вот, ознакомтесь!"
    )
    await update.message.reply_text(
        f"1) {bodies[0].text}\n"
        f"2) {bodies[2][0].text}\n"
        f"3) {bodies[3][0].text}\n"
        f"4) {bodies[4][0].text}\n"
        f"5) {bodies[5][0].text}\n"
    )
    return 2


async def pf_second(update, context):
    bodies = await get_bodies()

    answer = int(update.message.text)
    log(update.effective_chat.id, f'{answer}')
    bot_answer = ""

    if answer == 1:
        bot_answer = bodies[1].text
    elif answer > 1 and answer < 6:
        bot_answer = bodies[answer][1].text
    else:
        bot_answer = 'Кажется, вы где-то запутались...'

    await update.message.reply_text(bot_answer)

    return ConversationHandler.END


async def stop(update, context):
    log(update.effective_chat.id, '/stop')
    await update.message.reply_text("Никогда не поздно!")
    return ConversationHandler.END


async def get_bodies():
    site = requests.get('https://mks-onlain.ru/nazvaniya-vsekh-nebesnykh-tel/').text

    site_text = BeautifulSoup(site, "html.parser")

    solar_system = site_text.find(id='solnechnaya-sistema')

    bodies = (solar_system.find_next_siblings())

    planets = bodies[0]
    constellations = [bodies[1], bodies[2]]
    stars = [bodies[3], bodies[4]]
    galaxies = [bodies[20], bodies[22]]
    comets = [bodies[23], bodies[25]]

    return [solar_system, planets, constellations, stars, galaxies, comets]
