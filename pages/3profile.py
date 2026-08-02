import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pymongo
conn=pymongo.MongoClient("mongodb+srv://sk3538970_db_user:Yn1qjlwb3oJ4z6K1@pyversedb.bxahnpm.mongodb.net/?appName=PyverseDB")
mydb=conn["ojt"]
my=mydb["user_info"]
st.set_page_config(page_title="My Profile", page_icon="👤", layout="wide")   
# Login check
if st.session_state.get("username", False):
    st.write("You are safely inside the app!")
else:
    st.warning("First Login !!!")
    st.stop()
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
        if st.button("⬅ Back", use_container_width=True):
            st.switch_page("main.py")
# ---------------- CSS ----------------
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

h1{
    background:linear-gradient(90deg,#00c6ff,#ffffff);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-align:center;
    font-size:45px !important;
    font-weight:bold;
}
.profile-card{
    background: rgba(17, 18, 42, 0.7);
    backdrop-filter: blur(12px);
    border-radius:16px;
    padding:25px;
    width:100%;
    max-width:900px;
    border:1px solid #2E2F5B;
    box-shadow:0 0 15px rgba(77,163,255,0.2);
    transition:.3s ease;
    color:#CBD5E1;
    margin-top:25px;
}

.profile-card:hover{
    box-shadow:
        0 0 25px rgba(59,130,246,0.5),
        0 0 45px rgba(168,85,247,0.6);
}
</style>
""", unsafe_allow_html=True)
# ---------------- TITLE ----------------

st.title("👤 My Profile")
st.write("")
# ---------------- BUTTONS ----------------
with stylable_container(
    key="main_buttons",
    css_styles="""
    button {
        width:100%;
        height:55px;
        background:linear-gradient(90deg,#0040ff,#8c00ff);
        color:white;
        border:none;
        border-radius:14px;
        font-size:17px;
        font-weight:bold;
        transition:.3s;
    }

    button:hover{
        transform:scale(1.04);
        background:linear-gradient(90deg,#0066ff,#a855f7);
        box-shadow:0 0 18px #60A5FA;
    }
    """
):
    c1,c2,c3,c4,c5= st.columns(5)

    with c1:
        b1 = st.button("👤 See Profile", use_container_width=True)

    with c2:
        b2 = st.button("🔒 Change Password", use_container_width=True)

    with c3:
        b3 = st.button("🚀 PyVerseAI Career guide", use_container_width=True)

    with c4:
        b4 = st.button("📄 PyVerseAI CV Analyzer", use_container_width=True)

    with c5:
        b5 = st.button("🚪 Logout", use_container_width=True)

# ---------------- CHANGE PASSWORD DIALOG ----------------
@st.dialog("🔒 CHANGE PASSWORD")
def cp():

    old = st.text_input("Old Password", type="password")
    new = st.text_input("New Password", type="password")
    confirm = st.text_input("Confirm New Password", type="password")

    if st.button("Change Password", use_container_width=True):

        if old == "" or new == "" or confirm == "":
            st.error("Please fill all fields")

        elif new != confirm:
            st.error("New Password and Confirm Password do not match")

        else:

            user = my.find_one({
                "Username": st.session_state["username"],
                "Password": old
            })

            if user:

                my.update_one(
                    {
                        "Username": st.session_state["username"]
                    },
                    {
                        "$set":{
                            "Password":new
                        }
                    }
                )

                st.session_state["password"]=new
                st.success("✅ Password Changed Successfuly")
                st.rerun()
                
            else:
                st.error("❌ Old Password is Incorrect")

# ---------------- SEE PROFILE ----------------
if b1:

    data = my.find_one({
        "Username": st.session_state["username"],
        "Password": st.session_state["password"]
    })

    if data:

        st.markdown(f"""
        <div class="profile-card">

        <h2 style="text-align:center; color:#90E0EF;">👤 PROFILE DETAILS</h2>

        <hr style="border:1px solid #2E2F5B;">

        <b>Username :</b> {data["Username"]}<br><br>

        <b>Password :</b> {data["Password"]}<br><br>

        <b>Mobile Number :</b> {data["Mobile Number"]}<br><br>

        <b>Email Id:</b> {data["Email Id"]}<br><br>

        <b>DOB :</b> {data["DOB"]}

        </div>
        """, unsafe_allow_html=True)

    else:
        st.error("Profile not found")
# ---------------- OPEN DIALOG ----------------

if b2:
    cp()
# ---------------- AI IMPLEMENTATION ----------------

if b3:
    st.switch_page("pages/4AI.py")     # Agar AI.py ka naam alag hai to yahan change kar dena
if b4:
    st.switch_page("pages/5.5cv.py")     # Agar AI.py ka naam alag hai to yahan change kar dena


# ---------------- LOGOUT ----------------
if b5:
    st.session_state.logged_in = False

    if "username" in st.session_state:
        del st.session_state["username"]

    if "password" in st.session_state:
        del st.session_state["password"]

    st.success("Logged Out Successfully")
    st.switch_page("main.py")

