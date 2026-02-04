import streamlit as st
import time

# Sayfa Ayarları
st.set_page_config(page_title="Sana Özel ❤️", page_icon="❤️", layout="centered")

# Tasarım (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #ffe6e6;
        background-image: url("https://www.transparenttextures.com/patterns/hearts.png");
    }
    h1 {
        color: #d63384;
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    .text-msg {
        font-size: 20px;
        color: #5c0029;
        text-align: center;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.6);
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Şifre Kontrolü
if 'giris_yapildi' not in st.session_state:
    st.session_state['giris_yapildi'] = False

if not st.session_state['giris_yapildi']:
    st.title("🔒 Giriş Yapın")
    sifre = st.text_input("Lütfen şifreyi girin:", type="password")

    if st.button("Giriş"):
        if sifre == "04052025":  # Şifren
            st.session_state['giris_yapildi'] = True
            st.rerun()
        else:
            st.error("Yanlış şifre! İpucu: Yıldönümümüz 😉")

# Giriş Başarılıysa
else:
    st.balloons()
    st.title("❤️ Seni Çok Seviyorum Sevgiim ❤️")

    # Sadece senin fotoğrafın (GIF satırını sildim)
    # oyku.jpg dosyasının bu kodla AYNI KLASÖRDE olduğundan emin ol!
    st.image("oyku.jpeg", caption="Benim dünyalar güzelim... ❤️", use_container_width=True)

    st.markdown("""
    <div class="text-msg">
    Dünyanın en güzel kızı...<br>
    Varlığın bana en büyük hediye.<br>
    🌸 💑 🌸
    </div>
    """, unsafe_allow_html=True)

    if st.button("Tekrar Seni Seviyorum De 😍"):
        st.toast('Seni çoook seviyorum!', icon='💖')

        st.balloons()

