
# File 8: utils/helpers.py - Fixed version
helpers_content = '''"""Helper functions for loan evaluation system"""
import numpy as np

def format_currency(amount):
    """Format amount as currency"""
    try:
        return f"${amount:,.2f}"
    except:
        return "$0.00"

def calculate_monthly_payment(principal, annual_rate, term_months):
    """Calculate monthly loan payment"""
    try:
        if annual_rate <= 0:
            return principal / term_months if term_months > 0 else 0
        
        monthly_rate = annual_rate / 12
        if monthly_rate <= 0 or term_months <= 0:
            return 0
        
        payment = principal * (monthly_rate * (1 + monthly_rate) ** term_months) / ((1 + monthly_rate) ** term_months - 1)
        return payment
    except:
        return 0.0

def safe_float_conversion(value, default=0.0):
    """Safely convert value to float"""
    if value is None:
        return default
    try:
        return float(value)
    except:
        return default

def calculate_debt_to_income_ratio(monthly_debt, monthly_income):
    """Calculate debt-to-income ratio"""
    try:
        if monthly_income <= 0:
            return float('inf')
        return monthly_debt / monthly_income
    except:
        return 0.0
'''

with open('loan_evaluation_system_complete/utils/helpers.py', 'w') as f:
    f.write(helpers_content)

print("✅ Created utils/helpers.py")
