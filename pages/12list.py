import streamlit  as st
st.set_page_config(page_title="List program", layout="centered")
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
st.markdown("<div class='title'>List program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Create and Access List Elements.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Create and Access List")

elements = st.text_input("Enter List Elements")

if st.button("CREATE LIST", key="btn1"):
    lst = elements.split()

    st.success(lst)
    st.success(f"First Element = {lst[0]}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter List Elements", key="list1")

if st.button("CREATE LIST", key="work1"):
    lst = elements.split()

    st.success(lst)
    st.success(f"First Element = {lst[0]}")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Add, Update and Delete Elements.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Add Update Delete List")

elements = st.text_input("Enter List Elements")
new_element = st.text_input("Enter New Element")

if st.button("UPDATE LIST", key="btn2"):
    lst = elements.split()

    lst.append(new_element)

    if len(lst)>1:
        lst[0] = new_element

    lst.pop()

    st.success(lst)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter List Elements", key="list2")
new_element = st.text_input("Enter New Element", key="element2")

if st.button("UPDATE LIST", key="work2"):
    lst = elements.split()

    lst.append(new_element)

    if len(lst)>1:
        lst[0] = new_element

    lst.pop()

    st.success(lst)


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Length of List.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Length of List")

elements = st.text_input("Enter List Elements")

if st.button("FIND LENGTH", key="btn3"):
    lst = elements.split()

    st.success(f"Length = {len(lst)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

elements = st.text_input("Enter List Elements", key="list3")

if st.button("FIND LENGTH", key="work3"):
    lst = elements.split()

    st.success(f"Length = {len(lst)}")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Maximum and Minimum Element.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Maximum and Minimum Element")

numbers = st.text_input("Enter Numbers")

if st.button("FIND", key="btn4"):
    lst = list(map(int,numbers.split()))

    st.success(f"Maximum = {max(lst)}")
    st.success(f"Minimum = {min(lst)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter Numbers", key="list4")

if st.button("FIND", key="work4"):
    lst = list(map(int,numbers.split()))

    st.success(f"Maximum = {max(lst)}")
    st.success(f"Minimum = {min(lst)}")


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Sum and Average of List.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Sum and Average of List")

numbers = st.text_input("Enter Numbers")

if st.button("CALCULATE", key="btn5"):
    lst = list(map(int,numbers.split()))

    total = sum(lst)
    average = total / len(lst)

    st.success(f"Sum = {total}")
    st.success(f"Average = {average}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter Numbers", key="list5")

if st.button("CALCULATE", key="work5"):
    lst = list(map(int,numbers.split()))

    total = sum(lst)
    average = total / len(lst)

    st.success(f"Sum = {total}")
    st.success(f"Average = {average}")


#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Sort List (Ascending/Descending).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Sort List")

numbers = st.text_input("Enter Numbers")

if st.button("SORT", key="btn6"):
    lst = list(map(int,numbers.split()))

    st.success(f"Ascending = {sorted(lst)}")
    st.success(f"Descending = {sorted(lst,reverse=True)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter Numbers", key="list6")

if st.button("SORT", key="work6"):
    lst = list(map(int,numbers.split()))

    st.success(f"Ascending = {sorted(lst)}")
    st.success(f"Descending = {sorted(lst,reverse=True)}")

#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Reverse a List.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Reverse a List")

numbers = st.text_input("Enter List Elements")

if st.button("REVERSE", key="btn7"):
    lst = numbers.split()

    lst.reverse()

    st.success(lst)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter List Elements", key="list7")

if st.button("REVERSE", key="work7"):
    lst = numbers.split()

    lst.reverse()

    st.success(lst)


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Search an Element in List.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Search Element")

numbers = st.text_input("Enter List Elements")
element = st.text_input("Enter Element to Search")

if st.button("SEARCH", key="btn8"):
    lst = numbers.split()

    if element in lst:
        st.success("Element Found")
    else:
        st.success("Element Not Found")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter List Elements", key="list8")
element = st.text_input("Enter Element to Search", key="element8")

if st.button("SEARCH", key="work8"):
    lst = numbers.split()

    if element in lst:
        st.success("Element Found")
    else:
        st.success("Element Not Found")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Remove Duplicate Elements from List.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Remove Duplicate Elements")

numbers = st.text_input("Enter List Elements")

if st.button("REMOVE", key="btn9"):
    lst = numbers.split()

    result = []

    for i in lst:
        if i not in result:
            result.append(i)

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter List Elements", key="list9")

if st.button("REMOVE", key="work9"):
    lst = numbers.split()

    result = []

    for i in lst:
        if i not in result:
            result.append(i)

    st.success(result)


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Merge Two Lists.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Merge Two Lists")

list1 = st.text_input("Enter First List")
list2 = st.text_input("Enter Second List")

if st.button("MERGE", key="btn10"):
    l1 = list1.split()
    l2 = list2.split()

    result = l1 + l2

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

list1 = st.text_input("Enter First List", key="list10")
list2 = st.text_input("Enter Second List", key="list11")

if st.button("MERGE", key="work10"):
    l1 = list1.split()
    l2 = list2.split()

    result = l1 + l2

    st.success(result)


#---------------------11----------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Common Elements Between Two Lists.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Common Elements")

list1 = st.text_input("Enter First List")
list2 = st.text_input("Enter Second List")

if st.button("FIND", key="btn11"):
    l1 = list1.split()
    l2 = list2.split()

    common = []

    for i in l1:
        if i in l2:
            common.append(i)

    st.success(common)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

list1 = st.text_input("Enter First List", key="list12")
list2 = st.text_input("Enter Second List", key="list13")

if st.button("FIND", key="work11"):
    l1 = list1.split()
    l2 = list2.split()

    common = []

    for i in l1:
        if i in l2:
            common.append(i)

    st.success(common)


























