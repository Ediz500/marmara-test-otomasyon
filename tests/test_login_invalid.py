from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Tarayıcı başlatılır (chromedriver ile)
driver = webdriver.Chrome()

# Login sayfasına git
driver.get("https://the-internet.herokuapp.com/login")

# Yanlış kullanıcı adı ve şifre gir
driver.find_element(By.ID, "username").send_keys("yanlisKullanici")
driver.find_element(By.ID, "password").send_keys("yanlisSifre")

# Login butonuna tıkla
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Bekleme (sayfa yüklensin diye)
time.sleep(2)

# Hata mesajını kontrol et
try:
    mesaj = driver.find_element(By.ID, "flash").text
    if "Your username is invalid!" in mesaj:
        print("Test Başarılı ✅ - Hata mesajı göründü.")
    else:
        print("Test Başarısız ❌ - Beklenen mesaj görünmedi.")
except:
    print("Test Başarısız ❌ - Hata mesajı bulunamadı.")

# Tarayıcıyı kapat
driver.quit()
