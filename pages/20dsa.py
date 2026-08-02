from pathlib import Path
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="DSA Tutorial", layout="centered")

if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
    st.warning("First Login !!!")
    st.stop()

from streamlit_extras.stylable_container import stylable_container

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
            st.session_state["from_page"] = "20dsa"
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

.title {
    color: #90E0EF;
    font-size: 40px;
    text-align: left;
    font-weight: bold;
    margin-bottom: 20px;
}

.section {
    color: #90E0EF;
    text-align: left;
    font-size: 26px;
    margin-top: 25px;
}

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
st.markdown("<div class='title'>📊 DSA Tutorial</div>", unsafe_allow_html=True)

# ---------------- INTRO ----------------
st.markdown("<div class='section'>📘 Introduction</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>DSA (Data Structures and Algorithms) helps in organizing data efficiently and solving problems quickly. It is very important for coding interviews and software development.</div>", unsafe_allow_html=True)

# ---------------- IMPORTANCE ----------------
st.markdown("<div class='section'>⭐ Why Learn DSA?</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>• Improves problem-solving skills<br> • Helps in coding interviews<br> • Makes programs faster and efficient<br> • Used in real-world applications</div>", unsafe_allow_html=True)

# ---------------- TYPES ----------------
st.markdown("<div class='section'>📂 Types of Data Structures</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>• Linear: Array, Linked List, Stack, Queue<br> • Non-Linear: Tree, Graph</div>", unsafe_allow_html=True)

# ---------------- EXAMPLE ----------------
st.markdown("<div class='section'>💡 Example: Linear Search</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
arr = [10, 20, 30, 40]
key = 30

for i in arr:
    if i == key:
        print("Found")
""", language="python")

st.markdown("<div class='content'>🚀 Output</div>", unsafe_allow_html=True)
st.write("Found")

# ---------------- COURSE CONTENT ----------------
st.markdown('<div class="section">📚 Course Content</div>', unsafe_allow_html=True)

courses = [
    ("🟢 Arrays", "Chapter 1 ⟶", "21array.py"),
    ("🔵 Linked List", "Chapter 2 ⟶", "22linkedlist.py"),
    ("🟡 Stack", "Chapter 3 ⟶", "23stack.py"),
    ("🟠 Queue", "Chapter 4 ⟶", "24queue.py"),
    ("⭐ Recursion", "Chapter 5 ⟶", "25recursion.py"),
    ("🌳 Tree", "Chapter 6 ⟶", "26tree.py"),
    ("📊 Graph", "Chapter 7 ⟶", "27graph.py"),
    ("⚡ Searching", "Chapter 8 ⟶", "28searching.py"),
    ("🔄 Sorting", "Chapter 9 ⟶", "29sorting.py"),
    ("🎯 Greedy Algorithm", "Chapter 10 ⟶", "30greedy.py"),
    ("🧠 Dynamic Programming", "Chapter 11 ⟶", "31dp.py"),
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
