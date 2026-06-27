import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from engine import execute_analytical_query

st.title("🔬 Advanced Data Desk & SQL Auditing")
st.markdown("Granular evaluation of calculated database window functions and analytical dimensions.")
st.divider()

@st.cache_data
def load_warehouse_analytics():
    return execute_analytical_query()

df = load_warehouse_analytics()

# =====================================================================
# 🔍 INTERACTIVE COUNTRY DEEP-DIVE
# =====================================================================
st.subheader("🗺️ Country Variance Ledger")
countries = df['country'].unique()
selected_country = st.selectbox("Isolate market dimension for audit:", countries)

# Slice and order data cleanly
country_df = df[df['country'] == selected_country].sort_values(by='year', ascending=False)

# Format column names for enterprise dashboard standard
display_df = country_df.rename(columns={
    "year": "Reporting Year",
    "fx_rate": "Exchange Rate (Base USD)",
    "fx_net_change": "Net Currency Change",
    "fx_yoy_volatility_pct": "YoY Volatility (%)",
    "gdp_growth_pct": "GDP Growth Rate (%)",
    "inflation_rate_pct": "CPI Inflation Rate (%)"
}).drop(columns=['country'])

st.dataframe(display_df, use_container_width=True, hide_index=True)

# =====================================================================
# 📊 WAREHOUSE HEALTH AUDIT TRAIL
# =====================================================================
st.divider()
st.subheader("📦 Comprehensive Warehouse Extract")
st.markdown("Raw analytical dataframe output retrieved via localized DuckDB connection mapping.")
st.dataframe(df, use_container_width=True)

# CSV Export portal link
csv_data = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Engineered Warehouse Extract (CSV)",
    data=csv_data,
    file_name="macro_warehouse_analytics_extract.csv",
    mime="text/csv"
)