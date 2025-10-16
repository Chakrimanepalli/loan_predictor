"""Risk analysis module for loan evaluation"""
import numpy as np
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class RiskAssessment:
    """Risk assessment results"""
    risk_score: float
    risk_category: str
    contributing_factors: Dict[str, float]
    confidence: float
    recommendation: str

class RiskAnalyzer:
    """Risk assessment system"""

    def __init__(self):
        self.is_trained = False

    def calculate_risk_score(self, application_data: Dict[str, Any]) -> float:
        """Calculate risk score for loan application"""
        try:
            risk_factors = []

            # Financial risk
            financial = application_data.get('financial', {})
            annual_income = financial.get('annual_income', 0)
            existing_debts = financial.get('existing_debts', 0)

            if annual_income > 0:
                debt_ratio = existing_debts / annual_income
                if debt_ratio > 0.5:
                    risk_factors.append(0.4)
                elif debt_ratio > 0.3:
                    risk_factors.append(0.25)
                else:
                    risk_factors.append(0.1)
            else:
                risk_factors.append(0.6)

            # Credit risk
            credit = application_data.get('credit', {})
            credit_score = credit.get('credit_score', 600)
            if credit_score < 500:
                risk_factors.append(0.5)
            elif credit_score < 650:
                risk_factors.append(0.35)
            elif credit_score < 750:
                risk_factors.append(0.2)
            else:
                risk_factors.append(0.1)

            # Employment risk
            personal = application_data.get('personal', {})
            employment_status = personal.get('employment_status', '')
            if employment_status == 'Unemployed':
                risk_factors.append(0.6)
            elif employment_status == 'Self-Employed':
                risk_factors.append(0.3)
            else:
                risk_factors.append(0.1)

            # Calculate average risk score
            risk_score = np.mean(risk_factors) if risk_factors else 0.5
            return np.clip(risk_score, 0.0, 1.0)

        except Exception as e:
            return 0.5

    def assess_comprehensive_risk(self, application_data: Dict[str, Any]) -> RiskAssessment:
        """Perform comprehensive risk assessment"""
        risk_score = self.calculate_risk_score(application_data)

        # Determine risk category
        if risk_score < 0.3:
            risk_category = "LOW"
        elif risk_score < 0.6:
            risk_category = "MEDIUM"
        else:
            risk_category = "HIGH"

        # Contributing factors
        contributing_factors = {
            'financial_risk': risk_score * 0.4,
            'credit_risk': risk_score * 0.35,
            'employment_risk': risk_score * 0.25
        }

        # Generate recommendation
        if risk_score < 0.3:
            recommendation = "Low risk applicant. Recommend approval with standard terms."
        elif risk_score < 0.6:
            recommendation = "Moderate risk. Consider approval with adjusted terms."
        else:
            recommendation = "High risk applicant. Recommend additional review or rejection."

        return RiskAssessment(
            risk_score=risk_score,
            risk_category=risk_category,
            contributing_factors=contributing_factors,
            confidence=0.85,
            recommendation=recommendation
        )
