#Program Toko Kue Adel
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')\

def menu():
    print("Selamat datang di Toko Kue Adel\n")
    print("Kue yang tersedia di Toko Kue Adel: \n")
    print("Cokelat  = Rp30000")
    print("Oreo     = Rp40000\n")
    print("Stock kue kami tiap harinya adalah 35 untuk cokelat dan 25 untuk Oreo\n")
    print("DAPATKAN DISKON SAMPAI DENGAN  15% !!!")
    print("beli kue cokelat 5-20 dapat diskon 7%")
    print("beli kue cokelat 21-35 dapat diskon 12%")
    print("beli kue Oreo 4-15 dapat diskon 10%")
    print("beli kue Oreo 16-25 dapat diskon 15%\n")
    

    jumlah_cokelat = int(input("Beli berapa kue cokelat ? "))
    jumlah_Oreo = int(input("Beli berapa kue Oreo? "))
    clear_screen()
    if (jumlah_cokelat >= 1 and jumlah_cokelat <= 4):
        biaya_cokelat = 30000*jumlah_cokelat
        total_harga_cokelat = biaya_cokelat
        print("Total pembelian kue cokelat anda: %d" % (jumlah_cokelat))
        print("Total biaya kue cokelat anda: Rp %d" % (biaya_cokelat))
    elif (jumlah_cokelat >= 5 and jumlah_cokelat <= 20):
        biaya_cokelat =  30000*jumlah_cokelat
        diskon_cokelat = biaya_cokelat*7/100
        total_harga_cokelat = biaya_cokelat-diskon_cokelat
        print("Total pembelian kue cokelat:  %d"  % (jumlah_cokelat))
        print("Total biaya kue cokelat: Rp %d" % (biaya_cokelat))
        print("Diskon kue cokelat yang anda dapat: Rp %d" % (diskon_cokelat))
        print("Total kue cokelat yang harus anda bayar: Rp %d" % (total_harga_cokelat))
    elif(jumlah_cokelat >= 21 and jumlah_cokelat <= 35):
        biaya_cokelat = 30000*jumlah_cokelat
        diskon_cokelat = biaya_cokelat*12/100
        total_harga_cokelat = biaya_cokelat-diskon_cokelat
        print("Total pembelian cokelat: %d" % (jumlah_cokelat))
        print("Total biaya kue cokelat : Rp %d" % (biaya_cokelat))
        print("Diskon kue cokelat yang anda dapat: Rp %d" % (diskon_cokelat))
        print("Total kue cokelat yang harus anda bayar: Rp %d" % (total_harga_cokelat))
    elif(jumlah_cokelat == 0):
        total_harga_cokelat = 0
        print("Anda tidak membeli kue cokelat")    
    else:
        total_harga_cokelat = 0
        print("\n*Jumlah kue cokelat yang anda pilih tidak tersedia")
        time.sleep(5)

    if(jumlah_Oreo >= 1 and jumlah_Oreo <= 3):
        biaya_Oreo = 40000*jumlah_Oreo
        total_harga_Oreo = biaya_Oreo
        print("\nTotal pembelian kue cokelat anda: %d" % (jumlah_Oreo))
        print("Total biaya kue Oreo anda: Rp %d" % (biaya_Oreo))
    elif(jumlah_Oreo >= 4 and jumlah_Oreo <= 15):
        biaya_Oreo = 40000*jumlah_Oreo
        diskon_Oreo = biaya_Oreo*10/100
        total_harga_Oreo = biaya_Oreo-diskon_Oreo
        print("\nTotal pembelian kue Oreo: %d" % (jumlah_Oreo))
        print("Total biaya kue Oreo: Rp. %d" % (biaya_Oreo))
        print("Diskon kue Oreo yang anda dapat: Rp. %d" % (diskon_Oreo))
        print("Total kue Oreo yang harus anda bayar: Rp %d" % (total_harga_Oreo))
    elif(jumlah_Oreo >= 16 and jumlah_Oreo <= 25):
        biaya_Oreo = 40000*jumlah_Oreo
        diskon_Oreo = biaya_Oreo*25/100
        total_harga_Oreo = biaya_Oreo-diskon_Oreo
        print("Total pembelian kue Oreo: %d" % (jumlah_Oreo))
        print("Total biaya kue Oreo: Rp. %d" % (biaya_Oreo))
        print("Diskon kue Oreo yang anda dapat: Rp. %d" % (diskon_Oreo))
        print("Total kue Oreo yang harus anda bayar: Rp %d" % (total_harga_Oreo))
    elif(jumlah_Oreo == 0):
        total_harga_Oreo = 0
        print("Anda tidak membeli kue Oreo")
    else:
        total_harga_Oreo = 0
        print("\n*Jumlah kue Oreo yang anda pilih tidak tersedia")
        time.sleep(5)

    total_semua = total_harga_cokelat+total_harga_Oreo
    print("\nJumlah total biaya kue anda: Rp %d" % (total_semua)) 
    bayar = float(input("\nMasukkan nominal uang yang anda akan berikan: Rp "))
    angsul = bayar-total_semua
    if(bayar >= total_semua):
        print("Kembalian: Rp %d" % (angsul))
        print("\nTerima kasih sudah membeli kue di toko ini !!!")
    else:
        print("\nUang anda Kurang!")
        time.sleep(10)
        clear_screen()
        menu()

menu()
