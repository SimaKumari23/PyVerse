import streamlit  as st
st.set_page_config(page_title="Basics program", layout="centered")
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
st.markdown("<div class='title'>Basics program</div>", unsafe_allow_html=True)
#------------------------1--------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to Add two number on click of button and input must be entered through text box.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("Addition Of two number on click of button and input must be inside text box")
t1=(st.text_input("Enter 1st number"))
t2=(st.text_input("Enter 2nd number"))
b1=st.button("ADD")
if b1:
    c=int(t1)+int(t2)
    st.write(c)

""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
t1=(st.text_input("Enter 1st number"))
t2=(st.text_input("Enter 2nd number"))
b1=st.button("ADD", key="q1_btn")
if b1:
    c=int(t1)+int(t2)
    st.write(c)
#------------------------2--------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to display a success message using st.success()with an emogi.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.header("how to attached success emogi in streamlit. ")
t1=st.text_input("Enter 1st no")
t2=st.text_input("Enter 2nd no")
b=st.button("ADD")
if b:
    st.success(f"✅ Sum={int(t1)+int(t2)}") 
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
t1=st.text_input("Enter 1st no")
t2=st.text_input("Enter 2nd no")
b=st.button("ADD", key="q2_btn")
if b:
    st.success(f"✅Sum={int(t1)+int(t2)}")

#--------------3--------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to display your name and details. <br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("🧑‍💻 Print Details")
name = st.text_input("Enter your name")
age = st.text_input("Enter your age")
if st.button("Show"):
    st.success(f"✅ Name: {name}, Age: {age}")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
name=st.text_input("Enter your name")
age = st.text_input("Enter your age")
if st.button("Show"):
    st.success(f"✅ Name: {name}, Age: {age}")
        
#----------------4-------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to Subtract Two Numbers.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("➖ Subtract Two Numbers")
a = st.text_input("Enter first number")
b = st.text_input("Enter second number")
if st.button("Subtract"):
    st.success(f"✅ Result = {int(a)-int(b)}")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
a = st.text_input("Enter first number",key="q3_a")
b = st.text_input("Enter second number",key="q3_b")
if st.button("Subtract",key="q3_btn"):
    st.success(f"✅ Result = {int(a)-int(b)}")
#----------------5-------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to swap two no. <br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("🔄 Swap Two Numbers")
a = st.text_input("Enter first number")
b = st.text_input("Enter second number")
if st.button("Swap"):
    a, b = b, a
    st.success(f"✅ After Swap: a={a}, b={b}")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
a = st.text_input("Enter first number",key="q4_a")
b = st.text_input("Enter second number",key="q4_b")
if st.button("Swap",key="q4_btn"):
    a, b = b, a
    st.success(f"✅ After Swap: a={a}, b={b}")

#----------------6-------------
st.markdown("<div class='section'>Question6 .</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to find square of a number.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("🔢 Square of Number")
n = st.text_input("Enter number")
if st.button("Find Square"):
    st.success(f"✅ Square = {int(n)**2}")
""", language="python")
st.markdown("<div class='content'>🚀working</div>", unsafe_allow_html=True)
n = st.text_input("Enter number")
if st.button("Find Square"):
    st.success(f"✅ Square = {int(n)**2}")
#----------------7-------------
st.markdown("<div class='section'>Question7 .</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to find cube of a no.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("🔢 Cube of Number")
n = st.text_input("Enter number")
if st.button("Find Cube"):
    st.success(f"✅ Cube = {int(n)**3}")
""", language="python")
st.markdown("<div class='content'>🚀working</div>", unsafe_allow_html=True)
n = st.text_input("Enter number",key="q5_n")
if st.button("Find Cube",key="q5_btn"):
    st.success(f"✅ Cube = {int(n)**3}")
