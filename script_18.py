
# Create test files
test_models_content = '''"""Unit tests for models"""
import unittest
from models.risk_analyzer import RiskAnalyzer
from models.credit_scorer import CreditScorer
from models.geolocation_analyzer import GeolocationAnalyzer
from models.loan_recommender import LoanRecommender

class TestRiskAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = RiskAnalyzer()
        self.sample_data = {
            'personal': {'age': 35, 'employment_status': 'Employed'},
            'financial': {'annual_income': 75000, 'existing_debts': 15000},
            'credit': {'credit_score': 720, 'previous_defaults': 0},
            'geolocation': {'state': 'California', 'city': 'LA'}
        }
    
    def test_calculate_risk_score(self):
        risk_score = self.analyzer.calculate_risk_score(self.sample_data)
        self.assertIsInstance(risk_score, float)
        self.assertGreaterEqual(risk_score, 0.0)
        self.assertLessEqual(risk_score, 1.0)

if __name__ == '__main__':
    unittest.main()
'''

with open('loan_evaluation_system_complete/tests/test_models.py', 'w') as f:
    f.write(test_models_content)

test_data_content = '''"""Unit tests for data processing"""
import unittest
from data.data_processor import DataProcessor
from data.validators import InputValidator

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()
    
    def test_process_application(self):
        raw_data = {
            'personal': {'age': '35'},
            'financial': {'annual_income': '75000'},
            'loan': {'loan_amount': '25000'},
            'credit': {'credit_score': '720'},
            'geolocation': {'state': 'CA'}
        }
        result = self.processor.process_application(raw_data)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
'''

with open('loan_evaluation_system_complete/tests/test_data.py', 'w') as f:
    f.write(test_data_content)

print("✅ Created test files")
