import streamlit as st
st.markdown("<h1 style='text-align: center; color: Black;'>Hello Everyone! </h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: Red;'>Kavya Rao </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: left; color: black;'>Data Science Intern </h2>", unsafe_allow_html=True)



st.markdown("I am Kavya . Data science Intern Looking for New Challenges/Opportunities in the field of Data  Science and an aspiring Data scientist who enjoys connecting the dots: be it ideas from different disciplines, people from different teams, or applications from different industries.I have strong technical skills and an academic background in engineering, statistics, and machine learning.")




st.header("Skills")
st.text("Python ,Tableau,Power Bi,Machine Learning,Statistical Analysis, Data Analysis")

url = "https://www.linkedin.com/in/kavyaarao/"
              
git = "https://github.com/Kavyarao01"

st.snow()

btn_click = st.button("Click Me !")

if btn_click == True:

 st.markdown("Lets Get Connected:handshake: [Kavya Rao](%s)" % url)
 st.markdown("My Work! :computer: [Kavya Rao](%s)" % git)
