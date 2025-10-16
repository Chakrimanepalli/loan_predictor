
# File 7: config.py - Simple version without syntax errors
config_content = '''"""Configuration settings for the Loan Evaluation System"""

class LoanConfig:
    """Loan configuration settings"""
    min_loan_amount = 1000.0
    max_loan_amount = 500000.0
    min_loan_term = 12
    max_loan_term = 360
    default_interest_rate = 0.08

class RiskConfig:
    """Risk assessment configuration"""
    low_risk_threshold = 0.3
    medium_risk_threshold = 0.7
    high_risk_threshold = 1.0
    approval_threshold = 0.6

class CreditConfig:
    """Credit scoring configuration"""
    min_credit_score = 300
    max_credit_score = 850

# Application configuration
APP_CONFIG = {
    'title': "Loan Evaluation System",
    'version': "1.0.0",
    'description': "AI-powered loan approval prediction and risk assessment system",
    'author': "Data Science Team"
}

# Risk categories
RISK_CATEGORIES = {
    'VERY_LOW': {'score_range': (0.0, 0.2), 'color': 'green', 'approval_rate': 0.95},
    'LOW': {'score_range': (0.2, 0.4), 'color': 'lightgreen', 'approval_rate': 0.85},
    'MEDIUM': {'score_range': (0.4, 0.6), 'color': 'yellow', 'approval_rate': 0.65},
    'HIGH': {'score_range': (0.6, 0.8), 'color': 'orange', 'approval_rate': 0.35},
    'VERY_HIGH': {'score_range': (0.8, 1.0), 'color': 'red', 'approval_rate': 0.10}
}

# Feature columns
FEATURE_COLUMNS = {
    'personal': ['age', 'gender', 'marital_status', 'education', 'employment_status'],
    'financial': ['annual_income', 'monthly_expenses', 'existing_debts'],
    'loan': ['loan_amount', 'loan_purpose', 'loan_term', 'collateral_value'],
    'credit': ['credit_score', 'credit_history_length', 'previous_defaults', 'current_loans'],
    'geolocation': ['state', 'city', 'zip_code']
}

# Initialize configuration objects
loan_config = LoanConfig()
risk_config = RiskConfig()
credit_config = CreditConfig()
'''

with open('loan_evaluation_system_complete/config.py', 'w') as f:
    f.write(config_content)

print("✅ Created config.py")
