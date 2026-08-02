import streamlit as st

st.set_page_config(page_title="DSA Queue", layout="centered")


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
# ---------- QUEUE CLASS ----------

class Queue:

    def __init__(self):
        self.items = [10,20,30]


    def enqueue(self,data):
        self.items.append(data)


    def dequeue(self):

        if self.items:
            return self.items.pop(0)

        return None


    def front(self):

        if self.items:
            return self.items[0]

        return None


    def display(self):
        return self.items



# ---------- SESSION STATE ----------

if "queue_obj" not in st.session_state:
    st.session_state.queue_obj = Queue()


queue = st.session_state.queue_obj



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
"<div class='title'>DSA Queue</div>",
unsafe_allow_html=True
)




# ================= Q1 =================

st.markdown(
"<div class='section'>Question 1.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Traverse Queue<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def display(self):

        for i in self.items:

            print(i)



q=Queue()

q.display()

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Show Queue",key="q1"):

    st.success("Queue Elements")

    st.write(queue.display())






# ================= Q2 =================

st.markdown(
"<div class='section'>Question 2.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Enqueue Operation<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[]


    def enqueue(self,data):

        self.items.append(data)



q=Queue()

q.enqueue(40)


print(q.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


value = st.text_input(
    "Enter value",
    key="q2_input"
)


if st.button("Enqueue",key="q2"):

    if value:

        queue.enqueue(int(value))

        st.success("Updated Queue")

        st.write(queue.display())







# ================= Q3 =================

st.markdown(
"<div class='section'>Question 3.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Dequeue Operation<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def dequeue(self):

        return self.items.pop(0)



q=Queue()


removed=q.dequeue()


print(removed)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Dequeue",key="q3"):

    removed = queue.dequeue()


    if removed is not None:

        st.success("Removed Element")

        st.write(removed)


        st.success("Updated Queue")

        st.write(queue.display())

    else:

        st.error("Queue Empty")







# ================= Q4 =================

st.markdown(
"<div class='section'>Question 4.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Front Element<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def front(self):

        return self.items[0]



q=Queue()


print(q.front())

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Front",key="q4"):

    result = queue.front()


    if result:

        st.success("Front Element")

        st.write(result)

    else:

        st.error("Queue Empty")







# ================= Q5 =================

st.markdown(
"<div class='section'>Question 5.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Check Empty Queue<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[]



if len(q.items)==0:

    print("Queue Empty")

else:

    print("Queue Not Empty")

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Check Empty",key="q5"):

    if len(queue.display())==0:

        st.success("Queue Empty")

    else:

        st.success("Queue Not Empty")

# ================= Q6 =================

st.markdown(
"<div class='section'>Question 6.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Size of Queue<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def size(self):

        return len(self.items)



q=Queue()


print("Queue Size:",q.size())

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Find Size",key="q6"):

    st.success("Queue Size")

    st.write(len(queue.display()))





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

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def search(self,key):

        if key in self.items:

            print("Found")

        else:

            print("Not Found")



q=Queue()


q.search(20)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


num = st.text_input(
    "Enter number",
    key="q7_input"
)


if st.button("Search",key="q7"):

    if num:

        if int(num) in queue.display():

            st.success("Found")

        else:

            st.error("Not Found")






# ================= Q8 =================

st.markdown(
"<div class='section'>Question 8.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Reverse Queue<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def reverse(self):

        self.items.reverse()



q=Queue()


q.reverse()


print(q.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Reverse Queue",key="q8"):

    queue.items.reverse()

    st.success("Reversed Queue")

    st.write(queue.display())







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

class Queue:

    def __init__(self):

        self.items=[10,20,30]


    def maximum(self):

        return max(self.items)



q=Queue()


print(q.maximum())

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Find Maximum",key="q9"):

    if queue.display():

        st.success(max(queue.display()))

    else:

        st.error("Queue Empty")







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

class Queue:

    def __init__(self):

        self.items=[10,20,20,30]


    def remove_duplicate(self):

        self.items=list(set(self.items))



q=Queue()


q.remove_duplicate()


print(q.items)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Remove Duplicates",key="q10"):

    queue.items = list(set(queue.items))

    st.success("After Removing Duplicate")

    st.write(queue.display())        
