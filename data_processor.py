"""Data processing for loan evaluation system"""
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    """Data preprocessing system"""

    def __init__(self):
        self.processed_applications = []

    def process_application(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process raw application data"""
        try:
            # Clean and standardize data
            processed_data = self._clean_data(raw_data)

            # Add derived metrics
            processed_data = self._add_derived_metrics(processed_data)

            self.processed_applications.append(processed_data)
            return processed_data

        except Exception as e:
            logger.error(f"Error processing application: {str(e)}")
            return raw_data

    def _clean_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and standardize input data"""
        cleaned = {}

        for section, values in data.items():
            if isinstance(values, dict):
                cleaned[section] = {}
                for key, value in values.items():
                    # Convert strings to proper types
                    if isinstance(value, str):
                        try:
                            # Try to convert to float
                            cleaned[section][key] = float(value.replace(',', '').replace('$', ''))
                        except:
                            cleaned[section][key] = value
                    else:
                        cleaned[section][key] = value
            else:
                cleaned[section] = values

        return cleaned

    def _add_derived_metrics(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Add derived financial metrics"""
        data['derived_metrics'] = {}

        if 'financial' in data:
            financial = data['financial']
            annual_income = financial.get('annual_income', 0)
            monthly_expenses = financial.get('monthly_expenses', 0)
            existing_debts = financial.get('existing_debts', 0)

            # Calculate derived metrics
            data['derived_metrics']['monthly_income'] = annual_income / 12 if annual_income > 0 else 0
            data['derived_metrics']['debt_to_income'] = existing_debts / annual_income if annual_income > 0 else 0
            data['derived_metrics']['expense_ratio'] = (monthly_expenses * 12) / annual_income if annual_income > 0 else 0

        return data
