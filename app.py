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

st.image("logo (1).png", width=250)
st.title("🛡️ SafeLink ULTRA PRO")
st.markdown("---")

tab1, tab2, tab3, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16 = st.tabs(["🔗 URL", "🔑 Password", "📧 Email", "🔒 Hash", "📱 QR", "🌍 IP", "💬 WhatsApp", "📸 Insta", "💥 Email Leak", "🔗 Link Expand", "📄 File Scan", "🌐 Website Info", "💳 JC/Easypaisa", "🆔 CNIC Guide", "📱 SIM Check", "🚨 Scam Report"])
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

with tab7:
    st.subheader("💬 WhatsApp Safe")
    wa_input = st.text_input("WhatsApp Link / Number:", key="wa")
    if st.button("Check WhatsApp", key="btn_wa"):
        if "bit.ly" in wa_input or "tinyurl" in wa_input:
            st.error("⚠️ Khatra! Scam link ho sakta hai!")
        else:
            st.success("✅ Format sahi hai!")

with tab8:
    st.subheader("📸 Insta Info")
    insta_user = st.text_input("Insta Username:", key="insta2")
    if st.button("Insta Check", key="btn_insta2"):
        if insta_user:
            st.success(f"Link: https://www.instagram.com/{insta_user}/")
            st.info("Private data nahi nikalte - Ethical Hacking!")
st.markdown("---")
# --- LEVEL 1 & 2 NEW TOOLS BY FOUJI KING ---

with tab9:
    st.subheader("💥 Email Hack Check - Level 1")
    email_leak = st.text_input("Apna Email dalo:", key="leak2")
    if st.button("Check Leak", key="btn_leak"):
        if "@" in email_leak:
            st.warning(f"⚠️ {email_leak} 3 data leaks me mila hai! (Demo)")
            st.info("Real check ke liye haveibeenpwned.com par jao")
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
            st.error("Link galat hai ya internet slow hai")

with tab11:
    st.subheader("📄 File Virus Scan (Basic)")
    file = st.file_uploader("Koi File upload karo:", key="file_scan")
    if file:
        if file.name.endswith(('.exe', '.bat', '.sh')):
            st.error("⚠️ Khatra! Ye file virus ho sakti hai!")
        else:
            st.success("✅ File format safe lag raha hai (Basic Check)")

with tab12:
    st.subheader("🌐 Website Info")
    site = st.text_input("Website ka naam: ex google.com", key="whois")
    if st.button("Get Info", key="btn_whois"):
        try:
            ip = __import__('socket').gethostbyname(site)
            st.code(f"Website: {site}\nIP Address: {ip}\nServer: Cloudflare / Google (Basic Info)")
        except:
            st.error("Website nahi mili!")

with tab13:
    st.subheader("💳 JazzCash / Easypaisa Checker - Pakistan Special")
    jc_num = st.text_input("Number (03xx...):", key="jc")
    if st.button("Check Wallet", key="btn_jc"):
        if jc_num.startswith("03") and len(jc_num)==11:
            st.success(f"{jc_num} - Valid Pakistani Number hai! JazzCash/Easypaisa account ho sakta hai.")
        else:
            st.error("Sahi 11 hindso wala number dalo!")

with tab14:
    st.subheader("🆔 CNIC Guide - Legal Tareeka")
    st.info("Pakistan me CNIC se naam check karne ka legal tareeka:")
    st.write("1. 8300 par CNIC number SMS karo (PTA)")
    st.write("2. Apni SIMs check karne ke liye: cnic.sims.pk")
    st.warning("Kisi aur ka CNIC data nikalna illegal hai!")

with tab15:
    st.subheader("📱 SIM Check Guide")
    st.write("Apne CNIC par kitni SIMs hain? Check karo:")
    st.code("Apna CNIC Number likh kar 668 par SMS karo")
    st.success("Jawab me sab networks ki SIMs aa jayengi!")

with tab16:
    st.subheader("🚨 Scam Number Reporter")
    st.write("Ye Numbers Scam Reported Hain (Awam ne report kiye):")
    st.error("0321-1234567 - JazzCash Fraud\n0300-7654321 - Army Officer Ban Kar Fraud\n0333-0000000 - Lottery Scam")
    report_num = st.text_input("Koi Scam Number Report Karna Hai?:", key="report")
    if st.button("Report Karo", key="btn_report"):
        st.success(f"Shukria! {report_num} ko hum list me add kar denge!")
st.markdown("---")
st.caption("Made with 💚 by Fouji King | Pakistan Zindabad 🇵🇰 | Kasur Pakistan")
