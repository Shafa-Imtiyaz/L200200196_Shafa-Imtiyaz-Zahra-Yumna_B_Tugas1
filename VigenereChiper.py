#Fungsi untuk enkripsi 
def enkripsi(pesan, kunci):
    pesan_enkripsi= ''  
    for i in range(len(pesan)):
        char = pesan[i]  
        kunci_char = kunci[i % len(kunci)] 
        if char.isalpha():
            no_char = ord(char.upper()) - 65  
            no_kunci = ord(kunci_char.upper()) - 65 
            no_enkripsi = (no_char + no_kunci) % 26 
            char_enkripsi = chr(no_enkripsi + 65)
            if char.isupper(): 
                pesan_enkripsi += char_enkripsi  
            else:
                pesan_enkripsi += char_enkripsi.lower() 
        else:
            pesan_enkripsi += char 
    return pesan_enkripsi 

#Fungsi untuk deskripsi
def dekripsi(teks_chiper, kunci):
    pesan_dekripsi = ''  
    for i in range(len(teks_chiper)):
        char = teks_chiper[i]  
        kunci_char = kunci[i % len(kunci)]  

        if char.isalpha():  
            no_char = ord(char.upper()) - 65  
            no_kunci = ord(kunci_char.upper()) - 65  

            no_dekripsi = (no_char - no_kunci) % 26  
            char_dekripsi = chr(no_dekripsi + 65)  

            if char.isupper():  
                pesan_dekripsi += char_dekripsi  
            else:
                pesan_dekripsi += char_dekripsi.lower()  
        else:
            pesan_dekripsi += char  
    return pesan_dekripsi  

#====================[ FUNGSI UNTUK MENJALANKAN PROSES ENKRIPSI DEKRIPSI VIGENERE CHIPER ]======================
def main():
    print("______________________________________________________")
    print("=======> [ Proses Enkripsi Deskripsi Pesan ] <========")
    print("______________________________________________________")
    print("Silahkan masukkan isi pesan di bawah ini!")
    pesan = input('Isi Pesan      : ')  
    kunci = ('196') #menggunakan kunci 196 dengan 3 digit terakhir dari NIM L200200196
    teks_chiper = enkripsi(pesan, kunci)
    print('Hasil enkripsi :', teks_chiper)
    print(' ')
    print('Hasil dekripsi :', dekripsi(teks_chiper, kunci))
    print("______________________________________________________")
   
if __name__ == '__main__':
    main()