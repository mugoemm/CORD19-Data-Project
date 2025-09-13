# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned dataset
df = pd.read_csv("cleaned_cord19.csv")

# Title & Description
st.title("📊 CORD-19 Data Explorer")
st.write("A simple interactive dashboard to explore COVID-19 research papers.")

# Year filter
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", year_min, year_max, (2020, 2021))
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications over time
st.subheader("📈 Publications Over Time")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top journals
st.subheader("🏢 Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
st.bar_chart(top_journals)

# WordCloud of titles
st.subheader("☁️ WordCloud of Paper Titles")
text = " ".join(filtered_df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Data sample
st.subheader("📄 Sample Data")
st.write(filtered_df.head(10))

