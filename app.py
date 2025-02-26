import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌻", layout="wide")

# Header Section
st.title("🌱 Growth Mindset Challenge")
st.header("Start Your Growth Journey With Us ✨")
st.write("Embrace challenges, persist in the face of setbacks, and see effort as a path to mastery.")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Challenges", "Daily Tips", "Community"])  

# Home Page
if page == "Home":
    st.subheader("Welcome to Growth Mindset Challenge")
    st.write("A place to develop a positive mindset through interactive challenges and daily motivation.")
    st.image("https://source.unsplash.com/800x400/?growth,success", caption="Believe in Your Growth")

# Challenges Page
elif page == "Challenges":
    st.subheader("🚀 Take on Challenges")
    challenge = st.selectbox("Choose a Challenge", [
        "Overcome a Fear", 
        "Learn a New Skill", 
        "Daily Gratitude Journal", 
        "Step Out of Comfort Zone"])
    
    st.write(f"**Your Challenge:** {challenge}")
    st.text_area("Write about your experience:")
    st.button("Submit")

# Daily Tips Page
elif page == "Daily Tips":
    st.subheader("💡 Daily Growth Tips")
    st.write("Here's a tip to boost your mindset today:")
    tips = [
        "Failures are proof that you're trying. Keep going!", 
        "Your brain is like a muscle. The more you use it, the stronger it gets!", 
        "Don't compare your Chapter 1 to someone else's Chapter 20.",
        "Surround yourself with positive influences."]
    st.success(tips[st.session_state.get('tip_index', 0)])
    if st.button("Next Tip"):
        st.session_state['tip_index'] = (st.session_state.get('tip_index', 0) + 1) % len(tips)

# Community Page
elif page == "Community":
    st.subheader("🤝 Join the Growth Community")
    st.write("Share your progress and learn from others!")
    username = st.text_input("Enter your name:")
    message = st.text_area("Share your thoughts:")
    if st.button("Post Message"):
        st.success(f"Thank you, {username}! Your message has been shared.")
    
# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")