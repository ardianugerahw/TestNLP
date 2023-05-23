from telebot import *                                       # mengimpor semua modul pyTelegramBotAPI
import re                                                   # modul re digunakan untuk membuat chatbot lebih interaktif
import random                                               # modul random untuk membuat chatbot lebih interaktif

api = '6283619133:AAHRJcXqLPDygCaezBCmARKxuOFKF0mPKFQ'      # buat variabel api dan disi token api yang didapat dari botfather telegram
bot = TeleBot(api)                                          # buat variabel bot yang menghubungkan api telegram

#start
@bot.message_handler(commands=['start'])                    # command awal chatbot dengan input nanti garis miring start
def selamat_datang(message):                                # membuat fungsi selamat datang

    chatid = message.chat.id                                      # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_message(chatid, 'Selamat Datang Pengguna')           # command untuk merespon tanpa reply pesan inputan
    bot.send_message(chatid, 'Ketikkan /tanya untuk memulai')     # command untuk merespon tanpa reply pesan inputan
    

#bantuan 
@bot.message_handler(commands=['bantuan'])                          # command awal chatbot dengan input nanti garis miring bantuan
def bantuan(message):                                               # membuat fungsi bantuan
    chatid = message.chat.id                                        # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_message(chatid, 'oke, ini dia list perintah yang bisa digunakan')  # command untuk merespon tanpa reply pesan inputan
    markup = types.ReplyKeyboardMarkup()                            # buat variabel markup yang fungsinya bisa mereply button
    item1 = types.KeyboardButton('/tanya')                          # button yang berisikan item 1
    item2 = types.KeyboardButton('/foto')                           # button yang berisikan item 2
    item3 = types.KeyboardButton('/dokumen')                        # button yang berisikan item 3
    markup.row (item1)                                              # buat baris yang terdiri dari item1
    markup.row (item2, item3)                                       # buat baris yang terdiri dari item2 dan item 3

    bot.reply_to(message, 'Silahkan pilih', reply_markup=markup)    # command agar bot mereply pesan string dan variabel markup

#tanya
@bot.message_handler(commands=['tanya'])                        # command awal chatbot dengan input nanti garis miring tanya
def tanya(message):                                             # membuat fungsi tanya
    chatid = message.chat.id                                    # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_message(chatid, 'kamu bisa bertanya tentang diriku dengan pertanyaan siapa aku, dimana aku tinggal, minta fotoku, minta dokumenku, dll')   # command untuk merespon inputan
    bot.send_message(chatid, 'Tanyakan seputar biodataku yah teman teman ntar kujawab')                                                                 # command untuk merespon inputan

#dokumen 
@bot.message_handler(commands=['dokumen'])                     # command awal chatbot dengan garis miring
def kirim_dokumen(message):                                    # membuat fungsi selamat datang

    chatid = message.chat.id                                      # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_document(chatid, open('D:\\dokument.docx','rb'))     # command untuk merespon dengan foto yang telah ditentukan pathnya dan tidak mereply pesan inputan


#foto
@bot.message_handler(commands=['foto'])                     # command awal chatbot dengan garis miring
def kirim_foto(message):                                    # membuat fungsi selamat datang

    chatid = message.chat.id                                # variabel id agar bot bisa membalas tanpa mereply pesan
    bot.send_photo(chatid, open('D:\\tesnlp.png','rb'))     # command untuk merespon dengan foto yang telah ditentukan pathnya dan tidak mereply pesan inputan

#sapa how who where when why what
sapa = ['halo juga', 'hai juga']                          # variabel sapa menyimpan list respon yakni halo juga dan hai juga
how = ['aku baik-baik saja','alhamdulillah baik']         # variabel sapa menyimpan list respon yakni aku baik baik saja dan alhamdulillah baik
who = ['aku adalah chatbot nlp']                          # variabel sapa menyimpan list respon yakni aku adalah chatbot nlp
where = ['aku tinggal di telegram']                       # variabel sapa menyimpan list respon yakni aku tinggal di telegram
when = ['aku lahir pada tanggal 25 Maret 2023']           # variabel sapa menyimpan list respon yakni aku lahir pada tanggal 25 Maret 2023
why = ['aku dibuat untuk memenuhi tugas matkul']          # variabel sapa menyimpan list respon yakni aku dibuat untuk memenuhi tugas matkul
what = ['mungkin iya', 'bisa jadi']                       # variabel sapa menyimpan list respon yakni mungkin iya dan bisa jadi
bantuan = ['tenang, coba pilih /bantuan']                 # variabel sapa menyimpan list respon yakni tenang, coba pilih /bantuan
dokumen = ['oke, coba pilih /dokumen']                    # variabel sapa menyimpan list respon yakni oke, coba pilih /dokumen
foto = ['baiklah, coba pilih /foto']                          # variabel sapa menyimpan list respon yakni tenang, coba pilih /foto
creator = ['hanya tuhan yang tahu','siapa hayo','saya dibuat oleh kelompok 2']   # variabel sapa menyimpan list respon yakni hanya tuhan yang tahu, siapa hayo, saya dibuat oleh kelompok 2
thanks =['sama sama']                                     # variabel sapa menyimpan list respon yakni sama sama

@bot.message_handler(content_types={'text'})                # setiap kita nulis ndak peru kasi garis miring
def chatbot(message):  
    teks = message.text                                     # variabel teks akan menyimpan setiap data inputan kita seperti halo, hai
    if re.findall('halo|hai|Hai|Halo', teks):               # ini fungsi dari modul re jadi apabila terdapat kata hai atau halo maka akan dijalankan kondisi selanjutnya
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(sapa))       # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel sapa secara acak

    elif re.findall ('bagaimana|Bagaimana|Gimana|gimana|kabar|Kabar', teks):    # ini fungsi dari modul re jadi apabila terdapat kata hai atau halo maka akan dijalankan kondisi selanjutnya
        chatid = message.chat.id                                                # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(how))                            # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel how secara acak
        
    elif re.findall ('siapa pembuatmu|siapa yang membuatmu ', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(creator))    # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam creator secara acak

    
    
    elif re.findall ('Siapa|siapa', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(who))        # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel who secara acak

    elif re.findall ('Dimana|dimana', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(where))      # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel where secara acak

    elif re.findall ('Kapan|kapan', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(when))       # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel when secara acak

    elif re.findall ('Mengapa|mengapa', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(why))        # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel why secara acak

    elif re.findall ('Siri|siri|Assistant|assistant|Asisten|asisten', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(what))       # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel what secara acak

    elif re.findall ('bantuan|Bantuan|bingung|Bingung', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(bantuan))    # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel bantuan secara acak

    elif re.findall ('Dokumen|dokumen', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(dokumen))    # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel dokumen secara acak

    elif re.findall ('Foto|foto', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(foto))       # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel foto secara acak

    elif re.findall ('Terima|terima|Kasih|kasih|Makasih|makasih', teks):
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, random.choice(thanks))     # ini kegunaan dari modul random untuk merespon dengan list kata yang berada didalam variabel thanks secara acak


    else:
        chatid = message.chat.id                            # variabel id agar bot bisa membalas tanpa mereply pesan
        bot.send_message(chatid, 'Maaf saya tidak paham')   # command untuk merespon jika tidak ada inputan yang sesuai


bot.infinity_polling(timeout=10, long_polling_timeout = 5)  # berfungsi untuk merunning kode program 






