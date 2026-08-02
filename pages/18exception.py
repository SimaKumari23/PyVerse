import streamlit  as st
st.set_page_config(page_title="Exception handling program", layout="centered")
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
st.markdown("<div class='title'>Exception handling program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Handle ZeroDivisionError (Division by Zero Exception).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("ZeroDivisionError Handling")

a = st.number_input("Enter First Number")
b = st.number_input("Enter Second Number")

if st.button("DIVIDE", key="btn1"):
    try:
        result = a / b
        st.success(result)

    except ZeroDivisionError:
        st.error("Cannot divide by zero")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

a = st.number_input("Enter First Number", key="a1")
b = st.number_input("Enter Second Number", key="b1")

if st.button("DIVIDE", key="work1"):
    try:
        result = a / b
        st.success(result)

    except ZeroDivisionError:
        st.error("Cannot divide by zero")


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Handle ValueError (Wrong Input Type).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("ValueError Handling")

value = st.text_input("Enter Number")

if st.button("CHECK", key="btn2"):
    try:
        num = int(value)
        st.success(num)

    except ValueError:
        st.error("Invalid Input")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

value = st.text_input("Enter Number", key="value2")

if st.button("CHECK", key="work2"):
    try:
        num = int(value)
        st.success(num)

    except ValueError:
        st.error("Invalid Input")


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Handle TypeError (Different Data Types Operation Error).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("TypeError Handling")

a = st.text_input("Enter First Value")
b = st.text_input("Enter Second Value")

if st.button("ADD", key="btn3"):
    try:
        result = a + b
        st.success(result)

    except TypeError:
        st.error("Different Data Types Error")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

a = st.text_input("Enter First Value", key="a3")
b = st.text_input("Enter Second Value", key="b3")

if st.button("ADD", key="work3"):
    try:
        result = int(a) + b
        st.success(result)

    except TypeError:
        st.error("Different Data Types Error")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Handle IndexError (List Index Out of Range).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("IndexError Handling")

if st.button("RUN", key="btn4"):

    try:
        my_list = [10,20,30]
        st.success(my_list[5])

    except IndexError:
        st.error("List Index Out of Range")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("RUN", key="work4"):

    try:
        my_list = [10,20,30]
        st.success(my_list[5])

    except IndexError:
        st.error("List Index Out of Range")


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Handle KeyError (Missing Dictionary Key).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("KeyError Handling")

if st.button("CHECK", key="btn5"):

    try:
        student = {
            "name":"Sima",
            "age":20
        }

        st.success(student["marks"])

    except KeyError:
        st.error("Key Not Found")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("CHECK", key="work5"):

    try:
        student = {
            "name":"Sima",
            "age":20
        }

        st.success(student["marks"])

    except KeyError:
        st.error("Key Not Found")
#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Multiple Exception Handling.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Multiple Exception Handling")

a = st.text_input("Enter First Number")
b = st.text_input("Enter Second Number")

if st.button("DIVIDE", key="btn6"):

    try:
        x = int(a)
        y = int(b)

        result = x/y

        st.success(result)

    except ValueError:
        st.error("Enter Valid Number")

    except ZeroDivisionError:
        st.error("Cannot Divide by Zero")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

a = st.text_input("Enter First Number", key="a6")
b = st.text_input("Enter Second Number", key="b6")

if st.button("DIVIDE", key="work6"):

    try:
        x = int(a)
        y = int(b)

        result = x/y

        st.success(result)

    except ValueError:
        st.error("Enter Valid Number")

    except ZeroDivisionError:
        st.error("Cannot Divide by Zero")


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Using try-except-else Block.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Try Except Else")

num = st.text_input("Enter Number")

if st.button("CHECK", key="btn7"):

    try:
        n = int(num)

    except ValueError:
        st.error("Invalid Input")

    else:
        st.success(f"Number = {n}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

num = st.text_input("Enter Number", key="num7")

if st.button("CHECK", key="work7"):

    try:
        n = int(num)

    except ValueError:
        st.error("Invalid Input")

    else:
        st.success(f"Number = {n}")


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Using try-except-finally Block.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Try Except Finally")

if st.button("RUN", key="btn8"):

    try:
        x = 10/0
        st.success(x)

    except ZeroDivisionError:
        st.error("Division by Zero Error")

    finally:
        st.info("Finally Block Executed")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("RUN", key="work8"):

    try:
        x = 10/0
        st.success(x)

    except ZeroDivisionError:
        st.error("Division by Zero Error")

    finally:
        st.info("Finally Block Executed")


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Create User Defined Exception using raise Keyword.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("User Defined Exception")

age = st.number_input("Enter Age")

if st.button("CHECK", key="btn9"):

    try:
        if age < 18:
            raise Exception("Not Eligible")

        else:
            st.success("Eligible")

    except Exception as e:
        st.error(e)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

age = st.number_input("Enter Age", key="age9")

if st.button("CHECK", key="work9"):

    try:
        if age < 18:
            raise Exception("Not Eligible")

        else:
            st.success("Eligible")

    except Exception as e:
        st.error(e)


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> File Handling with Exception Handling.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("File Handling Exception")

if st.button("READ FILE", key="btn10"):

    try:
        file = open("sample.txt","r")

        data = file.read()

        file.close()

        st.success(data)

    except FileNotFoundError:
        st.error("File Not Found")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("READ FILE", key="work10"):

    try:
        file = open("sample.txt","r")

        data = file.read()

        file.close()

        st.success(data)

    except FileNotFoundError:
        st.error("File Not Found")

        
