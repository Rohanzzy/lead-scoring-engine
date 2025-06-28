import streamlit as st
import pandas as pd

df = pd.read_csv('lead_data.csv')

# Define scoring function
def score_lead(row):
    score = 0
    if row['job_title'] in ['CEO', 'CTO']:
        score += 30
    elif row['job_title'] == 'VP Sales':
        score += 20
    elif row['job_title'] == 'Marketing Manager':
        score += 15
    else:
        score += 10
    score += row['personalization_score'] * 3
    return score

df['lead_score'] = df.apply(score_lead, axis=1)

# Streamlit App
st.title("Lead Scoring Engine")

st.write("### Filter Leads")

# Filter by job title
job_titles = df['job_title'].unique()
selected_job = st.selectbox("Select Job Title", options=['All'] + list(job_titles))

# Filter by minimum score
min_score = st.slider("Minimum Lead Score", min_value=int(df['lead_score'].min()), max_value=int(df['lead_score'].max()), value=10)

# Apply filters
filtered_df = df.copy()
if selected_job != 'All':
    filtered_df = filtered_df[filtered_df['job_title'] == selected_job]

filtered_df = filtered_df[filtered_df['lead_score'] >= min_score]

# Show filtered dataframe
st.write(f"### Showing {len(filtered_df)} leads")
st.dataframe(filtered_df[['lead_id', 'job_title', 'personalization_score', 'lead_score']].sort_values('lead_score', ascending=False))

# Download button for full data
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV of Filtered Leads", data=csv, file_name="filtered_leads.csv", mime='text/csv')
