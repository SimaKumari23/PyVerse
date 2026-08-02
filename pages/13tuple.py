import streamlit  as st
st.set_page_config(page_title="Tuple program", layout="centered")
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
st.markdown("<div class='title'>Tuple program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Create and Access Tuple Elements.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Create and Access Tuple")

elements = st.text_input("Enter Tuple Elements")

if st.button("CREATE TUPLE", key="btn1"):
    my_tuple = tuple(elements.split())

    st.success(my_tuple)
    st.success(f"First Element = {my_tuple[0]}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Tuple Elements", key="tuple1")

if st.button("CREATE TUPLE", key="work1"):
    my_tuple = tuple(elements.split())

    st.success(my_tuple)
    st.success(f"First Element = {my_tuple[0]}")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Length of Tuple.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Length of Tuple")

elements = st.text_input("Enter Tuple Elements")

if st.button("FIND LENGTH", key="btn2"):
    my_tuple = tuple(elements.split())

    st.success(f"Length = {len(my_tuple)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Tuple Elements", key="tuple2")

if st.button("FIND LENGTH", key="work2"):
    my_tuple = tuple(elements.split())

    st.success(f"Length = {len(my_tuple)}")


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Count Element in Tuple.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Count Element in Tuple")

elements = st.text_input("Enter Tuple Elements")
element = st.text_input("Enter Element")

if st.button("COUNT", key="btn3"):
    my_tuple = tuple(elements.split())

    count = my_tuple.count(element)

    st.success(f"Count = {count}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Tuple Elements", key="tuple3")
element = st.text_input("Enter Element", key="element3")

if st.button("COUNT", key="work3"):
    my_tuple = tuple(elements.split())

    count = my_tuple.count(element)

    st.success(f"Count = {count}")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Index of Element.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Find Index of Element")

elements = st.text_input("Enter Tuple Elements (space separated)")
element = st.text_input("Enter Element")

if st.button("FIND INDEX"):

    my_tuple = tuple(elements.split())

    if element in my_tuple:
        index = my_tuple.index(element)
        st.success(f"Index = {index}")
    else:
        st.error("Element not found in tuple")
""", language="python")
elements = st.text_input("Enter Tuple Elements (space separated)")
element = st.text_input("Enter Element")

if st.button("FIND INDEX"):

    my_tuple = tuple(elements.split())

    if element in my_tuple:
        index = my_tuple.index(element)
        st.success(f"Index = {index}")
    else:
        st.error("Element not found in tuple")    

#---------------------6----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Convert Tuple to List.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Tuple to List")

elements = st.text_input("Enter Tuple Elements")

if st.button("CONVERT", key="btn6"):
    my_tuple = tuple(elements.split())

    my_list = list(my_tuple)

    st.success(my_list)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Tuple Elements", key="tuple6")

if st.button("CONVERT", key="work6"):
    my_tuple = tuple(elements.split())

    my_list = list(my_tuple)

    st.success(my_list)


#---------------------7----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Maximum and Minimum Element.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Maximum and Minimum Element")

numbers = st.text_input("Enter Tuple Numbers")
if st.button("FIND", key="btn7"):
    my_tuple = tuple(map(int,numbers.split()))

    st.success(f"Maximum = {max(my_tuple)}")
    st.success(f"Minimum = {min(my_tuple)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter Tuple Numbers", key="tuple7")

if st.button("FIND", key="work7"):
    my_tuple = tuple(map(int,numbers.split()))

    st.success(f"Maximum = {max(my_tuple)}")
    st.success(f"Minimum = {min(my_tuple)}")


#---------------------8----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Concatenate Two Tuples.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Concatenate Two Tuples")

tuple1 = st.text_input("Enter First Tuple")
tuple2 = st.text_input("Enter Second Tuple")

if st.button("CONCATENATE", key="btn8"):
    t1 = tuple1.split()
    t2 = tuple2.split()

    result = tuple(t1 + t2)

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

tuple1 = st.text_input("Enter First Tuple", key="tuple8")
tuple2 = st.text_input("Enter Second Tuple", key="tuple9")

if st.button("CONCATENATE", key="work8"):
    t1 = tuple1.split()
    t2 = tuple2.split()

    result = tuple(t1 + t2)

    st.success(result)


#---------------------9----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Reverse a Tuple.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Reverse a Tuple")

elements = st.text_input("Enter Tuple Elements")

if st.button("REVERSE", key="btn9"):
    my_tuple = tuple(elements.split())

    result = my_tuple[::-1]

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Tuple Elements", key="tuple10")

if st.button("REVERSE", key="work9"):
    my_tuple = tuple(elements.split())

    result = my_tuple[::-1]

    st.success(result)

    

