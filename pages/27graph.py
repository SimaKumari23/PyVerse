import streamlit as st

st.set_page_config(page_title="DSA Graph", layout="centered")

# ---------- LOGIN ----------
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
            st.switch_page("pages/20dsa.py")
# ---------- GRAPH CLASS ----------
class Graph:

    def __init__(self):
        self.graph={}

    def add_edge(self,u,v):

        if u not in self.graph:
            self.graph[u]=[]

        if v not in self.graph:
            self.graph[v]=[]

        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self,node,visited,result):

        visited.add(node)
        result.append(node)

        for i in self.graph[node]:
            if i not in visited:
                self.dfs(i,visited,result)


    def bfs(self,start):

        visited=set()
        queue=[start]
        result=[]

        visited.add(start)

        while queue:

            temp=queue.pop(0)
            result.append(temp)

            for i in self.graph[temp]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

        return result


# ---------- CREATE SAMPLE GRAPH ----------
if "graph" not in st.session_state:

    g=Graph()

    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(2,5)

    st.session_state.graph=g

graph=st.session_state.graph


# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
    background:
        radial-gradient(circle at center, rgba(168,85,247,0.28), transparent 70%),
        linear-gradient(135deg,#0B1026,#1A1D3A);
}

.title{
    color:#90E0EF;
    font-size:40px;
    font-weight:bold;
}

.section{
    color:#90E0EF;
    font-size:26px;
    margin-top:25px;
}

.content{
    color:#9CA3AF;
    font-size:22px;
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
""",unsafe_allow_html=True)


st.markdown("<div class='title'>DSA Graph</div>",unsafe_allow_html=True)


# ================= Q1 =================
st.markdown("<div class='section'>Question 1.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Create Graph<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

graph={}
graph[1]=[2,3]
graph[2]=[1,4,5]

print(graph)

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Show Graph",key="q1"):
    st.success(graph.graph)


# ================= Q2 =================
st.markdown("<div class='section'>Question 2.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>DFS Traversal<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def dfs(graph,node,visited):

    visited.add(node)
    print(node,end=" ")

    for i in graph[node]:
        if i not in visited:
            dfs(graph,i,visited)

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("DFS",key="q2"):

    visited=set()
    result=[]

    graph.dfs(1,visited,result)

    st.success(result)


# ================= Q3 =================
st.markdown("<div class='section'>Question 3.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>BFS Traversal<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def bfs(graph,start):

    visited=set()
    queue=[start]

    visited.add(start)

    while queue:

        temp=queue.pop(0)
        print(temp,end=" ")

        for i in graph[temp]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("BFS",key="q3"):
    st.success(graph.bfs(1))


# ================= Q4 =================
st.markdown("<div class='section'>Question 4.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Search Node<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def search(graph,key):

    if key in graph:
        return True

    return False

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

val=st.number_input("Enter value",key="q4_input")

if st.button("Search Node",key="q4"):

    if val in graph.graph:
        st.success("Found")
    else:
        st.error("Not Found")


# ================= Q5 =================
st.markdown("<div class='section'>Question 5.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Count Nodes<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def count(graph):

    return len(graph)

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Count Nodes",key="q5"):
    st.success(len(graph.graph))


# ================= Q6 =================
st.markdown("<div class='section'>Question 6.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Count Edges<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def edges(graph):

    count=0

    for i in graph:
        count+=len(graph[i])

    return count//2

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

if st.button("Count Edges",key="q6"):

    edges=sum(len(v) for v in graph.graph.values())//2

    st.success(edges)


# ================= Q7 =================
st.markdown("<div class='section'>Question 7.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Add Edge<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def add_edge(graph,u,v):

    graph[u].append(v)
    graph[v].append(u)

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

u=st.number_input("Node U",key="q7_u")
v=st.number_input("Node V",key="q7_v")

if st.button("Add Edge",key="q7"):

    graph.add_edge(u,v)
    st.success(graph.graph)


# ================= Q8 =================
st.markdown("<div class='section'>Question 8.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Display Graph</div>",unsafe_allow_html=True)

if st.button("Display",key="q8"):
    st.write(graph.graph)


# ================= Q9 =================
st.markdown("<div class='section'>Question 9.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Degree of Node<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def degree(graph,node):

    return len(graph[node])

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

node=st.number_input("Enter node",key="q9_input")

if st.button("Find Degree",key="q9"):

    if node in graph.graph:
        st.success(len(graph.graph[node]))
    else:
        st.error("Not Found")


# ================= Q10 =================
st.markdown("<div class='section'>Question 10.</div>",unsafe_allow_html=True)

st.markdown("<div class='content'>Remove Edge<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""

def remove_edge(graph,u,v):

    graph[u].remove(v)
    graph[v].remove(u)

""")

st.markdown("<div class='content'>🚀 Working</div>",unsafe_allow_html=True)

u1=st.number_input("Node U ",key="q10_u")
v1=st.number_input("Node V ",key="q10_v")

if st.button("Remove Edge",key="q10"):

    if u1 in graph.graph and v1 in graph.graph[u1]:
        graph.graph[u1].remove(v1)
        graph.graph[v1].remove(u1)

        st.success("Removed")
        st.write(graph.graph)

    else:
        st.error("Edge not found")
