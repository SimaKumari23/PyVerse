import streamlit  as st
st.set_page_config(page_title="Conditional program", layout="centered")
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
st.markdown("<div class='title'>Conditional program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>if statement</div>", unsafe_allow_html=True)
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to check whether a number is positive or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("Positive Number Checker")
num = st.number_input("Enter a number")
if st.button("CHECK"):
    if num > 0:
        st.success(f"{num} is a Positive Number")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
num = st.number_input("Enter a number")
if st.button("CHECK"):
    if num > 0:
        st.success(f"{num} is a Positive Number")

#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is a multiple of 7 or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Multiple of 7 Checker")

num = st.number_input("Enter a number")

if st.button("CHECK"):
    if num % 7 == 0:
        st.success(f"{num} is Multiple of 7")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a number", key="q2")

if st.button("CHECK", key="btn2"):
    if num % 7 == 0:
        st.success(f"{num} is Multiple of 7")


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is divisible by 3 or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Divisible by 3 Checker")

num = st.number_input("Enter a number")

if st.button("CHECK"):
    if num % 3 == 0:
        st.success(f"{num} is Divisible by 3")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a number", key="q3")

if st.button("CHECK", key="btn3"):
    if num % 3 == 0:
        st.success(f"{num} is Divisible by 3")


#---------------------4----------------
st.markdown("<div class='section'>if-else statement</div>", unsafe_allow_html=True)        
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is odd or even.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🔢 Odd Even Checker")

t = st.slider("Enter a number")

if st.button("check odd or even"):
    if t % 2 == 0:
        st.success("even")
    else:
        st.success("odd")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t = st.slider("Enter a number", key="q4")

if st.button("check odd or even", key="btn4"):
    if t % 2 == 0:
        st.success("even")
    else:
        st.success("odd")


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the greater number between two numbers.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("⚖️ Greater Between Two Numbers")

t1 = st.text_input("Enter 1st no")
t2 = st.text_input("Enter 2nd no")

