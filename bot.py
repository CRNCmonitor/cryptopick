import asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import TELEGRAM_BOT_TOKEN
from handlers.start_handler import start
from handlers.market_handler import handle_market
from handlers.news_handler import handle_news
from handlers.sentiment_handler import handle_sentiment
from handlers.alerts_handler import handle_alerts

async def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(handle_market, pattern='market'))
    app.add_handler(CallbackQueryHandler(handle_news, pattern='news'))
    app.add_handler(CallbackQueryHandler(handle_sentiment, pattern='sentiment'))
    app.add_handler(CallbackQueryHandler(handle_alerts, pattern='alerts'))
    await app.run_polling()

if __name__ == '__main__': asyncio.run(main())
