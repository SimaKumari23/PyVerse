import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Terms of Use", layout="wide")

# ---------------- LOGIN CHECK ----------------
if st.session_state.get("username", False):
    pass
else:
    st.warning("First Login !!!")
    st.stop()

# ---------------- BACK BUTTON ----------------
with stylable_container(
    key="terms_back",
    css_styles="""
    button{
        background:rgba(255,255,255,0.08);
        color:#E2E8F0;
        border:1px solid rgba(255,255,255,0.15);
        border-radius:14px;
        padding:12px;
        font-weight:600;
        backdrop-filter:blur(10px);
        box-shadow:0 4px 12px rgba(0,0,0,0.25);
    }

    button:hover{
        background:rgba(168,85,247,0.18);
        border:1px solid #A855F7;
        color:white;
        transform:translateY(-2px);
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
radial-gradient(
circle at center,
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
text-align:center;
font-size:42px;
font-weight:bold;
background:linear-gradient(90deg,#00c6ff,#ffffff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-bottom:30px;
}

.card{
background:rgba(17,18,42,0.7);
backdrop-filter:blur(12px);
border-radius:18px;
padding:30px;
border:1px solid #2E2F5B;
box-shadow:0 0 15px rgba(77,163,255,0.2);
color:#CBD5E1;
margin-bottom:25px;
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

p,li{
color:#CBD5E1;
font-size:17px;
line-height:1.8;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📜 Terms of Use</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h3>Welcome to PyVerse</h3>

<p>

By accessing and using PyVerse, you agree to comply with these Terms of Use.
These terms are designed to ensure a safe, secure and productive learning
environment for all users.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h3>📘 Educational Purpose</h3>

<p>

PyVerse is developed for educational and learning purposes. The tutorials,
quizzes and AI tools are intended to help users improve their programming
knowledge and career preparation.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">

<h3>👤 User Responsibilities</h3>

<ul>

<li>Provide accurate account information.</li>

<li>Keep your login credentials secure.</li>

<li>Use the platform responsibly.</li>

<li>Do not misuse AI tools or learning content.</li>

</ul>

</div>
""", unsafe_allow_html=True)
# ---------------- TERMS CONTENT ----------------

st.markdown("""
<div class="card">

<h2>1. Acceptance of Terms</h2>
<p>
By accessing or using PyVerse, you agree to comply with these Terms of Use.
If you do not agree with these terms, please do not use the platform.
</p>

<h2>2. Educational Purpose</h2>
<p>
PyVerse is created for educational and learning purposes.
Python tutorials, DSA content, quizzes, AI Career Guide, and AI CV Analyzer
are provided to help users improve their programming skills.
</p>

<h2>3. User Responsibilities</h2>
<ul>
<li>Provide accurate information while creating an account.</li>
<li>Keep your password secure.</li>
<li>Do not misuse or attempt to damage the platform.</li>
<li>Do not copy or redistribute PyVerse content without permission.</li>
</ul>

<h2>4. AI Features</h2>
<p>
The AI Career Guide and AI CV Analyzer provide suggestions based on available
data and machine learning models. These recommendations are for guidance only
and should not be considered professional career advice.
</p>

<h2>5. Intellectual Property</h2>
<p>
All learning materials, quizzes, interface design, logos, and other content
available on PyVerse belong to the developers unless otherwise stated.
Unauthorized copying or distribution is prohibited.
</p>

<h2>6. Limitation of Liability</h2>
<p>
PyVerse is provided on an "as available" basis.
We are not responsible for any loss, damage, or decisions made using
the educational or AI-generated content.
</p>

<h2>7. Account Termination</h2>
<p>
We reserve the right to suspend or terminate any account that violates these
Terms of Use or attempts to misuse the platform.
</p>

<h2>8. Changes to Terms</h2>
<p>
These Terms may be updated from time to time.
Continued use of PyVerse after updates means you accept the revised Terms.
</p>

<h2>9. Contact</h2>
<p>
For any questions regarding these Terms, please contact the PyVerse
development team.
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
