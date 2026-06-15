"""
Recovery Performance Dashboard
================================
Run: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

st.set_page_config(
    page_title="Recovery Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Synthetic but realistic data ──────────────────────────────────────────────
random.seed(42)
estates = ["Shopping Mall", "Hemsford City", "MKH City"]

def generate_accounts():
    names = [
        "Ahmad Olowookere","Fatima Bello","James Adeyemi","Chioma Okafor",
        "Emeka Nwosu","Grace Lawal","Tunde Fashola","Amina Suleiman",
        "Biodun Obi","Kelvin Eze","Sandra Okonkwo","Patrick Adeleke"
    ]
    rows = []
    for i, name in enumerate(names):
        estate = estates[i % 3]
        total = random.randint(500_000, 5_000_000)
        paid = random.randint(0, total)
        overdue = random.randint(0, 90)
        rows.append({
            "Client": name, "Estate": estate,
            "Total (₦)": total, "Paid (₦)": paid,
            "Outstanding (₦)": total - paid,
            "Days Overdue": overdue,
            "Risk": "🔴 High" if overdue > 45 else ("🟡 Medium" if overdue > 20 else "🟢 Low")
        })
    return pd.DataFrame(rows)

def generate_weekly_trend():
    weeks = [f"W{i}" for i in range(1, 13)]
    rates = [42, 45, 48, 44, 51, 55, 53, 58, 62, 60, 65, 68]
    targets = [60] * 12
    return pd.DataFrame({"Week": weeks, "Recovery Rate (%)": rates, "Target (%)": targets})

df = generate_accounts()
trend_df = generate_weekly_trend()

# ── Sidebar ───────────────────────────────────────────────────────────────────
st.sidebar.image("https://img.shields.io/badge/Recovery-Dashboard-16a34a?style=for-the-badge", use_column_width=True)
st.sidebar.markdown("### 🔍 Filters")
selected_estate = st.sidebar.multiselect("Estate", estates, default=estates)
risk_filter = st.sidebar.multiselect("Risk Level", ["🔴 High", "🟡 Medium", "🟢 Low"], default=["🔴 High", "🟡 Medium", "🟢 Low"])

filtered = df[df["Estate"].isin(selected_estate) & df["Risk"].isin(risk_filter)]

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("## 📊 Recovery Performance Dashboard")
st.markdown(f"*Last updated: {datetime.now().strftime('%d %B %Y, %H:%M')}*")
st.divider()

# ── KPI Cards ─────────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
total_outstanding = filtered["Outstanding (₦)"].sum()
total_paid = filtered["Paid (₦)"].sum()
recovery_rate = (total_paid / (total_paid + total_outstanding)) * 100 if (total_paid + total_outstanding) > 0 else 0
high_risk_count = len(filtered[filtered["Risk"] == "🔴 High"])

col1.metric("💰 Total Recovered", f"₦{total_paid:,.0f}", delta="▲ 25.7% vs last week")
col2.metric("📈 Recovery Rate", f"{recovery_rate:.1f}%", delta="▲ 14.2pp vs last week")
col3.metric("⚠️ High Risk Accounts", high_risk_count, delta=f"-{9 - high_risk_count} vs last week", delta_color="inverse")
col4.metric("📋 Active Accounts", len(filtered), delta=None)

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("#### 📈 12-Week Recovery Rate Trend")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trend_df["Week"], y=trend_df["Recovery Rate (%)"],
                             mode="lines+markers", name="Actual", line=dict(color="#16a34a", width=3)))
    fig.add_trace(go.Scatter(x=trend_df["Week"], y=trend_df["Target (%)"],
                             mode="lines", name="Target", line=dict(color="#dc2626", width=2, dash="dash")))
    fig.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0),
                      plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown("#### 🏢 Outstanding by Estate")
    estate_summary = filtered.groupby("Estate")["Outstanding (₦)"].sum().reset_index()
    fig2 = px.pie(estate_summary, values="Outstanding (₦)", names="Estate",
                  color_discrete_sequence=["#16a34a", "#166534", "#4ade80"])
    fig2.update_layout(height=300, margin=dict(l=0, r=0, t=10, b=0),
                       paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig2, use_container_width=True)

# ── Account Table ─────────────────────────────────────────────────────────────
st.markdown("#### 👥 Client Account Overview")
display_df = filtered[["Client", "Estate", "Outstanding (₦)", "Days Overdue", "Risk"]].sort_values(
    "Outstanding (₦)", ascending=False
)
display_df["Outstanding (₦)"] = display_df["Outstanding (₦)"].apply(lambda x: f"₦{x:,.0f}")
st.dataframe(display_df, use_container_width=True, hide_index=True)
