import json                  # impor file json 

a = open('data.json')        # variabel a adalah open file bernama data.json
data = json.load(a)          # variabel data adalah json load dari variabel a

print('''
1. Melatih Bot
2. Berbicara dengan Bot
''')

while True:
    input_awal = input ("Masukan kode: ")    # melatih botnya berbicara
    if input_awal == "1": 
        while True:
            x = input("User\t: ")           # data dari user
            if x == "keluar":               # jika x sama dengan keluar maka break
                break
            else:
                y = input("Bot\t: ")           # data dari bot
                data[x] = y                    # data[x] sebagai kunci dan y sebagai nilai dari kuncinya
                b = open('data.json', "w")     # data json akan ditulis lagi/diperbarui lagi dengan write
                json.dump(data,b)
                b.close()

    elif input_awal == "2":
        while True:
            x = input("User\t: ")
            if x == 'keluar':                        # jika x sama dengan kelur maka break
                break
            if x in data:                            # jika x didalam variabel data yang berfungsi sebagai kunci
                print(f'Bot\t: {data[x]}')           # maka printkan nilai didalam data{x} yang bertindak sebagai kata kunci 
            else:                                       # jika tidak
                print("Bot\t: Itu kata yang baru")      # printkan itu kata yang baru

    else:           # jika bukan memilih kode 1 atau 2
        pass        # maka ulangi hingga user memilih kode 1 atau 2
