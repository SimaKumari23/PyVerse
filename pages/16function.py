import streamlit  as st
st.set_page_config(page_title="Function program", layout="centered")
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
st.markdown("<div class='title'>Function program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Factorial using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Factorial Using Function")

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

num = st.slider("Select Number",1,100)

if st.button("FACTORIAL", key="btn1"):
    st.success(factorial(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,100,key="num1")

def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    return f

if st.button("FACTORIAL", key="work1"):
    st.success(factorial(num))


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Fibonacci using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Fibonacci Using Function")

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        c = a+b
        a = b
        b = c

    return result

num = st.slider("Select Number",1,20)

if st.button("FIBONACCI", key="btn2"):
    st.success(fibonacci(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,20,key="num2")

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        c = a+b
        a = b
        b = c

    return result

if st.button("FIBONACCI", key="work2"):
    st.success(fibonacci(num))


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Multiplication Table using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Table Using Function")

def table(n):
    result=[]
    for i in range(1,11):
        result.append(n*i)
    return result

num = st.slider("Select Number",1,100)

if st.button("TABLE", key="btn3"):
    st.success(table(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,100,key="num3")

def table(n):
    result=[]
    for i in range(1,11):
        result.append(n*i)
    return result

if st.button("TABLE", key="work3"):
    st.success(table(num))


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Sum of N Natural Numbers using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Sum Using Function")

def sum_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

num = st.slider("Select Number",1,100)

if st.button("SUM", key="btn4"):
    st.success(sum_n(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,100,key="num4")

def sum_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total

if st.button("SUM", key="work4"):
    st.success(sum_n(num))


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Greatest of 3 Numbers using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Greatest of 3 Numbers")

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")
c = st.number_input("Enter Third Number")

if st.button("FIND", key="btn5"):
    st.success(greatest(a,b,c))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

a = st.number_input("Enter First Number",key="a5")
b = st.number_input("Enter Second Number",key="b5")
c = st.number_input("Enter Third Number",key="c5")

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

if st.button("FIND", key="work5"):
    st.success(greatest(a,b,c))
#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Prime Number using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Prime Number Using Function")

def prime(n):
    count = 0

    for i in range(1,n+1):
        if n%i==0:
            count += 1

    if count == 2:
        return "PRIME NUMBER"
    else:
        return "NOT A PRIME NUMBER"

num = st.slider("Select Number",1,100)

if st.button("CHECK", key="btn6"):
    st.success(prime(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,100,key="num6")

def prime(n):
    count = 0

    for i in range(1,n+1):
        if n%i==0:
            count += 1

    if count == 2:
        return "PRIME NUMBER"
    else:
        return "NOT A PRIME NUMBER"

if st.button("CHECK", key="work6"):
    st.success(prime(num))


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Palindrome Number using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Palindrome Using Function")

def palindrome(n):
    temp = n
    rev = 0

    while n>0:
        r = n%10
        rev = rev*10+r
        n = n//10

    if temp == rev:
        return "PALINDROME NUMBER"
    else:
        return "NOT A PALINDROME NUMBER"

num = st.number_input("Enter Number",min_value=1)

if st.button("CHECK", key="btn7"):
    st.success(palindrome(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number",min_value=1,key="num7")

def palindrome(n):
    temp = n
    rev = 0

    while n>0:
        r = n%10
        rev = rev*10+r
        n = n//10

    if temp == rev:
        return "PALINDROME NUMBER"
    else:
        return "NOT A PALINDROME NUMBER"

if st.button("CHECK", key="work7"):
    st.success(palindrome(num))


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Armstrong Number using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Armstrong Using Function")

def armstrong(n):
    temp = n
    total = 0

    while n>0:
        r = n%10
        total = total + (r*r*r)
        n = n//10

    if temp == total:
        return "ARMSTRONG NUMBER"
    else:
        return "NOT AN ARMSTRONG NUMBER"

num = st.number_input("Enter Number",min_value=1)

if st.button("CHECK", key="btn8"):
    st.success(armstrong(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number",min_value=1,key="num8")

def armstrong(n):
    temp = n
    total = 0

    while n>0:
        r = n%10
        total = total + (r*r*r)
        n = n//10

    if temp == total:
        return "ARMSTRONG NUMBER"
    else:
        return "NOT AN ARMSTRONG NUMBER"

if st.button("CHECK", key="work8"):
    st.success(armstrong(num))


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Even/Odd using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Even Odd Using Function")

def even_odd(n):
    if n%2==0:
        return "EVEN NUMBER"
    else:
        return "ODD NUMBER"

num = st.number_input("Enter Number")

if st.button("CHECK", key="btn9"):
    st.success(even_odd(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number",key="num9")

def even_odd(n):
    if n%2==0:
        return "EVEN NUMBER"
    else:
        return "ODD NUMBER"

if st.button("CHECK", key="work9"):
    st.success(even_odd(num))


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Sum of Digits using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Sum of Digits Using Function")

def sum_digits(n):
    total = 0

    while n>0:
        r = n%10
        total += r
        n = n//10

    return total

num = st.number_input("Enter Number")

if st.button("SUM", key="btn10"):
    st.success(sum_digits(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number",key="num10")

def sum_digits(n):
    total = 0

    while n>0:
        r = n%10
        total += r
        n = n//10

    return total

if st.button("SUM", key="work10"):
    st.success(sum_digits(num))
#---------------------11----------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> String Reverse using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("String Reverse Using Function")

def reverse_string(s):
    return s[::-1]

text = st.text_input("Enter String")

if st.button("REVERSE", key="btn11"):
    st.success(reverse_string(text))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text11")

def reverse_string(s):
    return s[::-1]

if st.button("REVERSE", key="work11"):
    st.success(reverse_string(text))


#---------------------12----------------
st.markdown("<div class='section'>Question 12.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> String Palindrome using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("String Palindrome Using Function")

def palindrome(s):
    if s == s[::-1]:
        return "PALINDROME STRING"
    else:
        return "NOT A PALINDROME STRING"

text = st.text_input("Enter String")

if st.button("CHECK", key="btn12"):
    st.success(palindrome(text))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text12")

def palindrome(s):
    if s == s[::-1]:
        return "PALINDROME STRING"
    else:
        return "NOT A PALINDROME STRING"

if st.button("CHECK", key="work12"):
    st.success(palindrome(text))


#---------------------13----------------
st.markdown("<div class='section'>Question 13.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> List Sum using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("List Sum Using Function")

def list_sum(lst):
    total = 0

    for i in lst:
        total += i

    return total

numbers = st.text_input("Enter List Numbers")

if st.button("SUM", key="btn13"):
    lst = list(map(int,numbers.split()))

    st.success(list_sum(lst))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter List Numbers", key="list13")

def list_sum(lst):
    total = 0

    for i in lst:
        total += i

    return total

if st.button("SUM", key="work13"):
    lst = list(map(int,numbers.split()))

    st.success(list_sum(lst))


#---------------------14----------------
st.markdown("<div class='section'>Question 14.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> List Maximum/Minimum using Function.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("List Max Min Using Function")

def max_min(lst):
    return max(lst), min(lst)

numbers = st.text_input("Enter List Numbers")

if st.button("FIND", key="btn14"):
    lst = list(map(int,numbers.split()))

    result = max_min(lst)

    st.success(f"Maximum = {result[0]}")
    st.success(f"Minimum = {result[1]}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

numbers = st.text_input("Enter List Numbers", key="list14")

def max_min(lst):
    return max(lst), min(lst)

if st.button("FIND", key="work14"):
    lst = list(map(int,numbers.split()))

    result = max_min(lst)

    st.success(f"Maximum = {result[0]}")
    st.success(f"Minimum = {result[1]}")


#---------------------15----------------
st.markdown("<div class='section'>Question 15.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Factorial & Fibonacci using Recursion.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Recursion Factorial and Fibonacci")

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


num = st.slider("Select Number",1,10)

if st.button("RUN", key="btn15"):
    st.success(f"Factorial = {factorial(num)}")

    result=[]

    for i in range(num):
        result.append(fibonacci(i))

    st.success(f"Fibonacci = {result}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,10,key="num15")

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

if st.button("RUN", key="work15"):
    st.success(f"Factorial = {factorial(num)}")

    result=[]

    for i in range(num):
        result.append(fibonacci(i))

    st.success(f"Fibonacci = {result}")
st.markdown("<div class='title'>Recursion program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Factorial using Recursion.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Factorial Using Recursion")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = st.slider("Select Number",1,10)

if st.button("FACTORIAL", key="btn1"):
    st.success(factorial(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,10,key="num16")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if st.button("FACTORIAL", key="work16"):
    st.success(factorial(num))


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Fibonacci Series using Recursion.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Fibonacci Using Recursion")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num = st.slider("Select Number",1,10)

if st.button("FIBONACCI", key="btn2"):
    result = []

    for i in range(num):
        result.append(fibonacci(i))

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,10,key="num17")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if st.button("FIBONACCI", key="work17"):
    result = []

    for i in range(num):
        result.append(fibonacci(i))

    st.success(result)


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Sum of N Natural Numbers using Recursion.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Sum of Natural Numbers Using Recursion")

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

num = st.slider("Select Number",1,100)

if st.button("SUM", key="btn3"):
    st.success(sum_n(num))
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number",1,100,key="num18")

def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

if st.button("SUM", key="work18"):
    st.success(sum_n(num))    
