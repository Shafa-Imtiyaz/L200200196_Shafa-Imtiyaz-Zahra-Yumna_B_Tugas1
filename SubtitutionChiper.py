import string, random

#fungsi untuk enkripsi
def enkripsi(plaintext):
    huruf = list(string.ascii_uppercase)
    random.shuffle(huruf)
    peta_subtitution = {}
    for i in range(26):
        peta_subtitution[huruf[i]] = string.ascii_uppercase[i]
    teks_chiper = ''
    for char in plaintext:
        if char.isalpha(): 
            teks_chiper += peta_subtitution[char.upper()] 
        else: 
           teks_chiper += char
    return teks_chiper, peta_subtitution

#fungsi untuk deskripsi
def dekripsi(teks_chiper, peta_substitusi):
    pesan_dekripsi = ''
    for char in teks_chiper:
        if char.isalpha(): 
            for kunci, value in peta_substitusi.items(): 
                if char.upper() == value: 
                    pesan_dekripsi += kunci
        else: 
            pesan_dekripsi += char 
    return pesan_dekripsi
#fungsi untuk ekripsi dekripsi
def main():
    print(" ______________________________________________________")
    print("|=======> [ Proses Enkripsi Deskripsi Pesan ] <========|")
    print("|______________________________________________________|")
    print("Silahkan masukkan isi pesan di bawah ini!")
    plaintext = input('Isi Pesan      :')
    teks_chiper,peta_substitusi = enkripsi(plaintext)  
    print('Hasil enkripsi: ', teks_chiper) 
    print(' ') 
    print('Hasil dekripsi: ', dekripsi(teks_chiper, peta_substitusi))  

if __name__ == '__main__':
    main()