
# File 5: utils/__init__.py
utils_init = """\"\"\"Utils module for loan evaluation system\"\"\"
from .helpers import format_currency, calculate_monthly_payment
from .constants import LOAN_PURPOSES, RISK_CATEGORIES

__all__ = ['format_currency', 'calculate_monthly_payment', 'LOAN_PURPOSES', 'RISK_CATEGORIES']
"""

with open('loan_evaluation_system_complete/utils/__init__.py', 'w') as f:
    f.write(utils_init)

print("✅ Created utils/__init__.py")
