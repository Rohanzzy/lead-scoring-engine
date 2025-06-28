# Lead Scoring Engine

This project builds a simple rule-based lead scoring system to prioritize outbound leads based on their job title and personalization score.

---

## Problem Statement

Sales and growth teams often handle hundreds or thousands of outbound leads. Identifying which leads are most valuable to contact first can improve conversion rates and team efficiency.

---

## What This Project Does

- Generates a synthetic dataset of 1,000 outbound leads
- Builds a rule-based scoring function that assigns scores based on:
  - Job Title (higher scores for C-level roles like CEO, CTO)
  - Personalization Score (emails with higher personalization get extra points)
- Outputs the top-scoring leads to prioritize outreach

---

## Dataset Overview

The dataset simulates typical cold outreach data with the following columns:

| Column | Description |
|--------|-------------|
| lead_id | Unique identifier for each lead |
| job_title | Title of the lead (CEO, CTO, VP Sales, etc) |
| company_size | Company size category (Small, Medium, Large) |
| industry | Industry sector (SaaS, Fintech, etc) |
| location | Geography (US, India, Europe) |
| personalization_score | Level of personalization in email (1-10) |
| subject_length | Length of email subject line in words |
| day_sent | Day of the week email was sent |
| followups_sent | Number of follow-ups sent |
| replied | Whether the lead replied (1) or not (0); this is the target column |

---

## How the Scoring Works

1. Job Title Weighting
   - CEO, CTO: +30 points
   - VP Sales: +20 points
   - Marketing Manager: +15 points
   - Others: +10 points

2. Personalization Score
   - Each personalization point adds +3 to the score

3. Final Score
   - Sum of job title weight and personalization impact

---

## Why This Matters

Companies like Clay.com build tools to enrich, deduplicate, and prioritize leads. This project demonstrates:

- Domain understanding of outbound sales
- Ability to build a practical scoring algorithm without machine learning
- How simple business logic can drive immediate value

---

## Next Steps

- Integrate with Streamlit to create an interactive lead scoring app
- Expand the scoring function to include:
  - Industry weightings
  - Day sent impact
  - Follow-up penalties

---

## Project Files

| File | Description |
|------|-------------|
| lead_scoring.ipynb | Jupyter notebook with code, EDA, and scoring function |
| README.md | This project documentation |

---

## Author

Rohan Pathak  
Growth & Data Science Learner | Focused on Outbound Tools & GTM Automation

---

### Connect with Me

- LinkedIn - https://www.linkedin.com/in/pathakrohan/
- GitHub - https://github.com/Rohanzzy

---

