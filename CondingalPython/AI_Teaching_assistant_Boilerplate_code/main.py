import streamlit as st
import AIimage
import MathAssistant



option = st.selectbox('Change AI', ('Safe AI image', 'Math Mastermind', 'Continuous Chat'))
st.write("You selected:", option)
def AIimage():
    image = AIimage.main()
    return image