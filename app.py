from dotenv import load_dotenv
load_dotenv()  ## load all the environment variables

import streamlit as st
import os 
import sqlite3

import google.generativeai as genai

## Configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

## Function to retrieve the query from sql database
def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARCKS \n\nFor example, \nExample 1 - How many entries are present,
    the SQL command will be something like this SELECT COUNT(* FROM STUDENT);
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="Data Science";
    also sql code should not have ``` in beginning or end and sql word in output
    """
    ]

## Streamlit App
st.set_page_config(page_title="I Can Retrieve Any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

## if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)