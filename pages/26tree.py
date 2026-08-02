import streamlit as st

st.set_page_config(page_title="DSA Tree", layout="centered")


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
# ---------- TREE CLASS ----------

class Node:

    def __init__(self,data):

        self.data=data
        self.left=None
        self.right=None



class BinaryTree:

    def __init__(self):

        self.root=None



    def preorder(self,node,result):

        if node:

            result.append(node.data)

            self.preorder(node.left,result)

            self.preorder(node.right,result)



    def inorder(self,node,result):

        if node:

            self.inorder(node.left,result)

            result.append(node.data)

            self.inorder(node.right,result)



    def postorder(self,node,result):

        if node:

            self.postorder(node.left,result)

            self.postorder(node.right,result)

            result.append(node.data)



    def level_order(self):

        result=[]

        if not self.root:
            return result


        queue=[self.root]


        while queue:

            temp=queue.pop(0)

            result.append(temp.data)


            if temp.left:
                queue.append(temp.left)


            if temp.right:
                queue.append(temp.right)


        return result



# ---------- CREATE SAMPLE TREE ----------

if "tree" not in st.session_state:

    tree=BinaryTree()


    tree.root=Node(10)

    tree.root.left=Node(20)

    tree.root.right=Node(30)

    tree.root.left.left=Node(40)

    tree.root.left.right=Node(50)


    st.session_state.tree=tree



tree=st.session_state.tree




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

    background-attachment:fixed;
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
    line-height:1.6;
}


.stButton>button{

    background:linear-gradient(90deg,#0040ff,#8c00ff);
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 22px;
    font-weight:bold;

}

</style>
""",unsafe_allow_html=True)



st.markdown(
"<div class='title'>DSA Tree</div>",
unsafe_allow_html=True
)






# ================= Q1 =================


st.markdown(
"<div class='section'>Question 1.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Create Binary Tree<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

class Node:

    def __init__(self,data):

        self.data=data

        self.left=None

        self.right=None



root=Node(10)

root.left=Node(20)

root.right=Node(30)


print(root.data)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Show Tree",key="q1"):

    st.success("Binary Tree Created")

    st.write(
        "        10"
    )

    st.write(
        "      /    \\"
    )

    st.write(
        "    20      30"
    )

    st.write(
        "   /  \\"
    )

    st.write(
        " 40    50"
    )







# ================= Q2 =================


st.markdown(
"<div class='section'>Question 2.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Preorder Traversal<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def preorder(root):

    if root:

        print(root.data)

        preorder(root.left)

        preorder(root.right)



preorder(root)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Preorder",key="q2"):


    result=[]

    tree.preorder(tree.root,result)


    st.success(result)







# ================= Q3 =================


st.markdown(
"<div class='section'>Question 3.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Inorder Traversal<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def inorder(root):

    if root:

        inorder(root.left)

        print(root.data)

        inorder(root.right)



inorder(root)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Inorder",key="q3"):


    result=[]

    tree.inorder(tree.root,result)


    st.success(result)







# ================= Q4 =================


st.markdown(
"<div class='section'>Question 4.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Postorder Traversal<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def postorder(root):

    if root:

        postorder(root.left)

        postorder(root.right)

        print(root.data)



postorder(root)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Postorder",key="q4"):


    result=[]

    tree.postorder(tree.root,result)


    st.success(result)







# ================= Q5 =================


st.markdown(
"<div class='section'>Question 5.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Level Order Traversal<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

queue=[root]


while queue:

    temp=queue.pop(0)

    print(temp.data)



""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Level Order",key="q5"):


    st.success(tree.level_order())

# ================= Q6 =================

st.markdown(
"<div class='section'>Question 6.</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='content'>Search Node in Tree<br>💻 Code</div>",
unsafe_allow_html=True
)


with st.expander("👨‍💻 See the Code"):

    st.code("""

def search(root,key):

    if root is None:

        return False


    if root.data==key:

        return True


    return search(root.left,key) or search(root.right,key)



print(search(root,30))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


search_value = st.number_input(
    "Enter value",
    key="q6_input"
)


if st.button("Search Node",key="q6"):


    def search_node(node,key):

        if node is None:

            return False


        if node.data==key:

            return True


        return search_node(node.left,key) or search_node(node.right,key)



    if search_node(tree.root,search_value):

        st.success("Found")

    else:

        st.error("Not Found")







# ================= Q7 =================

st.markdown(
"<div class='section'>Question 7.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Count Total Nodes<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def count(root):

    if root is None:

        return 0


    return 1 + count(root.left) + count(root.right)



print(count(root))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)


if st.button("Count Nodes",key="q7"):


    def count_nodes(node):

        if node is None:

            return 0


        return 1 + count_nodes(node.left) + count_nodes(node.right)



    st.success(count_nodes(tree.root))







# ================= Q8 =================

st.markdown(
"<div class='section'>Question 8.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Find Height of Tree<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def height(root):

    if root is None:

        return 0


    return 1 + max(
        height(root.left),
        height(root.right)
    )



print(height(root))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Find Height",key="q8"):


    def tree_height(node):

        if node is None:

            return 0


        return 1 + max(
            tree_height(node.left),
            tree_height(node.right)
        )



    st.success(tree_height(tree.root))







# ================= Q9 =================

st.markdown(
"<div class='section'>Question 9.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Find Maximum Element<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def maximum(root):

    if root is None:

        return -1


    left=maximum(root.left)

    right=maximum(root.right)


    return max(root.data,left,right)



print(maximum(root))

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



if st.button("Find Maximum",key="q9"):


    def max_element(node):

        if node is None:

            return -1


        left=max_element(node.left)

        right=max_element(node.right)


        return max(
            node.data,
            left,
            right
        )



    st.success(max_element(tree.root))







# ================= Q10 =================

st.markdown(
"<div class='section'>Question 10.</div>",
unsafe_allow_html=True
)


st.markdown(
"<div class='content'>Delete Node from BST<br>💻 Code</div>",
unsafe_allow_html=True
)



with st.expander("👨‍💻 See the Code"):

    st.code("""

def delete(root,key):

    if root is None:

        return root


    if key < root.data:

        root.left=delete(root.left,key)


    elif key > root.data:

        root.right=delete(root.right,key)


    else:

        return None


    return root



root=delete(root,20)

""")


st.markdown(
"<div class='content'>🚀 Working</div>",
unsafe_allow_html=True
)



delete_value = st.number_input(
    "Enter node to delete",
    key="q10_input"
)



if st.button("Delete Node",key="q10"):


    def delete_node(root,key):

        if root is None:

            return None


        if key < root.data:

            root.left=delete_node(
                root.left,
                key
            )


        elif key > root.data:

            root.right=delete_node(
                root.right,
                key
            )


        else:

            return None


        return root



    tree.root = delete_node(
        tree.root,
        delete_value
    )


    result=[]

    tree.inorder(
        tree.root,
        result
    )


    st.success("After Delete")

    st.write(result)    
