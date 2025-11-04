# Kullanıcı çıkmak isteyene kadar program devam etmelidir.
while True:
    print("\n--- Basit Hesap Makinesi ---")
    print("İşlemler: +, -, *, /")
    print("Çıkış için 'q' veya 'Q' yazın.")
    print("-" * 30)

    # İşlem alınır
    islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /) veya 'q': ").strip()

    # Kullanıcı çıkmak isterse döngüyü sonlandır
    if islem.lower() == 'q':
        print("Hesap makinesi kapatılıyor. Güle güle!")
        break

    # Geçerli bir işlem olup olmadığını kontrol et
    if islem not in ('+', '-', '*', '/'):
        print("❌ Hata: Geçersiz işlem girdiniz. Lütfen +, -, *, / veya q girin.")
        continue # Döngünün başına dön

    # Sayıları alırken hata kontrolü yap
    try:
        # Kullanıcıdan iki sayı alınır.
        sayi1 = float(input("İlk sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("❌ Hata: Lütfen geçerli bir sayı girin.")
        continue # Döngünün başına dön

    sonuc = 0

    # Girilen işleme göre sonucu hesaplayıp ekrana yazdırın.
    if islem == '+':
        sonuc = sayi1 + sayi2
        print(f"Sonuç: {sayi1} + {sayi2} = **{sonuc}**")

    elif islem == '-':
        sonuc = sayi1 - sayi2
        print(f"Sonuç: {sayi1} - {sayi2} = **{sonuc}**")

    elif islem == '*':
        sonuc = sayi1 * sayi2
        print(f"Sonuç: {sayi1} * {sayi2} = **{sonuc}**")

    elif islem == '/':
        # Sıfıra bölme durumu kontrol edilmeli, uygun hata mesajı gösterilmelidir.
        if sayi2 == 0:
            print("❌ Hata: Bir sayı sıfıra bölünemez!")
        else:
            sonuc = sayi1 / sayi2
            print(f"Sonuç: {sayi1} / {sayi2} = **{sonuc}**")