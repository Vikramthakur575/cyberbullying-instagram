import streamlit as st

bullying_words = ["stupid", "idiot", "useless", "hate", "kill"]

st.set_page_config(page_title="Cyberbullying Detection", layout="centered")

st.markdown("## 📸 Mini Instagram – Cyberbullying Detection")

st.image("static/post.jpg", use_column_width=True)
st.markdown("**@insta_fun_user**")

comment = st.text_input("Add a comment")

if st.button("Post"):
    if any(word in comment.lower() for word in bullying_words):
        st.error("⚠️ Cyberbullying detected! Delete the comment or action will be taken.")
        st.image("static/warning.png", width=300)
    else:
        st.success("✅ Comment posted successfully.")
