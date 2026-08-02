import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="About PyVerse", layout="wide")

# Login Check
if st.session_state.get("username", False):
    pass
else:
    st.warning("First Login !!!")
    st.stop()

# ---------------- Back Button ----------------
with stylable_container(
    key="back_btn",
    css_styles="""
    button{
        background:rgba(255,255,255,0.08);
        color:white;
        border:1px solid rgba(255,255,255,0.15);
        border-radius:14px;
        font-weight:600;
    }
    button:hover{
        background:rgba(168,85,247,0.18);
        border:1px solid #A855F7;
    }
    """
):
    if st.button("⬅go to previous"):
        st.switch_page("main.py")

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at center,
rgba(168,85,247,0.28)0%,
rgba(168,85,247,0.18)20%,
rgba(168,85,247,0.08)40%,
transparent 70%),

linear-gradient(
135deg,
#0B1026 0%,
#11122A 45%,
#1A1D3A 75%,
#0B1026 100%);
background-attachment:fixed;
}

.title{
font-size:42px;
font-weight:bold;
text-align:center;
background:linear-gradient(90deg,#00c6ff,#ffffff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:25px;
}

.card{
background:rgba(17,18,42,0.7);
backdrop-filter:blur(12px);
padding:30px;
border-radius:18px;
border:1px solid #2E2F5B;
box-shadow:0 0 15px rgba(77,163,255,0.2);
color:#CBD5E1;
transition:.3s;
}

.card:hover{
box-shadow:
0 0 25px rgba(59,130,246,.5),
0 0 45px rgba(168,85,247,.6);
}

h3{
color:#90E0EF;
}

p{
font-size:18px;
line-height:1.8;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>💙 About PyVerse</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h3>🚀 Welcome to PyVerse</h3>

<p>
PyVerse is an AI-powered learning platform developed to help students learn
Python Programming and Data Structures & Algorithms through structured
tutorials, practical coding examples, interactive quizzes and AI-powered
career tools.
</p>

<hr>

<h3>🎯 Our Mission</h3>

<p>
To make programming education simple, practical and accessible for every
student while helping them build strong coding skills and prepare for
successful careers in technology.
</p>

<hr>

<h3>✨ What We Offer</h3>

<p>
✅ Python Programming Tutorials<br>
✅ Data Structures & Algorithms Tutorials<br>
✅ Chapter-wise Interactive Quizzes<br>
✅ AI Career Guide<br>
✅ AI CV Analyzer
</p>

<hr>

<h3>⭐ Why Choose PyVerse?</h3>

<p>
• Beginner Friendly Learning<br>
• Modern Glass UI<br>
• Practical Programs<br>
• Interactive Quizzes<br>
• AI Powered Features<br>
• Easy Navigation
</p>

<hr>

<h3>🛠 Technologies Used</h3>

<p>
Python • Streamlit • MongoDB • Scikit-learn • Pandas • Matplotlib • HTML • CSS
</p>

<hr>

<h3>📩 Contact</h3>

<p>
Email : support@pyverse.com
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#9CA3AF;">
© 2026 <b>PyVerse</b><br>
Code • Learn • Build • Evolve
</div>
""", unsafe_allow_html=True)
