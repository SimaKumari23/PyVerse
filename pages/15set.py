import streamlit  as st
st.set_page_config(page_title="Sets program", layout="centered")
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
        if st.button("⬅️ go to previous", use_container_width=True):
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
st.markdown("<div class='title'>Sets program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Create and Access Set.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Create and Access Set")

elements = st.text_input("Enter Set Elements")

if st.button("CREATE SET", key="btn1"):
    my_set = set(elements.split())

    st.success(my_set)
    st.success(f"First Element = {next(iter(my_set))}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Set Elements", key="set1")

if st.button("CREATE SET", key="work1"):
    my_set = set(elements.split())

    st.success(my_set)
    st.success(f"First Element = {next(iter(my_set))}")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Add and Remove Elements from Set.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Add and Remove Set Element")

element = st.text_input("Enter Element")

if st.button("UPDATE SET", key="btn2"):
    my_set = {"Python","Java","C"}

    my_set.add(element)

    my_set.remove("Java")

    st.success(my_set)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

element = st.text_input("Enter Element", key="element2")

if st.button("UPDATE SET", key="work2"):
    my_set = {"Python","Java","C"}

    my_set.add(element)

    my_set.remove("Java")

    st.success(my_set)


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Length of Set.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Length of Set")

elements = st.text_input("Enter Set Elements")

if st.button("FIND LENGTH", key="btn3"):
    my_set = set(elements.split())

    st.success(f"Length = {len(my_set)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Set Elements", key="set3")

if st.button("FIND LENGTH", key="work3"):
    my_set = set(elements.split())

    st.success(f"Length = {len(my_set)}")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Union of Two Sets.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Union of Two Sets")

set1 = st.text_input("Enter First Set")
set2 = st.text_input("Enter Second Set")

if st.button("UNION", key="btn4"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.union(s2)

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

set1 = st.text_input("Enter First Set", key="set4")
set2 = st.text_input("Enter Second Set", key="set5")

if st.button("UNION", key="work4"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.union(s2)

    st.success(result)


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Intersection of Two Sets.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Intersection of Two Sets")

set1 = st.text_input("Enter First Set")
set2 = st.text_input("Enter Second Set")

if st.button("INTERSECTION", key="btn5"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.intersection(s2)

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

set1 = st.text_input("Enter First Set", key="set6")
set2 = st.text_input("Enter Second Set", key="set7")

if st.button("INTERSECTION", key="work5"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.intersection(s2)

    st.success(result)
#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Difference Between Two Sets.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Difference of Two Sets")

set1 = st.text_input("Enter First Set")
set2 = st.text_input("Enter Second Set")

if st.button("DIFFERENCE", key="btn6"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.difference(s2)

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

set1 = st.text_input("Enter First Set", key="set8")
set2 = st.text_input("Enter Second Set", key="set9")

if st.button("DIFFERENCE", key="work6"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.difference(s2)

    st.success(result)


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Symmetric Difference of Two Sets.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Symmetric Difference")

set1 = st.text_input("Enter First Set")
set2 = st.text_input("Enter Second Set")

if st.button("SYMMETRIC DIFFERENCE", key="btn7"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.symmetric_difference(s2)

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

set1 = st.text_input("Enter First Set", key="set10")
set2 = st.text_input("Enter Second Set", key="set11")

if st.button("SYMMETRIC DIFFERENCE", key="work7"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    result = s1.symmetric_difference(s2)

    st.success(result)


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Check Subset and Superset.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Subset and Superset")

set1 = st.text_input("Enter First Set")
set2 = st.text_input("Enter Second Set")

if st.button("CHECK", key="btn8"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    st.success(f"Subset = {s1.issubset(s2)}")
    st.success(f"Superset = {s1.issuperset(s2)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

set1 = st.text_input("Enter First Set", key="set12")
set2 = st.text_input("Enter Second Set", key="set13")

if st.button("CHECK", key="work8"):
    s1 = set(set1.split())
    s2 = set(set2.split())

    st.success(f"Subset = {s1.issubset(s2)}")
    st.success(f"Superset = {s1.issuperset(s2)}")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Remove Duplicate Elements Using Set.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Remove Duplicate Elements")

elements = st.text_input("Enter Elements")

if st.button("REMOVE", key="btn9"):
    my_set = set(elements.split())

    st.success(my_set)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter Elements")

if st.button("REMOVE", key="key9"):
    my_set = set(elements.split())

    st.success(my_set)
