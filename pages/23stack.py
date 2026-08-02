import streamlit as st

st.set_page_config(page_title="DSA Stack", layout="centered")


# ---------- LOGIN ----------
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
# ---------- STACK CLASS ----------

class Stack:

    def __init__(self):
        self.items = [10,20,30]


    def push(self,data):
        self.items.append(data)


    def pop(self):
        if self.items:
            return self.items.pop()
        return "Stack Empty"


    def peek(self):
        if self.items:
            return self.items[-1]
        return "Stack Empty"


    def display(self):
        return self.items



# ---------- SESSION STATE ----------

if "stack_obj" not in st.session_state:
    st.session_state.stack_obj = Stack()


stack = st.session_state.stack_obj



# ---------- CSS ----------

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
    color:#90E0EF;
    font-size:40px;
    font-weight:bold;
}


.section{
    color:#90E0EF;
    font-size:26px;
    margin-top:25px;
}


.content{
    color:#9CA3AF;
    font-size:22px;
    line-height:1.6;
}


.stButton>button{

    background:linear-gradient(90deg,#0040ff,#8c00ff);
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 22px;
    font-weight:bold;

}

</style>
""", unsafe_allow_html=True)



st.markdown(
"<div class='title'>DSA Stack</div>",
unsafe_allow_html=True
)



# ================= Q1 =================

st.markdown(
"<div class='section'>Question 1.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Traverse Stack<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):
        self.items=[10,20,30]


    def display(self):

        for i in self.items:
            print(i)



s=Stack()

s.display()

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Show Stack",key="q1"):

    st.success(stack.display())





# ================= Q2 =================

st.markdown(
"<div class='section'>Question 2.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Push Operation<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):
        self.items=[]


    def push(self,data):

        self.items.append(data)



s=Stack()

s.push(10)

s.push(20)


print(s.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


value = st.text_input("Enter value",key="push_input")


if st.button("Push",key="q2"):

    if value:

        stack.push(int(value))

        st.success(stack.display())





# ================= Q3 =================

st.markdown(
"<div class='section'>Question 3.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Pop Operation<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[10,20,30]


    def pop(self):

        return self.items.pop()



s=Stack()

print(s.pop())

print(s.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Pop",key="q3"):

    result=stack.pop()

    st.success(stack.display())





# ================= Q4 =================

st.markdown(
"<div class='section'>Question 4.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Peek Top Element<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[10,20,30]


    def peek(self):

        return self.items[-1]



s=Stack()

print(s.peek())

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Peek",key="q4"):

    st.success(stack.peek())





# ================= Q5 =================

st.markdown(
"<div class='section'>Question 5.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Check Empty Stack<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[]



if len(s.items)==0:

    print("Empty")

else:

    print("Not Empty")

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Check Empty",key="q5"):

    if len(stack.display())==0:

        st.success("Stack Empty")

    else:

        st.success("Stack Not Empty")

# ================= Q6 =================

st.markdown(
"<div class='section'>Question 6.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Size of Stack<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):
        self.items=[10,20,30]


    def size(self):

        return len(self.items)



s=Stack()

print("Stack Size:",s.size())

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Find Size",key="q6"):

    st.success(len(stack.display()))





# ================= Q7 =================

st.markdown(
"<div class='section'>Question 7.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Search Element<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[10,20,30]


    def search(self,key):

        if key in self.items:

            print("Found")

        else:

            print("Not Found")



s=Stack()

s.search(20)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


search_value = st.text_input(
    "Enter element",
    key="search_stack"
)


if st.button("Search",key="q7"):

    if search_value:

        if int(search_value) in stack.display():

            st.success("Found")

        else:

            st.error("Not Found")





# ================= Q8 =================

st.markdown(
"<div class='section'>Question 8.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Reverse Stack<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[10,20,30]


    def reverse(self):

        self.items.reverse()



s=Stack()

s.reverse()


print(s.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Reverse Stack",key="q8"):

    stack.items.reverse()

    st.success(stack.display())





# ================= Q9 =================

st.markdown(
"<div class='section'>Question 9.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Find Maximum Element<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[10,20,30]


    def maximum(self):

        return max(self.items)



s=Stack()

print(s.maximum())

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Find Maximum",key="q9"):

    if stack.display():

        st.success(max(stack.display()))

    else:

        st.error("Empty Stack")





# ================= Q10 =================

st.markdown(
"<div class='section'>Question 10.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Remove Duplicates<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
class Stack:

    def __init__(self):

        self.items=[10,20,20,30]


    def remove_duplicate(self):

        self.items=list(set(self.items))



s=Stack()

s.remove_duplicate()


print(s.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Remove Duplicates",key="q10"):

    stack.items=list(set(stack.items))

    st.success(stack.display())        
