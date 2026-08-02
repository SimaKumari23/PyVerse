import streamlit as st

st.set_page_config(page_title="DSA Searching", layout="centered")

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
# ---------- SAMPLE DATA ----------
arr = [10, 20, 30, 40, 50, 60, 70]


# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background:
        radial-gradient(circle at center, rgba(168,85,247,0.28), transparent 70%),
        linear-gradient(135deg,#0B1026,#1A1D3A);
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
""",unsafe_allow_html=True)

st.markdown("<div class='title'>DSA Searching</div>",unsafe_allow_html=True)


# ================= Q1 =================
st.markdown("<div class='section'>Question 1.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Display Array<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
arr=[10,20,30,40,50]
print(arr)
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Show Array",key="q1"):
    st.success(arr)


# ================= Q2 =================
st.markdown("<div class='section'>Question 2.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Linear Search<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

val=st.number_input("Enter value",key="q2_input")

if st.button("Linear Search",key="q2"):

    def linear_search(arr,key):
        for i in range(len(arr)):
            if arr[i]==key:
                return i
        return -1

    res=linear_search(arr,val)

    if res!=-1:
        st.success(f"Found at index {res}")
    else:
        st.error("Not Found")


# ================= Q3 =================
st.markdown("<div class='section'>Question 3.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Binary Search<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def binary_search(arr,key):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1

    return -1
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

val=st.number_input("Enter value ",key="q3_input")

if st.button("Binary Search",key="q3"):

    def binary_search(arr,key):
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]==key:
                return mid
            elif arr[mid]<key:
                low=mid+1
            else:
                high=mid-1

        return -1

    res=binary_search(arr,val)

    if res!=-1:
        st.success(f"Found at index {res}")
    else:
        st.error("Not Found")


# ================= Q4 =================
st.markdown("<div class='section'>Question 4.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Find Maximum<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
print(max(arr))
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Find Max",key="q4"):
    st.success(max(arr))


# ================= Q5 =================
st.markdown("<div class='section'>Question 5.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Find Minimum<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
print(min(arr))
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Find Min",key="q5"):
    st.success(min(arr))


# ================= Q6 =================
st.markdown("<div class='section'>Question 6.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Count Elements<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
print(len(arr))
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Count Elements",key="q6"):
    st.success(len(arr))


# ================= Q7 =================
st.markdown("<div class='section'>Question 7.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Check Sorted<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
print(arr==sorted(arr))
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Check Sorted",key="q7"):
    st.success(arr==sorted(arr))


# ================= Q8 =================
st.markdown("<div class='section'>Question 8.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Reverse Array<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
arr.reverse()
print(arr)
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Reverse",key="q8"):
    st.success(list(reversed(arr)))


# ================= Q9 =================
st.markdown("<div class='section'>Question 9.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Sort Array<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
arr.sort()
print(arr)
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Sort",key="q9"):
    st.success(sorted(arr))


# ================= Q10 =================
st.markdown("<div class='section'>Question 10.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Insert Element<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
arr.append(100)
print(arr)
""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

val=st.number_input("Enter element",key="q10_input")

if st.button("Insert",key="q10"):
    arr.append(val)
    st.success(arr)
