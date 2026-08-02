import streamlit  as st
st.set_page_config(page_title="Dictionary program", layout="centered")
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
st.markdown("<div class='title'>Dictionary program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Create and Access Dictionary Elements.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Create and Access Dictionary")

key = st.text_input("Enter Key")
value = st.text_input("Enter Value")

if st.button("CREATE", key="btn1"):
    my_dict = {key:value}

    st.success(my_dict)
    st.success(f"Access Value = {my_dict[key]}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

key = st.text_input("Enter Key", key="key1")
value = st.text_input("Enter Value", key="value1")

if st.button("CREATE", key="work1"):
    my_dict = {key:value}

    st.success(my_dict)
    st.success(f"Access Value = {my_dict[key]}")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Add New Key-Value Pair.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Add Key Value Pair")

key = st.text_input("Enter Key")
value = st.text_input("Enter Value")

if st.button("ADD", key="btn2"):
    my_dict = {}

    my_dict[key] = value

    st.success(my_dict)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

key = st.text_input("Enter Key", key="key2")
value = st.text_input("Enter Value", key="value2")

if st.button("ADD", key="work2"):
    my_dict = {}

    my_dict[key] = value

    st.success(my_dict)


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Update Dictionary Value.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Update Dictionary Value")

key = st.text_input("Enter Key")
value = st.text_input("Enter New Value")

if st.button("UPDATE", key="btn3"):
    my_dict = {"Name":"Python"}

    my_dict[key] = value

    st.success(my_dict)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

key = st.text_input("Enter Key", key="key3")
value = st.text_input("Enter New Value", key="value3")

if st.button("UPDATE", key="work3"):
    my_dict = {"Name":"Python"}

    my_dict[key] = value

    st.success(my_dict)


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Delete Key-Value Pair.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Delete Dictionary Element")

key = st.text_input("Enter Key")

if st.button("DELETE", key="btn4"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA"
    }

    if key in my_dict:
        del my_dict[key]

    st.success(my_dict)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

key = st.text_input("Enter Key", key="key4")

if st.button("DELETE", key="work4"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA"
    }

    if key in my_dict:
        del my_dict[key]

    st.success(my_dict)


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Length of Dictionary.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Length of Dictionary")

if st.button("FIND LENGTH", key="btn5"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA",
        "Year":"2026"
    }

    st.success(f"Length = {len(my_dict)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("FIND LENGTH", key="work5"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA",
        "Year":"2026"
    }

    st.success(f"Length = {len(my_dict)}")


#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Check Key Exists or Not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Check Key Exists")

key = st.text_input("Enter Key")

if st.button("CHECK", key="btn6"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA"
    }

    if key in my_dict:
        st.success("Key Exists")
    else:
        st.success("Key Does Not Exist")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

key = st.text_input("Enter Key", key="key6")

if st.button("CHECK", key="work6"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA"
    }

    if key in my_dict:
        st.success("Key Exists")
    else:
        st.success("Key Does Not Exist")

#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Display All Keys and Values.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Display Keys and Values")

if st.button("DISPLAY", key="btn7"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA",
        "Year":"2026"
    }

    st.success(list(my_dict.keys()))
    st.success(list(my_dict.values()))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("DISPLAY", key="work7"):
    my_dict = {
        "Name":"Python",
        "Course":"BCA",
        "Year":"2026"
    }

    st.success(list(my_dict.keys()))
    st.success(list(my_dict.values()))


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Merge Two Dictionaries.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Merge Two Dictionaries")

if st.button("MERGE", key="btn8"):
    dict1 = {
        "Name":"Python"
    }

    dict2 = {
        "Course":"BCA"
    }

    dict1.update(dict2)

    st.success(dict1)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("MERGE", key="work8"):
    dict1 = {
        "Name":"Python"
    }

    dict2 = {
        "Course":"BCA"
    }

    dict1.update(dict2)

    st.success(dict1)
