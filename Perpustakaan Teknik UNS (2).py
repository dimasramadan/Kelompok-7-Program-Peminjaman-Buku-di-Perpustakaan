
import os

def garis():
    print("=====================================================================")
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def keluar():
    print("")
    tawaran_keluar=input("Apakah Anda ingin keluar? (Y/T) : ")
    if(tawaran_keluar=="Y") or (tawaran_keluar=="y"):
        clear_screen()
        garis()
        print("PERPUSTAKAAN TEKNIK UNS".center(70))
        print("JL. Ir. Sutami No. 36 Telp. 08123456789".center(70))
        garis()
        print("")
        print("Terimakasih telah menggunakan sistem Perpustakaan Teknik UNS.".center(70))
        print("")
        garis()
        print("")
        input("Tekan tombol apa saja untuk keluar... : ")
        exit()
    elif(tawaran_keluar=="T") or (tawaran_keluar=="t"):
        print("")
        clear_screen()
        display_menu()
    else:
        clear_screen()
        print("Masukkan sesuai petunjuk!")
        keluar()


def kembali():
    print("")
    input("Tekan tombol apa saja untuk kembali... : ")
    print("")
    clear_screen()
    display_menu()


def deskripsi_stock():
    global judul_buku
    global penulis
    global stock
    global harga
    global kategori
    judul_buku=[]
    penulis=[]
    stock=[]
    harga=[]
    kategori=[]
    with open("stock.txt","r+") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    judul_buku.append(a)
                elif(ind==1):
                    penulis.append(a)
                elif(ind==2):
                    stock.append(a)
                elif(ind==3):
                    harga.append(a.strip("Rp"))
                elif(ind==4):
                    kategori.append(a)
                ind+=1


def tanggal():
    import datetime
    now=datetime.datetime.now
    return str(now().date())


def waktu():
    import datetime
    now=datetime.datetime.now
    return str(now().time())


def header():
    garis()
    print("PERPUSTAKAAN TEKNIK UNS".center(70))
    print("JL. Ir. Sutami No. 36 Telp. 08123456789".center(70))
    

def display_menu():
    while(True):
        header()
        garis()
        print()
        print("Selamat Datang di Perpustakaan Teknik UNS".center(70))
        print("")
        print(" | 1 | Tampilkan Buku")
        print(" | 2 | Meminjam Buku")
        print(" | 3 | Mengembalikan Buku")  
        print(" | 4 | Menghilangkan Buku")
        print(" | 5 | Untuk Keluar")
        print("")
        garis()
        print("")
        try:
            menu=int(input("Silahkan input Menu yang diinginkan (1-5): "))
            print()
            if(menu==1):
                clear_screen()
                deskripsi_stock()
                display_buku()
                keluar()
            elif(menu==2):
                clear_screen()
                deskripsi_stock()
                pinjamkan_buku()
                keluar()
            elif(menu==3):
                clear_screen()
                deskripsi_stock()
                kembalikan_buku()
                keluar()
            elif(menu==4):
                clear_screen()
                deskripsi_stock()
                buku_hilang()
                keluar()                
            elif(menu==5):
                clear_screen()
                garis()
                print("PERPUSTAKAAN TEKNIK UNS".center(70))
                print("JL. Ir. Sutami No. 36 Telp. 08123456789".center(70))
                garis()
                print("")
                print("Terimakasih telah menggunakan sistem Perpustakaan Teknik UNS.".center(70))
                print("")
                garis()
                print("")
                input("Tekan tombol apa saja untuk keluar... : ")
                exit()
            else:
                clear_screen()
                print("Masukkan angka 1 hingga 5 untuk memilih Menu.")
                kembali()
        except ValueError:
            clear_screen()
            print("Masukkan sesuai perintah!")
            kembali()


def buku_perpus():
    with open("stock.txt","r+") as f:
        lines=f.readlines()
        for i in range(len(lines)):
            print('-', '"'+judul_buku[i]+'"', 'ditulis oleh', penulis[i]+'.', '\t(Buku tersedia: '+stock[i]+')')


def display_buku():
    print("========================================================================================")
    print("|--------------------------------------------------------------------------------------|")
    print("|------------------------DAFTAR BUKU DI PERPUSTAKAAN TEKNIK UNS------------------------|")
    print("|--------------------------------------------------------------------------------------|")
    print("========================================================================================")
    print("")
    print("")
    print("Berikut adalah daftar buku yang terdapat di Perpustakaan Teknik UNS :")
    print("")
    buku_perpus()
    print("")
    print("")
    print("|==================================MOHON DIPERHATIKAN==================================|")
    print("|----------------Anda dapat meminjam bermacam judul buku yang berbeda.-----------------|")
    print("|--------------------Namun, Anda tidak dapat meminjam lebih dari-----------------------|")
    print("|--------------------satu buku dengan judul yang sama dikarenakan----------------------|")
    print("|--------------------------------terbatasnya stok buku.--------------------------------|")
    print("|=====================================TERIMA KASIH=====================================|")


