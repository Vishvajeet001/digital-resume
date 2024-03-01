from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portfolio Website | Vishvajeet"
PAGE_ICON = ":wave:"
NAME = "Vishvajeet"
DESCRIPTION = """
Full-Stack Developer , 🚀 BTech in CSE | Passionate about Software & Full Stack Development.
"""
EMAIL = "vishvajeetdeswal93056@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/vishvajeet-deswal-b65146276/",
    "GitHub": "https://github.com/Vishvajeet001",
    "HackerRank" : "https://www.hackerrank.com/profile/vishvajeetdeswa1",
    "LeetCode" : "https://leetcode.com/vishvajeetdeswal/"
}

PROJECTS = {
    "🏆 Digital Clock GUI - Python Tkinter for GUI and date, time, & sys modules ": "https://drive.google.com/drive/folders/1HusrGNQ3BFE0MIMiDcqgVC1CPJKADm5i",
    "🏆 Personal Budget Tracker - Python PyQt for GUI and widgets for ploting data": "https://drive.google.com/drive/folders/1PEswdl8gpGYAjfSZzgeE2CC1Nn84QhJW",
    "🏆 URL Shortener - Python Pyshorteners module": "https://drive.google.com/drive/folders/1LY7p3kFCWmN8f3InxjPNMcBifhmW8olH"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 6 Months experience in Full-Stack Development at Uptricks Services Pvt. Ltd.
- ✔️ 3 Months experience in Python Development at CyberDosti an IT Company.
- ✔️ Btech CSE | 2024 | 7.5+ CGPA
- ✔️ Diploma CSE | 2021 | 87%
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C/C++.
- 📊 FrontEnd: HTML, CSS, JavaScript.
- 📚 BackEnd: Django, SQL.
- 🗄️ Additionals: MySQL, Git/Github, Ms Excel.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
