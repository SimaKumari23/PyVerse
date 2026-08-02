import streamlit as st
import PyPDF2
import docx
# ================= CONFIG =================
st.set_page_config(page_title="PyVerseAI Career Assistant", layout="wide")
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
    st.warning("First Login !!!")
    st.stop()
from streamlit_extras.stylable_container import stylable_container
with stylable_container(
    key="nav_buttons",
    css_styles="""
    button {
        background: rgba(255,255,255,0.08);
        color: #E2E8F0;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 14px;
        padding: 12px;
        font-weight: 600;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }
    button:hover {
        background: rgba(168,85,247,0.18);
        border: 1px solid #A855F7;
        color: white;
        transform: translateY(-2px);
    }
    """
):
    col1,col2= st.columns([1,1], gap="medium")

    with col1:
        if st.button("⬅go to previous", use_container_width=True):
            st.switch_page("pages/3profile.py")
st.markdown("""
<style>
.stApp{
    background:
        radial-gradient(
            circle at center,
            rgba(168,85,247,0.28) 0%,
            rgba(168,85,247,0.18) 20%,
            rgba(168,85,247,0.08) 40%,
            transparent 70%
        ),

      linear-gradient(
            135deg,
            #0B1026 0%,
            #11122A 45%,
            #1A1D3A 75%,
            #0B1026 100%
        );
    background-attachment:fixed;
}
.title {
    color: #90E0EF;
    font-size: 40px;
    text-align: left;
    font-weight: bold;
    margin-bottom: 20px;
}
/* Content text */
.content {
    color: #9CA3AF;
    font-size: 22px;
    line-height: 1.6;
}
.stButton>button{
        background:linear-gradient(90deg,#0040ff,#8c00ff);
        color:white;
        border:none;
        border-radius:10px;
        padding:10px 22px;
        font-weight:bold;
   }
    button:hover{
        background:linear-gradient(90deg,#005eff,#a855f7);
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class='title'>CV Analyzer</div>
""", unsafe_allow_html=True)

text = ""

# Upload File
f = st.file_uploader("Upload Your CV", type=["pdf", "docx"])

if st.button("AI Analyzer"):

    if f is None:
        st.warning("⚠️ Please upload your CV first.")
        st.stop()

    # Read PDF
    if f.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    # Read DOCX
    elif f.name.endswith(".docx"):
        doc = docx.Document(f)
        text = "\n".join([p.text for p in doc.paragraphs])

    text = text.lower()

    st.subheader("CV Text")
    st.write(text)

    skills = {
        "python": 20,
        "java": 15,
        "sql": 15,
        "react": 10,
        "flask": 10,
        "html": 10,
        "css": 10,
        "javascript": 10,
        "machine learning": 20,
        "mongodb": 10,
        "postgresql": 10,
        "django": 10,
        "node.js": 10,
        "typescript": 9,
        "html5": 10,
        "css3": 7
    }

    score = 0
    found = []

    for skill, marks in skills.items():
        if skill in text:
            score += marks
            found.append(skill)

    st.header(f"🎯 Score: {score}/100")

    st.subheader("✅ Skills Found")
    if found:
        st.write(found)
    else:
        st.write("No matching skills found.")

    suggestions = []

    if "python" not in found:
        suggestions.append("Learn Python")
    if "sql" not in found:
        suggestions.append("Learn SQL")
    if "flask" not in found:
        suggestions.append("Learn Flask")
    if len(found) < 3:
        suggestions.append("Add more technical skills to your CV.")

    st.subheader("💡 Suggestions")
    if suggestions:
        for s in suggestions:
            st.write("•", s)
    else:
        st.success("Excellent! Your CV contains good technical skills.")
