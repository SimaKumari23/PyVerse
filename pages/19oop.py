import streamlit  as st
st.set_page_config(page_title="OOPs program", layout="centered")
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
st.markdown("<div class='title'>OOPs program</div>", unsafe_allow_html=True)
#---------------------1----------------
st.markdown("<div class='section'>Question 1.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Create Class and Object.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Class and Object")

class Student:
    def display(self):
        return "Hello Student"

if st.button("CREATE OBJECT", key="btn1"):
    obj = Student()
    st.success(obj.display())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Student:
    def display(self):
        return "Hello Student"

if st.button("CREATE OBJECT", key="work1"):
    obj = Student()
    st.success(obj.display())


#---------------------2----------------
st.markdown("<div class='section'>Question 2.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Constructor Program (__init__).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Constructor Program")

class Student:
    def __init__(self,name):
        self.name = name

    def show(self):
        return self.name

name = st.text_input("Enter Name")

if st.button("DISPLAY", key="btn2"):
    obj = Student(name)
    st.success(obj.show())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Student:
    def __init__(self,name):
        self.name = name

    def show(self):
        return self.name

name = st.text_input("Enter Name", key="name2")

if st.button("DISPLAY", key="work2"):
    obj = Student(name)
    st.success(obj.show())


#---------------------3----------------
st.markdown("<div class='section'>Question 3.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Instance Variable and Method Program.<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Instance Variable and Method")

class Student:
    def __init__(self,age):
        self.age = age

    def show(self):
        return self.age

age = st.number_input("Enter Age")

if st.button("SHOW", key="btn3"):
    obj = Student(age)
    st.success(obj.show())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Student:
    def __init__(self,age):
        self.age = age

    def show(self):
        return self.age

age = st.number_input("Enter Age", key="age3")

if st.button("SHOW", key="work3"):
    obj = Student(age)
    st.success(obj.show())


#---------------------4----------------
st.markdown("<div class='section'>Question 4.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Student Class Program (Name, Roll No, Marks).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Student Class")

class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        return self.name,self.roll,self.marks

name = st.text_input("Name")
roll = st.number_input("Roll No")
marks = st.number_input("Marks")

if st.button("DISPLAY", key="btn4"):
    obj = Student(name,roll,marks)
    st.success(obj.display())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        return self.name,self.roll,self.marks

name = st.text_input("Name", key="name4")
roll = st.number_input("Roll No", key="roll4")
marks = st.number_input("Marks", key="marks4")

if st.button("DISPLAY", key="work4"):
    obj = Student(name,roll,marks)
    st.success(obj.display())

#---------------------7----------------
st.markdown("<div class='section'>Question 5.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Single Inheritance (One Parent → One Child).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Single Inheritance")

class Animal:
    def sound(self):
        return "Animal makes sound"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

if st.button("RUN", key="btn7"):
    obj = Dog()

    st.success(obj.sound())
    st.success(obj.bark())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Animal:
    def sound(self):
        return "Animal makes sound"

class Dog(Animal):
    def bark(self):
        return "Dog barks"

if st.button("RUN", key="work7"):
    obj = Dog()

    st.success(obj.sound())
    st.success(obj.bark())


#---------------------8----------------
st.markdown("<div class='section'>Question 6.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Multilevel Inheritance (Grandparent → Parent → Child).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Multilevel Inheritance")

class Grandparent:
    def show1(self):
        return "Grandparent Class"

class Parent(Grandparent):
    def show2(self):
        return "Parent Class"

class Child(Parent):
    def show3(self):
        return "Child Class"

if st.button("RUN", key="btn8"):
    obj = Child()

    st.success(obj.show1())
    st.success(obj.show2())
    st.success(obj.show3())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Grandparent:
    def show1(self):
        return "Grandparent Class"

class Parent(Grandparent):
    def show2(self):
        return "Parent Class"

class Child(Parent):
    def show3(self):
        return "Child Class"

if st.button("RUN", key="work8"):
    obj = Child()

    st.success(obj.show1())
    st.success(obj.show2())
    st.success(obj.show3())


#---------------------9----------------
st.markdown("<div class='section'>Question 7.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Method Overriding (Same Method Redefined in Child Class).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Method Overriding")

class Parent:
    def show(self):
        return "Parent Method"

class Child(Parent):
    def show(self):
        return "Child Method"

if st.button("RUN", key="btn9"):
    obj = Child()

    st.success(obj.show())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Parent:
    def show(self):
        return "Parent Method"

class Child(Parent):
    def show(self):
        return "Child Method"

if st.button("RUN", key="work9"):
    obj = Child()

    st.success(obj.show())


#---------------------10----------------
st.markdown("<div class='section'>Question 8.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Encapsulation Program (Private Variable __variable).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Encapsulation")

class Student:

    def __init__(self):
        self.__marks = 90

    def show(self):
        return self.__marks

if st.button("SHOW", key="btn10"):
    obj = Student()

    st.success(obj.show())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Student:

    def __init__(self):
        self.__marks = 90

    def show(self):
        return self.__marks

if st.button("SHOW", key="work10"):
    obj = Student()

    st.success(obj.show())


#---------------------11----------------
st.markdown("<div class='section'>Question 9.</div>", unsafe_allow_html=True)
st.markdown("<div class='content'> Polymorphism Program (Same Method, Different Behavior).<br>💻 Code</div>", unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""import streamlit as st

st.title("Polymorphism")

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

if st.button("RUN", key="btn11"):

    c = Cat()
    d = Dog()

    st.success(c.sound())
    st.success(d.sound())
""", language="python")

st.markdown("<div class='content'>🚀 working</div>", unsafe_allow_html=True)

class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

if st.button("RUN", key="work11"):

    c = Cat()
    d = Dog()

    st.success(c.sound())
    st.success(d.sound())

