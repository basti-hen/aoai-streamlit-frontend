import streamlit as st
from helper import get_database_answer

# st.set_page_config(layout="wide")
hide_menu_style = """<style>#MainMenu {visibility: hidden;}</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.image('./microsoft.png', width=200)
st.title('Azure OpenAI Service Q&A Demo')
st.caption('This demo is powered by Azure OpenAI Service')
st.write('This demo shows how Azure OpenAI Service can be used to answer questions on structured data stored in a SQL database. ')

tab1, tab2, tab3 = st.tabs(["Demo", "Sample questions", "How does this demo work?"])

with tab1:
    #st.write('Try asking a question like:\n\nWhat is Azure? Give me a long answer!')
    question = st.text_input("Question:")

    if question != '':
        answer, prompt = get_database_answer(question)
        st.write(f"**Question:** {question}")
        st.write(f"**Answer:** {answer}")
        with st.expander("Click here to see the prompt we've used to generate the answer", expanded=False):
            prompt = prompt.replace('$', '\$')
            st.markdown(f":star: **Short explanation**\n1. The first part of the prompt is the retrieved documents that were likely to contain the answer\n1. The second part is the actual prompt to answer our question\n\n:star: **Prompt:**\n{prompt}")
with tab2:
    st.write('Try asking questions like:')
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("""
* Question 1
* Question 2
* Question 3""")

    with col2:
        st.markdown("""
* Question 4
* Question 5
* Question 6""")

    st.write("You can also ask questions in other languages, e.g., try to ask a question in German or Spanish.")

with tab3:
   st.header("How does this demo work?")
   st.markdown("""
               This demo leverages the following components to achieve a ChatGPT-like experience on unstructured documents:
               * **Azure OpenAI Service** to generate answers to questions
               * **Langchain** to query a SQL database containing data to answer the questions
               """)
   #st.image("./architecture.png", caption="Solution Architecture")