# Lead Scoring Engine

In this project, I built a simple rule-based lead scoring system to help prioritize outbound leads based on their job title and how personalized the outreach was.

## Problem Statement

Sales and growth teams often deal with hundreds or thousands of leads at once. Figuring out which leads are worth reaching out to first can save time and boost conversion rates.

## What This Project Does

✅ Creates a fake dataset of 1,000 outbound leads to work with  
✅ Builds a scoring function that gives each lead a score based on:
- **Job Title** – giving higher points to decision-makers like CEOs and CTOs
- **Personalization Score** – adding extra points if the outreach was more personalized

✅ Shows the top-scoring leads so outreach efforts can focus on them first

---

## Dataset Overview

Here’s what the dataset looks like:

| Column               | Description                                     |
|-----------------------|------------------------------------------------|
| `lead_id`            | Unique ID for each lead                       |
| `job_title`          | The person’s job title (e.g. CEO, CTO, VP Sales) |
| `company_size`       | Size category of the company (Small, Medium, Large) |
| `industry`           | Industry sector (SaaS, Fintech, etc.)          |
| `location`           | Country or region (US, India, Europe)          |
| `personalization_score` | How personalized the email was (scale of 1–10) |
| `subject_length`     | Number of words in the email subject line      |
| `day_sent`           | Day of the week the email was sent             |
| `followups_sent`     | Number of follow-up emails sent                |
| `replied`            | Whether the lead replied (1) or didn’t (0) – this is the target column |

---

## How the Scoring Works

### Job Title Weighting

- CEO, CTO: **+30 points**
- VP Sales: **+20 points**
- Marketing Manager: **+15 points**
- Others: **+10 points**

### Personalization Score

- Each personalization point adds **+3 to the score**

### Final Score

The total is calculated by adding the **job title weight** and **personalization impact**.

---

## Why This Matters

Tools like [Clay.com](https://clay.com) help sales teams enrich, clean, and prioritize their leads. This project shows how basic scoring logic can already make a big difference before adding complex machine learning models.

---

## Next Steps

Here’s what I plan to add next:

- Turn this into a small **Streamlit app** so anyone can score leads interactively
- Make the scoring logic smarter by including:
  - Industry-based scoring
  - Day sent impact
  - Follow-up penalties or bonuses

---

## Project Files

| File                | Description                                         |
|---------------------|-----------------------------------------------------|
| `lead_scoring.ipynb` | The Jupyter notebook with all code, data generation, and analysis |
| `README.md`         | This project description file                      |

---

## About Me

I’m **Rohan Pathak**. I work in Growth and am learning Data Science, focusing on outbound tools and GTM automation. I have more than a year of experience working as Head of Growrh in high growth YC-backed company where I was responsible for customer retention, customer LTV increase and overseeing data of customers to help make data driven decisions. I want to take this experience and dive into the world of data science and help companies improve their decision making with data and increase ROI. 

### Connect with Me

- My LinkedIn - https://www.linkedin.com/in/pathakrohan/
- My Github - https://github.com/Rohanzzy

---
