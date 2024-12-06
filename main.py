import os
import termcolor
from tabulate import tabulate
import datetime as dt
import csv
import time

def clear():
    os.system("cls")

def pagar():
    print("="*98)

def green(perintah):
    clear()
    logo()
    termcolor.cprint(perintah.center(98),'green')
    pagar()
    input("Tekan Enter Untuk Kembali")
    time.sleep(1)

def yellow(perintah):
    clear()
    logo()
    termcolor.cprint(perintah.center(98),'yellow')
    pagar()
    input("Tekan Enter Untuk Kembali")
    time.sleep(1)

def red(perintah):
    clear()
    logo()
    termcolor.cprint(perintah.center(98),'red')
    pagar()
    input("Tekan Enter Untuk Kembali")
    time.sleep(1)

def lightred(perintah):
    clear()
    logo()
    termcolor.cprint(perintah.center(98),"light_red")
    pagar()
    input("Tekan Enter Untuk Kembali")
    time.sleep(1)

def wait(perintah):
    clear()
    logo()
    print("Loading".center(98))
    pagar()
    time.sleep(0.5)
    clear()
    logo()
    print("Loading.".center(98))
    pagar()
    time.sleep(0.5)
    clear()
    logo()
    print("Loading..".center(98))
    pagar()
    time.sleep(0.5)
    clear()
    logo()
    print("Loading...".center(98))
    pagar()
    time.sleep(0.5)
    clear()
    logo()
    termcolor.cprint(perintah.center(98),'yellow')
    pagar()
    time.sleep(1)
    clear()

def logo():
    pagar()
    print("""

    ░        ░░░      ░░░       ░░░  ░░░░  ░░░      ░░░        ░░        ░░░      ░░░  ░░░░  ░
    ▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒   ▒▒   ▒▒  ▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒
    ▓      ▓▓▓▓  ▓▓▓▓  ▓▓       ▓▓▓        ▓▓  ▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓      ▓▓▓▓  ▓▓▓▓▓▓▓▓        ▓
    █  ████████        ██  ███  ███  █  █  ██        █████  █████  ████████  ████  ██  ████  █
    █  ████████  ████  ██  ████  ██  ████  ██  ████  █████  █████        ███      ███  ████  █
                                                                                            
    """)
    pagar()

def main():
    while True:
        clear()
        logo()
        print("SELAMAT DATANG SILAHKAN LOGIN TERLEBIH DAHULU".center(98))
        pagar()
        print("""
1. Admin
2. User
3. Exit
              """)
        try:
            pilih = int(input("Pilih Login Sebagai: "))
            if pilih == 1:
                login_admin()
                break
            elif pilih == 2:
                login_user()
                break
            elif pilih == 3:
                clear()
                exit()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

# ---------------------------------------------------------[Log In]-------------------------------------------------------------------------------
def login_admin():
    while True:
        clear()
        logo()
        print("LOGIN ADMIN".center(98))
        pagar()
        username = input("Masukkan username anda: ")
        password = input("Masukkan Password anda: ")
        with open("CSV/admin.csv", mode="r") as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                if row == [username,password]:
                    clear()
                    logo()
                    termcolor.cprint("LOGIN BERHASIL".center(98),'green')
                    pagar()
                    time.sleep(1)
                    wait("MEMASUKI MENU ADMIN")
                    main_admin()
                    break    
                else:
                    red("USERNAME ATAU PASSWORD SALAH")
                    main()
                    break

def login_user():
    while True:
        clear()
        logo()
        print("LOGIN USER".center(98))
        pagar()
        global username
        username = input("Masukkan username anda: ")
        password = input("Masukkan Password anda: ")
        indikator_login = 0
        with open("CSV/pengguna.csv", mode="r") as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                if row == [username,password]:
                    indikator_login += 1 
                else:
                    continue

        if indikator_login == 1:
            clear()
            logo()
            termcolor.cprint("LOGIN BERHASIL".center(98),'green')
            pagar()
            time.sleep(1)
            wait("MEMASUKI MENU USER")
            main_user()
            break  
        else:
            red("USERNAME ATAU PASSWORD SALAH")
            time.sleep(1)
            main()

# ---------------------------------------------------------------[Menu]-----------------------------------------------------------------------
def main_admin():
    clear()
    while True:
        logo()
        print('SELAMAT DATANG DI MENU ADMIN FARMATECH'.center(98))
        pagar()
        print("""
1. Kelola User
2. Kelola Data Alat
3. Kelola Data Bahan
4. Kelola Informasi
5. Lihat Peminjaman
6. Lihat Laporan
7. Pembaharuan Alat
8. Pembaharuan Bahan
9. Log Out
        """)
        try:
            pilih = int(input("Silahkkan Pilih Menu:"))
            if pilih == 1:
                wait("MEMASUKI KELOLA USER")
                kelola_user()
                break
            elif pilih == 2:
                wait("MEMASUKI KELOLA ALAT") 
                Kelola_alat()
                break
            elif pilih == 3: 
                wait("MEMASUKI KELOLA BAHAN") 
                Kelola_bahan()
                break
            elif pilih == 4:
                wait("MEMASUKI KELOLA INFORMASI") 
                kelola_informasi()
                break
            elif pilih == 5:
                wait("MEMASUKI LIHAT PEMINJAMAN") 
                lihat_minjam()
            elif pilih == 6:
                wait("MEMASUKI MENU LIHAT LAPORAN") 
                laporan()
                break
            elif pilih == 7:
                wait("MEMASUKI PEMBAHARUAN ALAT") 
                pembaharuan_alat()
                break
            elif pilih == 8:
                wait("MEMASUKI PEMBAHARUAN BAHAN") 
                pembaharuan_bahan()
                break
            elif pilih == 9:
                wait("SELAMAT ISTIRAHAT TUAN ADMIN!") 
                main()
                break
            else:
                clear()
                continue
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def main_user():
    while True:
        clear()
        logo()
        print("SELAMAT DATANG DI MENU FARMATECH".center(98))
        pagar()
        print("""
1. Meminjam
2. Mengembalikan Alat
3. Lihat Stock
4. Lihat Informasi
5. Lihat Peminjaman
6. Log out
""")
        try:
            pilih = int(input("Silahkkan Pilih Menu:"))

            if pilih == 1: 
                wait("MEMASUKI MENU MINJAM") 
                menu_minjam()
                break
            elif pilih == 2:
                wait("MEMASUKI MENGEMBALIKAN ALAT") 
                kembalikan()
                break
            elif pilih == 3: 
                wait("MEMASUKI MENU LIHAT STOCK") 
                lihat_stock()
            elif pilih == 4:
                wait("MEMASUKI MENU LIHAT INFORMASI") 
                lihat_informasi()
            elif pilih == 5:
                wait("MEMASUKI MENU LIHAT INFORMASI") 
                lihat_minjam()
            elif pilih == 6:
                wait("SELAMAT TINGGAL, TERIMAKASIH TELAH MENGGUNAKAN FARMATECH") 
                main()
                break
            else:
                clear()
                continue
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

