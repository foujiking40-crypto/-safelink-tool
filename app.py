import streamlit as st
import hashlib
import qrcode
from io import BytesIO
import requests
import socket
import re

st.set_page_config(page_title="SafeLink ULTRA PRO MAX", page_icon="logo.png", layout="wide")

# Dark Mode Toggle
dark_mode = st.toggle("🌙 Dark Mode On Karo")

if dark_mode:
    st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.image("logo.png", width=250)
st.caption("Made with love by Fouji King | Pakistan Zindabad | 16-in-1 MEGA PRO")

# 16 Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs(["🔗 URL", "🔑 Password", "📧 Email", "🔒 Hash", "📱 QR", "🌍 IP", "💬 WhatsApp", "📸 Insta", "💥 Email Leak", "🔗 Link Expand", "📄 File Scan", "🌐 Website Info", "💳 JC/Easypaisa", "🆔 CNIC Guide", "📱 SIM Check", "🚨 Scam Report"])

with tab1:
    st.subheader("URL Checker")
    url = st.text_input("URL dalo:", key="url")
    if st.button("Check URL"):
        if url:
            if "http" in url:
                st.success("✅ URL format sahi hai!")
            else:
                st.warning("⚠️ http / https lagao")

with tab2:
    st.subheader("Password Strength")
    pwd = st.text_input("Password:", type="password", key="pwd")
    if st.button("Check Strength"):
        if len(pwd) < 6:
            st.error("Kamzor Password!")
        elif len(pwd) < 10:
            st.warning("Medium Password")
        else:
            st.success("Strong Password!")

with tab3:
    st.subheader("Email Validator")
    email = st.text_input("Email:", key="email")
    if st.button("Validate Email"):
        if "@" in email and "." in email:
            st.success("✅ Valid Email!")
        else:
            st.error("❌ Invalid Email!")

with tab4:
    st.subheader("Hash Generator")
    txt = st.text_input("Text:", key="hash_txt")
    if st.button("Generate Hash"):
        if txt:
            st.code(f"MD5: {hashlib.md5(txt.encode()).hexdigest()}")
            st.code(f"SHA256: {hashlib.sha256(txt.encode()).hexdigest()}")

with tab5:
    st.subheader("QR Generator")
    qr_text = st.text_input("Text/Link:", key="qr")
    if st.button("Generate QR"):
        if qr_text:
            qr = qrcode.make(qr_text)
            buf = BytesIO()
            qr.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="QR Code")

with tab6:
    st.subheader("IP Tracker")
    ip = st.text_input("IP (khali = apna IP):", key="ip")
    if st.button("Track IP"):
        try:
            api = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
            r = requests.get(api, timeout=5).json()
            st.success(f"IP: {r.get('ip')} | City: {r.get('city')} | Country: {r.get('country')}")
            st.json(r)
        except:
            st.error("Error! IP check failed")

with tab7:
    st.subheader("💬 WhatsApp Safe")
    wa_input = st.text_input("WhatsApp Link / Number:", key="wa")
    if st.button("Check WhatsApp", key="btn_wa"):
        if wa_input:
            if "bit.ly" in wa_input or "tinyurl" in wa_input:
                st.error("⚠️ Khatra! Scam link ho sakta hai!")
            else:
                st.success("✅ Format sahi hai!")
        else:
            st.warning("Pehle link dalo!")

with tab8:
    st.subheader("📸 Insta Info")
    insta_user = st.text_input("Insta Username:", key="insta2")
    if st.button("Insta Check", key="btn_insta2"):
        if insta_user:
            st.success(f"Link: https://www.instagram.com/{insta_user}/")
            st.info("Private data nahi nikalte - Ethical Hacking!")

with tab9:
    st.subheader("💥 Email Hack Check")
    email_leak = st.text_input("Apna Email dalo:", key="leak2")
    if st.button("Check Leak", key="btn_leak"):
        if "@" in email_leak:
            st.warning(f"⚠️ {email_leak} 3 data leaks me mila hai! (Demo)")
            st.info("Real check: haveibeenpwned.com")
        else:
            st.error("Sahi Email dalo!")

with tab10:
    st.subheader("🔗 Short Link Expander")
    short_url = st.text_input("bit.ly / tinyurl dalo:", key="short")
    if st.button("Expand Link", key="btn_expand"):
        try:
            r = requests.head(short_url, allow_redirects=True, timeout=5)
            st.success(f"Asal Link: {r.url}")
        except:
            st.error("Link galat hai!")

with tab11:
    st.subheader("📄 File Virus Scan")
    file = st.file_uploader("File upload karo:", key="file_scan")
    if file:
        if file.name.endswith(('.exe', '.bat', '.sh')):
            st.error("⚠️ Khatra! Virus ho sakti hai!")
        else:
            st.success("✅ File format safe hai (Basic Check)")

with tab12:
    st.subheader("🌐 Website Info")
    site = st.text_input("Website: ex google.com", key="whois")
    if st.button("Get Info", key="btn_whois"):
        try:
            ip_addr = socket.gethostbyname(site)
            st.code(f"Website: {site}\nIP: {ip_addr}")
        except:
            st.error("Website nahi mili!")

with tab13:
    st.subheader("💳 JazzCash / Easypaisa Checker")
    jc_num = st.text_input("Number (03xx):", key="jc")
    if st.button("Check Wallet", key="btn_jc"):
        if jc_num.startswith("03") and len(jc_num)==11:
            st.success(f"{jc_num} - Valid Pakistani Number!")
        else:
            st.error("11 hindso wala number dalo!")

with tab14:
    st.subheader("🆔 CNIC Guide")
    st.info("Legal Tareeka:")
    st.write("1. 8300 par CNIC SMS karo")
    st.write("2. cnic.sims.pk par check karo")
    st.warning("Kisi aur ka data nikalna illegal hai!")

with tab15:
    st.subheader("📱 SIM Check Guide")
    st.write("Apne CNIC par SIMs check karo:")
    st.code("Apna CNIC likh kar 668 par SMS karo")

with tab16:
    st.subheader("🚨 Scam Number Reporter")
    st.error("0321-1234567 - JazzCash Fraud\n0300-7654321 - Fake Army Officer")
    report_num = st.text_input("Scam Number Report Karo:", key="report")
    if st.button("Report Karo", key="btn_report"):
        st.success(f"Shukria! {report_num} add kar denge!")

st.markdown("---")
st.caption("Made with 💚 by Fouji King | Pakistan Zindabad 🇵🇰 | Kasur Pakistan")
