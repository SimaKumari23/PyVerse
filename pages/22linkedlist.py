import streamlit as st

st.set_page_config(page_title="DSA Linked List", layout="centered")


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
# ---------- FULL CSS ----------
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
    color:#90E0EF;
    font-size:40px;
    font-weight:bold;
}

.section {
    color:#90E0EF;
    font-size:26px;
    margin-top:25px;
}

.content {
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
    "<div class='title'>DSA Linked List</div>",
    unsafe_allow_html=True
)



# ---------- LINKED LIST CLASS ----------

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:

    def __init__(self):
        self.head=None


    def insert(self,data):

        new=Node(data)

        if not self.head:
            self.head=new
            return

        temp=self.head

        while temp.next:
            temp=temp.next

        temp.next=new



    def display(self):

        temp=self.head
        arr=[]

        while temp:
            arr.append(temp.data)
            temp=temp.next

        return arr



    def reverse(self):

        prev=None
        curr=self.head

        while curr:

            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        self.head=prev



    def search(self,key):

        temp=self.head

        while temp:

            if temp.data==key:
                return True

            temp=temp.next

        return False



# ---------- SAMPLE LIST ----------

ll=LinkedList()

for i in [10,20,30,40]:
    ll.insert(i)



# ================= Q1 =================

st.markdown(
"<div class='section'>Question 1.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Traverse Linked List<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)



temp=head

while temp:

    print(temp.data)

    temp=temp.next


""")


st.markdown(
"<div class='content'>🚀 working</div>",
unsafe_allow_html=True
)


if st.button("Show List",key="q1"):

    st.write(ll.display())





# ================= Q2 =================

st.markdown(
"<div class='section'>Question 2.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Insert Node<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)



new=Node(30)


temp=head


while temp.next:

    temp=temp.next



temp.next=new



while head:

    print(head.data)

    head=head.next


""")


val=st.text_input("Enter value",key="q2_input")


if st.button("Insert",key="q2"):

    ll.insert(int(val))

    st.success(ll.display())





# ================= Q3 =================


st.markdown(
"<div class='section'>Question 3.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Search Node<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)



key=20


temp=head


while temp:

    if temp.data==key:

        print("Found")

        break


    temp=temp.next


else:

    print("Not Found")


""")


num=st.text_input("Enter number",key="q3_input")


if st.button("Search",key="q3"):

    if ll.search(int(num)):

        st.success("Found")

    else:

        st.error("Not Found")





# ================= Q4 =================


st.markdown(
"<div class='section'>Question 4.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Reverse Linked List<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)



prev=None

curr=head



while curr:

    nxt=curr.next

    curr.next=prev

    prev=curr

    curr=nxt



head=prev



while head:

    print(head.data)

    head=head.next


""")


if st.button("Reverse",key="q4"):

    ll.reverse()

    st.success(ll.display())





# ================= Q5 =================


st.markdown(
"<div class='section'>Question 5.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Count Nodes<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)



count=0


temp=head


while temp:

    count=count+1

    temp=temp.next



print("Total Nodes:",count)


""")


if st.button("Count",key="q5"):

    st.success(len(ll.display()))


# ================= Q6 =================

st.markdown(
"<div class='section'>Question 6.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Find Maximum<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)



arr=[]

temp=head


while temp:

    arr.append(temp.data)

    temp=temp.next



maximum=max(arr)


print("Maximum Node:",maximum)


""")


if st.button("Find Max",key="q6"):

    st.success(max(ll.display()))





# ================= Q7 =================

st.markdown(
"<div class='section'>Question 7.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Find Minimum<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)



arr=[]

temp=head


while temp:

    arr.append(temp.data)

    temp=temp.next



minimum=min(arr)


print("Minimum Node:",minimum)


""")


if st.button("Find Min",key="q7"):

    st.success(min(ll.display()))





# ================= Q8 =================

st.markdown(
"<div class='section'>Question 8.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Sum of Nodes<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)



total=0


temp=head


while temp:

    total += temp.data

    temp=temp.next



print("Sum of Nodes:",total)


""")


if st.button("Find Sum",key="q8"):

    st.success(sum(ll.display()))





# ================= Q9 =================

st.markdown(
"<div class='section'>Question 9.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Average<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(30)



arr=[]


temp=head


while temp:

    arr.append(temp.data)

    temp=temp.next



average=sum(arr)/len(arr)


print("Average:",average)


""")


if st.button("Find Average",key="q9"):

    arr=ll.display()

    st.success(sum(arr)/len(arr))





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

class Node:

    def __init__(self,data):
        self.data=data
        self.next=None



head=Node(10)
head.next=Node(20)
head.next.next=Node(20)
head.next.next.next=Node(30)



arr=[]


temp=head


while temp:

    arr.append(temp.data)

    temp=temp.next



unique=list(set(arr))


print("After Removing Duplicate:")

print(unique)


""")


if st.button("Remove Duplicates",key="q10"):

    arr=list(set(ll.display()))

    st.success(arr)    
