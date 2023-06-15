from telegram import Update
from telegram.ext import ConversationHandler
import requests
from bs4 import BeautifulSoup

from ..service import log


async def facts(update, context):
    log(update.effective_chat.id, '/facts')
    await update.message.reply_text(
        "Вашему любопытству нет предела! Желаете узнать ещё больше о космосе?\n" \
        "Прекрасно! У меня есть 100 случайных фактов о космосе. Напишите что-нибудь, если вы согласны.\n" \
        "/stop слово!"
    )
    return 1


async def f_first(update, context):
    facts = await get_facts()
    await update.message.reply_text(
        "Какой бы факт вы хотели узнать сегодня?"
    )
    return 2


async def f_second(update, context):
    facts = await get_facts()

    answer = int(update.message.text)
    log(update.effective_chat.id, f'{answer}')
    bot_answer = ""

    if answer > 0 and answer < 101:
        bot_answer = facts[answer - 1]
    else:
        bot_answer = 'Кажется, вы где-то запутались...'

    await update.message.reply_text(bot_answer)

    return ConversationHandler.END


async def stop(update, context):
    log(update.effective_chat.id, '/stop')
    await update.message.reply_text("Никогда не поздно!")
    return ConversationHandler.END


async def get_facts():
    site = requests.get('https://100-faktov.ru/100-interesnyx-faktov-o-kosmose/').text

    site_text = BeautifulSoup(site, "html.parser")

    container = site_text.find(class_='nativerent-content-integration')

    elements = container.find_next_siblings()

    facts = []

    for element in elements:
        if elements.index(element) > 1 and elements.index(element) != 32 and elements.index(
                element) != 78 and elements.index(element) != 94 and elements.index(element) < 105:
            element = element.text
            facts.append(element)



    return facts
