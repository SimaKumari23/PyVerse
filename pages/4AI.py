import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
</style>
""", unsafe_allow_html=True)
# ================= UI =================
st.markdown("""
<div class='title'>🤖  AI Career Assistant</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='content'>
💡 Enter your skills to get personalized career recommendations in the engineering field.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
# ================= SESSION =================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ================= DATA =================
data_part1= {
    "career": ["Web Developer", "AI Engineer", "Data Scientist", "UI/UX Designer"],
    "Required_Skill": [
        "html css javascript react",
        "python deep learning nlp tensorflow",
        "python statistics machine learning data visualization",
        "figma ux research design thinking creativity"
    ]
}
data_part2 = {
    "career": [
        "Computer Science Engineer",
        "Software Engineer",
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Web Developer",
        "Frontend Developer",
        "Backend Developer",
        "Full Stack Developer"
    ],

    "Required_Skill": [

        "Programming, Software Engineering, Data Structures, Algorithms, OOP, Operating System, DBMS, Computer Networks, AI, Machine Learning, Cloud Computing, Cyber Security, Web Development, Software Testing, System Design, Linux, Git, Docker, SQL, MongoDB",

        "Software Development, Java, Python, C++, OOP, DSA, Algorithms, Debugging, Testing, Git, SDLC, Design Patterns, Microservices, API, Database, Docker, Cloud, System Design",

        "AI, Machine Learning, Deep Learning, Neural Networks, CNN, RNN, Transformers, NLP, LLM, Python, TensorFlow, PyTorch, Statistics, Data Processing, Model Training, Computer Vision, Generative AI, Deployment",

        "Python, Machine Learning, Scikit Learn, TensorFlow, Keras, PyTorch, XGBoost, Pandas, NumPy, Statistics, Feature Engineering, Model Deployment, MLOps, Docker, Cloud",

        "Python, Pandas, NumPy, Statistics, SQL, Machine Learning, Deep Learning, Data Visualization, Tableau, Power BI, Predictive Analytics, Data Cleaning, Feature Engineering",

        "Excel, SQL, Power BI, Tableau, Python, Pandas, Statistics, Dashboard, Reporting, Data Cleaning, Data Visualization",

        "HTML, CSS, JavaScript, React, Angular, Vue, Node, Express, PHP, Django, API, MySQL, MongoDB, Firebase, Deployment",

        "HTML, CSS, JavaScript, TypeScript, React, Angular, Vue, Redux, Tailwind, Bootstrap, UI/UX, API Integration",

        "Node, Express, Java, Spring Boot, Python, Django, Flask, PHP, Laravel, SQL, MySQL, PostgreSQL, MongoDB, Redis, API, Authentication, Docker, Kubernetes",

        "HTML, CSS, JavaScript, React, Node, Express, Django, Spring Boot, MySQL, PostgreSQL, MongoDB, Firebase, API, JWT, Deployment"
    ]
}
data_part3 = {
    "career": [
        "Android Developer",
        "iOS Developer",
        "Cloud Engineer",
        "DevOps Engineer",
        "Cyber Security Engineer",
        "Ethical Hacker",
        "Blockchain Engineer",
        "Game Developer",
        "Robotics Engineer",
        "IoT Engineer"
    ],

    "Required_Skill": [

        "Android Development, Java, Kotlin, Android Studio, XML, Jetpack Compose, Firebase, SQLite, API, UI/UX, Testing",

        "Swift, Objective-C, Xcode, SwiftUI, UIKit, Firebase, SQLite, API, iOS Development, Testing",

        "AWS, Azure, GCP, Cloud Storage, EC2, Networking, Docker, Kubernetes, Terraform, Linux, Security",

        "Docker, Kubernetes, Jenkins, Git, CI/CD, Terraform, Ansible, Linux, Monitoring, AWS, Azure",

        "Cyber Security, Ethical Hacking, Kali Linux, Penetration Testing, Firewall, Cryptography, Networking, Python, OWASP",

        "Penetration Testing, Kali Linux, Burp Suite, Metasploit, Wireshark, SQL Injection, XSS, Networking, Python",

        "Blockchain, Ethereum, Solidity, Smart Contract, Web3, Cryptography, DApps, NFT",

        "Unity, Unreal Engine, C#, C++, Blender, Game Design, Animation, Physics, AI",

        "Robotics, Python, C++, ROS, Arduino, Raspberry Pi, Sensors, AI, Computer Vision",

        "IoT, Embedded Systems, Arduino, ESP32, Sensors, MQTT, Cloud, Python, C++"
    ]
}
data_part4 = {
    "career": [
        "Civil Engineer",
        "Mechanical Engineer",
        "Electrical Engineer",
        "Electronics and Communication Engineer",
        "Chemical Engineer",
        "Automobile Engineer",
        "Aerospace Engineer",
        "Biomedical Engineer",
        "Biotechnology Engineer",
        "Mechatronics Engineer"
    ],

    "Required_Skill": [

        "AutoCAD, STAAD Pro, Revit, BIM, Surveying, Construction Management, Structural Engineering",

        "AutoCAD, SolidWorks, CATIA, ANSYS, Thermodynamics, Manufacturing, Machine Design",

        "Power Systems, Electrical Machines, PLC, SCADA, MATLAB, Control Systems, Renewable Energy",

        "Electronics, Communication Systems, Microcontroller, VLSI, Embedded Systems, IoT, MATLAB",

        "Process Engineering, Thermodynamics, Heat Transfer, Chemical Process, MATLAB, Safety",

        "Vehicle Design, EV, Automotive Electronics, CAD, MATLAB, Manufacturing",

        "Aircraft Design, Aerodynamics, Propulsion, Avionics, CFD, MATLAB",

        "Medical Devices, Biomedical Instrumentation, Biomaterials, AI, Healthcare Technology",

        "Genetic Engineering, Molecular Biology, Bioinformatics, Biotechnology, Research",

        "Robotics, Automation, PLC, Embedded Systems, Sensors, Mechanical, Electronics"
    ]
}
data_part5 = {
    "career": [
        "Petroleum Engineer",
        "Mining Engineer",
        "Marine Engineer",
        "Naval Architect",
        "Textile Engineer",
        "Food Technology Engineer",
        "Environmental Engineer",
        "Industrial Engineer",
        "Production Engineer",
        "Metallurgical Engineer",
        "Ceramic Engineer",
        "Nanotechnology Engineer",
        "Agricultural Engineer",
        "Materials Engineer",
        "Nuclear Engineer"
    ],

    "Required_Skill": [

        "Drilling, Reservoir Engineering, Oil & Gas Exploration, Petroleum Geology, Production Engineering, Pipeline Engineering",

        "Mining Technology, Mine Planning, Geology, Surveying, Safety Management",

        "Marine Systems, Ship Engineering, Naval Technology, Mechanical Systems",

        "Ship Design, Marine Engineering, CAD, Hydrodynamics",

        "Textile Technology, Fabric Design, Manufacturing, Quality Control",

        "Food Processing, Food Safety, Quality Control, Biotechnology",

        "Environmental Science, Waste Management, Pollution Control, Sustainability",

        "Industrial Engineering, Process Optimization, Quality Control, Lean Manufacturing",

        "Manufacturing, Production Planning, CNC, Quality Control",

        "Metallurgy, Material Science, Metal Processing",

        "Ceramic Processing, Material Science, Manufacturing",

        "Nanomaterials, Material Science, Research",

        "Agricultural Technology, Irrigation, Farm Machinery",

        "Material Science, Composite Materials, Testing",

        "Nuclear Technology, Reactor Physics, Radiation Safety"
    ]
}
df = pd.concat([
    pd.DataFrame(data_part1),
    pd.DataFrame(data_part2),
    pd.DataFrame(data_part3),
    pd.DataFrame(data_part4),
    pd.DataFrame(data_part5)
], ignore_index=True)
# ================= FUNCTIONS =================

