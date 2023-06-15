from telegram import Update
from .service import log


def getStartText(update):
    start_text = f'Здравствуйте, {update.effective_user.full_name}! Меня зовут {update.effective_chat.get_bot().first_name}! ' \
                 'Я помогу Вам ознакомиться c удивительным миром космоса и даже смогу показать вам его красоты! Хотите узнать побольше обо ' \
                 'мне? Напишите /about ! Хотите ознакомиться со списком команд? Напишите /help !'
    log(update.effective_chat.id, f'{start_text}')
    return start_text


def getAboutText(update):
    about_text = f'Меня зовут {update.effective_chat.get_bot().first_name}! Я был создан студентом Кемеровского ' \
                 'Государственного Университета группы МОА-211 Степанюк Дмитрием Александровичем! Надеюсь, вам понравится этот ' \
                 'учебный бот.'
    log(update.effective_chat.id, f'{about_text}')
    return about_text


def showCommands(update):
    commands_list = "/start - Начать приключение в увлекательный мир космоса! \n" \
                    "/about - Познакомиться с проектом \n" \
                    "/apod - Полюбоваться на одну из множества фотографий космоса со всех уголков вселенной (может занять некоторое время, " \
                    "фотография, как никак, летит прямо с космоса ;) \n" \
                    "/bodies - Узнайте короткие и интересные факты о разных космических телах! \n" \
                    "/facts - Время грызть гранит науки! Узнайте ещё 100 случайных фактов о космосе! \n" \
                    "/rpfm - Хотите полюбоваться на красоты Марса? Тогда вам сюда!\n" \
                    "/help - Мы готовы оказать помощь любому, кто потеряется в этом просторном, большом списке команд"
    log(update.effective_chat.id, f'{commands_list}')
    return commands_list
