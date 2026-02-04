import streamlit as st
import time

# Sayfa Ayarları (Başlık ve İkon)
st.set_page_config(page_title="Sana Özel ❤️", page_icon="❤️", layout="centered")

# Tasarım (CSS - Arka plan, renkler, yazı tipleri)
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
        margin-top: 20px;
    }
    /* İpucu kutusunun stili */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.5);
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Oturum Kontrolü (Sayfa yenilenince giriş bozulmasın diye)
if 'giris_yapildi' not in st.session_state:
    st.session_state['giris_yapildi'] = False

# --- GİRİŞ EKRANI ---
if not st.session_state['giris_yapildi']:
    st.title("🔒 Giriş Yapın")
    st.write("Bu sayfa N'ye özeldir. Lütfen şifreyi giriniz.")
    
    sifre = st.text_input("Şifre:", type="password")
    
    # İPUCU KISMI (Buraya ekledik)
    with st.expander("🔑 İpucunu görmek için tıkla"):
        st.write("Şifre: Yıldönümümüz (gün ay yıl bitişik) ❤️")

    if st.button("Giriş Yap"):
        if sifre == "04052025":  # ŞİFRE BURADA
            st.session_state['giris_yapildi'] = True
            st.rerun()
        else:
            st.error("Yanlış şifre! İpucuya bakabilirsin 😉")

# --- SÜRPRİZ EKRANI (Giriş Başarılıysa) ---
else:
    # Efektler
    st.balloons()
    
    st.title("❤️ Seni Çok Seviyorum Sevgilim ❤️")
    
    # Fotoğraf Kısmı (Dosya adının oyku.jpg olduğundan eminsin)
    try:
        st.image("oyku.jpg", caption="Benim dünyalar güzelim... ❤️", use_container_width=True)
    except:
        st.error("Fotoğraf yüklenemedi. 'oyku.jpg' dosyasının GitHub'da olduğundan emin ol.")
    
    # Romantik Mesaj
    st.markdown("""
    <div class="text-msg">
    Dünyanın en güzel kızı..<br>
    Varlığın bana en büyük hediye.<br>
    Seniçok seviyorum.<br>
    🌸 💑 🌸
    </div>
    """, unsafe_allow_html=True)
    
    # Ekstra Buton
    if st.button("Tekrar Seni Seviyorum De 😍"):
        st.toast('Seni çoook seviyorum!', icon='💖')
        time.sleep(0.5)
        st.balloons()
