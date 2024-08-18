buku = []

def addBook():
    showBook()
    judul = input("Masukan judul buku: ")
    buku.append(judul)

def showBook():
    if len(buku) <= 0:
        print("buku belum ditambahkan")
    else:
        print("Total jumlah buku: %d " % len(buku))
        for x in range(len(buku)):
            print(f"({x}) {buku[x]}")
def DeleteBook():
    showBook()
    id = int(input("masukan id buku: "))
    buku.pop(id)

def UpdateBook():
    showBook()
    id = int(input("Masukan ID buku: "))
    pesan = input("Judul: ")
    buku[id] = pesan

def main():
    print(" \n ")
    print("[1] Lihat stock buku")
    print("[2] Tambah stock buku")
    print("[3] Hapus stock buku")
    print("[4] Edit stock buku")

    pilih = int(input("Masukan pilihan anda: "))
    print(" \n ")

    try:
        if pilih == 1:
            showBook()
        elif pilih == 2:
            addBook()
        elif pilih == 3:
            DeleteBook()
        elif pilih == 4:
            UpdateBook()
        else:
            print("pilihan tidak ada")
    except ValueError:
        print("pilihan harus berupa angka")

if __name__ == "__main__":
    while(True):
        main()
