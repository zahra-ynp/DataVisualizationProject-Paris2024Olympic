import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- Page Config ---
st.set_page_config(page_title="Paris 2024 Athlete Analysis", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("athletes.csv")  # Replace with your CSV filename
    df['birth_date'] = pd.to_datetime(df['birth_date'], errors='coerce')
    df['age'] = (pd.to_datetime("2024-07-26") - df['birth_date']).dt.days // 365

    # Extract discipline
    df['discipline'] = df['disciplines'].str.extract(r"\['(.+?)'\]")

    # Group disciplines into categories
    discipline_map = {
    'Wrestling': 'Combat Sports',
    'Judo': 'Combat Sports',
    'Boxing': 'Combat Sports',
    'Taekwondo': 'Combat Sports',

    'Swimming': 'Aquatics',
    'Diving': 'Aquatics',
    'Artistic Swimming': 'Aquatics',

    'Athletics': 'Athletics',
    'Race Walking': 'Athletics',
    'Marathon': 'Athletics',

    'Basketball': 'Ball Sports',
    '3x3 Basketball': 'Ball Sports',
    'Volleyball': 'Ball Sports',
    'Beach Volleyball': 'Ball Sports',
    'Handball': 'Ball Sports',
    'Football': 'Ball Sports',
    'Rugby Sevens': 'Ball Sports',

    'Artistic Gymnastics': 'Gymnastics',
    'Rhythmic Gymnastics': 'Gymnastics',
    'Trampoline': 'Gymnastics',

    'BMX Freestyle': 'Cycling Sports',
    'BMX Racing': 'Cycling Sports',
    'Road Cycling': 'Cycling Sports',
    'Track Cycling': 'Cycling Sports',
    'Mountain Bike': 'Cycling Sports',

    'Tennis': 'Racquet Sports',
    'Table Tennis': 'Racquet Sports',
    'Badminton': 'Racquet Sports',

    'Rowing': 'Water Sports',
    'Canoe Slalom': 'Water Sports',
    'Canoe Sprint': 'Water Sports',
    'Sailing': 'Water Sports',

    'Skateboarding': 'Extreme Sports',
    'Sport Climbing': 'Extreme Sports',

    'Equestrian': 'Other',
    'Golf': 'Other',
    'Shooting': 'Other',
    'Archery': 'Other',
    'Fencing': 'Combat Sports',  # Considered combat due to nature
    }

    df['sport_category'] = df['discipline'].map(discipline_map)
    df = df.dropna(subset=['age', 'discipline', 'sport_category'])


    df = df.dropna(subset=['age', 'discipline'])
    return df

df = load_data()

st.title("🎯 Paris 2024 Athletes: Age & Sport Analysis")
st.markdown("Analyze how age varies across different Olympic disciplines.")

# --- Filters ---
sports = st.multiselect("Select Disciplines", sorted(df['sport_category'].unique()), default=None)
gender = st.radio("Gender", ["All", "Male", "Female"])

filtered_df = df.copy()
if sports:
    filtered_df = filtered_df[filtered_df['sport_category'].isin(sports)]
if gender != "All":
    filtered_df = filtered_df[filtered_df['gender'] == gender]

# 1. Calculate median ages per category
median_ages = df.groupby("sport_category")["age"].median().sort_values()

# 2. Create a sorted list of categories
sorted_categories = median_ages.index.tolist()


# --- 1. Histogram: Age Distribution ---
st.subheader("📊 Age Distribution")
fig1 = px.histogram(
    filtered_df,
    x="age",
    color="sport_category",
    nbins=20,
    title="Age Distribution by sport_categorye",
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(fig1, use_container_width=True)

# --- 2. Box Plot: Age vs Discipline ---
st.subheader("📦 Age Range per sport_category")
fig2 = px.box(
    filtered_df,
    x="sport_category",
    y="age",
    color="sport_category",
    title="Age Distribution by Sport",
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(fig2, use_container_width=True)



# --- 3. Bar Chart: Athlete Count by Discipline ---
st.subheader("📉 Athlete Count per Discipline")
discipline_counts = filtered_df['sport_category'].value_counts().reset_index()
discipline_counts.columns = ['sport_category', 'count']
fig3 = px.bar(
    discipline_counts,
    x="sport_category",
    y="count",
    color="count",
    color_continuous_scale="Viridis",
    title="Number of Athletes by Sport"
)
st.plotly_chart(fig3, use_container_width=True)

# --- 4. Scatter Plot: Age vs Discipline (Jittered) ---
st.subheader("🟢 Age Scatter by Sport")
fig4 = px.strip(
    filtered_df,
    x="sport_category",
    y="age",
    color="sport_category",
    title="Age Spread per Discipline",
    category_orders={"sport_category": sorted_categories},  # <- important
    color_discrete_sequence=px.colors.sequential.Viridis,
    stripmode="overlay"
)
st.plotly_chart(fig4, use_container_width=True)

# --- 5. Violin Plot ---
st.subheader("🎻 Age Distribution (Violin Plot)")
fig5 = px.violin(
    filtered_df,
    x="sport_category",
    y="age",
    box=True,
    points="all",
    color="sport_category",
    category_orders={"sport_category": sorted_categories},  # <- important
    color_discrete_sequence=px.colors.sequential.Viridis
)

for i, category in enumerate(sorted_categories):
    median_val = median_ages[category]
    fig5.add_annotation(
        x=category,
        y=median_val,
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-30,  # Adjust as needed to place label nicely
        font=dict(color="black", size=12)
    )

st.plotly_chart(fig5, use_container_width=True)


