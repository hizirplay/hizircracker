import itertools
import string

def sifre_tahmini(sifre):
    sifre = input("Sifre girin:")
    semboller = ("'", '@', '%', '-', '*', ',', '&', '`', '.', '_', '!', '#', '$')
    karakter = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
    denemeler = 0
    for sifre_uzunluğu in range(1, 9): #range içinde her bir karakteri password_lenght olarak adlandır
        for tahmin in itertools.product(karakter,semboller,repeat=sifre_uzunluğu): #guess i itertools.product içindeki (chars (yani "adhfdsfıo" ve "e32hr8h2") ve yanında 1,2,3,4,5,6,7,8,9 quess olarak adlandır
            denemeler += 1
            tahmin = ''.join(tahmin) #guess ^ birleştir veya yanyana yapıştır guess ile
            if tahmin == sifre:
                return 'Şifren -> {} <- bunu {}. tahminimde buldum.'.format(tahmin,denemeler)
            print(tahmin,denemeler)

print(sifre_tahmini(sifre=''))