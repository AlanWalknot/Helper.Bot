import logging

from api_token import api_token_tg, api_token_na

from handlers.simple import getStartText, getAboutText, showCommands
from handlers.query import sendAPOD, sendRPFM
from handlers.converastions.bodies_conv import pf_first, pf_second, showBodies, stop
from handlers.converastions.space_facts import facts, f_first, f_second, stop
from handlers.service import log

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ConversationHandler, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=getStartText(update))
    log(update.effective_chat.id, '/start')


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=getAboutText(update))
    log(update.effective_chat.id, '/about')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=showCommands(update))
    log(update.effective_chat.id, '/help')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Что-что? Не расслышал... Может, вам стоит обратиться к /help?')


def main():
    application = ApplicationBuilder().token(api_token_tg).build()

    start_handler = CommandHandler('start', start)
    about_handler = CommandHandler('about', about)
    help_handler = CommandHandler('help', help)
    apod_handler = CommandHandler('apod', sendAPOD)
    rpfm_handler = CommandHandler('rpfm', sendRPFM)

    pf_handler = ConversationHandler(
        entry_points=[CommandHandler('bodies', showBodies)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, pf_first)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, pf_second)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    sf_handler = ConversationHandler(
        entry_points=[CommandHandler('facts', facts)],

        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, f_first)],
            2: [MessageHandler(filters.TEXT & ~filters.COMMAND, f_second)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(about_handler)
    application.add_handler(help_handler)
    application.add_handler(apod_handler)
    application.add_handler(rpfm_handler)

    application.add_handler(pf_handler)
    application.add_handler(sf_handler)
    application.add_handler(echo_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
