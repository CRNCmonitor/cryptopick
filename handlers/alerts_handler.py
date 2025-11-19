from telegram import Update
from telegram.ext import ContextTypes

async def handle_alerts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text('Alerts ON/OFF not implemented yet.')