if st.button("GREATER"):
    if t1 > t2:
        st.success(f"Greater no={t1}")
    else:
        st.success(f"Greater no={t2}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1 = st.text_input("Enter 1st no", key="q5_1")
t2 = st.text_input("Enter 2nd no", key="q5_2")

if st.button("GREATER", key="btn5"):
    if t1 > t2:
        st.success(f"Greater no={t1}")
    else:
        st.success(f"Greater no={t2}")
#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a given year is a leap year or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("📅 Leap Year Checker")

year = st.number_input("Enter a year", min_value=1, step=1)

if st.button("CHECK LEAP"):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        st.success(f"{year} is a Leap Year")
    else:
        st.success(f"{year} is Not a Leap Year")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

year = st.number_input("Enter a year", min_value=1, step=1, key="q6")

if st.button("CHECK LEAP", key="btn6"):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        st.success(f"{year} is a Leap Year")
    else:
        st.success(f"{year} is Not a Leap Year")


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a given character is an alphabet or not.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Alphabet Checker")

ch = st.text_input("Enter a character")

if st.button("CHECK"):
    if ch.isalpha():
        st.success(f"{ch} is an Alphabet")
    else:
        st.success(f"{ch} is Not an Alphabet")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

ch = st.text_input("Enter a character", key="q7")

if st.button("CHECK", key="btn7"):
    if ch.isalpha():
        st.success(f"{ch} is an Alphabet")
    else:
        st.success(f"{ch} is Not an Alphabet")


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a given alphabet is a vowel or a consonant.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Vowel or Consonant Checker")

ch = st.text_input("Enter an alphabet")

if st.button("CHECK"):
    if ch.lower() in "aeiou":
        st.success(f"{ch} is a Vowel")
    else:
        st.success(f"{ch} is a Consonant")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

ch = st.text_input("Enter an alphabet", key="q8")

if st.button("CHECK", key="btn8"):
    if ch.lower() in "aeiou":
        st.success(f"{ch} is a Vowel")
    else:
        st.success(f"{ch} is a Consonant")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a given character is uppercase or lowercase.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Uppercase or Lowercase Checker")

ch = st.text_input("Enter a character")

if st.button("CHECK"):
    if ch.isupper():
        st.success(f"{ch} is Uppercase")
    else:
        st.success(f"{ch} is Lowercase")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

ch = st.text_input("Enter a character", key="q9")

if st.button("CHECK", key="btn9"):
    if ch.isupper():
        st.success(f"{ch} is Uppercase")
    else:
        st.success(f"{ch} is Lowercase")        
#---------------------10----------------
st.markdown("<div class='section'>Nested if statement</div>", unsafe_allow_html=True)        
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the greatest among three numbers using nested if statements.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🏆 Greatest Of Three Numbers")

t1 = st.slider("enter 1st no")
t2 = st.slider("enter 2nd no")
t3 = st.slider("enter 3rd no")

# using nested if else
if st.button("GREATEST NUMBER"):
    if t1 > t2 and t1 > t3:
        st.success(f"Greatest no={t1}")
    else:
        if t2 > t3:
            st.success(f"Greatest no={t2}")
        else:
            st.success(f"Greatest no={t3}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1 = st.slider("enter 1st no")
t2 = st.slider("enter 2nd no")
t3 = st.slider("enter 3rd no")

# using nested if else
if st.button("GREATEST NUMBER"):
    if t1 > t2 and t1 > t3:
        st.success(f"Greatest no={t1}")
    else:
        if t2 > t3:
            st.success(f"Greatest no={t2}")
        else:
            st.success(f"Greatest no={t3}")

#---------------------11----------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is divisible by both 3 and 7.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Divisible by Both 3 and 7")

num = st.number_input("Enter a number")

if st.button("CHECK"):
    if num % 3 == 0:
        if num % 7 == 0:
            st.success(f"{num} is Divisible by Both 3 and 7")
        else:
            st.success(f"{num} is Divisible by 3 but Not by 7")
    else:
        st.success(f"{num} is Not Divisible by 3 and 7")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a number", key="q10")

if st.button("CHECK", key="btn10"):
    if num % 3 == 0:
        if num % 7 == 0:
            st.success(f"{num} is Divisible by Both 3 and 7")
        else:
            st.success(f"{num} is Divisible by 3 but Not by 7")
    else:
        st.success(f"{num} is Not Divisible by 3 and 7")
#---------------------12----------------
st.markdown("<div class='section'>if-elif-else statement</div>", unsafe_allow_html=True)        
st.markdown("<div class='section'>Question 12.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to find the greatest among four numbers.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("🏅 Greatest Of Four Numbers")

t1 = st.slider("enter 1st no")
t2 = st.slider("enter 2nd no")
t3 = st.slider("enter 3rd no")
t4 = st.slider("enter 4th no")

# using multibranching or ladder
if st.button("GREATEST NUMBER"):
    if t1 > t2 and t1 > t3 and t1 > t4:
        st.success(f"Greatest no={t1}")

    elif t2 > t3 and t2 > t4:
        st.success(f"Greatest no={t2}")

    elif t3 > t4:
        st.success(f"Greatest no={t3}")

    elif t4 > t3:
        st.success(f"Greatest no={t4}")

    else:
        st.success("ALL are same")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

t1 = st.slider("enter 1st no", key="q11_1")
t2 = st.slider("enter 2nd no", key="q11_2")
t3 = st.slider("enter 3rd no", key="q11_3")
t4 = st.slider("enter 4th no", key="q11_4")

# using multibranching or ladder
if st.button("GREATEST NUMBER", key="btn11"):
    if t1 > t2 and t1 > t3 and t1 > t4:
        st.success(f"Greatest no={t1}")

    elif t2 > t3 and t2 > t4:
        st.success(f"Greatest no={t2}")

    elif t3 > t4:
        st.success(f"Greatest no={t3}")

    elif t4 > t3:
        st.success(f"Greatest no={t4}")

    else:
        st.success("ALL are same")
#---------------------13----------------
st.markdown("<div class='section'>Question 13.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to prepare a student report card by calculating total marks, percentage, and division.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("📋 Student Report Card")

p1 = int(st.text_input("Enter the marks of phy"))
p2 = int(st.text_input("Enter the marks of chem"))
p3 = int(st.text_input("Enter the marks of maths"))
p4 = int(st.text_input("Enter the marks of cs"))

if st.button("GET THE RESULT"):
    t = p1 + p2 + p3 + p4
    p = t / 4

    st.success(f"📊Total={t}")
    st.success(f"📈Percentage={p}")

    if p >= 60:
        st.success("🏆1ST DIVISION")

    elif p >= 45 and p < 60:
        st.success("🥈2ND DIVISION")

    elif p >= 35 and p < 45:
        st.success("🥈3RD DIVISION")

    else:
        st.success("FAIL")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

p1 = st.number_input("Enter the marks of phy",key="q12_p1")
p2 = st.number_input("Enter the marks of chem",key="q12_p2")
p3 = st.number_input("Enter the marks of maths",key="q12_p3")
p4 = st.number_input("Enter the marks of cs",key="q12_p4")

if st.button("GET THE RESULT",key="btn12"):
    t = p1 + p2 + p3 + p4
    p = t / 4

    st.success(f"📊Total={t}")
    st.success(f"📈Percentage={p}")

    if p >= 60:
        st.success("🏆1ST DIVISION")

    elif p >= 45 and p < 60:
        st.success("🥈2ND DIVISION")

    elif p >= 35 and p < 45:
        st.success("🥈3RD DIVISION")

    else:
        st.success("FAIL")
#---------------------14----------------
st.markdown("<div class='section'>Question 14.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is positive, negative, or zero.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Positive Negative Zero Checker")

num = st.number_input("Enter a number")

if st.button("CHECK"):
    if num > 0:
        st.success("Positive Number")

    elif num < 0:
        st.success("Negative Number")

    else:
        st.success("Zero")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a number",key="q13")

if st.button("CHECK",key="btn13"):
    if num > 0:
        st.success("Positive Number")

    elif num < 0:
        st.success("Negative Number")

    else:
        st.success("Zero")
#---------------------15----------------
st.markdown("<div class='section'>Question 15.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to calculate the grade of a student based on marks.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Grade Calculator")

marks = st.number_input("Enter your marks", min_value=0, max_value=100)

if st.button("GET GRADE"):
    if marks >= 90:
        st.success("Grade A")

    elif marks >= 75:
        st.success("Grade B")

    elif marks >= 60:
        st.success("Grade C")

    elif marks >= 40:
        st.success("Grade D")

    else:
        st.success("Fail")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

marks = st.number_input("Enter your marks", min_value=0, max_value=100,key="q14")

if st.button("GET GRADE",key="btn14"):
    if marks >= 90:
        st.success("Grade A")

    elif marks >= 75:
        st.success("Grade B")

    elif marks >= 60:
        st.success("Grade C")

    elif marks >= 40:
        st.success("Grade D")

    else:
        st.success("Fail")
#---------------------16----------------
st.markdown("<div class='section'>Question 16.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a menu-driven program to perform addition, subtraction, multiplication, and division.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Menu Driven Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

choice = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("CALCULATE"):

    if choice == "Addition":
        st.success(f"Result={num1 + num2}")

    elif choice == "Subtraction":
        st.success(f"Result={num1 - num2}")

    elif choice == "Multiplication":
        st.success(f"Result={num1 * num2}")

    elif choice == "Division":
        if num2 != 0:
            st.success(f"Result={num1 / num2}")
        else:
            st.error("Cannot divide by zero")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num1 = st.number_input("Enter first number", key="q15_1")
num2 = st.number_input("Enter second number", key="q15_2")

choice = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("CALCULATE", key="btn15"):

    if choice == "Addition":
        st.success(f"Result={num1 + num2}")

    elif choice == "Subtraction":
        st.success(f"Result={num1 - num2}")

    elif choice == "Multiplication":
        st.success(f"Result={num1 * num2}")

    elif choice == "Division":
        if num2 != 0:
            st.success(f"Result={num1 / num2}")
        else:
            st.error("Cannot divide by zero")
#---------------------17----------------
st.markdown("<div class='section'>Question 17.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to display the square of a number if it is even; otherwise display that the number is odd.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Square of Even Number")

num = st.number_input("Enter a number")

if st.button("CHECK"):

    if num % 2 == 0:
        st.success(f"Square={num*num}")

    else:
        st.success(f"{num} is Odd")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a number", key="q16")

if st.button("CHECK", key="btn16"):

    if num % 2 == 0:
        st.success(f"Square={num*num}")

    else:
        st.success(f"{num} is Odd")
#---------------------18----------------
st.markdown("<div class='section'>Question 18.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a ≥ b and display True or False.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Check a ≥ b")

a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")

if st.button("Check"):
    if a >= b:
        st.write(True)
    else:
        st.write(False)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

a = st.number_input("Enter First Number", key="q17_a")
b = st.number_input("Enter Second Number", key="q17_b")

if st.button("Check", key="btn17"):
    if a >= b:
        st.write(True)
    else:
        st.write(False)
#---------------------19----------------
st.markdown("<div class='section'>Question 19.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to display the square of an even number and the cube of an odd number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Square (Even) / Cube (Odd)")

num = st.number_input("Enter a Number", step=1)

if st.button("Show Result"):
    if num % 2 == 0:
        st.write(num ** 2)
    else:
        st.write(num ** 3)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a Number", step=1, key="q18")

if st.button("Show Result", key="btn18"):
    if num % 2 == 0:
        st.write(num ** 2)
    else:
        st.write(num ** 3)
#---------------------20----------------
st.markdown("<div class='section'>Question 20.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a menu-driven program to perform basic arithmetic operations based on the user's choice.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Basic Arithmetic Operations")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

st.write("1. Addition")
st.write("2. Subtraction")
st.write("3. Multiplication")
st.write("4. Division")

choice = st.number_input("Enter Your Choice", min_value=1, max_value=4, step=1)

if st.button("Calculate"):
    if choice == 1:
        st.write(num1 + num2)
    elif choice == 2:
        st.write(num1 - num2)
    elif choice == 3:
        st.write(num1 * num2)
    elif choice == 4:
        st.write(num1 / num2)
    else:
        st.write("Invalid Syntax")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num1 = st.number_input("Enter First Number", key="q19_1")
num2 = st.number_input("Enter Second Number", key="q19_2")

st.write("1. Addition")
st.write("2. Subtraction")
st.write("3. Multiplication")
st.write("4. Division")

choice = st.number_input("Enter Your Choice", min_value=1, max_value=4, step=1)

if st.button("Calculate",key="btn19"):
    if choice == 1:
        st.write(num1 + num2)
    elif choice == 2:
        st.write(num1 - num2)
    elif choice == 3:
        st.write(num1 * num2)
    elif choice == 4:
        st.write(num1 / num2)
    else:
        st.write("Invalid Syntax")
#---------------------21----------------
st.markdown("<div class='section'>Logical Operator</div>", unsafe_allow_html=True)
st.markdown("<div class='section'>Question 21.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a number is divisible by both 5 and 11.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Divisible by Both 5 and 11")

num = st.number_input("Enter a number")

if st.button("CHECK"):
    if num % 5 == 0 and num % 11 == 0:
        st.success(f"{num} is Divisible by Both 5 and 11")
    else:
        st.success(f"{num} is Not Divisible by Both 5 and 11")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.number_input("Enter a number", key="q20")

if st.button("CHECK", key="btn20"):
    if num % 5 == 0 and num % 11 == 0:
        st.success(f"{num} is Divisible by Both 5 and 11")
    else:
        st.success(f"{num} is Not Divisible by Both 5 and 11")
#---------------------22----------------
st.markdown("<div class='section'>Question 22.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to check whether a person is eligible for voting based on age.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Voting Eligibility Checker")

age = st.number_input("Enter your age", min_value=0, step=1)

if st.button("CHECK ELIGIBILITY"):
    if age >= 18:
        st.success("You are Eligible for Voting")
    else:
        st.success("You are Not Eligible for Voting")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

age = st.number_input("Enter your age", min_value=0, step=1)

if st.button("CHECK ELIGIBILITY"):
    if age >= 18:
        st.success("You are Eligible for Voting")
    else:
        st.success("You are Not Eligible for Voting")        

        
