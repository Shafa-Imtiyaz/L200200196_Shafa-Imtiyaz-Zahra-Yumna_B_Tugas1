#Fungsi untuk proses Enkripsi
def enkripsi(pesan, kunci):
    chiper = '' 
    for char in pesan:
        if char.isupper(): 
            chiper += chr((ord(char) - 65 + kunci) % 26 + 65)     
        elif char.islower():
            chiper += chr((ord(char) - 97 + kunci) % 26 + 97)  
        else:  
            chiper += char   
    return chiper

#Fungsi untuk proses Deskripsi
def dekripsi(chiper, kunci):
    pesan = '' 
    for char in chiper:
        if char.isupper():  
            pesan += chr((ord(char) - 65 - kunci) % 26 + 65) 
        elif char.islower(): 
            pesan += chr((ord(char) - 97 - kunci) % 26 + 97)  
        else:  
            pesan += char 
    return pesan

#Untuk menjalankan proses Enkripsi Deskripsi
def main():
    print("______________________________________________________")
    print("=======> [ Proses Enkripsi Deskripsi Pesan ] <========")
    print("______________________________________________________")
    print("Silahkan masukkan isi pesan di bawah ini!")
    pesan = input('Isi Pesan      : ')
    print("______________________________________________________")
    kunci = 96 #menggunakan kunci dengan angka 2 digit terakhir dari NIM L200200196
    chiper = enkripsi(pesan, kunci)
    
    print('Hasil enkripsi :', chiper)
    print(' ')
    print('Hasil dekripsi :', dekripsi(chiper, kunci))
    print("______________________________________________________")

if __name__ == '__main__': 
    main()