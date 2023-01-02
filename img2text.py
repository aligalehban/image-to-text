from sys import path
from telegram.ext import *
import telegram
import PIL 
from PIL import Image
import pytesseract


def start_command(update, context):
    name = update.message.chat.first_name
    update.message.reply_text("Hello " + name)
    update.message.reply_text("Please share your image")

def downloader(update, context):
    context.bot.get_file(update.message.document).download()

    # writing to a custom file
    with open("./file.jpg", 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)
        update.message.reply_text("Image received")
    image ="./file.jpg"
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HP\AppData\Local\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(image), lang="eng")
    update.message.reply_text(text)


def main():
    print("Started")
    TOKEN = ""
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.document, downloader))
    

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()