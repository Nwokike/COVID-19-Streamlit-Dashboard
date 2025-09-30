import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS

# --- Page Configuration ---
st.set_page_config(page_title="CORD-19 Research Dashboard", page_icon="🔬", layout="wide")

# --- Data Loading & Caching ---
@st.cache_data
def load_data():
    df = pd.read_csv('data/metadata.csv', usecols=['title', 'abstract', 'publish_time', 'journal'])
    df.dropna(subset=['title', 'abstract', 'publish_time', 'journal'], inplace=True)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df.dropna(subset=['publish_time'], inplace=True)
    df['year'] = df['publish_time'].dt.year
    df['year'] = df['year'].astype(int)
    df['abstract_word_count'] = df['abstract'].str.split().str.len()
    df = df[df['year'] <= 2024]
    return df

# --- Plotting Functions ---
def plot_pubs_over_time(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    papers_by_year = df['year'].value_counts().sort_index()
    sns.lineplot(x=papers_by_year.index, y=papers_by_year.values, ax=ax, marker='o')
    ax.set_title('Publications Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Publications')
    return fig

def plot_word_cloud(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    text = " ".join(title for title in df.title)
    stopwords = set(STOPWORDS)
    stopwords.update(["patient", "study", "result", "conclusion", "method"])
    wc = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text)
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    return fig

def plot_abstract_histogram(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df['abstract_word_count'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribution of Abstract Lengths')
    ax.set_xlabel('Word Count')
    ax.set_ylabel('Frequency')
    ax.set_xlim(0, 800)
    return fig

# --- Main App ---
df = load_data()

st.title("🔬 CORD-19 Research Dashboard")
st.markdown("An interactive dashboard for exploring COVID-19 scientific literature.")

# --- Sidebar ---
st.sidebar.header("User Controls")
start_year, end_year = st.sidebar.select_slider(
    "Select Year Range",
    options=sorted(df['year'].unique()),
    value=(2019, 2021)
)
filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]

# --- Dashboard Metrics ---
st.header(f"Dashboard for {start_year} - {end_year}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Publications", f"{filtered_df.shape[0]:,}")
col2.metric("Unique Journals", f"{filtered_df.journal.nunique():,}")
col3.metric("Avg. Abstract Length", f"{int(filtered_df.abstract_word_count.mean())} words")

st.markdown("---")

# --- Visualizations ---
c1, c2 = st.columns((0.6, 0.4))
with c1:
    st.subheader("Publication Trend")
    st.pyplot(plot_pubs_over_time(filtered_df))

with c2:
    st.subheader("Abstract Lengths")
    st.pyplot(plot_abstract_histogram(filtered_df))

st.subheader("Key Topics in Paper Titles")
st.pyplot(plot_word_cloud(filtered_df))

# --- Data Table ---
with st.expander("Show Raw Data Sample"):
    st.dataframe(filtered_df[['title', 'journal', 'year', 'abstract_word_count']].head(10))