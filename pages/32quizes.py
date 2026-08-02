import streamlit as st

st.set_page_config(layout="wide")
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
    if st.button("⬅ Go to Previous", use_container_width=True):

        if st.session_state.get("from_page") == "5python":
            st.switch_page("pages/5python.py")

        elif st.session_state.get("from_page") == "20dsa":
            st.switch_page("pages/20dsa.py")

        else:
            st.switch_page("main.py")
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
           background-attachment: fixed;
}
div[role="radiogroup"] > label {
    display: inline-flex;
    align-items: center;
    margin-right: 40px;
    cursor: pointer;
    font-size: 18px;
    color: gray;
}
div[role="radiogroup"] input {
    display: none;
}
div[role="radiogroup"] input:checked + div {
    color: red;
    border-bottom: 3px solid red;
}
div[role="radiogroup"] {
    border-bottom: 2px solid #ccc;
    padding-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* SELECTBOX MAIN BOX */
div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.08) !important;
    color: #E2E8F0 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 14px !important;
    backdrop-filter: blur(10px) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
}

/* HOVER EFFECT */
div[data-baseweb="select"] > div:hover {
    border: 1px solid #A855F7 !important;
}

/* DROPDOWN LIST */
ul[role="listbox"] {
    background: #11122A !important;
    border-radius: 10px !important;
}

/* OPTIONS */
li[role="option"] {
    color: white !important;
}