# Typing Effect
def type_effect(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(full_text)
        time.sleep(0.01)
    return full_text

# Career Recommendation
def recommend_career(user_input):
    user_input = user_input.lower().replace(",", " ")

    v = TfidfVectorizer()
    skill_matrix = v.fit_transform(df["Required_Skill"].str.lower())
    user_vector = v.transform([user_input])

    similarity = cosine_similarity(user_vector, skill_matrix).flatten()

    result = df.copy()
    result["match_score"] = similarity

    return result.sort_values(by="match_score", ascending=False)
# ================= CHAT HISTORY =================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ================= INPUT =================
prompt = st.chat_input("Enter your skills (example: python, machine learning)")
# ================= RESPONSE =================
if prompt:

    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🔍 Finding the best career for you..."):
            time.sleep(2)

            result = recommend_career(prompt)

        st.subheader("🎯 Top Career Matches")

        # 🔥 Always Top 5 only
        top = result.sort_values(by="match_score", ascending=False).head(5)

        st.table(top[["career", "match_score"]])

        # 🔥 Pie Chart Fix (Dynamic)
        labels = top["career"]
        sizes = top["match_score"]

        if sizes.sum() == 0:
            st.warning("⚠️ No matching skills found. Try valid skills.")
            reply = "❌ No match found. Try: python, web development, ui design"

        else:
            fig, ax = plt.subplots()
            ax.pie(
                sizes,
                labels=labels,
                autopct='%1.1f%%',
                startangle=90
            )
            ax.axis('equal')

            st.pyplot(fig)

            # 🔥 Best career (Top 1)
            reply = f"🚀 Best career for you: **{top.iloc[0]['career']}**"

        type_effect(reply)

        # Save assistant reply
        st.session_state.messages.append({"role": "assistant", "content": reply})
# ================= SIDEBAR =================
st.sidebar.title("⚙️ Settings")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown(" 💼 Career Dataset")
st.sidebar.write(df)
