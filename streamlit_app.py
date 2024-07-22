import streamlit as st
import pandas as pd
st.title("매출, 영업 이익 데이터")

# Load the dataset
df = pd.read_csv("practice_sales_dataset.csv")

# Display the dataframe
st.write(df)

# Show "연도 별 매출 현황" text
st.header("연도 별 매출 현황")

# Create a line plot
st.line_chart(data=df, x="year", y="sales")

# Show "연도 별 영업 이익 현황" text
st.header("연도 별 영업 이익 현황")

# Create a bar chart
st.bar_chart(data=df, x="year", y="profit")