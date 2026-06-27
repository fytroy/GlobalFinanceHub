import streamlit as st

# Configure global page properties across the app
st.set_page_config(
    page_title="Global Market Intelligence Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the structural page navigation mapping
pages = {
    "Executive Suite": [
        st.Page("views/overview.py", title="🏠 Executive Overview", default=True),
    ],
    "Data Desk": [
        st.Page("views/summary.py", title="📊 Analytical Summary"),
    ]
}

# Initialize navigation engine
pg = st.navigation(pages)

# Execute the routed page view
pg.run()