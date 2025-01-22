import streamlit as st
import math
import pytube
import youtube_dl
from pytube import YouTube
import yt_dlp
from streamlit import text_input
import yt_dlp as youtube_dl
import os

# Sayfa başlığı
st.set_page_config(page_title="Çok İşlevli Web Site ", page_icon=':flag_tr:')
st.title("Çok İşlevli Web Site ")
st.write("Bu basit hesap makinesinde 5 tane işlem yapabilirsiniz: toplama, çıkarma, çarpma, bölme, yüzde hesaplama ve daha fazlası.")

# Kullanıcıdan iki sayı alın
sayi1 = st.number_input("Birinci Sayıyı Girin", step=1.0)
sayi2 = st.number_input("İkinci Sayıyı Girin", step=1.0)

# İşlem Butonları için sütunlar
col1, col2, col3 = st.columns(3)

# Toplama
with col1:
    if st.button("Topla"):
        sonuc = sayi1 + sayi2
        st.success(f"Sonuç: {sonuc}")

# Çıkarma
with col2:
    if st.button("Çıkar"):
        sonuc = sayi1 - sayi2
        st.success(f"Sonuç: {sonuc}")

# Çarpma
with col3:
    if st.button("Çarp"):
        sonuc = sayi1 * sayi2
        st.success(f"Sonuç: {sonuc}")

# Bölme
if st.button("Böl"):
    if sayi2 == 0:
        st.error("Bir Sayı 0'a Bölünemez. Geçerli Bir Sayı Deneyiniz!")
    else:
        sonuc = sayi1 / sayi2
        st.success(f"Sonuç: {sonuc}")

# Yüzde Hesaplama
if st.button("Yüzde Hesapla"):
    if sayi2 == 0:
        st.error("Yüzde hesaplamak için 2. sayı 0 olamaz.")
    else:
        sonuc = (sayi1 / sayi2) * 100
        st.success(f"{sayi1} sayısının {sayi2}'ye yüzdesi: {sonuc}%")

#Plaka Sorgulama
plaka_dict = {
    1: "Adana", 2: "Adıyaman", 3: "Afyonkarahisar", 4: "Ağrı", 5: "Amasya", 6: "Ankara", 7: "Antalya",
    8: "Artvin", 9: "Aydın", 10: "Balıkesir", 11: "Bilecik", 12: "Bingöl", 13: "Bitlis", 14: "Bolu",
    15: "Burdur", 16: "Bursa", 17: "Çanakkale", 18: "Çankırı", 19: "Çorum", 20: "Denizli", 21: "Diyarbakır",
    22: "Edirne", 23: "Elazığ", 24: "Erzincan", 25: "Erzurum", 26: "Eskişehir", 27: "Gaziantep", 28: "Giresun",
    29: "Gümüşhane", 30: "Hakkâri", 31: "Hatay", 32: "Isparta", 33: "Mersin", 34: "İstanbul", 35: "İzmir",
    36: "Kars", 37: "Kastamonu", 38: "Kayseri", 39: "Kırklareli", 40: "Kırşehir", 41: "Kocaeli", 42: "Konya",
    43: "Kütahya", 44: "Malatya", 45: "Manisa", 46: "Kahramanmaraş", 47: "Mardin", 48: "Muğla", 49: "Muş",
    50: "Nevşehir", 51: "Niğde", 52: "Ordu", 53: "Rize", 54: "Sakarya", 55: "Samsun", 56: "Siirt",
    57: "Sinop", 58: "Sivas", 59: "Tekirdağ", 60: "Tokat", 61: "Trabzon", 62: "Tunceli", 63: "Şanlıurfa",
    64: "Uşak", 65: "Van", 66: "Yozgat", 67: "Zonguldak", 68: "Aksaray", 69: "Bayburt", 70: "Karaman",
    71: "Kırıkkale", 72: "Batman", 73: "Şırnak", 74: "Bartın", 75: "Ardahan", 76: "Iğdır", 77: "Yalova",
    78: "Karabük", 79: "Kilis", 80: "Osmaniye", 81: "Düzce"
}
#plakayı alma
st.write("#### Plaka Sorgulama (1-81)")
sayı = st.number_input("Plakasını Sorgulamak İstediğiniz Sayıyı Giriniz!", min_value=0, step=1, max_value=81, format="%d")
#plakayı göster butonu
if st.button("Plakayı Göster"):
    if sayı in plaka_dict:
        st.success(f"{sayı}.Plaka kodu: {plaka_dict[sayı]}")
    else:
        st.error("Böyle Bir İl Plaka Kodu Mevcut Değil Lütfen Geçerli Sayılar Giriniz!")


# Saat-Dakika-Saniye Hesaplama
st.write("### Saat, Dakika ve Saniye Hesaplama")
saat = st.number_input("Saat Girin", min_value=0, step=1)
dakika = st.number_input("Dakika Girin", min_value=0, step=1)
saniye = st.number_input("Saniye Girin", min_value=0, step=1)

if st.button("Toplam Saniyeyi Hesapla"):
    toplam_saniye = (saat * 3600) + (dakika * 60) + saniye
    st.success(f"Toplam Saniye: {toplam_saniye} saniye")

# Ortalama Hesaplama
st.write("### Ortalama Hesaplama")
sayilar = st.text_input("Sayılari Virgülle Ayırarak Girin (Örn: 5,10,15)")

if st.button("Ortalama Hesapla"):
    try:
        sayilar_listesi = [float(x) for x in sayilar.split(',')]
        ortalama = sum(sayilar_listesi) / len(sayilar_listesi)
        st.success(f"Ortalama: {ortalama}")
    except ValueError:
        st.error("Geçersiz giriş, lütfen yalnızca sayıları virgülle ayırarak girin.")

# Üslü Hesaplama (X^Y)
st.write("### Üslü Hesaplama (X^Y)")
base = st.number_input("Tabanı Girin", step=1, format="%d")
exponent = st.number_input("Üssü Girin", step=1)

if st.button("Üssü Hesapla"):
    sonuc = base ** exponent
    st.success(f"{base} üssü {exponent}: {sonuc}")


# FORM DENEMESİ
st.write("### Başvuru Formu(Daha fazla soru eklenebilir)")
with st.form(key='form1'):
    ad = st.text_input("İsminizi Giriniz:", key="isim.input")
    yas = st.number_input("Yaşınızı Giriniz:", min_value=0 , max_value=100, step=1, key="yas.input")
    cinsiyet = st.radio("Cinsiyetinizi Seçiniz:",["Erkek", "Kadın"],key="cinsiyet.input")
    eposta = st.text_input("E-Postanızı Girin", key="eposta.input")
    hobiler = st.text_input("Neler Yapmaktan Hoşlanırsınız?", key="hobi.input")

    form_submit = st.form_submit_button("Gönder")
if form_submit:
    if not ad or not yas or not cinsiyet or not eposta or not hobiler:
        st.error("Tüm Alanları Doldurmalısın!")
    elif not (eposta.endswith("@gmail.com") or eposta.endswith("@hotmail.com") or eposta.endswith("@outlook.com")):
        st.error("E-Posta Adresiniz Hatalı")
    else:
        st.success("Başvurunuz Alındı")
st.write("bu kadardı site")