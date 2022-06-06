def garis():
    print("---------------------------------------------------------------------")
garis()
print("PERPUSTAKAAN TEKNIK UNS".center(70))
print("JL. Ir. Sutami No. 36 Telp. 08123456789".center(70))
garis()
print("")

def keluar():
    print("\n")
    keluar=input("Apakah Anda ingin keluar? (Y/T) : ")
    if (keluar=="Y") or (keluar=="y"):
        exit()
    else:
        display_menu()

def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali...")
    display_menu()

def display_menu():
    while(True):
        print("Selamat Datang di Perpustakaan Teknik UNS".center(70))
        garis()
        print(" | 1 | Tampilkan Buku")
        print(" | 2 | Meminjam Buku")
        print(" | 3 | Mengembalikan Buku")  
        print(" | 4 | Menghilangkan Buku")
        print(" | 5 | Untuk Keluar")
        print("")
        try:
            menu=int(input("pilih menu 1-5: "))
            print()
            if(menu==1):
                display_buku()
                keluar()
            elif(menu==2):
                listSplit()
                pinjamkan_buku()
                keluar()
            elif(menu==3):
                listSplit()
                kembalikan_buku()
                keluar()
            elif(menu==4):
                listSplit()
                buku_hilang()
                keluar()                
            elif(menu==5):
                print("Terimakasih telah menggunakan sistem perpustakaan Teknik UNS")
                exit()
            else:
                print("Masukkan angka 1-5")
                kembali()
                continue
        except ValueError:
            print("Masukkan sesuai perintah !")
            kembali()
            continue


def listSplit():
    global judul_buku
    global penulis
    global stock
    global harga
    judul_buku=[]
    penulis=[]
    stock=[]
    harga=[]
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
                ind+=1

def getDate():
    import datetime
    now=datetime.datetime.now
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    return str(now().time())

def display_buku():
    with open("stock.txt","r+") as f:
        lines=f.read()
        print(lines)
        print()


def pinjamkan_buku():
    success=False
    while(True):
        firstName=input("Masukkan nama depan peminjam: ")
        if firstName.isalpha():
            break
        print("Masukkan huruf A-Z")
    while(True):
        lastName=input("Masukkan nama belakang peminjam: ")
        if lastName.isalpha():
            break
        print("Masukkan huruf A-Z")
        print("")
    display_buku()

                
    t="Pinjaman-"+firstName+".txt"
    with open(t,"w+") as f:
        f.write("            Perpustakaan Teknik UNS  \n")
        f.write("                   Dipinjam oleh: "+ firstName+" "+lastName+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N. \t\t Judul buku \t      penulis \n" )

    while success==False:
        print("Pilih menu di bawah ini :")
        for i in range(len(judul_buku)):
            print("Masukkan", i, "untuk meminjam buku", judul_buku[i])
    
        try:   
            a=int(input())
            try:
                if(int(stock[a])>0):
                    print("Buku Tersedia")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ judul_buku[a]+"\t\t  "+penulis[a]+"\n")

                    stock[a]=int(stock[a])-1
                    with open("stock.txt","r+") as f:
                        for i in range(8):
                            f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+"\n")
                            continue

                    #jika buku yang dipinjam lebih dari 1
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Apakah ingin pinjam buku lagi ? Masukkan y jika ya dan n jika tidak."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Pilih menu di bawah ini :")
                            for i in range(len(judul_buku)):
                                print("Masukkan", i, "untuk meminjam buku", judul_buku[i])
                            a=int(input())
                            if(int(stock[a])>0):
                                print("Buku tersedia")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ judul_buku[a]+"\t\t  "+penulis[a]+"\n")

                                stock[a]=int(stock[a])-1
                                with open("stock.txt","r+") as f:
                                    for i in range(8):
                                        f.write(judul_buku[i]+","+penulis[i]+","+str(stock[i])+","+"Rp"+harga[i]+"\n")
                                        success=False
                                        continue
                            else:
                                loop=False
                                continue
                        elif (choice.upper()=="N"):
                            print ("Terimakasih telah meminjam buku. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Masukkan sesuai petunjuk !")
                        
                else:
                    print("Buku tidak tersedia")
                    pinjamkan_buku()
                    success=False
                    continue
            except IndexError:
                print("")
                print("Pilih buku sesuai nomor.")
        except ValueError:
            print("")
            print("Pilih sesuai petunjuk !.")

def kembalikan_buku():
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
        print("Nama peminjam salah")
        kembalikan_buku()

    b="Pengembalian-"+name+".txt"
    with open(b,"w+")as f:
        f.write("             Perpustakaan Teknik UNS \n")
        f.write("                   Dikembalikan oleh: "+ name+"\n")
        f.write("    Tanggal: " + getDate()+"    Waktu:"+ getTime()+"\n\n")
        f.write("S.N.\t\tJudul Buku\t\tTotal\n")

    #koding belum selesai

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
        print("Nama peminjam salah")
        buku_hilang()

    with open("stock.txt", "a+") as f:
        judul = input("judul = ")
        pengarang = input("pengarang = ")
        stok = input("stok = ")
        harga = input("harga = Rp ")   
        pembatas = ","
        f.write('\n' + judul + pembatas + pengarang + pembatas + stok + pembatas + 'Rp' + harga)

def buku_hilang():
    print("SESUAI DENGAN KETENTUAN YANG BERLAKU")
    print("MAKA AKAN DIKENAKAN DENDA BERUPA")
    print("--------------------------------------------")
    print("1. MEMBELI BUKU DENGAN JUDUL YANG SAMA")
    print("2. MENGGANTI DENGAN NOMINAL BUKU YANG HILANG")
    print("--------------------------------------------")
    menuhilang=input("Pilih Menu ! (1/2) : ")
    if (menuhilang==1):
        mengganti_buku()

        #problem

        #koding txt pinjam, menunjukkan buku yg dipinjam

display_menu()