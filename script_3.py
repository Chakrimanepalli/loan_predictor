
# File 3: models/__init__.py
models_init = """\"\"\"Models module for loan evaluation system\"\"\"
from .risk_analyzer import RiskAnalyzer
from .credit_scorer import CreditScorer
from .geolocation_analyzer import GeolocationAnalyzer
from .loan_recommender import LoanRecommender

__all__ = ['RiskAnalyzer', 'CreditScorer', 'GeolocationAnalyzer', 'LoanRecommender']
"""

with open('loan_evaluation_system_complete/models/__init__.py', 'w') as f:
    f.write(models_init)

print("✅ Created models/__init__.py")
