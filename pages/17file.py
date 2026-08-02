import streamlit  as st
st.set_page_config(page_title="File I/O program", layout="centered")
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
            st.switch_page("pages/5python.py")  
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
st.markdown("<div class='title'>File I/O program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write Data into a File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Write Data into File")

data = st.text_area("Enter Data")

if st.button("WRITE", key="btn1"):
    file = open("data.txt","w")
    file.write(data)
    file.close()

    st.success("Data Written Successfully")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

data = st.text_area("Enter Data", key="data1")

if st.button("WRITE", key="work1"):
    file = open("data.txt","w")
    file.write(data)
    file.close()

    st.success("Data Written Successfully")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Read Data from a File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Read Data from File")

if st.button("READ", key="btn2"):
    file = open("data.txt","r")
    data = file.read()
    file.close()

    st.success(data)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("READ", key="work2"):
    file = open("data.txt","r")
    data = file.read()
    file.close()

    st.success(data)


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Append Data into a File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Append Data into File")

data = st.text_area("Enter Data")

if st.button("APPEND", key="btn3"):
    file = open("data.txt","a")
    file.write(data)
    file.close()

    st.success("Data Added Successfully")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

data = st.text_area("Enter Data", key="data3")

if st.button("APPEND", key="work3"):
    file = open("data.txt","a")
    file.write(data)
    file.close()

    st.success("Data Added Successfully")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Count Lines, Words and Characters in a File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Count Lines Words Characters")

if st.button("COUNT", key="btn4"):

    file = open("data.txt","r")
    data = file.read()
    file.close()

    lines = data.split("\\n")
    words = data.split()
    characters = len(data)

    st.success(f"Lines = {len(lines)}")
    st.success(f"Words = {len(words)}")
    st.success(f"Characters = {characters}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("COUNT", key="work4"):

    file = open("data.txt","r")
    data = file.read()
    file.close()

    lines = data.split("\n")
    words = data.split()
    characters = len(data)

    st.success(f"Lines = {len(lines)}")
    st.success(f"Words = {len(words)}")
    st.success(f"Characters = {characters}")


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Copy One File Content to Another File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Copy File Content")

if st.button("COPY", key="btn5"):

    file1 = open("data.txt","r")
    content = file1.read()
    file1.close()

    file2 = open("copy.txt","w")
    file2.write(content)
    file2.close()

    st.success("File Copied Successfully")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("COPY", key="work5"):

    file1 = open("data.txt","r")
    content = file1.read()
    file1.close()

    file2 = open("copy.txt","w")
    file2.write(content)
    file2.close()

    st.success("File Copied Successfully")

#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Search a Word in a File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Search Word in File")

word = st.text_input("Enter Word")

if st.button("SEARCH", key="btn6"):
    file = open("data.txt","r")
    data = file.read()
    file.close()

    if word in data:
        st.success("Word Found")
    else:
        st.error("Word Not Found")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

word = st.text_input("Enter Word", key="word6")

if st.button("SEARCH", key="work6"):
    file = open("data.txt","r")
    data = file.read()
    file.close()

    if word in data:
        st.success("Word Found")
    else:
        st.error("Word Not Found")


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Count Word Frequency in a File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Word Frequency")

word = st.text_input("Enter Word")

if st.button("COUNT", key="btn7"):

    file = open("data.txt","r")
    data = file.read()
    file.close()

    count = data.split().count(word)

    st.success(f"Frequency = {count}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

word = st.text_input("Enter Word", key="word7")

if st.button("COUNT", key="work7"):

    file = open("data.txt","r")
    data = file.read()
    file.close()

    count = data.split().count(word)

    st.success(f"Frequency = {count}")


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Count Vowels, Digits and Special Characters in File.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Count Vowels Digits Special Characters")

if st.button("COUNT", key="btn8"):

    file = open("data.txt","r")
    data = file.read()
    file.close()

    vowels = 0
    digits = 0
    special = 0

    for i in data:
        if i.lower() in "aeiou":
            vowels += 1
        elif i.isdigit():
            digits += 1
        elif not i.isalnum() and i != " ":
            special += 1

    st.success(f"Vowels = {vowels}")
    st.success(f"Digits = {digits}")
    st.success(f"Special Characters = {special}")
""", language="python")    
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
if st.button("COUNT", key="work8"):

    file = open("data.txt","r")
    data = file.read()
    file.close()

    vowels = 0
    digits = 0
    special = 0
    for i in data:
        if i.lower() in "aeiou":
            vowels += 1
        elif i.isdigit():
            digits += 1
        elif not i.isalnum() and i != " ":
            special += 1

    st.success(f"Vowels = {vowels}")
    st.success(f"Digits = {digits}")
    st.success(f"Special Characters = {special}")
