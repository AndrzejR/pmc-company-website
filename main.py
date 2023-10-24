import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="The Best Company")

st.title("The Best Company")

company_description = ("Picture a company where innovation and creativity are not just encouraged but\n"
                       " celebrated, where employees are not just cogs in a machine but valued \n"
                       " contributors to a shared vision. This company fosters a culture of \n"
                       " collaboration and growth, where every individual feels empowered to make a \n"
                       " difference. It's a place where passion and purpose converge, where work is \n"
                       " not just a job but an opportunity to shape a better future. This company is \n"
                       " not just a business; it's a force for positive change, committed to making a "
                       "lasting impact on the world. That is the essence of the best company ever.\n")

st.write(company_description)

st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.2, 1, 0.2, 1])

data = pd.read_csv("data.csv")


def write_person(record):
    st.subheader(f"{record['first name']} {record['last name']}".title())
    st.write(record['role'])
    st.image(f"images/{record['image']}")


with col1:
    for idx, row in data[0::3].iterrows():
        write_person(row)

with col2:
    for idx, row in data[1::3].iterrows():
        write_person(row)

with col3:
    for idx, row in data[2::3].iterrows():
        write_person(row)
