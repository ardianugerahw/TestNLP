from telebot import *
import re                                                   # modul re digunakan untuk membuat chatbot lebih interaktif
import random                                               # modul random untuk membuat chatbot lebih interaktif

api = '6283619133:AAHRJcXqLPDygCaezBCmARKxuOFKF0mPKFQ'      # buat variabel api dan disi token api yang didapat dari botfather telegram
bot = TeleBot(api)                                          # buat variabel bot

#start
@bot.message_handler(commands=['start'])                    # command awal chatbot dengan garis miring
def selamat_datang(message):                                # membuat fungsi selamat datang
    bot.reply_to(message, 'Selamat Datang')                 # command untuk merespon dengan mereply pesan inputan

    chatid = message.chat.id                                # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_message(chatid, 'Selamat Datang Pengguna')     # command untuk merespon tanpa reply pesan inputan

#foto
@bot.message_handler(commands=['foto'])                     # command awal chatbot dengan garis miring
def kirim_foto(message):                                    # membuat fungsi selamat datang

    chatid = message.chat.id                                # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_photo(chatid, open('D:\\piring.png','rb'))     # command untuk merespon dengan foto yang telah ditentukan pathnya dan tidak mereply pesan inputan


#sapa
sapa = ['halo juga', 'hai juga']                            # variabel sapa menyimpan list respon yakni halo juga dan hai juga
@bot.message_handler(content_types={'text'})                # setiap kita nulis ndak peru kasi garis miring
def chatbot(message):                                       # membuat fungsi chatbot
    teks = message.text                                     # variabel teks akan menyimpan setiap data inputan kita seperti halo, hai
    if re.findall('halo|hai|Hai|Halo', teks):               # ini fungsi dari modul re jadi apabila terdapat kata hai atau halo maka akan dijalankan kondisi selanjutnya
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(sapa))       # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel sapa secara acak

    else:
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, 'Maaf saya tidak paham')   # command untuk merespon jika tidak ada inputan yang sesuai
bot.infinity_polling(timeout=10, long_polling_timeout = 5)  # berfungsi untuk merunning kode program 