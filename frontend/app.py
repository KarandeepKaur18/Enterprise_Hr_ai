import streamlit as st
import requests
import pandas as pd

# Tech magic: Advanced page configuration
st.set_page_config(page_title="Agentic HRMS", layout="wide", initial_sidebar_state="expanded")

# --- SIDEBAR ---
st.sidebar.title("⚙️ HR Platform")
st.sidebar.info("Enterprise Workforce Intelligence")
st.sidebar.markdown("---")
st.sidebar.text("Version: 1.0.0 MVP")
st.sidebar.text("Status: API Online 🟢")

# --- MAIN HEADER ---
st.title("🤖 AI Workforce Intelligence Platform")
st.markdown("Monitor attrition risks, skill gaps, and employee engagement in real-time.")
st.markdown("---")

# --- INTERACTIVE TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Dashboard Overview", "⚠️ Skill Gaps", "🔮 Risk Predictor"])

with tab1:
    API_URL = "http://127.0.0.1:8000/dashboard/summary"
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            
            # Upgraded KPI Cards with trend indicators (deltas)
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Employees", data["total_employees"], delta="Stable")
            col2.metric("High Risk Employees", data["high_risk_employees"], delta="-5 this month", delta_color="inverse")
            col3.metric("Avg Engagement", f"{data['average_engagement']}%", delta="+2% vs last quarter")
        else:
            st.error("API returned an error.")
    except Exception as e:
        st.error("Could not connect to the FastAPI backend. Is it running?")

with tab2:
    colA, colB = st.columns(2)
    
    gap_data = pd.DataFrame({
        "Skill": ["MLOps", "Cloud", "Generative AI", "Python"],
        "Missing_Count": [120, 75, 30, 15]
    })
    
    with colA:
        st.subheader("Critical Organization Gaps")
        # Visual styling for the dataframe
        st.dataframe(gap_data.style.background_gradient(cmap="Reds"), use_container_width=True)
        
    with colB:
        st.subheader("Skill Gap Distribution")
        # Native Streamlit bar chart!
        st.bar_chart(gap_data.set_index("Skill"))

with tab3:
    st.subheader("Actionable Recommendations")
    
    # Expanders for clean UI organization
    with st.expander("View Employee 101 Details", expanded=True):
        st.warning("**Risk Level:** HIGH (82% Attrition Probability)")
        st.info("**Action:** Needs MLOps Training ➔ Recommend: 'Deploying and Monitoring ML Systems'")
        
    with st.expander("View Employee 102 Details"):
        st.success("**Risk Level:** LOW (12% Attrition Probability)")
        st.info("**Action:** Needs AWS Training ➔ Recommend: 'AWS Cloud Practitioner Essentials'")