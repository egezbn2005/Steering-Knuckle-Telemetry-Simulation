import time
import random
from datetime import datetime # Zaman damgası için yeni kütüphane eklendi

def read_virtual_sensors():
    # Sensör verilerini simüle ediyoruz
    speed = random.randint(20, 140) 
    steering_angle = random.uniform(-35.0, 35.0) 
    suspension_load = random.uniform(250.0, 900.0) 
    
    return speed, steering_angle, suspension_load

print("--- Tekerlek Taşıyıcı Telemetri Sistemi Başlatılıyor ---")
print("Sanal sensör verileri okunuyor ve 'telemetry_log.txt' dosyasına kaydediliyor...\n")

try:
    # Dosyayı 'a' (append/ekleme) modunda açıyoruz ki eski verileri silmeden altına eklesin
    with open("telemetry_log.txt", "a", encoding="utf-8") as log_file:
        
        # Sürüş başladığında dosyaya bir başlık atalım
        log_file.write(f"\n--- YENİ TEST SÜRÜŞÜ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        
        while True:
            s, a, l = read_virtual_sensors()
            current_time = datetime.now().strftime('%H:%M:%S') # Anlık saati alıyoruz
            
            # Kaydedilecek metni tek bir satırda formatlıyoruz
            log_text = f"[{current_time}] Hız: {s:03d} km/h | Rot Açısı: {a:>6.2f}° | Süspansiyon Yükü: {l:>6.2f} kg"
            
            # Eğer yük çok artarsa metnin sonuna uyarıyı ekle
            if l > 800:
                log_text += "  ⚠️ KRİTİK UYARI: Limit aşıldı!"
                
            # 1. Terminale (ekrana) yazdır
            print(log_text)
            
            # 2. Dosyaya yazdır ve alt satıra geç (\n)
            log_file.write(log_text + "\n")
            log_file.flush() # Veriyi RAM'de bekletme, anında dosyaya işle
            
            time.sleep(1) 
            
except KeyboardInterrupt:
    print("\nTelemetri akışı durduruldu. Kayıtlar 'telemetry_log.txt' dosyasına mühürlendi.")