# Lead Scoring Engine

In this project, I built a **simple rule-based lead scoring system** to help prioritize outbound leads based on their job title and how personalized the outreach was.

---

## Problem Statement

Sales and growth teams often deal with hundreds or thousands of leads at once. Figuring out which leads are worth reaching out to first can save time and boost conversion rates.

---

## What This Project Does

- Creates a **fake dataset of 1,000 outbound leads** to work with  
- Builds a **scoring function** that gives each lead a score based on:
  - **Job Title** – higher points to decision-makers like CEOs and CTOs
  - **Personalization Score** – extra points for more personalized outreach
- Displays leads with filters to prioritize outreach efficiently
- Allows **downloading scored data for team use**

---

## Dataset Overview

| Column                 | Description                                         |
|-------------------------|-----------------------------------------------------|
| `lead_id`              | Unique ID for each lead                             |
| `job_title`            | The person’s job title (e.g. CEO, CTO, VP Sales)    |
| `company_size`         | Size category of the company (Small, Medium, Large) |
| `industry`             | Industry sector (SaaS, Fintech, etc.)               |
| `location`             | Country or region (US, India, Europe)               |
| `personalization_score`| How personalized the email was (scale of 1–10)      |
| `subject_length`       | Number of words in the email subject line           |
| `day_sent`             | Day of the week the email was sent                  |
| `followups_sent`       | Number of follow-up emails sent                     |
| `replied`              | Whether the lead replied (1) or didn’t (0) – target column |

---

## How the Scoring Works

### **Job Title Weighting**

- CEO, CTO: **+30 points**
- VP Sales: **+20 points**
- Marketing Manager: **+15 points**
- Others: **+10 points**

### **Personalization Score Impact**

- Each personalization point adds **+3 to the score**

---

### **Final Score Calculation**

The **total score** is calculated by adding:

✅ Job Title Weight  
✅ Personalization Score Impact

---

## Why This Matters

Tools like [Clay.com](https://clay.com) help sales teams **enrich, clean, and prioritize leads**. This project demonstrates how **simple scoring logic** can already make a big difference before introducing machine learning models.

---

## Live Streamlit App

Try out the interactive app here:

👉 [Streamlit Lead Scoring App] https://lead-scoring-engine-rnbn7q3ugacx9nbnc3ra9f.streamlit.app/

---

## 🛠️ Next Steps

Here’s what I plan to add next:

- Make the scoring logic smarter by including:
  - Industry-based scoring
  - Day sent impact
  - Follow-up penalties or bonuses
- Explore ML models to **predict likelihood of reply** for each lead

---

## 📁 Project Files

| File            | Description                                         |
|-----------------|-----------------------------------------------------|
| `app.py`        | Streamlit app script for deployment                 |
| `lead_data.csv` | Synthetic dataset generated for the project         |
| `README.md`     | This project description file                      |

---

## 👤 About Me

I’m **Rohan Pathak**, currently working as Head of Growth at Persana AI, a high-growth YC-backed company, where I focus on customer retention, increasing LTV, and data-driven decision making. I am now learning Data Science to help companies improve decisions and increase ROI with data.

---

### 📬 Connect with Me

- [LinkedIn](https://www.linkedin.com/in/pathakrohan/)
- [GitHub](https://github.com/Rohanzzy)

---
