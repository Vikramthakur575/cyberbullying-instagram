import streamlit as st
from pathlib import Path

# ------------------ Config ------------------
st.set_page_config(
    page_title="Cyberbullying Detection",
    layout="centered"
)

# ------------------ Paths -------------------
BASE_DIR = Path(__file__).parent
POST_IMAGE = BASE_DIR / "static" / "post.jpg"
WARNING_IMAGE = BASE_DIR / "static" / "warning.png"

# ------------------ Data --------------------
bullying_words = ["stupid", "idiot", "useless", "hate", "kill"]

# ------------------ UI ----------------------
st.markdown("## 📸 Mini Instagram – Cyberbullying Detection")

st.image(str(POST_IMAGE), width=400)
st.markdown("**@insta_fun_user**")

comment = st.text_input("Add a comment")

# ------------------ Logic -------------------
if st.button("Post"):
    if any(word in comment.lower() for word in bullying_words):
        st.error("⚠️ Cyberbullying detected! Delete the comment or action will be taken.")
        st.image(str(WARNING_IMAGE), width=300)
    elif comment.strip() == "":
        st.warning("Please write a comment before posting.")
    else:
        st.success("✅ Comment posted successfully.")
