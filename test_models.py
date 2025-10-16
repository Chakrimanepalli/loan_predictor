"""Unit tests for models"""
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
