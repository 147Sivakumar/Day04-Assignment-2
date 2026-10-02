import streamlit as st

st.title("Student Grade Manager")


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


if "students" not in st.session_state:
    st.session_state.students = []


with st.form("add_student"):
    name = st.text_input("Name")
    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add")

    if submitted:
        if not name.strip():
            st.warning("Please enter a student name.")
        else:
            st.session_state.students.append({
                "Name": name,
                "Mark": mark,
                "Grade": get_grade(mark)
            })
            st.success(f"{name} added successfully!")


if st.session_state.students:
    st.subheader("Student Records")

    st.table(st.session_state.students)

    marks = [student["Mark"] for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    col1, col2, col3 = st.columns(3)

    col1.metric("Average", f"{average:.1f}")
    col2.metric("Highest", highest)
    col3.metric("Lowest", lowest)
else:
    st.info("No students added yet.")
