import streamlit as st
import re

st.set_page_config(page_title="SafeLink & PassGuard", page_icon="🛡️", layout="centered")
st.title("🛡️ SafeLink & PassGuard")
st.write("100% Free & Legal Ethical Hacking Tool")

st.header("1. Phishing URL Checker")
url = st.text_input("URL Yahan Paste Karo", placeholder="https://example.com/login")

if st.button("URL Check Karo"):
    if not url:
        st.warning("Pehle URL to likho")
    else:
        risk = 0
        report = []
        if not url.startswith("https"):
            report.append("❌ https nahi hai")
            risk += 2
        else:
            report.append("✅ https hai")
        if re.search(r"http[s]?://\d+\.\d+\.\d+\.\d+", url):
            report.append("❌ IP wala URL hai - phishing ho sakta hai")
            risk += 3
        if "@" in url:
            report.append("❌ @ symbol hai - risky")
            risk += 2
        if len(url) > 75:
            report.append("⚠️ URL bahut lamba hai")
            risk += 1
        for r in report:
            st.write(r)
        if risk == 0:
            st.success("SAFE hai ✅")
        else:
            st.error(f"HIGH RISK! Score {risk}/8 ❌")

st.divider()
st.header("2. Password Strength Checker")
pwd = st.text_input("Password Yahan Likho", type="password")
if pwd:
    score = 0
    if len(pwd) >= 8: score += 1
    if re.search(r"[A-Z]", pwd): score += 1
    if re.search(r"[a-z]", pwd): score += 1
    if re.search(r"[0-9]", pwd): score += 1
    if re.search(r"[@$!%*?&]", pwd): score += 1
    st.progress(score / 5)
    if score <= 2:
        st.error(f"Weak - {score}/5")
    elif score <= 4:
        st.warning(f"Medium - {score}/5")
    else:
        st.success(f"Strong - {score}/5 💪")
