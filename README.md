# Student Grade Manager

A Streamlit application for managing student marks and grades.

# App in the Browser
![app in the browser](app_in_the_browser.png)

# What Went Wrong Before session_state

Before using st.session_state, the student list was reset every time Streamlit reran the script, so previously added students disappeared.