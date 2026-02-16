import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Konteyner Fabrikası", layout="wide")

# Başlık ve Görsel
st.title("🏗️ Özdemir Konteyner & Prefabrik")
st.subheader("Dayanıklı, Hızlı ve Ekonomik Yaşam Alanları")

# Yan Menü (Sidebar)
with st.sidebar:
    st.header("Teklif Al")
    boyut = st.selectbox("Konteyner Boyutu", ["3x7 Metre", "2.4x6 Metre", "Özel Ölçü"])
    ekstra = st.multiselect("Ekstralar", ["Klima", "Ekstra Yalıtım", "Mutfak Tezgahı"])
    if st.button("Fiyat Hesapla"):
        st.success("Talebiniz alındı, size döneceğiz!")

# Ana İçerik
col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/500x300", caption="Örnek Konteyner Modeli") 
    # Buraya gerçek konteyner fotoğraflarının linkini koyabilirsin.

with col2:
    st.write("""
    ### Neden Biz?
    * **Yüksek Kalite:** ISO sertifikalı üretim.
    * **Hızlı Teslimat:** Türkiye'nin her yerine 7 günde teslimat.
    * **Garanti:** 2 yıl yapısal garanti.
    """)

st.divider()
st.info("📍 Adres: Sanayi Bölgesi No:45 / İstanbul")
