from pathlib import Path
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Python Tutorial", layout="centered")
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
    st.warning("First Login !!!")
    st.stop()
# ---------------- NAV BUTTON STYLE ----------------
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
    col1, col2 = st.columns([1,1], gap="medium")

    with col1:
        if st.button("⬅go to previous", use_container_width=True):
            st.switch_page("main.py")
    with col2:
        if st.button("Next ➡", use_container_width=True):
            st.session_state["from_page"] = "5python"
            st.switch_page("pages/32quizes.py")        
# ---------------- DARK STYLE ----------------
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
/* Title */
.title {
    color: #90E0EF;
    font-size: 40px;
    text-align: left;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Section headings */
.section {
    color: #90E0EF;
    text-align: left;
    font-size: 26px;
    margin-top: 25px;
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

# ---------------- TITLE ----------------
st.markdown("<div class='title'>🐍 Python Tutorial</div>", unsafe_allow_html=True)
# ---------------- INTRO ----------------
st.markdown("<div class='section'>📘 Introduction</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Python is a simple and easy-to-learn programming language.It is widely used by beginners and professionals.</div>", unsafe_allow_html=True)


# ---------------- HISTORY ----------------
st.markdown("<div class='section'>📜 History</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Python was created by Guido van Rossum in 1991.It is known for its simple and readable syntax.</div>", unsafe_allow_html=True)

# ---------------- APPLICATIONS ----------
st.markdown("<div class='section'>🚀 Applications</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>•Web Development<br> • Data Science <br>• Machine Learning <br> • Automation etc.</div>", unsafe_allow_html=True)
# ---------------- PYTHON SYNTAX ----------------
st.markdown("<div class='section'>⌨️ Python Syntax</div>", unsafe_allow_html=True)

st.markdown("""
<div class='content'>
Python syntax is the set of rules used to write Python programs.
Python is easy to read because it uses indentation (spaces) instead of curly braces {}.

<b>Basic Syntax Rules:</b><br><br>

• Statements are written one per line.<br>
• Indentation is mandatory to define blocks of code.<br>
• Comments start with the <b>#</b> symbol.<br>
• Variable names should be meaningful.<br>
• Python is case-sensitive (Name and name are different).<br>
• Strings are written inside single (' ') or double (" ") quotes.
</div>
""", unsafe_allow_html=True)
# ---------------- EXAMPLE ----------------
st.markdown("<div class='section'>💡 Example: Print Hello World</div>", unsafe_allow_html=True)
# ---------------- CODE --------------
st.markdown("<div class='content'>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
import streamlit as st
st.title("Welcome!!!")
st.write("Hello World")
""", language="python")
#------------ OUTPUT CHECK ----------------
st.markdown("<div class='content'>🚀Output</div>", unsafe_allow_html=True)
st.write("Hello World")

# -------------------- COURSE CONTENT --------------------
# -------------------- COURSE CONTENT --------------------
st.markdown('<div class="section">📚 Course Content</div>', unsafe_allow_html=True)
courses = [
    ("🟢 Beginner Programs", "Chapter 1          ⟶", "6beginner.py"),
    ("🔵 Conditional Programs", "Chapter 2           ⟶", "7conditional.py"),
    ("🟡 Loop Programs", "Chapter 3          ⟶", "8loop.py"),
    ("🟠 Number Programs", "Chapter 4         ⟶", "9number.py"),
    ("⭐ Pattern Programs", "Chapter 5        ⟶", "10pattern.py"),
    ("🔤 String Programs", "Chapter 6         ⟶", "11string.py"),
    ("📋 List Programs", "Chapter 7          ⟶", "12list.py"),
    ("📦 Tuple Programs", "Chapter 8         ⟶", "13tuple.py"),
    ("📖 Dictionary Programs", "Chapter 9         ⟶", "14dictionary.py"),
    ("🎯 Set Programs", "Chapter 10        ⟶", "15set.py"),
    ("⚙️ Function Programs", "Chapter 11        ⟶", "16function.py"),
    ("📁 File Handling Programs", "Chapter 12      ⟶ ", "17file.py"),
    ("🛡️ Exception Handling Programs", "Chapter 13       ⟶", "18exception.py"),
    ("🏛️ OOP Programs", "Chapter 14        ⟶ ", "19oop.py"),
]
with stylable_container(
    key="course_buttons",
    css_styles="""
    button {
        background: rgba(255,255,255,0.08);
        color: #E2E8F0;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 14px;
        padding: 14px;
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
    for title, chapter, filename in courses:
        if st.button(f"{title}\n{chapter}", key=filename, use_container_width=True):
            target = Path(__file__).parent / filename
            st.switch_page(str(target))
