
# File 16: main.py - Complete Streamlit application
main_content = '''"""Main Streamlit application for Loan Evaluation System"""
import sys
import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Fix imports for Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import modules
try:
    from models.risk_analyzer import RiskAnalyzer
    from models.credit_scorer import CreditScorer
    from models.geolocation_analyzer import GeolocationAnalyzer
    from models.loan_recommender import LoanRecommender
    from data.data_processor import DataProcessor
    from data.validators import InputValidator
    from utils.helpers import format_currency, calculate_monthly_payment
    from config import APP_CONFIG, RISK_CATEGORIES, loan_config
    MODULES_LOADED = True
except ImportError as e:
    st.error(f"Import Error: {str(e)}")
    st.error("Please ensure all modules are in the correct directories")
    MODULES_LOADED = False

# Configure page
st.set_page_config(
    page_title="Loan Evaluation System",
    page_icon="🏦",
    layout="wide"
)

# Initialize session state
if 'applications' not in st.session_state:
    st.session_state.applications = []

def main():
    """Main application function"""
    
    st.title("🏦 Loan Evaluation System")
    st.markdown("*AI-powered loan approval prediction and risk assessment*")
    
    if not MODULES_LOADED:
        st.error("⚠️ Cannot load required modules. Please check file structure.")
        show_debug_info()
        return
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["🏠 Home", "📝 New Application", "📊 Analytics", "ℹ️ About"]
    )
    
    if page == "🏠 Home":
        show_home_page()
    elif page == "📝 New Application":
        show_application_form()
    elif page == "📊 Analytics":
        show_analytics()
    elif page == "ℹ️ About":
        show_about()

def show_home_page():
    """Display home page"""
    st.header("Welcome to Loan Evaluation System")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Applications", len(st.session_state.applications))
    
    with col2:
        approved = sum(1 for app in st.session_state.applications if app.get('approved', False))
        st.metric("Approved", approved)
    
    with col3:
        if st.session_state.applications:
            avg_amount = np.mean([app.get('loan_amount', 0) for app in st.session_state.applications])
            st.metric("Avg Loan Amount", format_currency(avg_amount))
        else:
            st.metric("Avg Loan Amount", "$0")
    
    st.markdown("---")
    
    st.subheader("🔍 System Features")
    features = [
        ("AI-Powered Risk Assessment", "Advanced algorithms analyze multiple risk factors"),
        ("Credit Score Analysis", "Comprehensive credit evaluation and scoring"),
        ("Geographic Risk Assessment", "Location-based economic risk analysis"),
        ("Loan Recommendations", "Personalized loan terms and amounts")
    ]
    
    for title, desc in features:
        st.success(f"**{title}**\\n{desc}")

def show_application_form():
    """Display loan application form"""
    st.header("📝 New Loan Application")
    
    with st.form("loan_application"):
        # Personal Information
        st.subheader("👤 Personal Information")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", min_value=18, max_value=100, value=30)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced", "Widowed"])
        
        with col2:
            education = st.selectbox("Education", ["High School", "Bachelor\\'s", "Master\\'s", "PhD", "Other"])
            employment_status = st.selectbox("Employment Status", ["Employed", "Self-Employed", "Unemployed", "Retired"])
        
        # Financial Information
        st.subheader("💰 Financial Information")
        col3, col4 = st.columns(2)
        
        with col3:
            annual_income = st.number_input("Annual Income ($)", min_value=0, value=50000)
            monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0, value=2000)
        
        with col4:
            existing_debts = st.number_input("Existing Debts ($)", min_value=0, value=5000)
        
        # Loan Information
        st.subheader("🏦 Loan Details")
        col5, col6 = st.columns(2)
        
        with col5:
            loan_amount = st.number_input("Requested Loan Amount ($)", min_value=1000, max_value=500000, value=25000)
            loan_purpose = st.selectbox("Loan Purpose", [
                "Home Purchase", "Home Improvement", "Auto Loan", "Personal Loan",
                "Business Loan", "Education", "Debt Consolidation", "Other"
            ])
        
        with col6:
            loan_term = st.number_input("Loan Term (months)", min_value=12, max_value=360, value=60)
            collateral_value = st.number_input("Collateral Value ($)", min_value=0, value=0)
        
        # Credit Information
        st.subheader("📊 Credit Information")
        col7, col8 = st.columns(2)
        
        with col7:
            credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
            credit_history_length = st.number_input("Credit History (years)", min_value=0, max_value=50, value=5)
        
        with col8:
            previous_defaults = st.number_input("Previous Defaults", min_value=0, max_value=10, value=0)
            current_loans = st.number_input("Current Loans", min_value=0, max_value=20, value=1)
        
        # Location Information
        st.subheader("📍 Location")
        col9, col10 = st.columns(2)
        
        with col9:
            state = st.text_input("State", value="California")
            city = st.text_input("City", value="Los Angeles")
        
        with col10:
            zip_code = st.text_input("ZIP Code", value="90210")
        
        # Submit button
        submitted = st.form_submit_button("🔍 Evaluate Application", use_container_width=True)
        
        if submitted:
            application_data = {
                'personal': {
                    'age': age, 'gender': gender, 'marital_status': marital_status,
                    'education': education, 'employment_status': employment_status
                },
                'financial': {
                    'annual_income': annual_income, 'monthly_expenses': monthly_expenses,
                    'existing_debts': existing_debts
                },
                'loan': {
                    'loan_amount': loan_amount, 'loan_purpose': loan_purpose,
                    'loan_term': loan_term, 'collateral_value': collateral_value
                },
                'credit': {
                    'credit_score': credit_score, 'credit_history_length': credit_history_length,
                    'previous_defaults': previous_defaults, 'current_loans': current_loans
                },
                'geolocation': {
                    'state': state, 'city': city, 'zip_code': zip_code
                }
            }
            
            process_application(application_data)

def process_application(data):
    """Process loan application"""
    st.success("✅ Application received! Processing...")
    
    try:
        with st.spinner("Analyzing application..."):
            # Initialize analyzers
            risk_analyzer = RiskAnalyzer()
            credit_scorer = CreditScorer()
            geo_analyzer = GeolocationAnalyzer()
            loan_recommender = LoanRecommender()
            
            # Perform analysis
            risk_score = risk_analyzer.calculate_risk_score(data)
            credit_analysis = credit_scorer.analyze_creditworthiness(data)
            geo_risk = geo_analyzer.assess_location_risk(data['geolocation'])
            recommendation = loan_recommender.recommend_loan_terms(data, risk_score)
            
            # Make decision
            approved = risk_score < 0.6 and credit_analysis.score > 600
            
            # Store result
            result = {
                'timestamp': datetime.now(),
                'loan_amount': data['loan']['loan_amount'],
                'risk_score': risk_score,
                'credit_score': credit_analysis.score,
                'approved': approved,
                'recommended_amount': recommendation.recommended_amount
            }
            st.session_state.applications.append(result)
            
            # Display results
            display_results(risk_score, credit_analysis, recommendation, approved)
    
    except Exception as e:
        st.error(f"Error processing application: {str(e)}")

def display_results(risk_score, credit_analysis, recommendation, approved):
    """Display application results"""
    st.markdown("---")
    st.header("📋 Application Results")
    
    # Decision banner
    if approved:
        st.success("🎉 **LOAN APPROVED!**")
    else:
        st.error("❌ **LOAN REJECTED**")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        risk_level = "LOW" if risk_score < 0.3 else "MEDIUM" if risk_score < 0.6 else "HIGH"
        st.metric("Risk Level", risk_level, f"{risk_score:.3f}")
    
    with col2:
        st.metric("Credit Score", credit_analysis.score)
    
    with col3:
        st.metric("Recommended Amount", format_currency(recommendation.recommended_amount))
    
    with col4:
        st.metric("Interest Rate", f"{recommendation.interest_rate:.2%}")
    
    # Detailed information
    with st.expander("📊 Detailed Analysis"):
        st.write("**Credit Grade:**", credit_analysis.grade)
        st.write("**Monthly Payment:**", format_currency(recommendation.monthly_payment))
        st.write("**Total Cost:**", format_currency(recommendation.total_cost))
        st.write("**Approval Probability:**", f"{recommendation.approval_probability:.1%}")

def show_analytics():
    """Display analytics dashboard"""
    st.header("📊 Analytics Dashboard")
    
    if not st.session_state.applications:
        st.info("No applications yet. Submit some applications to see analytics!")
        return
    
    df = pd.DataFrame(st.session_state.applications)
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Applications", len(df))
    
    with col2:
        approval_rate = df['approved'].mean()
        st.metric("Approval Rate", f"{approval_rate:.1%}")
    
    with col3:
        avg_risk = df['risk_score'].mean()
        st.metric("Avg Risk Score", f"{avg_risk:.3f}")
    
    with col4:
        avg_credit = df['credit_score'].mean()
        st.metric("Avg Credit Score", f"{avg_credit:.0f}")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.scatter(df, x='risk_score', y='approved', 
                         title='Approval by Risk Score',
                         color='approved')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.histogram(df, x='loan_amount', 
                           title='Loan Amount Distribution')
        st.plotly_chart(fig2, use_container_width=True)

def show_about():
    """Display about page"""
    st.header("ℹ️ About")
    
    st.markdown(f"""
    **Version:** {APP_CONFIG['version']}
    
    **Description:** {APP_CONFIG['description']}
    
    ### Features
    - AI-Powered Risk Assessment
    - Credit Score Analysis
    - Geographic Risk Evaluation
    - Loan Recommendations
    - Real-time Analytics
    
    ### Module Status
    - **Risk Analyzer:** {"✅" if MODULES_LOADED else "❌"}
    - **Credit Scorer:** {"✅" if MODULES_LOADED else "❌"}
    - **Geolocation Analyzer:** {"✅" if MODULES_LOADED else "❌"}
    - **Loan Recommender:** {"✅" if MODULES_LOADED else "❌"}
    """)

def show_debug_info():
    """Show debug information"""
    with st.expander("🔍 Debug Information"):
        st.code(f"""
Current Directory: {os.getcwd()}
Python Path: {sys.path[:3]}
Files in current directory: {os.listdir('.')}
        """)

if __name__ == "__main__":
    main()
'''

with open('loan_evaluation_system_complete/main.py', 'w') as f:
    f.write(main_content)

print("✅ Created main.py")
