import streamlit  as st
from io import StringIO
import sys
st.set_page_config(page_title="Pattern program", layout="centered")
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
st.markdown("<div class='title'>Pattern program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Number Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Number Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1, 5):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn1"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1, 5):
        for j in range(1, i + 1):
            print(j, end="")
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Right Triangle Number Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Right Triangle Number Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            print(k, end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn2"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            print(k, end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Star Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Star Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            print("*", end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn3"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            print("*", end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Star Pattern with Spaces.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Star Pattern With Spaces")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            print("* ", end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn4"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            print("* ", end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Star and Dollar Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Star and Dollar Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            if k == s or k == 1:
                print("* ", end="")
            else:
                print("$ ", end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn5"):
    buffer = StringIO()
    sys.stdout = buffer

    s = 1

    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(" ", end="")
        for k in range(1, s + 1):
            if k == s or k == 1:
                print("* ", end="")
            else:
                print("$ ", end="")
        s = s + 1
        print()

    sys.stdout = sys.__stdout__

    st.code(buffer.getvalue())


#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Square Star Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Square Star Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(4):
        for j in range(4):
            print("*", end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn6"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(4):
        for j in range(4):
            print("*", end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Right Triangle Star Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Right Triangle Star Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        for j in range(i):
            print("*", end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn7"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        for j in range(i):
            print("*", end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Inverted Right Triangle Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Inverted Right Triangle")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(4,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn8"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(4,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Pyramid Star Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Pyramid Star Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        for j in range(4-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn9"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        for j in range(4-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Inverted Pyramid Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Inverted Pyramid")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(4,0,-1):
        for j in range(4-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""",language="python")    
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn10"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(4,0,-1):
        for j in range(4-i):
            print(" ", end="")
        for k in range(2*i-1):
            print("*", end="")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
#---------------------11----------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Continuous Number Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Continuous Number Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    num=1

    for i in range(1,5):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn11"):
    buffer = StringIO()
    sys.stdout = buffer

    num=1

    for i in range(1,5):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------12----------------
st.markdown("<div class='section'>Question 12.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Repeated Number Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Repeated Number Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        for j in range(i):
            print(i,end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn12"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        for j in range(i):
            print(i,end=" ")
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------13----------------
st.markdown("<div class='section'>Question 13.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print Floyd's Triangle.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Floyd's Triangle")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    num=1

    for i in range(1,5):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn13"):
    buffer = StringIO()
    sys.stdout = buffer

    num=1

    for i in range(1,5):
        for j in range(i):
            print(num,end=" ")
            num+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------14----------------
st.markdown("<div class='section'>Question 14.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print Pascal's Triangle.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Pascal's Triangle")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    rows=5

    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        num=1
        for k in range(i+1):
            print(num,end=" ")
            num=num*(i-k)//(k+1)
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn14"):
    buffer = StringIO()
    sys.stdout = buffer

    rows=5

    for i in range(rows):
        for j in range(rows-i-1):
            print(" ",end="")
        num=1
        for k in range(i+1):
            print(num,end=" ")
            num=num*(i-k)//(k+1)
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------15----------------
st.markdown("<div class='section'>Question 15.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Alphabet Triangle.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Alphabet Triangle")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        ch=65
        for j in range(i):
            print(chr(ch),end=" ")
            ch+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn15"):
    buffer = StringIO()
    sys.stdout = buffer

    for i in range(1,5):
        ch=65
        for j in range(i):
            print(chr(ch),end=" ")
            ch+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())

#---------------------16----------------
st.markdown("<div class='section'>Question 16.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Repeated Alphabet Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Repeated Alphabet Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    ch=65

    for i in range(1,5):
        for j in range(i):
            print(chr(ch),end=" ")
        ch+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn16"):
    buffer = StringIO()
    sys.stdout = buffer

    ch=65

    for i in range(1,5):
        for j in range(i):
            print(chr(ch),end=" ")
        ch+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())


#---------------------17----------------
st.markdown("<div class='section'>Question 17.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Write a program to print the Continuous Alphabet Pattern.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
from io import StringIO
import sys

st.title("Continuous Alphabet Pattern")

if st.button("Run Code"):
    buffer = StringIO()
    sys.stdout = buffer

    ch=65

    for i in range(1,5):
        for j in range(i):
            print(chr(ch),end=" ")
            ch+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

if st.button("Run Code", key="btn17"):
    buffer = StringIO()
    sys.stdout = buffer

    ch=65

    for i in range(1,5):
        for j in range(i):
            print(chr(ch),end=" ")
            ch+=1
        print()

    sys.stdout = sys.__stdout__
    st.code(buffer.getvalue())    