# -------------------------------------------------------------[Fitur]-----------------------------------------------------------------------------

def menu_minjam():
    while True:
        clear()
        logo()
        print("MENU MINJAM".center(98))
        pagar()
        print("""
1. Alat
2. Bahan
3. Back
""")
        try:
            pilih = int(input("Masukkan pilihan peminjaman: "))
            if pilih == 1:
                pinjam_alat()
                break
            elif pilih == 2:
                pinjam_bahan()
                break
            elif pilih == 3:
                main_user()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def pinjam_alat():
    while True:
        clear()
        logo()
        header = ["NO","NAMA ALAT", "TAHUN ALAT", "KETERSEDIAAN", "STATUS", "LOKASI"]
        data = []
        with open('CSV/alat.csv', 'r', newline="") as f:
            reader = csv.reader(f)  
            for row in reader:
                data.append(row)
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center', showindex=range(1,len(data)+1)))
        
        try:
            pilih = int(input("Silahkan pilih barang yang ingin di pinjam: "))
            if data[pilih-1][2] == 'Tidak' or data[pilih-1][3] == 'Rusak':
                red("ALAT TIDAK DAPAT DIPINJAM")
                menu_minjam()
                break
            else:
                tujuan = input("Apa Tujuan Peminjaman Alat: ").capitalize()
                if tujuan in ("Penelitian","Matkul"):
                    tampung = []
                    tampung.append(username)
                    tampung.append(data[pilih-1][0])
                    x = dt.datetime.now()
                    waktu = x.strftime("%d-%m-%y %H:%M %p")
                    tampung.append(waktu)
                    tampung.append(data[pilih-1][3])
                    tampung.append(tujuan)
                    with open('CSV/pinjam alat.csv', mode='a', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(tampung)
                    data[pilih-1][2] = "Tidak"
                    with open ('CSV/alat.csv',mode='w') as f:
                        penampung = []
                        for i in data:
                            data_baru = ','.join(i)
                            penampung.append(data_baru)
                        for item in penampung:
                            f.write(f"{item}\n")
                    green("ALAT BERHASIL DIPINJAM")
                    menu_minjam()
                    break
                else:
                    red("TUJUAN PEMINJAMAN TIDAK DITERIMA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def pinjam_bahan():
    while True:
        clear()
        logo()
        header = ["NO","NAMA BAHAN", "TANGGAL KADALUARSA", "JUMLAH (liter)", "LOKASI"]
        data = []
        sekarang = dt.datetime.now()
        with open('CSV/bahan.csv', 'r', newline="") as f:
            reader = csv.reader(f)  
            for row in reader:
                data.append(row)
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center', showindex=range(1,len(data)+1)))
        try:
            try:
                pilih = int(input("Silahkan PIlih Bahan Yang Ingin Dipinjam: "))
                kadaluarsa = dt.datetime.strptime(data[pilih-1][1], "%d-%m-%y")
                if sekarang >= kadaluarsa or int(data[pilih-1][2]) == 0:
                    red("BAHAN TIDAK DAPAT DIPINJAM")
                else:
                    tujuan = input("Apa Tujuan Peminjaman Bahan: ").capitalize()
                    if tujuan in ('Penelitian','Matkul'):
                        tampung = []
                        tampung.append(username)
                        tampung.append(data[pilih-1][0])
                        tampung.append(sekarang.strftime("%d-%m-%y"))
                        try:
                            berapa = int(input("Masukkan Jumlah (Liter) Bahan yang Ingin Dipinjam: "))
                            if berapa > int(data[pilih-1][2]):
                                red(f"BAHAN HANYA TERSEDIA {data[pilih-1][2]}")
                            else:
                                tampung.append(berapa)
                                tampung.append(tujuan)
                                with open('CSV/pinjam bahan.csv', mode='a', newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow(tampung)
                                with open('CSV/bahan.csv', mode='w',newline='') as f:
                                    penampung = []
                                    data[pilih-1][2] = int(data[pilih-1][2]) - berapa
                                    for i in data:
                                        data_baru = ','.join(map(str, i))
                                        penampung.append(data_baru)
                                    for item in penampung:
                                        f.write(f"{item}\n")                            
                                green("BAHAN BERHASIL DIPINJAM")
                                menu_minjam()        
                                break
                        except ValueError: 
                            lightred("INPUTAN TIDAK VALID")
                            continue
                    else:
                        red("TUJUAN PEMINJAMAN TIDAK DITERIMA")
            except IndexError:
                lightred("PILIHAN TIDAK ADA")
                continue
        except ValueError: 
            lightred("INPUTAN TIDAK VALID")
            continue
    
def kembalikan():
    while True:
        clear()
        logo()
        header_pinjam = ["NO", "MAHASISWA", "ALAT","TANGGAL PEMINJAMAN","STATUS ALAT","TUJUAN PEMINJAMAN"]
        header_alat = ["NO","Nama Alat", "Tahun Alat", "Ketersediaan", "Status", "Lokasi"]
        data_pinjam = [] 
        data_alat = [] 
        with open('CSV/alat.csv', mode='r', newline="") as f:
            reader = csv.reader(f)  
            for row in reader:
                data_alat.append(row)
        with open("CSV/pinjam alat.csv", mode='r',newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data_pinjam.append(row)
        if len(data_pinjam) == 0:
            yellow("DATA PEMINJAMAN ALAT KOSONG")
            main_user()
            break
        else:
            print(tabulate(data_pinjam,headers=header_pinjam,tablefmt='simple_outline',stralign='center',showindex=range(1,len(data_pinjam)+1)))
            try:
                kembali = int(input("Pilih Alat yang ingin di kembalikan: "))
                if data_pinjam[kembali-1][0] != username:
                    red("BUKAN ALAT YANG ANDA PINJAM")
                    kembalikan()
                else:
                    try:
                        print(tabulate(data_alat, headers=header_alat,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data_alat)+1)))
                        taruh = int(input('Tolong Taruh Alat Pada Tempat Semula: '))
                        if data_pinjam[kembali-1][1] == data_alat[taruh-1][0]:
                            kondisi = input("Masukkan Kondisi Alat Setelah Peminjaman [Aman/Rusak]: ").capitalize()
                            if kondisi in ('Aman','Rusak'):
                                data_alat[taruh-1][2] = 'Ada'
                                data_alat[taruh-1][3] = kondisi
                                with open('CSV/alat.csv', mode='w',newline='') as f:
                                    penampung_alat = []
                                    for i in data_alat:
                                        data_alat_baru = ','.join(i)
                                        penampung_alat.append(data_alat_baru)
                                    for item in penampung_alat:
                                        f.write(f"{item}\n")
                                laporan = []
                                laporan.append(username) 
                                laporan.append(data_alat[taruh-1][0]) #alat
                                laporan.append(data_pinjam[kembali-1][2]) #tanggal minjam
                                laporan.append(data_alat[taruh-1][4]) #lokasi
                                laporan.append(data_pinjam[kembali-1][4]) #tujuan
                                with open("CSV/laporan peminjaman.csv",mode='a',newline='') as f:
                                    writer = csv.writer(f)
                                    writer.writerow(laporan)
                                with open('CSV/pinjam alat.csv', mode='w',newline='') as f:
                                    data_pinjam.pop(kembali-1)
                                    penampung_pinjam = [] 
                                    for i in data_pinjam:
                                        data_pinjam_baru = ','.join(i)
                                        penampung_pinjam.append(data_pinjam_baru)
                                    for item in penampung_pinjam:
                                        f.write(f"{item}\n")
                                green("ALAT BERHASIL DIKEMBALIKAN")
                                main_user()
                            else:
                                red("MASUKKAN KONDISI ALAT [AMAN/RUSAK]")
                                continue
                        else:
                            red('TARUH ALAT PADA TEMPAT YANG BENAR')
                            continue
                    except ValueError:
                        lightred("INPUTAN TIDAK VALID")
                        continue
            except IndexError:
                lightred("PILIHAN TIDAK ADA")
                continue

def lihat_stock():
    while True:
        clear()
        logo()
        print("MENU STOCK".center(98))
        pagar()
        print("""
1. Stock Alat
2. Stock Bahan
3. Back
""")
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                lihat_alat()
            elif pilihan == 2:
                lihat_bahan()
            elif pilihan == 3:
                main_user()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def lihat_minjam():
    while True:
        clear()
        logo()
        print("MENU LIHAT MINJAM".center(98))
        pagar()
        print("""
1. Lihat Peminjaman Alat
2. Lihat Peminjaman Bahan
3. Back
""")
        try:
            pilihan = int(input("Masukkan Pilihan Menu Lihat Peminjaman: "))
            if pilihan == 1:
                header = ["NO", "MAHASISWA", "ALAT","TANGGAL PEMINJAMAN","STATUS ALAT","TUJUAN PEMINJAMAN"]
                data = []

                with open("CSV/pinjam alat.csv", mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                if len(data) == 0:
                    yellow("DATA PEMINJAMAN ALAT KOSONG")
                else:
                    clear()
                    logo()
                    print(tabulate(data,headers=header,tablefmt='simple_outline',stralign='center',showindex=range(1,len(data)+1)))
                    input("Tekan Enter Untuk Kembali")
                    time.sleep(1)
                    break
            elif pilihan == 2:
                header = ["NO", "MAHASISWA", "BAHAN","TANGGAL PEMINJAMAN","TANGGAL KADALUARSA","TUJUAN PEMINJAMAN"]
                data = []
                with open("CSV/pinjam bahan.csv", mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                if len(data) == 0:
                    yellow("DATA PEMINJAMAN BAHAN KOSONG")
                else:
                    clear()
                    logo()
                    print(tabulate(data,headers=header,tablefmt='simple_outline',stralign='center',showindex=range(1,len(data)+1)))
                    input("Tekan Enter Untuk Kembali")
                    time.sleep(1)
                    clear()
                    break
            elif pilihan == 3:
                clear()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

# ======================================================[Kelola Stock Alat]=========================================================================
def Kelola_alat():
    while True:
        clear()
        logo()
        print("MENU KELOLA DATA".center(98))
        pagar()
        print("""
1. Tambah Data Alat
2. Hapus Data Alat
3. Update Data Alat
4. Lihat Data Alat
5. Back
""")
        try:
            pilih = int(input("Silahkkan Pilih Menu:"))
            if pilih == 1:
                tambah_alat()
                break
            elif pilih == 2:
                hapus_alat()
                break
            elif pilih == 3:
                update_alat()
                break
            elif pilih == 4:
                lihat_alat()
            elif pilih == 5:
                main_admin()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def tambah_alat():
    while True:
        clear()
        logo()
        data = []
        nama_alat = input("Masukkan Nama Alat: ").capitalize()
        data.append(nama_alat)
        tahun_alat = input("Masukkan Tahun Alat: ")
        data.append(tahun_alat)
        data.append("Ada")
        status_alat = input("Masukkan Status Alat [Aman/Rusak]: ").capitalize()
        if status_alat in ("Aman","Rusak"):
            data.append(status_alat)
            lokasi_alat = input("Masukkan Lokasi Alat [A/B/C]: ").capitalize()
            if lokasi_alat in ("A","B","C"):
                data.append(lokasi_alat)
                with open("CSV/alat.csv", mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                green("ALAT BERHASIL DITAMBAHKAN")
                Kelola_alat()
                break
            else:
                red("PILIH RAK LOKASI [A/B/C]")
        else:
            red("PILIH STATUS [AMAN/RUSAK]")

def hapus_alat():
    while True:
        clear()
        logo()
        header = ["NO","NAMA ALAT", "TAHUN ALAT", "KETERSEDIAAN", "STATUS", "LOKASI"]
        data = []
        with open('CSV/alat.csv', mode='r', newline='') as f:    
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA ALAT YANG TERSEDIA")
            Kelola_alat()
            break
        else:
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
            try:
                hapus = int(input("pilih bahan yang ingin dihapus: "))
                if hapus < 1 or hapus > len(data):
                    red("PILIHAN TIDAK ADA")
                else:
                    data.pop(hapus - 1)
                    with open('CSV/alat.csv', mode='w', newline='') as f:
                        penampung = []
                        for i in data:
                            data_baru = ','.join(i)
                            penampung.append(data_baru)
                        for item in penampung:
                            f.write(f"{item}\n")
                    green("ALAT BERHASIL DIHAPUS")
                    Kelola_alat()
                    break
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue

def update_alat(): 
    while True:
        clear()
        logo()
        header = ["NO","NAMA ALAT", "TAHUN ALAT", "KETERSEDIAAN", "STATUS", "LOKASI"]
        data = []

        with open('CSV/alat.csv', mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA ALAT YANG TERSEDIA")
            Kelola_alat()
            break
        else:
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
            try:
                ubah = int(input("Pilih Urutan Alat yang ingin di update:"))
                if ubah < 1 or ubah > len(data):
                    red("PILIHAN TIDAK ADA")
                else:
                    if data[ubah-1][2] == 'Tidak':
                        red("ALAT TIDAK DAPAT DIUBAH")
                    else:
                        data[ubah-1][0] = input("Masukkan Nama Alat: ").capitalize()
                        data[ubah-1][1] = input("Masukkan Tahun Alat: ").capitalize()
                        status = input("Masukkan Status Alat [Aman/Rusak]: ").capitalize()
                        if status in ("Aman","Rusak"):
                            data[ubah-1][3] = status
                            lokasi = input("Masukkan Lokasi Alat [A/B/C]:").capitalize()
                            if lokasi in ("A","B","C"):
                                data[ubah-1][4] = lokasi
                                penampung = []
                                with open("CSV/alat.csv", mode='w', newline='') as f:
                                    for i in data:
                                        data_baru = ','.join(i)
                                        penampung.append(data_baru)
                                    for item in penampung:
                                        f.write(f"{item}\n")
                                green("ALAT BERHASIL DIUPDATE")
                                Kelola_alat()
                                break
                            else:
                                red("PILIHAN LOKASI ALAT [A/B/C]")
                        else:
                            red("PILIH STATUS ALAT [AMAN/RUSAK]")
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue

def lihat_alat():
    while True:
        clear()
        logo()
        header = ["NO","NAMA ALAT", "TAHUN ALAT", "KETERSEDIAAN", "STATUS", "LOKASI"]
        data = []
            
        with open('CSV/alat.csv', mode='r', newline="") as f:
            reader = csv.reader(f)  
            for row in reader:
                data.append(row)
            if len(data) == 0:
                yellow("TIDAK ADA ALAT YANG TERSEDIA")
                Kelola_alat()
                break
            else:
                clear()
                logo()
                print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
                input("Tekan Enter Untuk Kembali")
                time.sleep(1)
                break


# =============================================================[Kelola Stock Bahan]=========================================
def Kelola_bahan(): 
    while True:
        clear()
        logo()
        print("MENU KELOLA BAHAN".center(98))
        pagar()
        print("""
1. Tambah Data bahan
2. Hapus Data bahan
3. Update Data bahan
4. Lihat Data bahan
5. Back
""")
        try:
            pilih = int(input("Silahkkan Pilih Menu:"))
            if pilih == 1:
                tambah_bahan()
                break
            elif pilih == 2:
                hapus_bahan()
                break
            elif pilih == 3:
                update_bahan()
                break
            elif pilih == 4:
                lihat_bahan()
            elif pilih == 5:
                main_admin()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def tambah_bahan():
    while True:
        clear()
        logo()
        data = []
        nama_bahan = input("Masukkan Nama bahan: ").upper()
        data.append(nama_bahan)
        x = dt.datetime.now()
        waktu = x + dt.timedelta(days=7)
        data.append(waktu.strftime("%d-%m-%y"))
        try:
            jumlah_bahan = int(input("Masukkan jumlah literan bahan: "))
            data.append(jumlah_bahan)
            lokasi_bahan = input("Masukkan Lokasi bahan [A/B/C]: ").capitalize()
            if lokasi_bahan in ("A","B","C"):
                data.append(lokasi_bahan)
                with open("CSV/bahan.csv", mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                green("BAHAN BERHASIL DITAMBAHKAN")
                Kelola_bahan()
                break
            else:
                red("PILIH LOKASI BAHAN [A/B/C]")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def hapus_bahan():
    while True:
        clear()
        logo()
        header = ["NO","NAMA BAHAN", "TANGGAL KADALUARSA", "JUMLAH (liter)", "LOKASI"]
        data = []
        with open('CSV/bahan.csv', mode='r', newline='') as f:    
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA BAHAN YANG TERSEDIA")
            Kelola_bahan()          
        else:
            print(tabulate(data,headers=header,tablefmt='rounded_outline', stralign='center',showindex=range(1,len(data)+1)))

            try:
                hapus = int(input("pilih informasi yang ingin dihapus: "))
                if hapus < 1 or hapus > len(data):
                    termcolor.cprint("Inputan Tidak Valid", 'red')
                else:
                    data.pop(hapus - 1)
                    with open('CSV/bahan.csv', mode='w', newline='') as f:
                        penampung = []
                        for i in data:
                            data_baru = ','.join(i)
                            penampung.append(data_baru)
                        for item in penampung:
                            f.write(f"{item}\n")
                    green("BAHAN BERHASIL DIHAPUS")
                    Kelola_bahan()
                    break
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue

def update_bahan():
    while True:
        clear()
        logo()
        header = ["NO","NAMA BAHAN", "TANGGAL KADALUARSA", "JUMLAH (liter)", "LOKASI"]
        data = []
        penampung = []
            
        with open('CSV/bahan.csv', mode='r', newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA BAHAN YANG TERSEDIA")
            Kelola_bahan()
            break    
        else:
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))

            try:
                ubah = int(input("Masukkan Bahan yang ingin diubah: "))
                if ubah < 1 or ubah > len(data):
                    red("PILIHAN TIDAK ADA")
                else:
                    data[ubah-1][0] = input('Masukkan Nama Bahan: ').upper()
                    lokasi = input("Masukkan Lokasi Bahan: ").capitalize()
                    if lokasi in ("A","B","C"):
                        data[ubah-1][3] = lokasi
                        with open("CSV/bahan.csv", mode='w', newline='') as f:
                            for i in data:
                                data_baru = ','.join(map(str, i))
                                penampung.append(data_baru)
                            for item in penampung:
                                f.write(f"{item}\n")
                        green("BAHAN BERHASIL DI UPDATE")
                        Kelola_bahan()
                        break
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue

def lihat_bahan():
    clear()
    logo()
    header = ["NO","NAMA BAHAN", "TANGGAL KADALUARSA", "JUMLAH (liter)", "LOKASI"]
    data = []
        
    with open('CSV/bahan.csv', mode='r', newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    if len(data) == 0:
        yellow("TIDAK ADA BAHAN YANG TERSEDIA") 
    else:     
        clear()
        logo()
        print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
        input("Tekan Enter Untuk Kembali")
        time.sleep(1)

# ===========================================================================[Kelola Informasi]====================================================
def kelola_informasi():
    clear()
    while True:
        logo()
        print("MENU KELOLA INFORMASI".center(98))
        pagar()
        print("""
1. Tambah Informasi
2. Hapus Informasi
3. Update Informasi
4. Lihat Informasi
5. Back
""")
        try:
            pilih = int(input("Silahkkan Pilih Menu:"))
            if pilih == 1:
                tambah_informasi()
                break
            elif pilih == 2:
                hapus_informasi()
                break
            elif pilih == 3:
                update_informasi()
                break
            elif pilih == 4:
                lihat_informasi()
            elif pilih == 5:
                main_admin()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def tambah_informasi():
    while True:
        clear() 
        logo()
        print("MENU TAMBAH INFORMASI".center(98))
        pagar()
        print("""
1. Informasi Alat
2. Informasi Bahan
3. Back
""")
        try:
            pilihan = int(input("Pilih Informasi: "))
            if pilihan == 1:
                clear()
                logo()
                data = []
                nama_alat = input("Masukkan nama alat: ").capitalize()
                deskripsi_alat = input("Tambahkan deksripsi alat: ")
                data.append(nama_alat)
                data.append(deskripsi_alat)
                with open('CSV/informasi alat.csv', mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                green("INFORMASI BERHASIL DITAMBAHKAN")
            elif pilihan == 2:
                clear()
                logo()
                data = []
                nama_bahan = input("Masukkan nama bahan: ").capitalize()
                deskripsi_bahan = input("Tambahkan deksripsi bahan: ")
                data.append(nama_bahan)
                data.append(deskripsi_bahan)
                with open('CSV/informasi bahan.csv', mode='a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data)
                green("INFORMASI BERHASIL DITAMBAHKAN")
            elif pilihan == 3:
                kelola_informasi()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def lihat_informasi(): 
    while True:
        clear()
        logo()
        print("MENU LIHAT INFORMASI".center(98))
        pagar()
        print("""
1. Informasi Alat
2. Informasi Bahan
3. Back
""")
        try:
            pilihan = int(input("Pilih Menu Lihat Informasi: "))
            if pilihan == 1:
                clear()
                logo()
                header = ["NO","ALAT","DESKRIPSI"]
                data = []
                with open("CSV/informasi alat.csv", mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                if len(data) == 0:
                    yellow("TIDAK ADA INFORMASI")
                else: 
                    clear()
                    logo()
                    print(tabulate(data,headers=header,tablefmt='simple_outline', stralign='left',showindex=range(1,len(data)+1)))
                    input("Tekan Enter Untuk Kembali")
                    time.sleep(1)
            elif pilihan == 2:
                clear()
                logo()
                header = ["NO","BAHAN","DESKRIPSI"]
                bahan = []
                with open("CSV/informasi bahan.csv", mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        bahan.append(row)
                if len(bahan) == 0:
                    yellow("TIDAK ADA INFORMASI")
                else:    
                    clear()
                    logo()
                    print(tabulate(bahan,headers=header,tablefmt='simple_outline', stralign='left',showindex=range(1,len(bahan)+1)))
                    input("Tekan Enter Untuk Kembali")
                    time.sleep(1)
            elif pilihan == 3:
                clear()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def update_informasi(): 
    while True:
        clear()
        logo()
        print("MENU UPDATE INFORMASI".center(98))
        pagar()
        print("""
1. Update Informasi Alat
2. Update Informasi Bahan
3. Back
""")
        try:
            pilihan = int(input("Pilih Menu Update Informasi: "))
            if pilihan == 1:
                header = ["NO","NAMA ALAT", "DEKSRIPSI"]
                data = []
                with open('CSV/informasi alat.csv', mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                    if len(data) == 0:
                        yellow("TIDAK ADA INFORMASI")
                    else:
                        clear()
                        logo()    
                        print(tabulate(data,headers=header,tablefmt='simple_outline',stralign='left',showindex=range(1,len(data)+1)))
                        try:
                            ubah = int(input("Pilih Informasi Alat yang diubah: "))
                            if ubah < 1 or ubah > len(data):
                                red("PILIHAN TIDAK ADA")
                            else:
                                data[ubah-1][0] = input("Masukkan Nama Alat: ")
                                data[ubah-1][1] = input("Masukkan Deskripsi Alat: ")
                                green("INFORMASI ALAT BERHASIL DIUPDATE")
                        except ValueError:
                            lightred("INPUTAN TIDAK VALID")
                            continue
            elif pilihan == 2:
                header = ["NO","NAMA BAHAN",'DESKRIPSI']
                data = []
                with open("CSV/informasi bahan.csv", mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                    if len(data) == 0:
                        yellow("TIDAK ADA INFORMASI")
                    else: 
                        clear()
                        logo()   
                        print(tabulate(data,headers=header,tablefmt='simple_outline',stralign='left',showindex=range(1,len(data)+1)))
                        try:
                            ubah = int(input("Pilih Informasi Bahan yang diubah: "))
                            if ubah < 1 or ubah > len(data):
                                red("PILIHAN TIDAK ADA")
                            else:
                                data[ubah-1][0] = input("Masukkan Nama Bahan: ")
                                data[ubah-1][1] = input("Masukkan Deksripsi Bahan: ")
                                green("INFORMASI ALAT BERHASIL DIUPDATE")
                        except ValueError:
                            lightred("INPUTAN TIDAK VALID")
                            continue
            elif pilihan == 3:
                kelola_informasi()
                break
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def hapus_informasi(): 
    while True:
        clear()
        logo()
        print("MENU HAPUS INFORMASI".center(98))
        pagar()
        print("""
1. Hapus Informasi Alat
2. Hapus Informasi Bahan
3. Back
""")
        try:
            pilihan = int(input("Pilih Menu Hapus Informasi: "))
            if pilihan == 1:
                header = ["NO","NAMA ALAT", "DEKSRIPSI"]
                data = []
                with open('CSV/informasi alat.csv', mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                    if len(data) == 0:
                        yellow("TIDAK ADA INFORMASI")
                        hapus_informasi()
                        break
                    else:                            
                        clear()
                        logo()
                        print(tabulate(data,headers=header,tablefmt="simple_outline",stralign='left',showindex=range(1,len(data)+1)))
                    try:
                        hapus = int(input("pilih informasi yang ingin dihapus: "))
                        if hapus < 1 or hapus > len(data):
                            termcolor.cprint("Inputan Tidak Valid", 'red')
                        else:
                            data.pop(hapus - 1)
                            with open("CSV/informasi alat.csv", mode='w', newline='') as f:
                                penampung = []
                                for i in data:
                                    data_baru = ','.join(i)
                                    penampung.append(data_baru)
                                for item in penampung:
                                    f.write(f"{item}\n")
                            green("INFORMASI ALAT BERHASIL DIHAPUS")
                    except ValueError:
                        lightred("INPUTAN TIDAK VALID")
                        continue

            elif pilihan == 2:
                header = ["NO","NAMA BAHAN", "DEKSRIPSI"]
                data = []
                with open('CSV/informasi bahan.csv', mode='r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        data.append(row)
                    if len(data) == 0:
                        yellow("TIDAK ADA INFORMASI")
                        hapus_informasi()
                        break
                    else:               
                        clear()
                        logo()             
                        print(tabulate(data,headers=header,tablefmt="simple_outline",stralign='left',showindex=range(1,len(data)+1)))

                        try:
                            hapus = int(input("pilih informasi yang ingin dihapus: "))
                            if hapus < 1 or hapus > len(data):
                                red("PILIHAN TIDAK ADA")
                            else:
                                data.pop(hapus - 1)
                                with open("CSV/informasi bahan.csv", mode='w', newline='') as f:
                                    penampung = []
                                    for i in data:
                                        data_baru = ','.join(i)
                                        penampung.append(data_baru)
                                    for item in penampung:
                                        f.write(f"{item}\n")
                                green("INFORMASI BAHAN BERHASIL DIHAPUS")
                        except ValueError:
                            lightred("INPUTAN TIDAK VALID")
                            continue
            elif pilihan == 3:
                kelola_informasi()
                break
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue
# ============================================================================[Kelola User]==========================================================
def kelola_user():
    while True:
        clear()
        logo()
        print("MENU KELOLA USER".center(98))
        pagar()
        print("""
1. Tambah user
2. Hapus user
3. Lihat user
4. Back
""")
        try:
            pilih = int(input("Silahkkan Pilih Menu:"))
            if pilih == 1:
                tambah_user()
                break
            elif pilih == 2:
                hapus_user()
                break
            elif pilih == 3:
                lihat_user()
                break
            elif pilih == 4:
                main_admin()
                break
            else:
                red("PILIHAN TIDAK ADA")
                continue
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def tambah_user():
    clear()
    logo()
    data = []
    username = input("Masukkan Username Mahasiswa: ")
    password = input("Masukkan Password Mahasiswa: ")
    nim = input("masukkan 4 digit NIM: ")
    if len(nim) == 4:
        telepon = input("Masukkan no telepon mahasiswa: ")
        if len(telepon) == 12:
            data.append(username)
            data.append(password)
            with open('CSV/pengguna.csv', mode='a', newline='') as f:
                write = csv.writer(f)
                write.writerow(data)
            identitas = []
            identitas.append(username)
            identitas.append(nim)
            identitas.append(telepon)
            with open("CSV/identitas.csv", mode='a', newline='') as f:
                write = csv.writer(f)
                write.writerow(identitas)
            green("USER BERHASIL DITAMBAHKAN")
            kelola_user()
        else:
            red("No Telepon harus 12 digit")
            tambah_user()
    else:
        red("NIM harus 4 digit")
        tambah_user()

def lihat_user():
    clear()
    logo()
    header =["NO","USERNAME","PASSWORD"]
    header =["NO","USERNAME","NIM", "NO TELEPON"]
    data = []
    identitas = []
    with open("CSV/pengguna.csv", mode="r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    with open("CSV/identitas.csv", mode="r", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            identitas.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA USER")
            kelola_user()
        else:
            clear()
            logo()
            print(tabulate(data, headers=header, tablefmt='mixed_outline', stralign='center',showindex=range(1,len(data)+1)))
            print(tabulate(identitas, headers=header, tablefmt='mixed_outline', stralign='center',showindex=range(1,len(data)+1)))
            input("Tekan Enter Untuk Kembali")
            time.sleep(1)
            clear()
            kelola_user()

def hapus_user():
    while True:
        clear()
        logo()
        header_akun =["NO","USERNAME","PASSWORD"]
        header_identitas = ["NO","USERNAME","NIM","NO TELEPON"]
        data_akun = []
        data_identitas = []
        with open("CSV/pengguna.csv", mode="r", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data_akun.append(row)
        with open("CSV/identitas.csv", mode='r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                data_identitas.append(row)
        if len(data_akun) == 0:
            yellow("TIDAK ADA USER")
            kelola_user()
            break
        else:
            print(tabulate(data_akun, headers=header_akun, tablefmt='mixed_outline', stralign='center',showindex=range(1,len(data_akun)+1)))
            print(tabulate(data_identitas, headers=header_identitas, tablefmt='mixed_outline', stralign='center',showindex=range(1,len(data_akun)+1)))
            try:
                hapus = int(input("Hapus Username urutan mana: "))
                if hapus < 1 or hapus > len(data_akun):
                    red("PILIHAN TIDAK ADA")
                else:
                    data_akun.pop(hapus - 1)
                    with open("CSV/pengguna.csv", mode='w', newline='') as f:
                        tampungan = []
                        for i in data_akun:
                            dataakun_baru = ','.join(i)
                            tampungan.append(dataakun_baru)
                        for item in tampungan:
                            f.write(f"{item}\n")
                    data_identitas.pop(hapus-1)
                    with open("CSV/identitas.csv", mode='w', newline='') as f:
                        penampung = []
                        for i in data_identitas:
                            dataidentitas_baru = ','.join(i)
                            penampung.append(dataidentitas_baru)
                        for item in penampung:
                            f.write(f"{item}\n")
                    green("USERNAME BERHASIL DIHAPUS")
                    kelola_user()
                    break
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue
            

# ==========================================================[Fitur Khusus Admin]===================================================================
def pembaharuan_alat():
    while True:
        clear()
        logo()
        data = []
        header = ["NO","NAMA ALAT", "TAHUN ALAT", "KETERSEDIAAN", "STATUS", "LOKASI"]

        with open('CSV/alat.csv', mode='r', newline="") as f:
            reader = csv.reader(f)  
            for row in reader:
                data.append(row)
            if len(data) == 0:
                yellow("TIDAK ADA ALAT YANG TERSEDIA")           
            else:
                print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
                try:
                    pilih = int(input("Pilih Alat Yang Ingin Di Perbaharui: "))
                    if data[pilih-1][3] == 'Aman' or data[pilih-1][2] == 'Tidak':
                        red("ALAT TIDAK DAPAT DIPERBAHARUI")
                        main_admin()
                    else:
                        alasan = input("Alasan Pembaharuan: ").capitalize()
                        data[pilih-1][3] = 'Aman'
                        penampung = []
                        with open("CSV/alat.csv", mode='w', newline='') as f:
                            for i in data:
                                data_baru = ','.join(i)
                                penampung.append(data_baru)
                            for item in penampung:
                                f.write(f"{item}\n")

                        waktu = dt.datetime.now()
                        laporan = []
                        laporan.append(data[pilih-1][0])
                        laporan.append(alasan)
                        laporan.append(waktu.strftime("%d-%m-%y"))
                        with open("CSV/laporan pembaharuan.csv", mode='a',newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(laporan)
                        green("ALAT BERHASIL DIPERBAHARUI")
                        main_admin()
                        break
                except ValueError:
                    lightred("INPUTAN TIDAK VALID")
                    continue
                

def pembaharuan_bahan():
    while True:
        clear()
        logo()
        print("MENU PEMBAHARUAN BAHAN")
        pagar()
        print("""
1. Kadaluarsa
2. Refill
3. Back
""")
        try:
            pilihan = int(input("Masukkan Pilihan Menu Pembaharuan Bahan: "))
            if pilihan == 1:
                kadaluarsa()
                break
            elif pilihan == 2:
                habis()
                break
            elif pilihan == 3:
                main_admin()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue
            
def kadaluarsa():
    while True:
        clear()
        logo()
        header = ["NO","NAMA BAHAN", "TANGGAL KADALUARSA", "JUMLAH (liter)", "LOKASI"]
        data = []
        with open('CSV/bahan.csv', mode='r', newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA BAHAN YANG TERSEDIA")
        else:     
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
            try:
                pilih = int(input("Masukkan Bahan Yang Kadaluarsa: "))
                liter = int(data[pilih-1][2])
                if liter > 0:
                    sekarang = dt.datetime.now()
                    kadaluarsa = dt.datetime.strptime(data[pilih-1][1], "%d-%m-%y")
                    if sekarang >= kadaluarsa:
                        alasan = input("Alasan Pembaharuan: ").capitalize()
                        kadaluarsa = sekarang + dt.timedelta(days=7)
                        data[pilih-1][1]= kadaluarsa.strftime("%d-%m-%y")
                        penampung = []
                        with open("CSV/bahan.csv", mode='w', newline='') as f:
                            for i in data:
                                data_baru = ','.join(i)
                                penampung.append(data_baru)
                            for item in penampung:
                                f.write(f"{item}\n")
                        laporan = []
                        laporan.append(data[pilih-1][0])
                        laporan.append(alasan)
                        laporan.append(sekarang.strftime("%d-%m-%y"))
                        with open("CSV/laporan kadaluarsa.csv", mode='a',newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(laporan)
                        green("BAHAN BERHASIL DIGANTI")
                        pembaharuan_bahan()
                        break
                    else:
                        red("BAHAN TIDAK KADALUARSA")
                        pembaharuan_bahan()
                        break
                else:
                    red("BAHAN HABIS")
                    pembaharuan_bahan()
                    break
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue
    
def habis():
    while True:
        clear()
        logo()
        header = ["NO","NAMA BAHAN", "TANGGAL KADALUARSA", "JUMLAH (liter)", "LOKASI"]
        data = []
        sekarang = dt.datetime.now()


        with open('CSV/bahan.csv', mode='r', newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA BAHAN YANG TERSEDIA")
        else:     
            print(tabulate(data, headers=header,tablefmt="rounded_outline", stralign='center',showindex=range(1,len(data)+1)))
            try:
                pilih = int(input("Bahan Yang Ingin di Refill"))
                kadaluarsa = dt.datetime.strptime(data[pilih-1][1], "%d-%m-%y")
                if sekarang >= kadaluarsa:
                    red("BAHAN KADALUARSA")
                    pembaharuan_bahan()
                    break
                else:
                    habis = int(data[pilih-1][2])
                    if habis < 2:
                        nambah = int(input("Mau Tambah Berapa?: "))
                        if nambah <= 0:
                            red("TIDAK BISA REFILL 0 LITER")
                        else:
                            data[pilih-1][2] = nambah + habis
                            penampung = []
                            with open("CSV/bahan.csv", mode='w', newline='') as f:
                                for i in data:
                                    data_baru = ','.join(map(str, i))
                                    penampung.append(data_baru)
                                for item in penampung:
                                    f.write(f"{item}\n")
                            laporan = []
                            laporan.append(data[pilih-1][0])
                            laporan.append(nambah)
                            laporan.append(sekarang.strftime("%d-%m-%y"))
                            with open("CSV/laporan habis.csv", mode='a',newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(laporan)
                            green("BAHAN BERHASIL DIGANTI")
                            pembaharuan_bahan()
                            break
                    else:
                        red("BAHAN MASIH BANYAK")
                        pembaharuan_bahan()
                        break
            except ValueError:
                lightred("INPUTAN TIDAK VALID")
                continue

def laporan():
    clear()
    while True:
        logo()
        print("MENU LAPORAN".center(98))
        pagar()
        print("""
1. Laporan Peminjaman
2. Laporan Pembaharuan Alat
3. Laporan Kadaluarsa Bahan
4. Laporan Refill Bahan
5. Back
    """)
        try:
            pilihan = int(input("Silahkan PIlih Menu Laporan: "))
            if pilihan == 1:
                laporan_peminjaman()
                break
            elif pilihan == 2:
                laporan_service()
                break
            elif pilihan == 3:
                laporan_kadaluarsa()
                break
            elif pilihan == 4:
                laporan_habis()
                break
            elif pilihan == 5:
                main_admin()
                break
            else:
                red("PILIHAN TIDAK ADA")
        except ValueError:
            lightred("INPUTAN TIDAK VALID")
            continue

def laporan_peminjaman():
    clear()
    logo()
    header = ["NO",'NAMA MAHASISWA','ALAT','TANGGAL','LOKASI','TUJUAN PEMINJAMAN']
    data = []
    with open("CSV/laporan peminjaman.csv", mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA LAPORAN PEMINJAMAN")
            laporan()
        else:
            clear()
            logo()
            print(tabulate(data,headers=header,tablefmt='simple_outline', stralign='center',showindex=range(1,len(data)+1) ))
            input("Tekan Enter Untuk Kembali")
            time.sleep(1)
            clear()
            laporan()

def laporan_kadaluarsa():
    clear()
    logo()
    header = ["NO",'NAMA BAHAN','ALASAN PEMBAHARUAN','TANGGAL']
    data = []

    with open("CSV/laporan kadaluarsa.csv", mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA LAPORAN BAHAN KADALUARSA")
            laporan()
        else:      
            clear()
            logo()                  
            print(tabulate(data,headers=header,tablefmt='simple_outline', stralign='center',showindex=range(1,len(data)+1) ))
            input("Tekan Enter Untuk Kembali")
            time.sleep(1)
            clear()
            laporan()

def laporan_service():
    clear()
    logo()
    header = ["NO",'NAMA ALAT','ALASAN PEMBAHARUAN','TANGGAL']
    data = []
    with open("CSV/laporan pembaharuan.csv", mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA LAPORAN PEMBAHARUAN ALAT")
            laporan()
        else:
            clear()
            logo()  
            print(tabulate(data,headers=header,tablefmt='simple_outline', stralign='center',showindex=range(1,len(data)+1) ))
            input("Tekan Enter Untuk Kembali")
            time.sleep(1)
            clear()
            laporan()

def laporan_habis():
    clear()
    logo()
    header = ["NO",'NAMA BAHAN','JUMLAH REFILL','TANGGAL']
    data = []

    with open("CSV/laporan habis.csv", mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
        if len(data) == 0:
            yellow("TIDAK ADA LAPORAN BAHAN HABIS")
            laporan()
        else:
            clear()
            logo()  
            print(tabulate(data,headers=header,tablefmt='simple_outline', stralign='center',showindex=range(1,len(data)+1) ))
            input("Tekan Enter Untuk Kembali")
            time.sleep(1)
            clear()
            laporan()


if __name__ == "__main__":
    main()