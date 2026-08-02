import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="Privacy Policy", layout="wide")
# ---------------- BACK BUTTON ----------------
with stylable_container(
    key="privacy_back",
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
    transition:.3s;
    margin-bottom:25px;
}

.card:hover{
    box-shadow:
    0 0 25px rgba(59,130,246,0.5),
    0 0 45px rgba(168,85,247,0.6);
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

# ---------------- TITLE ----------------

st.markdown("""
<div class="title">
🔒 Privacy Policy
</div>
""", unsafe_allow_html=True)

# ---------------- INTRO ----------------

st.markdown("""
<div class="card">

<h3>Welcome to PyVerse</h3>

<p>

Your privacy is important to us. This Privacy Policy explains how PyVerse collects, uses and protects your personal information while you use our learning platform.

By using PyVerse, you agree to the practices described in this Privacy Policy.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- INFORMATION WE COLLECT ----------------

st.markdown("""
<div class="card">

<h3>📌 Information We Collect</h3>

<p>PyVerse may collect the following information:</p>

<ul>

<li>Username</li>

<li>Email Address</li>

<li>Mobile Number</li>

<li>Date of Birth</li>

<li>Login Credentials</li>

<li>Resume uploaded for AI CV Analysis</li>

</ul>

</div>
""", unsafe_allow_html=True)

# ---------------- HOW WE USE ----------------

st.markdown("""
<div class="card">

<h3>🎯 How We Use Your Information</h3>

<ul>

<li>Create and manage your account.</li>

<li>Provide Python and DSA learning content.</li>

<li>Generate AI Career recommendations.</li>

<li>Analyze resumes using AI CV Analyzer.</li>

<li>Improve user experience and platform performance.</li>

</ul>

</div>
""", unsafe_allow_html=True)
# ---------------- DATA SECURITY ----------------

st.markdown("""
<div class="card">

<h3>🔐 Data Security</h3>

<p>

PyVerse takes reasonable steps to protect your personal information from
unauthorized access, misuse or disclosure. Although we use appropriate
security measures, no online platform can guarantee complete security.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- AI CV ANALYZER ----------------

st.markdown("""
<div class="card">

<h3>📄 AI CV Analyzer</h3>

<p>

The resume uploaded by users is processed only to generate analysis and
career improvement suggestions. PyVerse does not intentionally share your
resume with third parties.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- THIRD PARTY ----------------

st.markdown("""
<div class="card">

<h3>🤝 Third-Party Services</h3>

<p>

PyVerse uses trusted technologies such as Python, Streamlit, MongoDB,
Scikit-learn, Pandas and Matplotlib to provide platform features and
improve user experience.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- USER RIGHTS ----------------

st.markdown("""
<div class="card">

<h3>👤 User Rights</h3>

<ul>

<li>Access your account information.</li>

<li>Update your profile details.</li>

<li>Change your password securely.</li>

<li>Use AI features responsibly.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# ---------------- POLICY UPDATES ----------------

st.markdown("""
<div class="card">

<h3>🔄 Policy Updates</h3>

<p>

PyVerse may update this Privacy Policy whenever required. Any changes will
be reflected on this page. Continued use of the platform indicates your
acceptance of the updated policy.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- CONTACT ----------------

st.markdown("""
<div class="card">

<h3>📩 Contact Us</h3>

<p>

If you have any questions regarding this Privacy Policy, you may contact
the PyVerse Team for assistance.

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("<hr style='border:1px solid #2E2F5B;'>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;color:#9CA3AF;">

© 2026 <b>PyVerse</b><br>

<span style="letter-spacing:2px;">
Code • Learn • Build • Evolve
</span>

</div>
""", unsafe_allow_html=True)
