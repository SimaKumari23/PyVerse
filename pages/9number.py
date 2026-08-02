import streamlit  as st
st.set_page_config(page_title="Number program", layout="centered")
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
st.markdown("<div class='title'>Number program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Using for loop</div>", unsafe_allow_html=True)
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is prime or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("⭐ Prime Number Checker")

n=st.slider("Select a number",1,100)

if st.button("CHECK PRIME"):
    f=0

    for i in range(1,n+1,1):
        if n%i==0:
            f=f+1

    if f==2:
        st.success("PRIME NUMBER")
    else:
        st.success("NOT A PRIME NUMBER")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n=st.slider("Select a number",1,100,key="q1")

if st.button("CHECK PRIME",key="btn1"):
    f=0

    for i in range(1,n+1,1):
        if n%i==0:
            f=f+1

    if f==2:
        st.success("PRIME NUMBER")
    else:
        st.success("NOT A PRIME NUMBER")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the factorial of a number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("📈 Factorial Program")

n=st.slider("pick a number",1,100)

if st.button("FACTORIAL"):
    f=1

    for i in range(1,n+1,1):
        f=f*i

    st.success(f"Factorial of {n}={f}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n=st.slider("pick a number",1,100,key="q2")

if st.button("FACTORIAL",key="btn2"):
    f=1

    for i in range(1,n+1,1):
        f=f*i

    st.success(f"Factorial of {n}={f}")


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Fibonacci series.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔄 Fibonacci Series")

t1=st.slider("Select a number",1,20)

if st.button("FIBONACCI"):
    a=0
    b=1

    st.write(a)
    st.write(b)

    for i in range(1,t1-1,1):
        c=a+b
        st.write(c)
        a=b
        b=c
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1=st.slider("Select a number",1,20,key="q3")

if st.button("FIBONACCI",key="btn3"):
    a=0
    b=1

    st.write(a)
    st.write(b)

    for i in range(1,t1-1,1):
        c=a+b
        st.write(c)
        a=b
        b=c


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print prime numbers in a given range.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("⭐ Prime Numbers in a Given Range")

n = st.slider("Select Ending Number", 2, 100)

if st.button("PRINT"):
    for num in range(2, n + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            st.success(num)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Ending Number", 2, 100,key="q4")

if st.button("PRINT",key="btn4"):
    for num in range(2, n + 1):
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            st.success(num)


#---------------------5----------------
st.markdown("<div class='section'>using while loop</div>", unsafe_allow_html=True)            
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is palindrome or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔁 Palindrome Number")

t1=st.slider("Select a number",1,1000)

if st.button("REVERSE"):
    n=t1#123
    s=0

    while n>0:
        r=n%10#3,2,1
        s=s*10+r#0*10+3=3,3*10+2=32,32*10+1=321
        n=int(n/10)#12,1,0

    st.success(f"Reverse={s}")

    if s==t1:
        st.success("PALINDROME NUMBER")
    else:
        st.success("NOT A PALINDROME NUMBER")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1=st.slider("Select a number",1,1000,key="q5")

if st.button("REVERSE",key="btn5"):
    n=t1#123
    s=0

    while n>0:
        r=n%10#3,2,1
        s=s*10+r#0*10+3=3,3*10+2=32,32*10+1=321
        n=int(n/10)#12,1,0

    st.success(f"Reverse={s}")

    if s==t1:
        st.success("PALINDROME NUMBER")
    else:
        st.success("NOT A PALINDROME NUMBER")
#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is an Armstrong number or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Armstrong Number")

t1=st.slider("Select a number",1,1000)

if st.button("CHECK ARMSTRONG"):
    n=t1
    s=0

    while n>0:
        r=n%10
        s=s+(r*r*r)
        n=int(n/10)

    if s==t1:
        st.success("ARMSTRONG NUMBER")
    else:
        st.success("NOT AN ARMSTRONG NUMBER")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1=st.slider("Select a number",1,1000,key="q6")

if st.button("CHECK ARMSTRONG",key="btn6"):
    n=t1
    s=0

    while n>0:
        r=n%10
        s=s+(r*r*r)
        n=int(n/10)

    if s==t1:
        st.success("ARMSTRONG NUMBER")
    else:
        st.success("NOT AN ARMSTRONG NUMBER")


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to reverse a number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔄 Reverse a Number")

t1=st.slider("Select a number",1,1000)

if st.button("REVERSE"):
    n=t1#123
    s=0

    while n>0:
        r=n%10#3,2,1
        s=s*10+r#0*10+3=3,3*10+2=32,32*10+1=321
        n=int(n/10)#12,1,0

    st.success(f"Reverse={s}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1=st.slider("Select a number",1,1000,key="q7")

if st.button("REVERSE",key="btn7"):
    n=t1#123
    s=0

    while n>0:
        r=n%10#3,2,1
        s=s*10+r#0*10+3=3,3*10+2=32,32*10+1=321
        n=int(n/10)#12,1,0

    st.success(f"Reverse={s}")


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to count the digits of a number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Count Digits")

num = st.number_input("Enter Number", min_value=0, step=1)

if st.button("COUNT"):
    temp = num
    count = 0

    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp //= 10

    st.success(f"Total Digits = {count}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number", min_value=0, step=1, key="q8")

if st.button("COUNT",key="btn8"):
    temp = num
    count = 0

    if temp == 0:
        count = 1
    else:
        while temp > 0:
            count += 1
            temp //= 10

    st.success(f"Total Digits = {count}")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of digits of a number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of Digits")

num = st.number_input("Enter Number", min_value=0, step=1)

if st.button("SUM"):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number", min_value=0, step=1, key="q9")

if st.button("SUM",key="btn9"):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10

    st.success(f"Sum = {total}")


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is a perfect number or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("✅ Perfect Number")

num = st.number_input("Enter Number", min_value=1, step=1)

if st.button("CHECK"):
    i = 1
    total = 0

    while i < num:
        if num % i == 0:
            total += i
        i += 1

    if total == num:
        st.success("Perfect Number")
    else:
        st.error("Not a Perfect Number")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter Number", min_value=1, step=1, key="q10")

if st.button("CHECK",key="btn10"):
    i = 1
    total = 0

    while i < num:
        if num % i == 0:
            total += i
        i += 1

    if total == num:
        st.success("Perfect Number")
    else:
        st.error("Not a Perfect Number")






