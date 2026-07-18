import streamlit as st
import re
import hashlib

st.set_page_config(page_title="SafeLink Pro", page_icon="🛡️", layout="centered")
st.title("🛡️ SafeLink Pro - Ethical Toolkit")
st.markdown("**100% Free & Legal | Made by Fouji King 🇵🇰**")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["🔗 URL", "🔑 Password", "📧 Email", "🔒 Hash"])

with tab1:
    st.subheader("Phishing URL Checker")
    url = st.text_input("URL daalo:", placeholder="https://example.com")
    if st.button("Check URL", key="url"):
        if not url: st.warning("URL likho!")
        else:
            score=0
            if "http://" in url: score+=2; st.write("❌ http hai")
            else: st.write("✅ https hai")
            if "@" in url: score+=2; st.write("❌ @ symbol hai")
            if len(url)>75: score+=1; st.write("⚠️ URL bohat lamba")
            if score>=3: st.error(f"🚨 HIGH RISK Score {score}")
            else: st.success(f"✅ SAFE Score {score}")

with tab2:
    st.subheader("Password Checker")
    pwd = st.text_input("Password:", type="password")
    if st.button("Check Pwd"):
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
    st.subheader("Email Leak Checker")
    email = st.text_input("Email:", placeholder="test@gmail.com")
    if st.button("Check Email"):
        if "@" not in email: st.warning("Sahi email likho")
        else: st.success("✅ No leak in demo DB. Tip: 2FA ON rakho!")

with tab4:
    st.subheader("Hash Generator")
    txt = st.text_input("Text:")
    if st.button("Generate"):
        if txt:
            st.code(f"MD5: {hashlib.md5(txt.encode()).hexdigest()}")
            st.code(f"SHA256: {hashlib.sha256(txt.encode()).hexdigest()}")

st.markdown("---")
st.markdown("Made by Fouji King | Educational Only")
