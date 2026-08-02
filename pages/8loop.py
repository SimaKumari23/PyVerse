import streamlit  as st
st.set_page_config(page_title="Loop program", layout="centered")
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
st.markdown("<div class='title'>Loop program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>for loop</div>", unsafe_allow_html=True)
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print Hello World N times using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("👋 Print Hello World N Times")

n = st.slider("Select Number", 1, 50)

if st.button("PRINT"):
    for i in range(n):
        st.success("Hello World")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 50, key="q1")

if st.button("PRINT", key="btn1"):
    for i in range(n):
        st.success("Hello World")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from 1 to 10 using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Numbers 1 To 10")

for i in range(1, 10, 1):
    st.success(f"i={i}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

for i in range(1, 10, 1):
    st.success(f"i={i}")


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from 10 to 1 using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔄 Reverse 10 To 1")

for i in range(10, 0, -1):
    st.success(f"i={i}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

for i in range(10, 0, -1):
    st.success(f"i={i}")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from 1 to N using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Numbers 1 To N")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    for i in range(1, n + 1):
        st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q4")

if st.button("PRINT", key="btn4"):
    for i in range(1, n + 1):
        st.success(i)


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from N to 1 using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔄 Print Numbers N To 1")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    for i in range(n, 0, -1):
        st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q5")

if st.button("PRINT", key="btn5"):
    for i in range(n, 0, -1):
        st.success(i)
#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print even numbers from 1 to N using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Even Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    for i in range(1, n + 1):
        if i % 2 == 0:
            st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q6")

if st.button("PRINT", key="btn6"):
    for i in range(1, n + 1):
        if i % 2 == 0:
            st.success(i)


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print odd numbers from 1 to N using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Odd Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    for i in range(1, n + 1):
        if i % 2 != 0:
            st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q7")

if st.button("PRINT", key="btn7"):
    for i in range(1, n + 1):
        if i % 2 != 0:
            st.success(i)


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of first 10 natural numbers.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of First 10 Natural Numbers")

if st.button("SUM"):
    total = 0

    for i in range(1, 11):
        total += i

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("SUM", key="btn8"):
    total = 0

    for i in range(1, 11):
        total += i

    st.success(f"Sum = {total}")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of first N natural numbers.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of First N Natural Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("SUM"):
    total = 0

    for i in range(1, n + 1):
        total += i

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q9")

if st.button("SUM", key="btn9"):
    total = 0

    for i in range(1, n + 1):
        total += i

    st.success(f"Sum = {total}")


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum and average of first N natural numbers.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum and Average of First N Natural Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("CALCULATE"):
    total = 0

    for i in range(1, n + 1):
        total += i

    average = total / n

    st.success(f"Sum = {total}")
    st.success(f"Average = {average}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q10")

if st.button("CALCULATE", key="btn10"):
    total = 0

    for i in range(1, n + 1):
        total += i

    average = total / n

    st.success(f"Sum = {total}")
    st.success(f"Average = {average}")

#---------------------11----------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to generate the multiplication table of a number using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🧮 Table Generator")

t1=st.slider("Select a number",1,100)

if st.button("TABLE"):
    for i in range(1,11,1):
        st.write(i*t1)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1=st.slider("Select a number",1,100,key="q11")

if st.button("TABLE",key="btn11"):
    for i in range(1,11,1):
        st.write(i*t1)


#---------------------12----------------
st.markdown("<div class='section'>Question 12.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of even numbers from 1 to N.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of Even Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("SUM"):
    total = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100,key="q12")

if st.button("SUM",key="btn12"):
    total = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i

    st.success(f"Sum = {total}")


#---------------------13----------------
st.markdown("<div class='section'>Question 13.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of odd numbers from 1 to N.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of Odd Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("SUM"):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100,key="q13")

if st.button("SUM",key="btn13"):
    total = 0

    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i

    st.success(f"Sum = {total}")


#---------------------14----------------
st.markdown("<div class='section'>Question 14.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the factors of a number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Factors of a Number")

n = st.slider("Select Number", 1, 100)

if st.button("FIND FACTORS"):
    st.write(f"Factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100,key="q14")

if st.button("FIND FACTORS",key="btn14"):
    st.write(f"Factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            st.success(i)


#---------------------15----------------
st.markdown("<div class='section'>Question 15.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to demonstrate the break statement using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("⛔ Break Statement")

if st.button("RUN"):
    for i in range(1, 11):
        if i == 6:
            break
        st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("RUN",key="btn15"):
    for i in range(1, 11):
        if i == 6:
            break
        st.success(i)


#---------------------16----------------
st.markdown("<div class='section'>Question 16.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to demonstrate the continue statement using a for loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("⏭️ Continue Statement")

if st.button("RUN"):
    for i in range(1, 11):
        if i == 6:
            continue
        st.success(i)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("RUN",key="btn16"):
    for i in range(1, 11):
        if i == 6:
            continue
        st.success(i)
#---------------------1----------------
st.markdown("<div class='section'>while loop</div>", unsafe_allow_html=True)        
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from 1 to 10 using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Numbers 1 to 10")

if st.button("PRINT"):
    i = 1
    while i <= 10:
        st.success(i)
        i += 1
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("PRINT", key="btn17"):
    i = 1
    while i <= 10:
        st.success(i)
        i += 1


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from 10 to 1 using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔄 Print Numbers 10 to 1")

if st.button("PRINT"):
    i = 10
    while i >= 1:
        st.success(i)
        i -= 1
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("PRINT", key="btn18"):
    i = 10
    while i >= 1:
        st.success(i)
        i -= 1


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from 1 to N using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Numbers 1 to N")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    i = 1
    while i <= n:
        st.success(i)
        i += 1
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q19")

if st.button("PRINT", key="btn19"):
    i = 1
    while i <= n:
        st.success(i)
        i += 1


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print numbers from N to 1 using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔄 Print Numbers N to 1")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    i = n
    while i >= 1:
        st.success(i)
        i -= 1
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q20")

if st.button("PRINT", key="btn20"):
    i = n
    while i >= 1:
        st.success(i)
        i -= 1


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print even numbers using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Even Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    i = 2
    while i <= n:
        st.success(i)
        i += 2
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q21")

if st.button("PRINT", key="btn21"):
    i = 2
    while i <= n:
        st.success(i)
        i += 2

#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print odd numbers using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Print Odd Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("PRINT"):
    i = 1
    while i <= n:
        st.success(i)
        i += 2
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q22")

if st.button("PRINT", key="btn22"):
    i = 1
    while i <= n:
        st.success(i)
        i += 2


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of first 10 natural numbers using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of First 10 Natural Numbers")

if st.button("SUM"):
    i = 1
    total = 0

    while i <= 10:
        total += i
        i += 1

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("SUM", key="btn23"):
    i = 1
    total = 0

    while i <= 10:
        total += i
        i += 1

    st.success(f"Sum = {total}")


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum of first N natural numbers using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum of First N Natural Numbers")

n = st.slider("Select Number", 1, 100)

if st.button("SUM"):
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    st.success(f"Sum = {total}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q24")

if st.button("SUM", key="btn24"):
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    st.success(f"Sum = {total}")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the sum and average of first N natural numbers using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("➕ Sum and Average")

n = st.slider("Select Number", 1, 100)

if st.button("CALCULATE"):
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    average = total / n

    st.success(f"Sum = {total}")
    st.success(f"Average = {average}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

n = st.slider("Select Number", 1, 100, key="q25")

if st.button("CALCULATE", key="btn25"):
    i = 1
    total = 0

    while i <= n:
        total += i
        i += 1

    average = total / n

    st.success(f"Sum = {total}")
    st.success(f"Average = {average}")


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to generate the multiplication table using a while loop.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🧮 Multiplication Table")

num = st.slider("Select Number", 1, 100)

if st.button("TABLE"):
    i = 1

    while i <= 10:
        st.write(f"{num} × {i} = {num * i}")
        i += 1
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.slider("Select Number", 1, 100, key="q26")

if st.button("TABLE", key="btn26"):
    i = 1

    while i <= 10:
        st.write(f"{num} × {i} = {num * i}")
        i += 1        
