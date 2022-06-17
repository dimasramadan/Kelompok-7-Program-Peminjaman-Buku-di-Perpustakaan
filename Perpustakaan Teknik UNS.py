
import os

def garis():
    print("=====================================================================")
    

def header():
    garis()
    print("PERPUSTAKAAN TEKNIK UNS".center(70))
    print("JL. Ir. Sutami No. 36 Telp. 08123456789".center(70))
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def keluar():
    print("")
    keluar=input("Apakah Anda ingin keluar? (Y/T) : ")
    if (keluar=="Y") or (keluar=="y"):
        clear_screen()
        garis()
        print("PERPUSTAKAAN TEKNIK UNS".center(70))
        print("JL. Ir. Sutami No. 36 Telp. 08123456789".center(70))
        garis()
        print("")
        print("Terimakasih telah menggunakan sistem perpustakaan Teknik UNS.".center(70))
        print("")
        input("Tekan tombol apa saja untuk keluar... : ")
        exit()
    else:
        print("")
        clear_screen()
        display_menu()


def kembali():
    print("")
    input("Tekan tombol apa saja untuk kembali... : ")
    print("")
    clear_screen()
    display_menu()


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
                listSplit()
                display_buku()
                keluar()
            elif(menu==2):
                clear_screen()
                listSplit()
                pinjamkan_buku()
                keluar()
            elif(menu==3):
                clear_screen()
                listSplit()
                kembalikan_buku()
                keluar()
            elif(menu==4):
                clear_screen()
                listSplit()
                buku_hilang()
                keluar()                
            elif(menu==5):
                print("Terimakasih telah menggunakan sistem perpustakaan Teknik UNS.")
                print("")
                exit()
            else:
                clear_screen()
                print("Masukkan angka 1 hingga 5 untuk memilih Menu.")
                kembali()
        except ValueError:
            clear_screen()
            print("Masukkan sesuai perintah !")
            kembali()


def listSplit():
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


def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())


def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())


def buku_perpus():
    with open("stock.txt","r+") as f:
        lines=f.readlines()
        for i in range(len(lines)):
            print('-', '"'+judul_buku[i]+'"', 'ditulis oleh', penulis[i]+'.', '\t(Buku tersedia: '+stock[i]+')')


def display_buku():
    print("======================================================================")
    print("|---------------DAFTAR BUKU DI PERPUSTAKAAN TEKNIK UNS---------------|")
    print("|-------------(JUDUL,PENULIS,STOK,BIAYA PINJAM,KATEGORI)-------------|")
    print("======================================================================")
    print("")
    print("Berikut adalah daftar buku yang terdapat di Perpustakaan Teknik UNS :")
    print("")
    buku_perpus()


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
    print("==============================")
    print("|-----DATA DIRI PEMINJAM-----|")
    print("==============================")
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
        f.write("\t\tTanggal: " + getDate()+" Waktu: "+ getTime()+"\n\n")
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
                        choice=str(input('Apakah Anda berniat meminjam buku lagi?\nMasukkan "Y" jika ya dan "T" jika tidak.\n\n'))
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
    print("==============================")
    print("|-----DATA DIRI PEMINJAM-----|")
    print("==============================")
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
            print(data)
    except:
        print()
        print("Nama yang diinput tidak terdaftar sebagai peminjam.")
        kembali()

    b="Pengembalian-"+name+".txt"
    with open(b,"w+")as f:
        f.write("             Perpustakaan Teknik UNS \n")
        f.write("                   Dikembalikan oleh: "+ name+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N.\t\tJudul Buku\t\tTotal\n")

    total=0.0
    for i in range(8):
        if judul_buku[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+judul_buku[i]+"\t\tRp"+harga[i]+"\n")
                stock[i]=int(stock[i])+1
            total+=float(harga[i])
            
    print("\t\t\t\t\t\t\t"+"Rp"+str(total))
    print("Apakah buku melewati batas peminjaman?")
    print("Masukkan Y jika ya dan T jika tidak.")
    print("")
    stat=input()
    if(stat.upper()=="Y"):
        print("Berapa hari keterlambatan?")
        hari=int(input())
        denda=1000*hari
        with open(b,"a+")as f:
            f.write("\t\t\t\t\tDenda: Rp"+ str(denda)+"\n")
        total=total+denda
    
    print("Total pembayaran: "+ "Rp"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: Rp"+ str(total))
        
    with open("stock.txt","r+") as f:
            for i in range(8):
                f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+","+kategori[i]+"\n")


def mengganti_buku():
    name=input("Masukkan nama peminjam: ")
    a="Pinjaman-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("Rp") for a in lines]

        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("")
        print("Nama yang diinput tidak terdaftar sebagai peminjam.")
        kembali()

    b="Buku-Hilang-"+name+".txt"
    with open(b,"w+")as f:
        f.write("             Perpustakaan Teknik UNS \n")
        f.write("                   Dihilangkan oleh: "+ name+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N.\t\tJudul Buku\t\tTotal\n")

    for i in range(8):
        if judul_buku[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+judul_buku[i]+"\t\tRp"+harga[i]+"\n")
                stock[i]=int(stock[i])+1

    with open(b,"r") as f:
        datahilang=f.read()
        print(datahilang)

    with open("stock.txt","r+") as f:
        for i in range(8):
            f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+","+kategori[i]+"\n")


def buku_hilang():
    print("================================================")    
    print("|----SESUAI DENGAN KETENTUAN YANG BERLAKU,-----|")
    print("|-------MAKA AKAN DIKENAKAN DENDA BERUPA-------|")
    print("|==============================================|")
    print("|----MENGGANTI BUKU DENGAN JUDUL DAN JUMLAH----|")
    print("|-------------------YANG SAMA------------------|")
    print("================================================")
    print("")
    menuhilang=int(input("Pilih Cara Pengembalian! (1/2) : "))
    if menuhilang == 1:
        mengganti_buku()


display_menu()