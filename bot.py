from telethon import TelegramClient, events

# Ganti dengan API ID dan API Hash Anda
api_id = '25177374'
api_hash = '7fd099fb58b09d78e7aad3d084eb4f05'
bot_token = '7922842410:AAH3gf4DZVl-eCJmwcY0Cm0FvJJZdhU-CJI'

# Membuat klien
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    # Mengirim pesan balik untuk setiap pesan baru
    await event.reply('Anda mengirim: ' + event.raw_text)

# Menjalankan bot
client.run_until_disconnected()
