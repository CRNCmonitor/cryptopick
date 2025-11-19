from telegram.ext import Application, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from handlers.start_handler import start
import asyncio

async def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
