import random

print(" Sayı Tahmin Oyununa Hoş Geldin!")
print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
print("Toplam 10 tahmin hakkın var.\n")

rastgele_sayi = random.randint(1, 100)
tahmin_hakki = 10

for deneme in range(1, tahmin_hakki + 1):
    try:
        tahmin = int(input(f"{deneme}. tahminini gir: "))
    except ValueError:
        print(" Lütfen sadece sayı gir! Bu tahmin hakkın sayılmadı.\n")
        continue

    if tahmin == rastgele_sayi:
        print(f"🎉 Tebrikler! {deneme}. denemede doğru bildin! ")
        break
    elif tahmin < rastgele_sayi:
        print("⬆ Daha büyük bir sayı dene.")
    else:
        print("⬇ Daha küçük bir sayı dene.")
    
    kalan_hak = tahmin_hakki - deneme
    if kalan_hak > 0:
        print(f"Kalan tahmin hakkın: {kalan_hak}\n")
    else:
        print("\n Tahmin hakkin bitti.")
        print(f"Doğru sayı: {rastgele_sayi}")

print("\nOyun bitti, teşekkürler! ") 