"""Unit tests for data processing"""
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
