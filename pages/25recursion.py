import streamlit as st

st.set_page_config(page_title="DSA Recursion", layout="centered")


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
"<div class='title'>DSA Recursion</div>",
unsafe_allow_html=True
)





# ================= Q1 =================

st.markdown(
"<div class='section'>Question 1.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Print Numbers using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def print_number(n):

    if n==0:
        return

    print_number(n-1)

    print(n)



print_number(5)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



n1 = st.number_input(
    "Enter number",
    min_value=1,
    key="q1_input"
)


if st.button("Print Numbers",key="q1"):

    result=[]


    def print_num(n):

        if n==0:
            return

        print_num(n-1)

        result.append(n)


    print_num(n1)


    st.success(result)







# ================= Q2 =================

st.markdown(
"<div class='section'>Question 2.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Sum of Natural Numbers<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def sum(n):

    if n==0:
        return 0

    return n + sum(n-1)



print(sum(5))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



n2 = st.number_input(
    "Enter number",
    min_value=0,
    key="q2_input"
)



if st.button("Find Sum",key="q2"):


    def recursive_sum(n):

        if n==0:
            return 0

        return n + recursive_sum(n-1)


    st.success(recursive_sum(n2))







# ================= Q3 =================

st.markdown("<div class='section'>Question 3.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Factorial using Recursion<br>💻 Code</div>",unsafe_allow_html=True)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def factorial(n):

    if n==0 or n==1:
        return 1

    return n * factorial(n-1)



print(factorial(5))

""")


st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)



n3 = st.number_input(
    "Enter number",
    min_value=0,
    key="q3_input"
)



if st.button("Factorial",key="q3"):


    def fact(n):

        if n==0 or n==1:
            return 1

        return n * fact(n-1)


    st.success(fact(n3))







# ================= Q4 =================

st.markdown(
"<div class='section'>Question 4.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Fibonacci Series using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def fibonacci(n):

    if n<=1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)



print(fibonacci(6))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



n4 = st.number_input(
    "Enter terms",
    min_value=1,
    key="q4_input"
)



if st.button("Generate Fibonacci",key="q4"):


    def fib(n):

        if n<=1:
            return n

        return fib(n-1)+fib(n-2)



    series=[]


    for i in range(n4):

        series.append(fib(i))


    st.success(series)







# ================= Q5 =================

st.markdown(
"<div class='section'>Question 5.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Reverse String using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def reverse(text):

    if len(text)==0:
        return text

    return reverse(text[1:])+text[0]



print(reverse("hello"))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



text = st.text_input(
    "Enter String",
    key="q5_input"
)



if st.button("Reverse",key="q5"):


    def reverse_string(s):

        if len(s)==0:
            return s

        return reverse_string(s[1:])+s[0]


    st.success(reverse_string(text))

# ================= Q6 =================

st.markdown(
"<div class='section'>Question 6.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Count Digits using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
def count_digit(n):

    if n==0:
        return 0

    return 1 + count_digit(n//10)



print(count_digit(12345))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


num6 = st.number_input(
    "Enter number",
    min_value=1,
    key="q6_input"
)


if st.button("Count Digits",key="q6"):


    def count_digits(n):

        if n==0:
            return 0

        return 1 + count_digits(n//10)


    st.success(count_digits(num6))





# ================= Q7 =================

st.markdown(
"<div class='section'>Question 7.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Power Calculation using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""
def power(a,b):

    if b==0:
        return 1

    return a * power(a,b-1)



print(power(2,5))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


base = st.number_input(
    "Enter Base",
    key="q7_base"
)

expo = st.number_input(
    "Enter Power",
    min_value=0,
    key="q7_power"
)


if st.button("Calculate Power",key="q7"):


    def power_rec(a,b):

        if b==0:
            return 1

        return a * power_rec(a,b-1)


    st.success(power_rec(base,expo))





# ================= Q8 =================

st.markdown(
"<div class='section'>Question 8.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>GCD using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def gcd(a,b):

    if b==0:
        return a

    return gcd(b,a%b)



print(gcd(12,18))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


a = st.number_input(
    "Enter First Number",
    key="q8_a"
)

b = st.number_input(
    "Enter Second Number",
    key="q8_b"
)


if st.button("Find GCD",key="q8"):


    def gcd_rec(x,y):

        if y==0:
            return x

        return gcd_rec(y,x%y)


    st.success(gcd_rec(a,b))





# ================= Q9 =================

st.markdown(
"<div class='section'>Question 9.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Binary Search using Recursion<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def binary_search(arr,left,right,key):

    if left<=right:

        mid=(left+right)//2


        if arr[mid]==key:
            return True


        elif key<arr[mid]:

            return binary_search(
                arr,left,mid-1,key
            )


        else:

            return binary_search(
                arr,mid+1,right,key
            )


    return False



arr=[10,20,30,40]

print(binary_search(arr,0,3,30))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



search = st.number_input(
    "Enter Search Element",
    key="q9_search"
)


if st.button("Binary Search",key="q9"):


    def binary_search(arr,left,right,key):

        if left<=right:

            mid=(left+right)//2


            if arr[mid]==key:
                return True


            elif key<arr[mid]:

                return binary_search(
                    arr,left,mid-1,key
                )


            else:

                return binary_search(
                    arr,mid+1,right,key
                )


        return False



    arr=[10,20,30,40,50]


    if binary_search(
        arr,
        0,
        len(arr)-1,
        search
    ):

        st.success("Found")

    else:

        st.error("Not Found")







# ================= Q10 =================

st.markdown(
"<div class='section'>Question 10.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Tower of Hanoi<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""
def tower(n,source,helper,destination):

    if n==1:

        print(
            source,
            "to",
            destination
        )

        return


    tower(
        n-1,
        source,
        destination,
        helper
    )


    print(
        source,
        "to",
        destination
    )


    tower(
        n-1,
        helper,
        source,
        destination
    )



tower(
3,
'A',
'B',
'C'
)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



disk = st.number_input(
    "Enter Number of Disks",
    min_value=1,
    max_value=5,
    key="q10_disk"
)


if st.button("Solve Tower of Hanoi",key="q10"):


    moves=[]


    def hanoi(n,source,helper,destination):

        if n==1:

            moves.append(
                f"{source} ➡ {destination}"
            )

            return


        hanoi(
            n-1,
            source,
            destination,
            helper
        )


        moves.append(
            f"{source} ➡ {destination}"
        )


        hanoi(
            n-1,
            helper,
            source,
            destination
        )


    hanoi(
        disk,
        "A",
        "B",
        "C"
    )


    st.success("Steps:")

    for m in moves:

        st.write(m)    
