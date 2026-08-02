import streamlit  as st
st.set_page_config(page_title="String program", layout="centered")
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
st.markdown("<div class='title'>String program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Reverse a String.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Reverse a String")

text = st.text_input("Enter String")

if st.button("REVERSE", key="btn1"):
    reverse = text[::-1]

    st.success(reverse)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text1")

if st.button("REVERSE", key="work1"):
    reverse = text[::-1]

    st.success(reverse)


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Check Palindrome String.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Palindrome String")

text = st.text_input("Enter String")

if st.button("CHECK", key="btn2"):
    if text == text[::-1]:
        st.success("Palindrome String")
    else:
        st.success("Not a Palindrome String")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text2")

if st.button("CHECK", key="work2"):
    if text == text[::-1]:
        st.success("Palindrome String")
    else:
        st.success("Not a Palindrome String")


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Length of String.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Length of String")

text = st.text_input("Enter String")

if st.button("FIND LENGTH", key="btn3"):
    st.success(f"Length = {len(text)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text3")

if st.button("FIND LENGTH", key="work3"):
    st.success(f"Length = {len(text)}")


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Count Vowels and Consonants.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Vowels and Consonants Count")

text = st.text_input("Enter String")

if st.button("COUNT", key="btn4"):
    vowels = 0
    consonants = 0

    for i in text:
        if i.lower() in "aeiou":
            vowels += 1
        elif i.isalpha():
            consonants += 1

    st.success(f"Vowels = {vowels}")
    st.success(f"Consonants = {consonants}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text4")

if st.button("COUNT", key="work4"):
    vowels = 0
    consonants = 0

    for i in text:
        if i.lower() in "aeiou":
            vowels += 1
        elif i.isalpha():
            consonants += 1

    st.success(f"Vowels = {vowels}")
    st.success(f"Consonants = {consonants}")


#---------------------5----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Count Words in String.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Count Words")

text = st.text_input("Enter Sentence")

if st.button("COUNT", key="btn5"):
    words = text.split()

    st.success(f"Total Words = {len(words)}")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter Sentence", key="text5")

if st.button("COUNT", key="work5"):
    words = text.split()

    st.success(f"Total Words = {len(words)}")


#---------------------6----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Character Frequency Count.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Character Frequency")

text = st.text_input("Enter String")

if st.button("COUNT", key="btn6"):
    freq = {}

    for i in text:
        freq[i] = freq.get(i,0) + 1

    st.success(freq)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text6")

if st.button("COUNT", key="work6"):
    freq = {}

    for i in text:
        freq[i] = freq.get(i,0) + 1

    st.success(freq)

#---------------------7----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find Duplicate Characters.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Duplicate Characters")

text = st.text_input("Enter String")

if st.button("FIND", key="btn7"):
    duplicate = []

    for i in text:
        if text.count(i) > 1 and i not in duplicate:
            duplicate.append(i)

    st.success(duplicate)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text7")

if st.button("FIND", key="work7"):
    duplicate = []

    for i in text:
        if text.count(i) > 1 and i not in duplicate:
            duplicate.append(i)

    st.success(duplicate)


#---------------------8----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Remove Duplicate Characters.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Remove Duplicate Characters")

text = st.text_input("Enter String")

if st.button("REMOVE", key="btn8"):
    result = ""

    for i in text:
        if i not in result:
            result += i

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text8")

if st.button("REMOVE", key="work8"):
    result = ""

    for i in text:
        if i not in result:
            result += i

    st.success(result)


#---------------------9----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Compare Two Strings.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Compare Two Strings")

str1 = st.text_input("Enter First String")
str2 = st.text_input("Enter Second String")

if st.button("COMPARE", key="btn9"):
    if str1 == str2:
        st.success("Both Strings are Same")
    else:
        st.success("Strings are Different")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

str1 = st.text_input("Enter First String", key="str1")
str2 = st.text_input("Enter Second String", key="str2")

if st.button("COMPARE", key="work9"):
    if str1 == str2:
        st.success("Both Strings are Same")
    else:
        st.success("Strings are Different")


#---------------------10----------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Concatenate Two Strings.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Concatenate Two Strings")

str1 = st.text_input("Enter First String")
str2 = st.text_input("Enter Second String")

if st.button("CONCATENATE", key="btn10"):
    result = str1 + str2

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

str1 = st.text_input("Enter First String", key="str3")
str2 = st.text_input("Enter Second String", key="str4")

if st.button("CONCATENATE", key="work10"):
    result = str1 + str2

    st.success(result)


#---------------------11----------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Check Anagram of Two Strings.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Anagram Checker")

str1 = st.text_input("Enter First String")
str2 = st.text_input("Enter Second String")

if st.button("CHECK", key="btn11"):
    if sorted(str1) == sorted(str2):
        st.success("Anagram String")
    else:
        st.success("Not Anagram")
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

str1 = st.text_input("Enter First String", key="str5")
str2 = st.text_input("Enter Second String", key="str6")

if st.button("CHECK", key="work11"):
    if sorted(str1) == sorted(str2):
        st.success("Anagram String")
    else:
        st.success("Not Anagram")


#---------------------12----------------
st.markdown("<div class='section'>Question 12.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Find First Non-Repeating Character.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("First Non-Repeating Character")

text = st.text_input("Enter String")

if st.button("FIND", key="btn12"):
    result = "No Character"

    for i in text:
        if text.count(i) == 1:
            result = i
            break

    st.success(result)
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

text = st.text_input("Enter String", key="text12")

if st.button("FIND", key="work12"):
    result = "No Character"

    for i in text:
        if text.count(i) == 1:
            result = i
            break

    st.success(result)

    