#----------------8-------------
st.markdown("<div class='section'>Question 8 .</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Wap in python streamlit to calculate simple interest.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("💰 Simple Interest")
p = st.text_input("Principal")
r = st.text_input("Rate")
t = st.text_input("Time")
if st.button("Calculate"):
    si = (float(p)*float(r)*float(t))/100
    st.success(f"✅ Simple Interest = {si}")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
p = st.text_input("Principal")
r = st.text_input("Rate")
t = st.text_input("Time")
if st.button("Calculate"):
    si = (float(p)*float(r)*float(t))/100
    st.success(f"✅ Simple Interest = {si}")

#----------------9-------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to find area of rectangle.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("📏 Area of Rectangle")
l = st.text_input("Length")
w = st.text_input("Width")
if st.button("Calculate"):
    area = float(l)*float(w)
    st.success(f"✅ Area = {area}")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
l = st.text_input("Length")
w = st.text_input("Width")
if st.button("Calculate",key="q6_btn"):
    area = float(l)*float(w)
    st.success(f"✅ Area = {area}")

#----------------10-------------
st.markdown("<div class='section'>Question 10.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to find area of a circle.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("⚪ Area of Circle")
r = st.text_input("Radius")
if st.button("Calculate"):
    area = 3.14 * float(r)**2
    st.success(f"✅ Area = {area}")
""", language="python")
st.markdown("<div class='content'>🚀working</div>", unsafe_allow_html=True)
r = st.text_input("Radius")
if st.button("Calculate",key="q7_btn"):
    area = 3.14 * float(r)**2
    st.success(f"✅ Area = {area}")
#----------------11-------------
st.markdown("<div class='section'>Question 11.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Wap in python streamlit to find perimeter of rectangle.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("📐 Perimeter of Rectangle")
l = st.text_input("Length")
w = st.text_input("Width")
if st.button("Calculate"):
    p = 2*(float(l)+float(w))
    st.success(f"✅ Perimeter = {p}")
""", language="python")
st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)
l = st.text_input("Length",key="q8_l")
w = st.text_input("Width",key="q8_b")
if st.button("Calculate",key="q8_btn"):
    p = 2*(float(l)+float(w))
    st.success(f"✅ Perimeter = {p}")

#----------------12-------------
st.markdown("<div class='section'>Question 12 .</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to calculate the average of three numbers. <br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("📊 Average")
a = st.text_input("First")
b = st.text_input("Second")
c = st.text_input("Third")
if st.button("Calculate"):
    avg = (float(a)+float(b)+float(c))/3
    st.success(f"✅ Average = {avg}")
""", language="python")
st.markdown("<div class='content'>🚀working</div>", unsafe_allow_html=True)
a = st.text_input("First",key="q9_a")
b = st.text_input("Second",key="q9_b")
c = st.text_input("Third",key="q9_c")
if st.button("Calculate",key="q9_btn"):
    avg = (float(a)+float(b)+float(c))/3
    st.success(f"✅ Average = {avg}")
#----------------13-------------
st.markdown("<div class='section'>Question 13.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>Wap in python streamlit to convert Celsius to Faharenheit.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("🌡️ Celsius to Fahrenheit")
c = st.text_input("Enter Celsius")
if st.button("Convert"):
    f = (float(c)*9/5)+32
    st.success(f"✅ Fahrenheit = {f}")
""", language="python")
st.markdown("<div class='content'>🚀working</div>", unsafe_allow_html=True)
c = st.text_input("Enter Celsius",key="q10_c")
if st.button("Convert",key="q10_btn"):
    f = (float(c)*9/5)+32
    st.success(f"✅ Fahrenheit = {f}")

#----------------14-------------
st.markdown("<div class='section'>Question 14.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> WAP in python streamlit to convert Fahrenheit to Celcius<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st
st.title("🌡️ Fahrenheit to Celsius")
f = st.text_input("Enter Fahrenheit")
if st.button("Convert"):
    c = (float(f)-32)*5/9
    st.success(f"✅ Celsius = {c}")
""", language="python")
st.markdown("<div class='content'>🚀working</div>", unsafe_allow_html=True)
f = st.text_input("Enter Fahrenheit")
if st.button("Convert",key="q11_btn"):
    c = (float(f)-32)*5/9
    st.success(f"✅ Celsius = {c}")

