/* HOVER OPTION */
li[role="option"]:hover {
    background: rgba(168,85,247,0.2) !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* STREAMLIT BUTTON FIX */
div.stButton > button {
    background: rgba(255,255,255,0.08) !important;
    color: #E2E8F0 !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 14px !important;
    padding: 12px 20px !important;
    font-weight: 600 !important;
    backdrop-filter: blur(10px) !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    transition: all 0.3s ease !important;
}

/* HOVER EFFECT */
div.stButton > button:hover {
    background: rgba(168,85,247,0.18) !important;
    border: 1px solid #A855F7 !important;
    color: white !important;
    transform: translateY(-2px) scale(1.02) !important;
}

/* CLICK EFFECT */
div.stButton > button:active {
    transform: scale(0.96) !important;
}

</style>
""", unsafe_allow_html=True)
# ---------- NAVBAR ----------
tab = st.radio("", ["Python Quiz", "DSA Quiz"], horizontal=True)

# ---------- SESSION STATE ----------
if "topic" not in st.session_state:
    st.session_state.topic = None

# ---------- CONTENT ----------
if tab == "Python Quiz":
    st.markdown("""
    <h1 style="
        font-size: 40px;
        font-weight: bold;
        background: #90E0EF;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    ">
     Python Quiz
    </h1>
    """, unsafe_allow_html=True)

    topic = st.selectbox(
        "Choose Topic",
        ["Select Topic", "Basic Python","Branching", "Looping","String","List","Tuple","Dictionary","Set","Function","File Handling","Exception Handling","OOP"]
    )

    # ================= BASIC =================
    if topic == "Basic Python":
        st.markdown("### 🟡 Basic Python Quiz")
        score = 0

        q1 = st.radio("Q1: Python is a ____ language?", ["High-level", "Low-level", "Machine", "Assembly"])
        q2 = st.radio("Q2: Python is ____ typed language?", ["Dynamically", "Statically"])
        q3 = st.radio("Q3: Which symbol is used for comments?", ["#", "//", "/*", "--"])
        q4 = st.radio("Q4: print() is used for?", ["Output", "Input", "Loop", "Condition"])
        q5 = st.radio("Q5: Python file extension?", [".py", ".java", ".c", ".html"])

        if st.button("Submit"):
            if q1 == "High-level": score += 1
            if q2 == "Dynamically": score += 1
            if q3 == "#": score += 1
            if q4 == "Output": score += 1
            if q5 == ".py": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= BRANCHING =================
    elif topic == "Branching":
        st.markdown("### 🔴 Branching Quiz")
        score = 0

        q1 = st.radio("Q1: Which keyword is used for decision making?", ["if", "for", "while", "loop"])
        q2 = st.radio("Q2: When is 'else' executed?", ["When condition is true", "When condition is false"])
        q3 = st.radio("Q3: What does 'elif' mean?", ["else if", "end if", "loop", "none"])
        q4 = st.radio("Q4: If condition is false, what runs?", ["if", "else", "for", "none"])
        q5 = st.radio("Q5: What is nested if?", ["if inside if", "loop", "function", "class"])

        if st.button("Submit"):
            if q1 == "if": score += 1
            if q2 == "When condition is false": score += 1
            if q3 == "else if": score += 1
            if q4 == "else": score += 1
            if q5 == "if inside if": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= LOOPING =================
    elif topic == "Looping":
        st.markdown("### 🔵 Looping Quiz")
        score = 0

        q1 = st.radio("Q1: Which is a loop?", ["for", "if", "def", "class"])
        q2 = st.radio("Q2: While loop runs when?", ["Condition is true", "Only once"])
        q3 = st.radio("Q3: Infinite loop means?", ["Never ends", "Runs once", "Error", "None"])
        q4 = st.radio("Q4: range() is used in?", ["for", "if", "while", "none"])
        q5 = st.radio("Q5: break is used to?", ["Stop loop", "Continue", "Start", "None"])

        if st.button("Submit"):
            if q1 == "for": score += 1
            if q2 == "Condition is true": score += 1
            if q3 == "Never ends": score += 1
            if q4 == "for": score += 1
            if q5 == "Stop loop": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= STRING =================
    elif topic == "String":
        st.markdown("### 🟢 String Quiz")
        score = 0

        q1 = st.radio("Q1: String is?", ["Text", "Number", "Boolean", "None"])
        q2 = st.radio("Q2: len() returns?", ["Length", "Sum", "Delete", "None"])
        q3 = st.radio("Q3: upper() does?", ["Uppercase", "Lowercase", "Delete", "None"])
        q4 = st.radio("Q4: Index starts from?", ["0", "1", "-1", "None"])
        q5 = st.radio("Q5: split() is used to?", ["Break string", "Join", "Delete", "None"])

        if st.button("Submit"):
            if q1 == "Text": score += 1
            if q2 == "Length": score += 1
            if q3 == "Uppercase": score += 1
            if q4 == "0": score += 1
            if q5 == "Break string": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= LIST =================
    elif topic == "List":
        st.markdown("### 🟣 List Quiz")
        score = 0

        q1 = st.radio("Q1: List uses?", ["[]", "()", "{}", "<>"])
        q2 = st.radio("Q2: List is mutable?", ["Yes", "No"])
        q3 = st.radio("Q3: append() does?", ["Add element", "Delete", "Sort", "None"])
        q4 = st.radio("Q4: Index starts from?", ["0", "1"])
        q5 = st.radio("Q5: pop() does?", ["Remove element", "Add", "Sort", "None"])

        if st.button("Submit"):
            if q1 == "[]": score += 1
            if q2 == "Yes": score += 1
            if q3 == "Add element": score += 1
            if q4 == "0": score += 1
            if q5 == "Remove element": score += 1
            st.success(f"✅ Your Score: {score}/5")


# ================= TUPLE =================
    elif topic == "Tuple":
        st.markdown("### 🟠 Tuple Quiz")
        score = 0

        q1 = st.radio("Q1: Tuple uses?", ["()", "[]", "{}", "<>"])
        q2 = st.radio("Q2: Tuple is mutable?", ["Yes", "No"])
        q3 = st.radio("Q3: Tuple allows duplicates?", ["Yes", "No"])
        q4 = st.radio("Q4: Index starts from?", ["0", "1"])
        q5 = st.radio("Q5: Tuple is faster than list?", ["Yes", "No"])

        if st.button("Submit"):
            if q1 == "()": score += 1
            if q2 == "No": score += 1
            if q3 == "Yes": score += 1
            if q4 == "0": score += 1
            if q5 == "Yes": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= DICTIONARY =================
    elif topic == "Dictionary":
        st.markdown("### 🔵 Dictionary Quiz")
        score = 0

        q1 = st.radio("Q1: Dictionary uses?", ["{}", "[]", "()", "<>"])
        q2 = st.radio("Q2: Data stored as?", ["Key-Value", "Only values", "Only keys"])
        q3 = st.radio("Q3: Keys must be?", ["Unique", "Duplicate"])
        q4 = st.radio("Q4: dict.keys() returns?", ["Keys", "Values", "Pairs"])
        q5 = st.radio("Q5: dict.values() returns?", ["Values", "Keys", "Pairs"])

        if st.button("Submit"):
            if q1 == "{}": score += 1
            if q2 == "Key-Value": score += 1
            if q3 == "Unique": score += 1
            if q4 == "Keys": score += 1
            if q5 == "Values": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= SET =================
    elif topic == "Set":
        st.markdown("### 🟢 Set Quiz")
        score = 0

        q1 = st.radio("Q1: Set uses?", ["{}", "[]", "()", "<>"])
        q2 = st.radio("Q2: Set allows duplicates?", ["Yes", "No"])
        q3 = st.radio("Q3: Set is unordered?", ["Yes", "No"])
        q4 = st.radio("Q4: add() does?", ["Add element", "Remove", "Sort"])
        q5 = st.radio("Q5: remove() does?", ["Remove element", "Add", "Sort"])

        if st.button("Submit"):
            if q1 == "{}": score += 1
            if q2 == "No": score += 1
            if q3 == "Yes": score += 1
            if q4 == "Add element": score += 1
            if q5 == "Remove element": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= FUNCTION =================
    elif topic == "Function":
        st.markdown("### 🟣 Function Quiz")
        score = 0

        q1 = st.radio("Q1: Function defined using?", ["def", "fun", "function", "define"])
        q2 = st.radio("Q2: Function is used for?", ["Reuse code", "Loop", "Condition"])
        q3 = st.radio("Q3: return keyword does?", ["Returns value", "Print", "Stop"])
        q4 = st.radio("Q4: Function call means?", ["Execute function", "Define function"])
        q5 = st.radio("Q5: Parameter means?", ["Input", "Output", "Loop"])

        if st.button("Submit"):
            if q1 == "def": score += 1
            if q2 == "Reuse code": score += 1
            if q3 == "Returns value": score += 1
            if q4 == "Execute function": score += 1
            if q5 == "Input": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= FILE HANDLING =================
    elif topic == "File Handling":
        st.markdown("### 🟤 File Handling Quiz")
        score = 0

        q1 = st.radio("Q1: File open function?", ["open()", "file()", "read()"])
        q2 = st.radio("Q2: 'r' mode means?", ["Read", "Write", "Append"])
        q3 = st.radio("Q3: 'w' mode means?", ["Write", "Read", "Append"])
        q4 = st.radio("Q4: read() does?", ["Reads file", "Writes file"])
        q5 = st.radio("Q5: close() does?", ["Closes file", "Opens file"])

        if st.button("Submit"):
            if q1 == "open()": score += 1
            if q2 == "Read": score += 1
            if q3 == "Write": score += 1
            if q4 == "Reads file": score += 1
            if q5 == "Closes file": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= EXCEPTION =================
    elif topic == "Exception Handling":
        st.markdown("### 🔴 Exception Handling Quiz")
        score = 0

        q1 = st.radio("Q1: Exception handled using?", ["try-except", "if-else", "loop"])
        q2 = st.radio("Q2: finally block runs?", ["Always", "Sometimes"])
        q3 = st.radio("Q3: except block handles?", ["Error", "Loop", "Condition"])
        q4 = st.radio("Q4: try block contains?", ["Risky code", "Safe code"])
        q5 = st.radio("Q5: raise keyword?", ["Raise error", "Ignore error"])

        if st.button("Submit"):
            if q1 == "try-except": score += 1
            if q2 == "Always": score += 1
            if q3 == "Error": score += 1
            if q4 == "Risky code": score += 1
            if q5 == "Raise error": score += 1
            st.success(f"✅ Your Score: {score}/5")

    # ================= OOP =================
    elif topic == "OOP":
        st.markdown("### ⚫ OOP Quiz")
        score = 0

        q1 = st.radio("Q1: OOP stands for?", ["Object Oriented Programming", "Only Programming"])
        q2 = st.radio("Q2: Class is?", ["Blueprint", "Object"])
        q3 = st.radio("Q3: Object is?", ["Instance of class", "Function"])
        q4 = st.radio("Q4: Inheritance means?", ["Reuse code", "Loop"])
        q5 = st.radio("Q5: Encapsulation means?", ["Data hiding", "Loop"])

        if st.button("Submit"):
            if q1 == "Object Oriented Programming": score += 1
            if q2 == "Blueprint": score += 1
            if q3 == "Instance of class": score += 1
            if q4 == "Reuse code": score += 1
            if q5 == "Data hiding": score += 1
            st.success(f"✅ Your Score: {score}/5")

if tab == "DSA Quiz":
    st.markdown("""
    <h1 style="
        font-size: 40px;
        font-weight: bold;
        background: #90E0EF;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    ">
     DSA Quiz
    </h1>
    """, unsafe_allow_html=True)

    topic = st.selectbox(
        "Choose Topic",
        ["Select Topic","Arrays","Linked List","Stack","Queue","Recursion","Tree","Graph","Searching","Sorting","Greedy Algorithm","Dynamic Programming"]
    )

    # ================= ARRAYS =================
    if topic == "Arrays":
        st.markdown("### 🟢 Arrays Quiz")
        score = 0

        q1 = st.radio("Q1: Array stores?", ["Same type elements", "Different types"])
        q2 = st.radio("Q2: Index starts from?", ["0", "1"])
        q3 = st.radio("Q3: Memory type?", ["Contiguous", "Random"])
        q4 = st.radio("Q4: Access time?", ["O(1)", "O(n)"])
        q5 = st.radio("Q5: Size is?", ["Fixed", "Dynamic"])

        if st.button("Submit"):
            if q1 == "Same type elements": score+=1
            if q2 == "0": score+=1
            if q3 == "Contiguous": score+=1
            if q4 == "O(1)": score+=1
            if q5 == "Fixed": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= LINKED LIST =================
    elif topic == "Linked List":
        st.markdown("### 🔵 Linked List Quiz")
        score = 0

        q1 = st.radio("Q1: Linked list uses?", ["Nodes", "Indexes"])
        q2 = st.radio("Q2: Memory?", ["Non-contiguous", "Contiguous"])
        q3 = st.radio("Q3: Node contains?", ["Data + Pointer", "Only data"])
        q4 = st.radio("Q4: Access time?", ["O(n)", "O(1)"])
        q5 = st.radio("Q5: Insertion?", ["Easy", "Hard"])

        if st.button("Submit"):
            if q1 == "Nodes": score+=1
            if q2 == "Non-contiguous": score+=1
            if q3 == "Data + Pointer": score+=1
            if q4 == "O(n)": score+=1
            if q5 == "Easy": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= STACK =================
    elif topic == "Stack":
        st.markdown("### 🔴 Stack Quiz")
        score = 0

        q1 = st.radio("Q1: Stack follows?", ["LIFO", "FIFO"])
        q2 = st.radio("Q2: push()?", ["Insert", "Delete"])
        q3 = st.radio("Q3: pop()?", ["Remove", "Insert"])
        q4 = st.radio("Q4: Top access?", ["O(1)", "O(n)"])
        q5 = st.radio("Q5: Used in?", ["Recursion", "Sorting"])

        if st.button("Submit"):
            if q1 == "LIFO": score+=1
            if q2 == "Insert": score+=1
            if q3 == "Remove": score+=1
            if q4 == "O(1)": score+=1
            if q5 == "Recursion": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= QUEUE =================
    elif topic == "Queue":
        st.markdown("### 🟡 Queue Quiz")
        score = 0

        q1 = st.radio("Q1: Queue follows?", ["FIFO", "LIFO"])
        q2 = st.radio("Q2: enqueue()?", ["Insert", "Delete"])
        q3 = st.radio("Q3: dequeue()?", ["Remove", "Insert"])
        q4 = st.radio("Q4: Used in?", ["Scheduling", "Sorting"])
        q5 = st.radio("Q5: Access?", ["O(1)", "O(n)"])

        if st.button("Submit"):
            if q1 == "FIFO": score+=1
            if q2 == "Insert": score+=1
            if q3 == "Remove": score+=1
            if q4 == "Scheduling": score+=1
            if q5 == "O(1)": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= RECURSION =================
    elif topic == "Recursion":
        st.markdown("### 🔁 Recursion Quiz")
        score = 0

        q1 = st.radio("Q1: Recursion means?", ["Function calls itself", "Loop"])
        q2 = st.radio("Q2: Base case?", ["Stopping condition", "Loop"])
        q3 = st.radio("Q3: Used in?", ["Factorial", "Sorting only"])
        q4 = st.radio("Q4: Stack used?", ["Yes", "No"])
        q5 = st.radio("Q5: Infinite recursion?", ["Error", "Correct"])

        if st.button("Submit"):
            if q1 == "Function calls itself": score+=1
            if q2 == "Stopping condition": score+=1
            if q3 == "Factorial": score+=1
            if q4 == "Yes": score+=1
            if q5 == "Error": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= TREE =================
    elif topic == "Tree":
        st.markdown("### 🌳 Tree Quiz")
        score = 0

        q1 = st.radio("Q1: Tree is?", ["Hierarchical", "Linear"])
        q2 = st.radio("Q2: Root?", ["Top node", "Leaf"])
        q3 = st.radio("Q3: Leaf node?", ["No children", "Many children"])
        q4 = st.radio("Q4: Binary tree children?", ["2", "3"])
        q5 = st.radio("Q5: Traversal?", ["DFS/BFS", "Sorting"])

        if st.button("Submit"):
            if q1 == "Hierarchical": score+=1
            if q2 == "Top node": score+=1
            if q3 == "No children": score+=1
            if q4 == "2": score+=1
            if q5 == "DFS/BFS": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= GRAPH =================
    elif topic == "Graph":
        st.markdown("### 🔗 Graph Quiz")
        score = 0

        q1 = st.radio("Q1: Graph has?", ["Vertices & Edges", "Nodes only"])
        q2 = st.radio("Q2: BFS uses?", ["Queue", "Stack"])
        q3 = st.radio("Q3: DFS uses?", ["Stack", "Queue"])
        q4 = st.radio("Q4: Graph type?", ["Directed/Undirected", "Only directed"])
        q5 = st.radio("Q5: Shortest path?", ["Dijkstra", "Bubble"])

        if st.button("Submit"):
            if q1 == "Vertices & Edges": score+=1
            if q2 == "Queue": score+=1
            if q3 == "Stack": score+=1
            if q4 == "Directed/Undirected": score+=1
            if q5 == "Dijkstra": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= GREEDY =================
    elif topic == "Greedy Algorithm":
        st.markdown("### 💡 Greedy Quiz")
        score = 0

        q1 = st.radio("Q1: Greedy means?", ["Best local choice", "Worst choice"])
        q2 = st.radio("Q2: Used in?", ["Knapsack", "Only sorting"])
        q3 = st.radio("Q3: Optimal solution?", ["Yes", "No"])
        q4 = st.radio("Q4: Approach?", ["Step by step", "Random"])
        q5 = st.radio("Q5: Example?", ["Activity selection", "Loop"])

        if st.button("Submit"):
            if q1 == "Best local choice": score+=1
            if q2 == "Knapsack": score+=1
            if q3 == "Yes": score+=1
            if q4 == "Step by step": score+=1
            if q5 == "Activity selection": score+=1
            st.success(f"✅ Your Score: {score}/5")

    # ================= DP =================
    elif topic == "Dynamic Programming":
        st.markdown("### ⚡ Dynamic Programming Quiz")
        score = 0

        q1 = st.radio("Q1: DP uses?", ["Memoization", "Loop only"])
        q2 = st.radio("Q2: Overlapping problems?", ["Yes", "No"])
        q3 = st.radio("Q3: Optimizes?", ["Time", "Memory only"])
        q4 = st.radio("Q4: Example?", ["Fibonacci", "Sorting"])
        q5 = st.radio("Q5: Bottom-up?", ["Tabulation", "Recursion"])

        if st.button("Submit"):
            if q1 == "Memoization": score+=1
            if q2 == "Yes": score+=1
            if q3 == "Time": score+=1
            if q4 == "Fibonacci": score+=1
            if q5 == "Tabulation": score+=1
            st.success(f"✅ Your Score: {score}/5")
