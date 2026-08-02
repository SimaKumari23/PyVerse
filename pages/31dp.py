import streamlit as st

st.set_page_config(page_title="DSA DP", layout="centered")

#---------- LOGIN ----------

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
#---------- CSS ----------

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

st.markdown("<div class='title'>DSA Dynamic Programming</div>",unsafe_allow_html=True)

#================= Q1 =================

st.markdown("<div class='section'>Question 1.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Fibonacci (DP)<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def fib(n):
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
""")

n = st.number_input("Enter n", min_value=1, key="q1_input")

if st.button("Find Fibonacci", key="q1"):

    def fib(n):
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

    st.success(fib(n))

#================= Q2 =================

st.markdown("<div class='section'>Question 2.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>0/1 Knapsack (DP)<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def knapsack(wt, val, W):
    n=len(wt)
    dp=[[0]*(W+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1]<=w:
                dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]

    return dp[n][W]
""")

wt = [10,20,30]
val = [60,100,120]
W = int(st.number_input("Enter Capacity", key="q2_input"))

if st.button("Run Knapsack DP", key="q2"):

    def knapsack(wt, val, W):
        n=len(wt)
        dp=[[0]*(W+1) for _ in range(n+1)]

        for i in range(1,n+1):
            for w in range(1,W+1):
                if wt[i-1]<=w:
                    dp[i][w]=max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
                else:
                    dp[i][w]=dp[i-1][w]

        return dp[n][W]

    st.success(knapsack(wt, val, W))

#================= Q3 =================

st.markdown("<div class='section'>Question 3.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Longest Common Subsequence<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def lcs(X,Y):
    m=len(X)
    n=len(Y)
    dp=[[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
""")

s1 = st.text_input("Enter String 1", key="q3_s1")
s2 = st.text_input("Enter String 2", key="q3_s2")

if st.button("Find LCS", key="q3"):

    def lcs(X,Y):
        m=len(X)
        n=len(Y)
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if X[i-1]==Y[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

    st.success(lcs(s1, s2))

#================= Q4 =================

st.markdown("<div class='section'>Question 4.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Coin Change (DP)<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def coin_change(coins, amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i]=min(dp[i], dp[i-coin]+1)

    return dp[amount] if dp[amount]!=float('inf') else -1
""")

coins = [1,2,5]
amt = st.number_input("Enter Amount", min_value=0, step=1, key="q4_input")
if st.button("Run Coin Change DP", key="q4"):

    def coin_change(coins, amount):
        dp=[float('inf')]*(amount+1)
        dp[0]=0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount]!=float('inf') else -1

    st.success(coin_change(coins, amt))

#================= Q5 =================

st.markdown("<div class='section'>Question 5.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Minimum Cost Path<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def min_cost(cost):
    m=len(cost)
    n=len(cost[0])
    dp=[[0]*n for _ in range(m)]

    dp[0][0]=cost[0][0]

    for i in range(1,m):
        dp[i][0]=dp[i-1][0]+cost[i][0]

    for j in range(1,n):
        dp[0][j]=dp[0][j-1]+cost[0][j]

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=cost[i][j]+min(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]
""")

cost = [
[1,3,1],
[1,5,1],
[4,2,1]
]

if st.button("Find Min Cost", key="q5"):

    def min_cost(cost):
        m=len(cost)
        n=len(cost[0])
        dp=[[0]*n for _ in range(m)]

        dp[0][0]=cost[0][0]

        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+cost[i][0]

        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+cost[0][j]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=cost[i][j]+min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]

    st.success(min_cost(cost))