def keterangan_biaya():
    print("=================================================")
    print("|-----KATEGORI BUKU-----|-----BIAYA PINJAM------|")
    print("|===============================================|")
    print("|--UMUM-----------------|--Rp.15000-------------|")
    print("|--SAINS DAN MATEMATIKA-|--Rp.10000-------------|")
    print("|--TEKNOLOGI------------|--Rp.5000--------------|")
    print("|--LAINNYA--------------|--Rp.3000--------------|")
    print("=================================================")
    print("")


def pinjamkan_buku():
    print("==============================================")
    print("|-------------DATA DIRI PEMINJAM-------------|")
    print("==============================================")
    print("")
    success=False
    while(True):
        NamaDepan=input("Masukkan nama depan peminjam: ")
        if NamaDepan.isalpha():
            break
        print("")
        print("Mohon untuk memasukkan nama depan Anda.")
        print("")
    while(True):
        NamaBelakang=input("Masukkan nama belakang peminjam: ")
        if NamaBelakang.isalpha():
            break
        print("")
        print("Mohon untuk memasukkan nama belakang Anda.")
        print("")
    clear_screen()
    keterangan_biaya()
                
    t="Pinjaman-"+NamaDepan+".txt"
    with open(t,"w+") as f:
        f.write("\t\t\t  Perpustakaan Teknik UNS  \n")
        f.write("\t\t\tDipinjam oleh: "+ NamaDepan+" "+NamaBelakang+"\n")
        f.write("\t\tTanggal: " + tanggal()+" Waktu: "+ waktu()+"\n\n")
        f.write("No.\t\t\t\tJudul Buku\t\t\t   Penulis \n" )

    while success==False:
        for i in range(8):
            print("Masukkan", i, "untuk meminjam buku", '"'+judul_buku[i]+'"', "dari kategori", kategori[i]+".")
        print("")
        print("Pilih salah satu menu di atas: ")
        print("")
    
        try:   
            a=int(input())
            try:
                if(int(stock[a])>0):
                    clear_screen()
                    print("Buku Tersedia.")
                    print("")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ judul_buku[a]+"\t\t"+penulis[a]+"\n")

                    stock[a]=int(stock[a])-1
                    with open("stock.txt","r+") as f:
                        for i in range(8):
                            f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+","+kategori[i]+"\n")
                            continue

                   #lebih dari satu buku dipinjam
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input('Apakah Anda berniat meminjam buku lagi?\nMasukkan "Y" jika Ya dan "T" jika Tidak.\n\n'))
                        print("")
                        if(choice.upper()=="Y"):
                            clear_screen()
                            keterangan_biaya()
                            count=count+1
                            for i in range(8):
                                print("Masukkan", i, "untuk meminjam buku", judul_buku[i], "dari kategori", kategori[i])      
                            print("")
                            print("Pilih salah satu menu di atas: ")
                            print("")
                            a=int(input())
                            if(int(stock[a])>0):
                                clear_screen()
                                print("Buku tersedia.")
                                print("")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ judul_buku[a]+"\t\t"+penulis[a]+"\n")

                                stock[a]=int(stock[a])-1
                                with open("stock.txt","r+") as f:
                                    for i in range(8):
                                        f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+","+kategori[i]+"\n")
                                        success=False
                                        continue
                            else:
                                loop=False
                                continue
                        elif (choice.upper()=="T"):
                            clear_screen()
                            a="Pinjaman-"+NamaDepan+".txt"
                            with open(a,"r") as f:
                                data=f.read()
                                print(data)
                            print("")
                            print("=============================================================================")
                            print("|----------------------TERIMAKASIH TELAH MEMINJAM BUKU----------------------|")
                            print("|===========================================================================|")
                            print("|----------------MASA PEMINJAMAN BUKU ADALAH SELAMA 2 BULAN-----------------|")
                            print("|-------------JIKA TERLAMBAT MENGEMBALIKAN MAKA DIKENAKAN DENDA-------------|")
                            print("|--------------------------SEBESAR RP.1000 PER HARI-------------------------|")
                            print("|--------DAN JIKA MENGHILANGKAN BUKU PINJAMAN MAKA DIKENAKAN SANKSI---------|")
                            print("=============================================================================")
                            loop=False
                            success=True
                            keluar()
                        else:
                            clear_screen()
                            print("Masukkan sesuai petunjuk!")
                            print("")
                        
                else:
                    clear_screen()
                    print("Maaf, buku tidak tersedia.")
                    print("Silakan untuk meminjam buku lainnya.")
                    print("")
                    pinjamkan_buku()
            except IndexError:
                clear_screen()
                print("Pilih buku sesuai nomor.")
                print("")
                keterangan_biaya()
        except ValueError:
            clear_screen()
            print("Pilih sesuai petunjuk!")
            print("")
            keterangan_biaya()
    

