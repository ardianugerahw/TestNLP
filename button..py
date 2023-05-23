from telebot import *                                               # berfungsi mengimpor modul pyTelegramAPI

api = '6283619133:AAHRJcXqLPDygCaezBCmARKxuOFKF0mPKFQ'              # buat variabel api yang berisi token api yang diambil dari bot father telegram
bot = TeleBot(api)                                                  # buat variabel bot yang menghubungkan api telegram

@bot.message_handler(commands=['start'])
def mulai(message):                                                 # buat fungsi mulai dengan parameter message 
    bot.reply_to(message, 'halo pengguna baru')                     # command agar bot mereply pesan inputan
    markup = types.ReplyKeyboardMarkup()                            # buat variabel markup yang fungsinya bisa mereply button
    item1 = types.KeyboardButton('/bantuan')                        # button yang berisikan item 1
    item2 = types.KeyboardButton('/start')                          # button yang berisikan item 2
    item3 = types.KeyboardButton('a')                               # button yang berisikan item 3
    markup.row (item1, item2)                                       # buat baris yang terdiri dari item1 dan item2
    markup.row (item3)                                              # buat baris yang terdiri dari item3
    bot.reply_to(message, 'Silahkan pilih', reply_markup=markup)    # command agar bot mereply pesan string dan variabel markup

@bot.message_handler(commands=['bantuan'])
def bantuan(message):                                               # buat fungsi bantuan dengan parameter message
    bot.reply_to(message, 'ada yang bisa saya bantu')               # command agar bot mereply pesan inputan


bot.infinity_polling(timeout = 10, long_polling_timeout = 5)        # command agar program running terus