from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Gantikan dengan token bot Anda
TOKEN = '7706413371:AAGCm9-dbsL4XOBA3e_NmCKeI5lngVEtHug'

def start(update, context):
    update.message.reply_text('Selamat datang di Bot Jual Beli! Ketik /help untuk melihat perintah.')

def help_command(update, context):
    update.message.reply_text('Perintah yang tersedia:\n/list - Lihat produk\n/order - Pesan produk')

# Fungsi utama
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