def kembalikan_buku():
    print("==============================================")
    print("|-------------DATA DIRI PEMINJAM-------------|")
    print("==============================================")
    print("")
    name=input("Masukkan nama peminjam: ")
    clear_screen()
    a="Pinjaman-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("Rp") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
    except:
        print("")
        print("Nama yang dimasukkan tidak terdaftar sebagai peminjam.")
        kembali()

    b="Pengembalian-"+name+".txt"
    with open(b,"w+")as f:
        f.write("\t\t\t  Perpustakaan Teknik UNS  \n")
        f.write("\t\t\t   Dipinjam oleh: "+name+"\n")
        f.write("\t\tTanggal: " + tanggal()+" Waktu: "+ waktu()+"\n\n")
        f.write("No.\t\t\t\tJudul Buku\t\t\t   Total\n")

    total=0.0
    count=0
    for i in range(8):
        if judul_buku[i] in data:
            count=count+1
            with open(b,"a") as f:
                f.write(str(count)+"\t\t"+judul_buku[i]+"\t\t Rp"+harga[i]+"\n")
                stock[i]=int(stock[i])+1
            total+=float(harga[i])

    with open(b,"r") as f:
        data=f.read()
        print(data)        
    print("\t\t\t\t\t\t\t\t "+"Rp"+str(total))
    print("")
    print("---------------------------------------------------------------------------")
    print("")
    print("Apakah Anda melewati batas peminjaman?")
    print('Masukkan "Y" jika Ya dan "T" jika Tidak.')
    print("")
    stat=input()
    if(stat.upper()=="Y"):
        print("")
        print("Berapa hari keterlambatan? (Masukkan angka) :")
        print("")
        hari=int(input())
        denda=1000*hari
        with open(b,"a+")as f:
            f.write("\t\t\t\t\t\t\t  Denda: Rp"+ str(denda)+"\n")
        total=total+denda
    elif(stat.upper()=="T"):
        print("")


    clear_screen()
    with open(b,"a")as f:
        f.write("\t\t\t\t\t\t\t  Total: Rp"+ str(total))
    with open(b,"r") as f:
        data=f.read()
        print(data)
    print("")
    print("---------------------------------------------------------------------------")
    print("")
    print("Maka total pembayaran yang harus Anda bayarkan adalah: "+ "Rp"+str(total))
    print("")
    print("---------------------------------------------------------------------------")
        
    with open("stock.txt","r+") as f:
            for i in range(8):
                f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+","+kategori[i]+"\n")


def buku_hilang():
    print("==============================================")
    print("|-------------DATA DIRI PEMINJAM-------------|")
    print("==============================================")
    print("")
    name=input("Masukkan nama peminjam: ")
    clear_screen()
    a="Pinjaman-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("Rp") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
    except:
        print("Nama yang dimasukkan tidak terdaftar sebagai peminjam.")
        kembali()
    print("================================================")    
    print("|----SESUAI DENGAN KETENTUAN YANG BERLAKU,-----|")
    print("|-------MAKA AKAN DIKENAKAN DENDA BERUPA-------|")
    print("|----MENGGANTI BUKU DENGAN JUDUL DAN JUMLAH----|")
    print("|-------------------YANG SAMA------------------|")
    print("|==============================================|")
    print("|---------------CATATAN  PENTING---------------|")
    print("|------DIMOHON UNTUK MENGISI DATA DENGAN-------|")
    print("|----------JUJUR DAN SESUAI PERINTAH-----------|")
    print("|------LALU BERIKAN BUKU PADA PUSTAKAWAN-------|")
    print("================================================")
    print("")
    input("Tekan tombol apa saja untuk melanjutkan... : ")
    clear_screen()
    print("Berikut adalah kategori buku: ")
    keterangan_biaya()
    print("Berikut adalah buku yang Anda pinjam: ")
    print("")
    b="Buku-Hilang-"+name+".txt"
    with open(b,"w+")as f:
        f.write("\t\t\t  Perpustakaan Teknik UNS  \n")
        f.write("\t\t\t   Dipinjam oleh: "+name+"\n")
        f.write("\t\tTanggal: " + tanggal()+" Waktu: "+ waktu()+"\n\n")
        f.write("No.\t\t\tJudul Buku\t\t  Penulis\t\t  Kategori\n")
    
    count=0
    for i in range(8):
        if judul_buku[i] in data:
            count=count+1
            with open(b,"a") as f:
                f.write(str(count)+"\t"+judul_buku[i]+"\t"+penulis[i]+"\t\t"+kategori[i]+"\n")

    with open(b,"r") as f:
        datahilang=f.read()
        print(datahilang)

    print("-----------------------------------------------------------------------------------------")

    with open("stock.txt", "a+") as f:
        judul_buku[i]=input("judul = ")
        penulis[i]=input("pengarang = ")
        stock[i]=input("stok = ")
        kategori[i]=input("kategori = ")
        harga[i]=input("harga = Rp ")   
        pembatas=","
        f.write('\n' + judul_buku[i] + pembatas + penulis[i] + pembatas + stock[i] + pembatas + 'Rp' + harga[i] + pembatas + kategori[i])


display_menu()