import streamlit as st
import re, hashlib, requests, qrcode
from io import BytesIO

st.set_page_config(page_title="SafeLink Ultra Pro", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #0E1117; color: #FAFAFA; }
[data-testid="stHeader"] { background: #0E1117; }
h1, h2, h3 { color: #00FF88 !important; font-family: monospace; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ SafeLink ULTRA PRO")
st.markdown("**by Fouji King 🇵🇰 | 6-in-1 Ethical Toolkit**")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔗 URL", "🔑 Pass", "📧 Email", "🔒 Hash", "📱 QR", "🌍 IP"])

with tab1:
    st.subheader("URL Checker")
    url = st.text_input("URL daalo:", key="u1")
    if st.button("Check URL"):
        score = 0
        if "http://" in url: score += 2
        if "@" in url: score += 2
        if len(url) > 75: score += 1
        if score >= 3: st.error(f"🚨 HIGH RISK {score}")
        else: st.success(f"✅ SAFE {score}")

with tab2:
    st.subheader("Password Strength")
    pwd = st.text_input("Password:", type="password", key="p1")
    if st.button("Check Pass"):
        s = 0
        if len(pwd) >= 8: s += 1
        if re.search(r"[A-Z]", pwd): s += 1
        if re.search(r"[0-9]", pwd): s += 1
        if re.search(r"[!@#$%]", pwd): s += 1
        if len(pwd) >= 12: s += 1
        st.progress(s/5)
        if s <= 2: st.error(f"Weak {s}/5")
        elif s == 3: st.warning(f"Medium {s}/5")
        else: st.success(f"Strong {s}/5 🔥")

with tab3:
    st.subheader("Email Leak Check")
    email = st.text_input("Email:", key="e1")
    if st.button("Check Email"):
        st.success("✅ No leak in demo DB")

with tab4:
    st.subheader("Hash Generator")
    txt = st.text_input("Text:", key="h1")
    if st.button("Generate Hash"):
        if txt:
            st.code(f"MD5: {hashlib.md5(txt.encode()).hexdigest()}")
            st.code(f"SHA256: {hashlib.sha256(txt.encode()).hexdigest()}")

with tab5:
    st.subheader("QR Generator")
    qr_text = st.text_input("Text/Link:", key="q1")
    if st.button("Generate QR"):
        if qr_text:
            qr = qrcode.make(qr_text)
            buf = BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), width=250)

with tab6:
    st.subheader("IP Tracker")
    ip = st.text_input("IP (khali = apna):", key="ip1")
    if st.button("Track IP"):
        try:
            api = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
            r = requests.get(api, timeout=5).json()
            st.success(f"IP: {r.get('ip')} - {r.get('city')}, {r.get('country')}")
            st.json(r)
        except:
            st.error("Error! IP check fail")

st.markdown("---")
st.caption("Made with 💚 by Fouji King | Pakistan Zindabad 🇵🇰")
