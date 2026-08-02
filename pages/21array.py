import streamlit as st
st.set_page_config(page_title="DSA Arrays", layout="centered")

# LOGIN
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
            st.switch_page("pages/20dsa.py")
# ---------- CSS ----------
st.markdown("""
<style>
.stApp{
    background:
        radial-gradient(circle at center,
        rgba(168,85,247,0.28) 0%,
        rgba(168,85,247,0.18) 20%,
        rgba(168,85,247,0.08) 40%,
        transparent 70%),
        linear-gradient(135deg,#0B1026 0%,#11122A 45%,#1A1D3A 75%,#0B1026 100%);
}

.title {
    color: #90E0EF;
    font-size: 40px;
    font-weight: bold;
}

.section {
    color: #90E0EF;
    font-size: 26px;
    margin-top: 25px;
}

.content {
    color: #9CA3AF;
    font-size: 22px;
}
.stButton>button{
    background:linear-gradient(90deg,#0040ff,#8c00ff);
    color:white;border:none;border-radius:10px;
    padding:10px 22px;font-weight:bold;
}
</style>
""", unsafe_allow_html=True)
st.markdown("<div class='title'>DSA Arrays</div>", unsafe_allow_html=True)

# ---------- Q1 ----------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Traverse Array<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,20,30,40]
for i in arr:
    print(i)""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q1"):
    for i in [10,20,30,40]:
        st.write(i)

# ---------- Q2 ----------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Find Maximum<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,50,30]
print(max(arr))""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q2"):
    st.success(max([10,50,30]))

# ---------- Q3 ----------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Find Minimum<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,50,30]
print(min(arr))""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q3"):
    st.success(min([10,50,30]))

# ---------- Q4 ----------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Reverse Array<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,20,30]
arr.reverse()
print(arr)""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q4"):
    arr=[10,20,30]
    arr.reverse()
    st.success(arr)

# ---------- Q5 ----------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Sort Array<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[30,10,20]
arr.sort()
print(arr)""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q5"):
    arr=[30,10,20]
    arr.sort()
    st.success(arr)

# ---------- Q6 ----------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Linear Search<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,20,30]
key=20
if key in arr:
    print("Found")
else:
    print("Not Found")""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
num = st.text_input("Enter number")
if st.button("Run Q6"):
    arr=[10,20,30]
    if num and int(num) in arr:
        st.success("Found")
    else:
        st.error("Not Found")

# ---------- Q7 ----------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Sum of Array<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,20,30]
print(sum(arr))""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q7"):
    st.success(sum([10,20,30]))

# ---------- Q8 ----------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Average<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,20,30]
print(sum(arr)/len(arr))""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q8"):
    arr=[10,20,30]
    st.success(sum(arr)/len(arr))

# ---------- Q9 ----------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Count Even Numbers<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,21,30]
count=len([i for i in arr if i%2==0])
print(count)""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q9"):
    arr=[10,21,30]
    count=len([i for i in arr if i%2==0])
    st.success(count)

# ---------- Q10 ----------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Remove Duplicates<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See Code"):
    st.code("""arr=[10,20,20,30]
arr=list(set(arr))
print(arr)""")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("Run Q10"):
    arr=[10,20,20,30]
    arr=list(set(arr))
    st.success(arr)
