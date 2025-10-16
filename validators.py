"""Input validation for loan evaluation system"""
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class ValidationResult:
    """Result of data validation"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    score: float = 1.0

class InputValidator:
    """Input validation system"""

    def __init__(self):
        self.required_fields = {
            'personal': ['age', 'employment_status'],
            'financial': ['annual_income'],
            'loan': ['loan_amount', 'loan_purpose'],
            'credit': ['credit_score'],
            'geolocation': ['state', 'city']
        }

    def validate_application_data(self, application_data: Dict[str, Any]) -> ValidationResult:
        """Validate complete application data"""
        errors = []
        warnings = []

        # Check required sections
        required_sections = ['personal', 'financial', 'loan', 'credit', 'geolocation']
        for section in required_sections:
            if section not in application_data:
                errors.append(f"Missing required section: {section}")

        # Check required fields in each section
        for section, fields in self.required_fields.items():
            if section in application_data:
                for field in fields:
                    if field not in application_data[section]:
                        errors.append(f"Missing required field: {section}.{field}")

        # Validate numeric ranges
        if 'personal' in application_data:
            age = application_data['personal'].get('age')
            if age and (age < 18 or age > 100):
                errors.append("Age must be between 18 and 100")

        if 'credit' in application_data:
            credit_score = application_data['credit'].get('credit_score')
            if credit_score and (credit_score < 300 or credit_score > 850):
                errors.append("Credit score must be between 300 and 850")

        is_valid = len(errors) == 0
        score = 1.0 if is_valid else 0.0

        return ValidationResult(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
            score=score
        )
