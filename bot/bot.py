import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage, AnswerInlineQuery
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle
from aiogram.utils.executor import start_webhook

from probs import probs
from settings import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler()
async def echo(message: types.Message):
    # Regular request
    # await bot.send_message(message.chat.id, "опять выходишь на связь, чудила?", reply_to_message_id=message.message_id)

    # or reply INTO webhook
    return SendMessage(message.chat.id, "опять выходишь на связь, чудила?", reply_to_message_id=message.message_id)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    custom_text = f'Вероятность, что <b>{(inline_query.query or "Автор сообщения лох")}</b> ' + '{0}{1}'
    items = list(
        InlineQueryResultArticle(
            id=str(ind),
            title=variant.title,
            input_message_content=InputTextMessageContent(
                (variant.message or custom_text).format(variant.prob, variant.units),
                parse_mode='html'
            )
        )
        for ind, variant in enumerate(probs())
    )
    # Regular request
    # await bot.answer_inline_query(inline_query.id, results=items)

    # or reply INTO webhook
    return AnswerInlineQuery(inline_query.id, results=items)


async def on_startup(dp):
    logging.warning(
        f'Starting with configs: WEBHOOK_HOST = {WEBHOOK_HOST}; WEBAPP_PORT = {WEBAPP_PORT}; WEBAPP_HOST = {WEBAPP_HOST}')
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    logging.warning('Shut down')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
    # executor.start_polling(dp, skip_updates=True)
