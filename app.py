 import streamlit as st
import re, hashlib, requests, qrcode
from io import BytesIO

st.set_page_config(page_title="SafeLink Ultra Pro", page_icon="🛡️", layout="centered")

# --- DARK HACKER THEME ---
st.markdown("""
<style>
.stApp { background-color: #0E1117; color: #FAFAFA; }
[data-testid="stHeader"] { background: #0E1117; }
h1, h2, h3 { color: #00FF88 !important; font-family: monospace; }
div[data-baseweb="tab-list"] { background: #161A23; border-radius: 10px; }
button { background: linear-gradient(90deg, #00FF88, #00C6FF) !important; color: black !important; font-weight: bold !important; }
</style>
""", unsafe_allow_html=True)

st.image("https://i.ibb.co/0y0XJpL/safelink-logo.png", width=120) # Logo baad me upload karenge
st.title("SafeLink ULTRA PRO")
st.markdown("**by Fouji King 🇵🇰 | 6-in-1 Ethical Hacking Toolkit**")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔗 URL", "🔑 Pass", "📧 Email", "🔒 Hash", "📱 QR", "🌍 IP"])

with tab1:
    st.subheader("🔗 Phishing URL Checker")
    url = st.text_input("URL daalo:")
    if st.button("Check URL"):
        score=0
        if "http://" in url: score+=2
        if "@" in url: score+=2
        if len(url)>75: score+=1
        if score>=3: st.error(f"🚨 HIGH RISK {score}/5")
        else: st.success(f"✅ SAFE {score}/5")

with tab2:
    st.subheader("🔑 Password Strength")
    pwd = st.text_input("Password:", type="password")
    if st.button("Check Pass"):
        s=sum([len(pwd)>=8, bool(re.search(r"[A-Z]",pwd)), bool(re.search(r"[0-9]",pwd)), bool(re.search(r"[!@#$%]",pwd)), len(pwd)>=12])
        st.progress(s/5)
        st.success(f"Strength {s}/5") if s>3 else st.warning(f"Medium {s}/5") if s==3 else st.error(f"Weak {s}/5")

with tab3:
    st.subheader("📧 Email Leak Check")
    email = st.text_input("Email:")
    if st.button("Check Email"): st.success("✅ No leak in demo DB")

with tab4:
    st.subheader("🔒 Hash Generator")
    txt = st.text_input("Text for Hash:")
    if st.button("Generate Hash"):
        if txt:
            st.code(hashlib.md5(txt.encode()).hexdigest(), language="bash")
            st.code(hashlib.sha256(txt.encode()).hexdigest(), language="bash")

with tab5:
    st.subheader("📱 QR Generator")
    qr_text = st.text_input("QR Text/Link:")
    if st.button("Generate QR"):
        if qr_text:
            qr = qrcode.make(qr_text)
            buf = BytesIO(); qr.save(buf, format="PNG")
            st.image(buf.getvalue(), width=250)

with tab6:
    st.subheader("🌍 IP Tracker")
    ip = st.text_input("IP (khali chhodo to apna):")
    if st.button("Track IP"):
        try:
            r = requests.get(f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json", timeout=5).json()
            st.success(f"IP: {r.get('ip')} | {r.get('city')}, {r.get('country')}")
            st.json(r)
        except: st.error("Error!")

st.markdown("---")
st.caption("Made with 💚 by Fouji King | Pakistan Zindabad 🇵🇰")        
