from pathlib import Path
import streamlit as st
import json
from PIL import Image

PAGE_TITLE = "Digital CV | Peter Ruzicska"
PAGE_ICON = ":page_with_curl:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Language selector
lang = st.sidebar.selectbox("Select Language / Válassz nyelvet", ["English", "Magyar"])

# Map selection to language code
lang_code = "en" if lang == "English" else "hu"

# Load CV data from the JSON file
with open('assets/cv_data.json', 'r', encoding='utf-8') as f:
    cv_data = json.load(f)

# Fetch CV data for the selected language
data = cv_data[lang_code]


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "my-profile-pic.png"


NAME = data["name"]
DESCRIPTION = data["description"]
#"""
#Medior/Senior Systems/DevOps/Cloud Engineer with an eye always on Security, keeping your IT systems up and running!
#"""
EMAIL = "***REMOVED***"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/peter-r-86554089",
    "GitHub": "https://github.com/peru85",
}

HOBBIES = data["hobbies"]
#{
#    "🏆 Playing around with open source software and hardware, homelabs ftw",
#    "🏆 Learning to play the electric guitar",
#    "🏆 Travelling",
#}

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download CV in PDF" if lang == "English" else "📄 CV letöltése PDF-ben",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Diploma
st.write('\n')
st.subheader("Diploma")
st.write(data["diploma"])

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience summary" if lang == "English" else "Tapasztalataim dióhéjban")
for exp in data["experience-summary"]:
    st.write(f"{exp}")

# Certifications
st.write('\n')
st.subheader("Certifications" if lang == "English" else "Tanúsítványok")
for cert in data["certifications"]:
    st.write(f"{cert}")

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills" if lang == "English" else "Szakmai kompetenciák")
for skill in data["hard-skills"]:
    st.write(f"{skill}")


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")

for job in data["experience"]:
    job_header_html = f"""
        <h4 style="font-size:24px; margin-bottom:0">{job['position']}</h4>
        <p style="margin-top:0"><i>{job['company']} ({job['years']})</i></p>
        """
    st.markdown(job_header_html, unsafe_allow_html=True)
    #st.write(f"{job['position']} at {job['company']} ({job['years']})")
    for history in job["history"]:
        st.write(f"{history}")


st.write('-----------------------------------------------------------------------------')
st.write('\n')
st.subheader("My Hobbies" if lang == "English" else "Hobbik")
st.write("---")
for hobby in HOBBIES:
    st.write(f"[{hobby}]")