import streamlit as st
import re
import hashlib
import requests
import qrcode
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="SafeLink Ultra Pro", page_icon="🛡️", layout="centered")

st.title("🛡️ SafeLink Ultra Pro")
st.markdown("**6-in-1 Toolkit | Made by Fouji King 🇵🇰**")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔗 URL", "🔑 Pass", "📧 Email", "🔒 Hash", "📱 QR", "🌍 IP"])

with tab1:
    st.subheader("Phishing URL Checker")
    url = st.text_input("URL daalo:", placeholder="https://example.com")
    if st.button("Check URL"):
        if not url: st.warning("URL likho!")
        else:
            score=0
            if "http://" in url: score+=2; st.write("❌ http (unsafe)")
            else: st.write("✅ https secure")
            if "@" in url: score+=2; st.write("❌ @ symbol trick")
            if len(url)>75: score+=1; st.write("⚠️ Lamba URL")
            if score>=3: st.error(f"🚨 HIGH RISK {score}")
            else: st.success(f"✅ SAFE {score}")

with tab2:
    st.subheader("Password Strength")
    pwd = st.text_input("Password:", type="password")
    if st.button("Check Pass"):
        s=0
        if len(pwd)>=8: s+=1
        if re.search(r"[A-Z]",pwd): s+=1
        if re.search(r"[0-9]",pwd): s+=1
        if re.search(r"[!@#$%]",pwd): s+=1
        if len(pwd)>=12: s+=1
        st.progress(s/5)
        if s<=2: st.error(f"Weak {s}/5")
        elif s==3: st.warning(f"Medium {s}/5")
        else: st.success(f"Strong {s}/5 🔥")

with tab3:
    st.subheader("Email Leak Check")
    email = st.text_input("Email:", placeholder="test@gmail.com")
    if st.button("Check Email"):
        if "@" not in email: st.warning("Sahi email likho")
        else: st.success("✅ No leak in demo. 2FA ON rakho!")

with tab4:
    st.subheader("Hash Generator")
    txt = st.text_input("Text for Hash:")
    if st.button("Generate Hash"):
        if txt:
            st.code(f"MD5: {hashlib.md5(txt.encode()).hexdigest()}")
            st.code(f"SHA256: {hashlib.sha256(txt.encode()).hexdigest()}")

with tab5:
    st.subheader("QR Code Generator")
    qr_text = st.text_input("QR ke liye text/link:", placeholder="https://google.com")
    if st.button("Generate QR"):
        if qr_text:
            qr = qrcode.make(qr_text)
            buf = BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="Tumhara QR Code", width=250)
            st.success("QR ban gaya! Isko scan karo!")
        else: st.warning("Pehle text likho!")

with tab6:
    st.subheader("IP Address Tracker")
    ip = st.text_input("IP daalo (khali chhodo to tumhara IP):", placeholder="8.8.8.8")
    if st.button("Track IP"):
        try:
            target = ip if ip else ""
            url_api = f"https://ipinfo.io/{target}/json" if target else "https://ipinfo.io/json"
            res = requests.get(url_api, timeout=5).json()
            st.success(f"IP: {res.get('ip')}")
            st.write(f"📍 City: {res.get('city')}, {res.get('region')}, {res.get('country')}")
            st.write(f"🏢 ISP: {res.get('org')}")
            st.write(f"📍 Location: {res.get('loc')}")
            st.write(f"🌐 Timezone: {res.get('timezone')}")
        except:
            st.error("IP nahi mila, internet check karo!")

st.markdown("---")
st.caption("Made with ❤️ by Fouji King | Educational Purpose Only 🇵🇰")
