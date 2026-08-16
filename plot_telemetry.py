import matplotlib.pyplot as plt

zamanlar = []
yukler = []

print("Kara kutu verileri okunuyor...")

try:
    # Kaydettiğimiz log dosyasını okuma modunda açıyoruz
    with open("telemetry_log.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya:
            # Sadece içinde "Süspansiyon Yükü" geçen veri satırlarını alıyoruz (başlıkları atlıyoruz)
            if "Süspansiyon Yükü" in satir:
                # Satırdan saati çekiyoruz (Örn: [17:32:05] -> 17:32:05)
                saat = satir[1:9]
                
                # Satırdan yük değerini ayıklayıp ondalıklı sayıya (float) çeviriyoruz
                yuk_kismi = satir.split("Süspansiyon Yükü: ")[1]
                yuk_degeri = float(yuk_kismi.split(" kg")[0])
                
                zamanlar.append(saat)
                yukler.append(yuk_degeri)

    # Artık grafiği çizdirebiliriz
    plt.figure(figsize=(10, 5))
    plt.plot(zamanlar, yukler, marker='o', color='#2ca02c', linewidth=2, label='Anlık Yük (kg)')
    
    # 800 kg limitine kırmızı bir uyarı çizgisi çekiyoruz
    plt.axhline(y=800, color='r', linestyle='--', linewidth=2, label='Kritik Kırılma Limiti (800 kg)')
    
    # Grafiği süslüyoruz
    plt.title('Tekerlek Taşıyıcı (Steering Knuckle) - Süspansiyon Yükü Analizi', fontsize=14, fontweight='bold')
    plt.xlabel('Zaman (Saat:Dakika:Saniye)', fontsize=11)
    plt.ylabel('Binen Yük (Kilogram)', fontsize=11)
    plt.xticks(rotation=45) # Saatleri yan yatırarak sığdırıyoruz
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    # Grafiği ekrana bas!
    print("Grafik oluşturuldu! Pencereyi kapattığınızda program sonlanacaktır.")
    plt.show()

except FileNotFoundError:
    print("Hata: 'telemetry_log.txt' dosyası bulunamadı. Lütfen önce diğer simülasyonu çalıştırıp veri üretin.")