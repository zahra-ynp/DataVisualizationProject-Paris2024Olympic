# 🏅 Paris 2024 Athlete Age Analysis

This Streamlit data visualization app explores the age distribution of athletes participating in the **Paris 2024 Summer Olympic Games**, categorized by custom-defined sport categories.

## 📊 Overview

Using data sourced from Kaggle, the app provides multiple interactive visualizations to help understand:

- How age is distributed across different Olympic sport categories
- Differences in age ranges by sport
- Athlete counts by sport
- Gender-specific filtering of age distributions

## 📁 Dataset

- **Source:** [Paris 2024 Olympic Summer Games - Kaggle Dataset](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games)
- **File Used:** `athletes.csv`
- **Note:** The dataset includes detailed biographical and sports information for Olympic athletes.

## 📌 Features

- **Custom Sport Categories**: Disciplines are grouped into meaningful categories such as "Combat Sports", "Aquatics", "Ball Sports", etc.
- **Interactive Filtering**: Filter by sport category and gender.
- **Visualizations**:
  - Histogram of age distribution
  - Box plot of age range
  - Bar chart of athlete counts
  - Scatter plot (strip) showing age spread
  - Violin plot with median age annotations

## 📦 Dependencies

To run this project, you’ll need the following Python packages:

```bash
pip install streamlit pandas plotly

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/zahra-ynp/DataVisualizationProject-Paris2024Olympic.git
cd paris2024-age-analysis

### 2. Download the Dataset
Download athletes.csv from the Kaggle dataset and place it in the root of your project directory.

### 3. Install the Dependencies
pip install streamlit pandas plotly

### 4. Run the App
streamlit run app.py

## 🧠 Author Notes
- Sport categories were self-defined for clearer comparative analysis.
- Ages are calculated based on birth dates relative to the Paris 2024 opening date (July 26, 2024).
- Only valid entries with complete birth dates and sport categories were considered in the analysis.
