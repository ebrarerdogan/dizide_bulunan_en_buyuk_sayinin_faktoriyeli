#kullanıcıdan sayı dizisi isteyen ve bu sayılar arasından en büyük sayının faktöriyelini bulan program.
def faktoriyel_hesaplama(sayi):
    faktoriyel = 1

    if sayi < 0:
        return "Negatif sayıların faktöriyeli olmaz."
    elif sayi == 0:
        return 1
    else:
        for i in range(1, sayi + 1):
            faktoriyel *= i

        return faktoriyel

def en_buyuk_faktoriyel():
    n = int(input("Lütfen sayı adedini giriniz: "))

    if n <= 0:
        print("En az bir sayı girmelisiniz.")
        return

    sayilar = []
    for i in range(n):
        sayi = int(input(f"{i + 1}. sayıyı girin: "))
        sayilar.append(sayi)

    en_buyuk_sayi = max(sayilar)

    sonuc = faktoriyel_hesaplama(en_buyuk_sayi)

    print(f"Girilen sayılar: {sayilar}")
    print(f"En büyük sayının faktöriyeli: {sonuc}")
en_buyuk_faktoriyel()