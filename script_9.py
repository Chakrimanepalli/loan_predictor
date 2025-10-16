
# File 9: utils/constants.py
constants_content = '''"""Constants for loan evaluation system"""

# Loan purposes
LOAN_PURPOSES = [
    'Home Purchase',
    'Home Improvement',
    'Auto Loan',
    'Personal Loan',
    'Business Loan',
    'Education',
    'Debt Consolidation',
    'Other'
]

# Employment types
EMPLOYMENT_TYPES = ['Employed', 'Self-Employed', 'Unemployed', 'Retired']

# Education levels
EDUCATION_LEVELS = ['High School', "Bachelor's", "Master's", 'PhD', 'Other']

# Marital statuses
MARITAL_STATUSES = ['Single', 'Married', 'Divorced', 'Widowed']

# Risk categories (duplicate from config for easy access)
RISK_CATEGORIES = {
    'VERY_LOW': {'score_range': (0.0, 0.2), 'color': 'green'},
    'LOW': {'score_range': (0.2, 0.4), 'color': 'lightgreen'},
    'MEDIUM': {'score_range': (0.4, 0.6), 'color': 'yellow'},
    'HIGH': {'score_range': (0.6, 0.8), 'color': 'orange'},
    'VERY_HIGH': {'score_range': (0.8, 1.0), 'color': 'red'}
}
'''

with open('loan_evaluation_system_complete/utils/constants.py', 'w') as f:
    f.write(constants_content)

print("✅ Created utils/constants.py")
