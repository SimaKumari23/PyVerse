import streamlit as st

st.set_page_config(page_title="DSA Sorting", layout="centered")

#---------- LOGIN ----------

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

#---------- SAMPLE DATA ----------
arr = [50, 30, 70, 10, 90, 20]

#================= Q1 =================

st.markdown("<div class='section'>Question 1.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Display Array<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
arr=[50,30,70,10,90]
print(arr)
""")

if st.button("Show Array",key="q1"):
    st.success(arr)

#================= Q2 =================

st.markdown("<div class='section'>Question 2.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Bubble Sort<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
""")

if st.button("Bubble Sort",key="q2"):

    def bubble_sort(arr):
        a=arr.copy()
        n=len(a)
        for i in range(n):
            for j in range(0,n-i-1):
                if a[j]>a[j+1]:
                    a[j],a[j+1]=a[j+1],a[j]
        return a   # FIX: return loop ke bahar

    st.success(bubble_sort(arr))

#================= Q3 =================

st.markdown("<div class='section'>Question 3.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Selection Sort<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
""")

if st.button("Selection Sort",key="q3"):

    def selection_sort(arr):
        a=arr.copy()
        for i in range(len(a)):
            min=i
            for j in range(i+1,len(a)):
                if a[j]<a[min]:
                    min=j
            a[i],a[min]=a[min],a[i]
        return a   # FIX

    st.success(selection_sort(arr))

#================= Q4 =================

st.markdown("<div class='section'>Question 4.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Insertion Sort<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
""")

if st.button("Insertion Sort",key="q4"):

    def insertion_sort(arr):
        a=arr.copy()
        for i in range(1,len(a)):
            key=a[i]
            j=i-1
            while j>=0 and key<a[j]:
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
        return a   # FIX

    st.success(insertion_sort(arr))

#================= Q5 =================

st.markdown("<div class='section'>Question 5.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Quick Sort<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x<=pivot]
    right=[x for x in arr[1:] if x>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
""")

if st.button("Quick Sort",key="q5"):

    def quick_sort(arr):
        if len(arr)<=1:
            return arr
        pivot=arr[0]
        left=[x for x in arr[1:] if x<=pivot]
        right=[x for x in arr[1:] if x>pivot]
        return quick_sort(left)+[pivot]+quick_sort(right)

    st.success(quick_sort(arr))

#================= Q6 =================

st.markdown("<div class='section'>Question 6.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Merge Sort<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
    return arr
""")

if st.button("Merge Sort",key="q6"):

    def merge_sort(arr):
        if len(arr)>1:
            mid=len(arr)//2
            left=arr[:mid]
            right=arr[mid:]

            merge_sort(left)
            merge_sort(right)

            i=j=k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k]=left[i]
                    i+=1
                else:
                    arr[k]=right[j]
                    j+=1
                k+=1

            while i<len(left):
                arr[k]=left[i]
                i+=1
                k+=1

            while j<len(right):
                arr[k]=right[j]
                j+=1
                k+=1

        return arr   # FIX

    st.success(merge_sort(arr.copy()))
