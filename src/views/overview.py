import streamlit as st
import pandas as pd
import sys
import os

# Align path resolution to import the core engine components
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from engine import execute_analytical_query

st.title("💼 Executive Macroeconomic & FX Analytics Portal")
st.markdown("Enterprise OLAP data warehouse interface serving calculated volatility trends.")
st.divider()

@st.cache_data
def load_warehouse_analytics():
    return execute_analytical_query()

df = load_warehouse_analytics()

# Filter data dynamically to represent the latest full performance period (2024)
df_2024 = df[df['year'] == 2024]

st.subheader("📊 2024 Key Performance Indicators (Star Schema Extract)")

cols = st.columns(len(df_2024))
for idx, (_, row) in enumerate(df_2024.iterrows()):
    with cols[idx]:
        st.markdown(f"### {row['country']}")
        
        # Color code the metric based on calculated net currency movement vectors
        volatility = row['fx_yoy_volatility_pct']
        delta_label = f"{row['fx_net_change']:.3f} ({volatility:.2f}% YoY)"
        
        st.metric(
            label="Avg FX Rate (vs USD)",
            value=f"{row['fx_rate']:.2f}",
            delta=delta_label,
            delta_color="inverse" if volatility > 0 else "normal"
        )
        
        st.metric(
            label="Real GDP Growth",
            value=f"{row['gdp_growth_pct']:.2f}%" if pd.notna(row['gdp_growth_pct']) else "N/A"
        )
        
        st.metric(
            label="Consumer Price Inflation",
            value=f"{row['inflation_rate_pct']:.2f}%" if pd.notna(row['inflation_rate_pct']) else "N/A"
        )
        st.divider()

# =====================================================================
# 📈 ADVANCED VISUALIZATION MATRIX
# =====================================================================
st.subheader("📉 Calculated Currency Volatility Trends (% Change YoY)")
volatility_pivot = df.pivot(index='year', columns='country', values='fx_yoy_volatility_pct').dropna(how='all')
st.line_chart(volatility_pivot)