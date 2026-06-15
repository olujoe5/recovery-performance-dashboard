
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16a34a,100:166534&height=200&section=header&text=Recovery%20Performance%20Dashboard&fontSize=34&fontColor=ffffff&fontAlignY=38&desc=Real-time%20KPI%20tracking%20for%20debt%20recovery%20operations&descAlignY=58&descSize=16" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualizations-119DFF?style=for-the-badge&logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

<br/>

> **Tracking ₦35M+ in outstanding receivables across 3 major estates | with automated KPI alerts, trend forecasting, and weekly variance reporting.**

</div>

---

## 🎯 The Problem

Recovery teams in real estate operations deal with hundreds of client accounts simultaneously. Tracking who has paid, who is overdue, and how much is still outstanding becomes a full-time job on its own. Spreadsheets break, emails get missed. Cash flow suffers.

**This dashboard eliminates that chaos.**

---

## 💡 What This Does

A lightweight, interactive recovery operations dashboard that:

-  Consolidates all outstanding client balances in one view
-  Tracks weekly recovery rate trends vs. targets
-  Flags high-risk accounts automatically
-  Calculates next-due dates and days overdue per client
-  Exports weekly performance reports with one click

---

## 📊 Key Metrics at a Glance

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Total Recovered | ₦35,319,139 | ₦28,100,000 | ▲ 25.7% |
| Recovery Rate | 68.4% | 54.2% | ▲ 14.2pp |
| Active Defaulters | 23 | 31 | ▼ 26% |
| Avg Days Overdue | 18 days | 24 days | ▼ 6 days |
| Accounts Escalated | 4 | 9 | ▼ 55% |

---

## 🏗️ Project Structure

```
recovery-performance-dashboard/
│
├── 📊 dashboard.py          # Main Streamlit app
├── 📁 data/
│   ├── accounts.csv         # Client account data (sample)
│   └── payments.csv         # Payment transaction log
├── 📁 utils/
│   ├── kpi_calculator.py    # Recovery rate & KPI logic
│   ├── alerts.py            # Auto-flag high-risk accounts
│   └── date_utils.py        # Due date & overdue calculations
├── 📁 reports/
│   └── weekly_export.py     # Auto-generate weekly PDF summary
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.11` | Core language |
| `Pandas` | Data cleaning, transformation, date logic |
| `Streamlit` | Interactive dashboard UI |
| `Plotly Express` | Recovery trend charts & bar graphs |
| `OpenPyXL` | Read/write Excel recovery sheets |
| `Schedule` | Automate weekly report generation |

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/olujoe5/recovery-performance-dashboard.git
cd recovery-performance-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the dashboard
streamlit run dashboard.py
```

Open your browser at `http://localhost:8501` — the dashboard loads instantly.

---

## 📈 Dashboard Features

```
┌──────────────────────────────────────────────────────────────────────┐
│  RECOVERY PERFORMANCE DASHBOARD                        Week 23       │
├──────────────┬──────────────┬────────────────────────────────────────┤
│   ₦35.3M     │    68.4%     │   23 Defaulters 🔴                    │
│  Recovered   │    Rate      │   Flagged                              │
├──────────────┴──────────────┴────────────────────────────────────────┤
│  Recovery Trend Chart — 12-week rolling                              │
│  ░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓████████                                       │
├──────────────────────────────┬───────────────────────────────────────┤
│ Estate Breakdown             │ Top Defaulters                        │
├──────────────────────────────┼───────────────────────────────────────┤
│ Shopping Mall   63%          │ Ahmad O.     ₦450,000                 │
│ Hemsford City   72%          │ James A.     ₦380,000                 │
│ Miles City      71%          │ Fatima B.    ₦310,000                 │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## 🔍 Key Insights From the Data

- **Shopping Mall** accounts for **63% of total outstanding receivables** — corner units show 2.3× higher default rates than regular units
- Clients in **months 4–6 of instalment plans** are the most likely to miss payments — early intervention at month 3 improves recovery rate by ~18%
- **Tuesday and Thursday** are the highest-performing collection days of the week

---

##  Context

This project was built from hands-on experience managing recovery operations in a legal/recovery department, tracking client accounts across multiple real estate estates. The data patterns and KPIs reflect real operational challenges.

---

<div align="center">

**Built with real operational experience**

[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/YOUR_PROFILE)
[![GitHub](https://img.shields.io/badge/Follow-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/olujoe5)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:166534,100:16a34a&height=100&section=footer" width="100%"/>

</div>
