# Marmara Test Otomasyon Ödevi

Bu ödevde verilen senaryo doğrultusunda, yanlış kullanıcı adı ve şifre ile login denemesi yapılmış, hata mesajı kontrol edilmiştir.

## Kullanılan Teknolojiler

- Python 3.10
- Selenium 4.x
- ChromeDriver 136

## Uygulama Senaryosu

1. Tarayıcı açılır.
2. https://the-internet.herokuapp.com/login adresine gidilir.
3. Yanlış kullanıcı adı ve şifre girilir.
4. “Your username is invalid!” hata mesajının görünüp görünmediği kontrol edilir.
5. Sonuç ekrana yazdırılır ve tarayıcı kapatılır.

## Proje Dosya Yapısı
```bash
📁 marmara-test-otomasyon
 ┣ 📁 tests/
 ┃ ┗ test_login_invalid.py (veya .java)
 ┣ 📄 README.md
 ┗ 📷 test-sonucu.png (ekran görüntüsü)
```
## Testin Çalıştırılması

Terminalden şu komut ile test çalıştırılır:
tests/test_login_invalid.py

## Test Sonucu

- Test başarılı olmuştur.
- Hata mesajı doğru şekilde görüntülenmiştir.
- [Ekran görüntüsü:](test-sonucu.png)
