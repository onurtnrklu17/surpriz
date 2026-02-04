import streamlit as st
import time

# Sayfa Ayarları (Başlık ve İkon)
st.set_page_config(page_title="Sana Özel 💙", page_icon="💙", layout="centered")

# --- YENİ TASARIM (MAVİ TEMA & NET YAZILAR) ---
st.markdown("""
    <style>
    /* Ana arka plan rengi (Açık Mavi) ve Kalp Deseni */
    .stApp {
        background-color: #e3f2fd; 
        background-image: url("https://www.transparenttextures.com/patterns/hearts.png");
        color: #0d47a1; /* Sayfadaki tüm ana yazıların rengi (Koyu Lacivert) */
    }
    
    /* Başlıkların stili */
    h1 {
        color: #0d47a1 !important; /* Koyu Lacivert */
        text-align: center;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    
    /* Giriş ekranındaki normal yazılar ve etiketler */
    label, .stMarkdown p {
        color: #1565c0 !important; /* Biraz daha açık lacivert */
        font-size: 18px;
    }

    /* Sürpriz ekranındaki mesaj kutusu */
    .text-msg {
        font-size: 20px;
        color: #0d47a1; /* Koyu Lacivert */
        text-align: center;
        padding: 25px;
        background-color: rgba(255, 255, 255, 0.85); /* Daha belirgin beyaz kutu */
        border-radius: 15px;
        margin-top: 20px;
        border: 2px solid #bbdefb; /* İnce mavi çerçeve */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Hafif gölge */
    }
    
    /* İpucu kutusunun başlığı */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.9) !important;
        color: #0d47a1 !important;
        border-radius: 10px;
        border: 1px solid #90caf9;
        font-weight: bold;
    }
    /* İpucu kutusunun içi */
    .streamlit-expanderContent {
         background-color: rgba(255, 255, 255, 0.7);
         border-radius: 0 0 10px 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Oturum Kontrolü
if 'giris_yapildi' not in st.session_state:
    st.session_state['giris_yapildi'] = False

# --- GİRİŞ EKRANI ---
if not st.session_state['giris_yapildi']:
    st.title("🔒 Giriş Yapın")
    st.markdown("Bu sayfa **Öyküme** özeldir. Lütfen şifreyi giriniz.")
    
    sifre = st.text_input("Şifre:", type="password")
    
    # İPUCU KISMI
    with st.expander("🔹 İpucunu görmek için tıkla"):
        st.write("Şifre: **Yıldönümümüz** (gün ay yıl bitişik) 💙")

    if st.button("Giriş Yap", type="primary"): # Butonu da mavi yaptık
        if sifre == "04042025":  # ŞİFREN
            st.session_state['giris_yapildi'] = True
            st.rerun()
        else:
            st.error("Yanlış şifre! İpucuya bakabilirsin 😉")

# --- SÜRPRİZ EKRANI (Giriş Başarılıysa) ---
else:
    st.balloons()
    
    st.title("💙 Seni Çok Seviyorum Sevgilim 💙")
    
    # Fotoğraf Kısmı
    try:
        st.image("oyku.jpeg", caption="Benim dünyalar güzelim... 💙", use_container_width=True)
    except:
        # Fotoğraf yüklenmezse geçici bir mavi kalp gifi gösterelim
        st.image("https://media.giphy.com/media/IsOqV4s4gN0bF0888S/giphy.gif", use_container_width=True)
        st.warning("Fotoğraf yüklenemedi, 'oyku.jpg' dosyasını kontrol et.")
    
    # Romantik Mesaj
    st.markdown("""
    <div class="text-msg">
    Dünyanın en güzel kız...<br>
    Varlığın bana en büyük hediye.<br>
    Seni her şeyden çok seviyorum.<br>
    🌊 💑 🌊
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Tekrar Seni Seviyorum De 😍"):
        st.toast('Seni çoook seviyorum!', icon='💙')
        time.sleep(0.5)
        st.balloons()

