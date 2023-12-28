from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN: Final = "6777078819:AAFDNPncWV3s7dAARDuN3YSe_s-ULsLGuIg"
BOT_USERNAME = "@kkumachi_bot"


# KUMPULAN COMMAND
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! ini awal")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! ini help")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! ini command")


# HANDLE RESPON untuk user
def handle_response(text: str) -> str:
    processed_text: str = text.lower()

    if "hello" in processed_text:
        return "Hi juga!, cek Instagram A.lifAnwar"

    if "apa kabar?" in processed_text:
        return "Baik, jangan lupa cek A.lifAnwar"

    return "Follow Instagram A.lifAnwa Github: https://github.com/Hypes-Astror"


# ketika user mengetik
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("bot", response)

    await update.message.reply_text(response)


# error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused Error {context.error} ")


if __name__ == "__main__":
    print("Starting bot ....")
    app = Application.builder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # message
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error
    app.add_error_handler(error)

    print("Polling bot ....")
    app.run_polling(poll_interval=3)
