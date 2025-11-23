import streamlit as st
import sqlite3

st.title("🗂 User Management App (SQLite)")

@st.cache_resource
def get_connection():
    return sqlite3.connect("users.db", check_same_thread=False)

conn = get_connection()

conn.execute('''CREATE TABLE IF NOT EXISTS users (
    Name TEXT PRIMARY KEY,
    Age INTEGER
)''')

name = st.text_input("Enter Name:")
age = st.number_input("Enter Age:", min_value=0, max_value=120, step=1)

if st.button("Add User"):
    if name.strip() == "":
        st.error("Name cannot be empty.")
    else:
        try:
            conn.execute("INSERT INTO users (Name, Age) VALUES (?, ?)", (name.strip(), age))
            conn.commit()
            st.success("User added!")
        except sqlite3.IntegrityError:
            st.error("User already exists.")

if st.button("View All Users"):
    cur = conn.cursor()
    cur.execute("SELECT Name, Age FROM users ORDER BY Name")
    rows = cur.fetchall()

    if not rows:
        st.info("No users found.")
    else:
        st.write("### User List")
        for r in rows:
            st.write(f"Name: {r[0]} | Age: {r[1]}")

if st.button("Clear All Users"):
    conn.execute("DELETE FROM users")
    conn.commit()
    st.success("All users deleted!")
