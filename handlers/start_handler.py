from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from config import BITUNIX_LINK

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    kb = [[InlineKeyboardButton('Market', callback_data='market')],[InlineKeyboardButton('News', callback_data='news')],[InlineKeyboardButton('Sentiment', callback_data='sentiment')],[InlineKeyboardButton('Alerts ON/OFF', callback_data='alerts')]]
    await update.message.reply_text('CryptoPick - tvoj krypto intel bot.\n\nBitunix: ' + BITUNIX_LINK, reply_markup=InlineKeyboardMarkup(kb))
