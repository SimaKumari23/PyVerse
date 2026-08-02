import streamlit as st

st.set_page_config(page_title="DSA Greedy", layout="centered")

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
#---------- SAMPLE DATA ----------

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

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
</style>""",unsafe_allow_html=True)

st.markdown("<div class='title'>DSA Greedy Algorithms</div>",unsafe_allow_html=True)

#================= Q1 =================

st.markdown("<div class='section'>Question 1.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Activity Selection<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def activity_selection(start, end):
    activities = sorted(zip(start, end), key=lambda x: x[1])
    result = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= result[-1][1]:
            result.append(activities[i])

    return result
""")

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]

if st.button("Run Activity Selection", key="q1"):

    def activity_selection(start, end):
        activities = sorted(zip(start, end), key=lambda x: x[1])
        result = [activities[0]]

        for i in range(1, len(activities)):
            if activities[i][0] >= result[-1][1]:
                result.append(activities[i])

        return result

    st.success(activity_selection(start, end))

#================= Q2 =================

st.markdown("<div class='section'>Question 2.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Fractional Knapsack<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def fractional_knapsack(weights, values, capacity):
    ratio = sorted([(v/w, w, v) for w, v in zip(weights, values)], reverse=True)
    total = 0

    for r, w, v in ratio:
        if capacity >= w:
            capacity -= w
            total += v
        else:
            total += r * capacity
            break

    return total
""")

if st.button("Run Knapsack", key="q2"):

    def fractional_knapsack(weights, values, capacity):
        ratio = sorted([(v/w, w, v) for w, v in zip(weights, values)], reverse=True)
        total = 0

        for r, w, v in ratio:
            if capacity >= w:
                capacity -= w
                total += v
            else:
                total += r * capacity
                break

        return total

    st.success(fractional_knapsack(weights, values, capacity))

#================= Q3 =================

st.markdown("<div class='section'>Question 3.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Coin Change (Greedy)<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result
""")

coins = [1,2,5,10,20]
amount = st.number_input("Enter Amount", key="q3_input")

if st.button("Run Coin Change", key="q3"):

    def coin_change(coins, amount):
        coins.sort(reverse=True)
        result = []

        for coin in coins:
            while amount >= coin:
                amount -= coin
                result.append(coin)

        return result

    st.success(coin_change(coins.copy(), amount))

#================= Q4 =================

st.markdown("<div class='section'>Question 4.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Job Sequencing<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def job_sequencing(jobs):
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [None]*max_deadline

    for job in jobs:
        for j in range(job[1]-1, -1, -1):
            if slots[j] is None:
                slots[j] = job[0]
                break

    return slots
""")

jobs = [
('A',2,100),
('B',1,19),
('C',2,27),
('D',1,25),
('E',3,15)
]

if st.button("Run Job Sequencing", key="q4"):

    def job_sequencing(jobs):
        jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
        max_deadline = max(job[1] for job in jobs)
        slots = [None]*max_deadline

        for job in jobs:
            for j in range(job[1]-1, -1, -1):
                if slots[j] is None:
                    slots[j] = job[0]
                    break

        return slots

    st.success(job_sequencing(jobs))

#================= Q5 =================

st.markdown("<div class='section'>Question 5.</div>",unsafe_allow_html=True)
st.markdown("<div class='content'>Minimum Platforms<br>💻 Code</div>",unsafe_allow_html=True)

with st.expander("👨‍💻 See the Code"):
    st.code("""
def min_platforms(arr, dep):
    arr.sort()
    dep.sort()
    i=j=0
    plat=0
    res=0

    while i<len(arr) and j<len(dep):
        if arr[i]<=dep[j]:
            plat+=1
            res=max(res,plat)
            i+=1
        else:
            plat-=1
            j+=1

    return res
""")

arr_time = [900, 940, 950, 1100, 1500, 1800]
dep_time = [910, 1200, 1120, 1130, 1900, 2000]

if st.button("Find Platforms", key="q5"):

    def min_platforms(arr, dep):
        arr.sort()
        dep.sort()
        i=j=0
        plat=0
        res=0

        while i<len(arr) and j<len(dep):
            if arr[i]<=dep[j]:
                plat+=1
                res=max(res,plat)
                i+=1
            else:
                plat-=1
                j+=1

        return res

    st.success(min_platforms(arr_time.copy(), dep_time.copy()))
