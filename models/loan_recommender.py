"""Loan recommendation module"""
import numpy as np
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class LoanRecommendation:
    """Loan recommendation results"""
    recommended_amount: float
    recommended_term: int
    interest_rate: float
    monthly_payment: float
    total_cost: float
    approval_probability: float
    alternative_options: List[Dict[str, Any]]
    reasoning: List[str]
    conditions: List[str]

class LoanRecommender:
    """Loan recommendation system"""

    def __init__(self):
        self.base_rates = {
            'excellent': 0.045,
            'very_good': 0.065,
            'good': 0.085,
            'fair': 0.105,
            'poor': 0.150
        }

    def recommend_loan_terms(self, application_data: Dict[str, Any], risk_score: float) -> LoanRecommendation:
        """Generate loan recommendations"""
        try:
            # Extract data
            financial = application_data.get('financial', {})
            loan = application_data.get('loan', {})
            credit = application_data.get('credit', {})

            annual_income = financial.get('annual_income', 0)
            requested_amount = loan.get('loan_amount', 25000)

            # Determine credit tier
            credit_score = credit.get('credit_score', 600)
            credit_tier = self._determine_credit_tier(credit_score, risk_score)

            # Calculate maximum affordable amount
            max_affordable = annual_income * 3 if annual_income > 0 else requested_amount
            recommended_amount = min(requested_amount, max_affordable, 500000)

            # Determine term
            recommended_term = 60  # 5 years default

            # Calculate interest rate
            interest_rate = self._calculate_interest_rate(credit_tier, risk_score)

            # Calculate monthly payment
            monthly_payment = self._calculate_monthly_payment(
                recommended_amount, interest_rate, recommended_term
            )

            total_cost = monthly_payment * recommended_term

            # Calculate approval probability
            approval_probability = self._calculate_approval_probability(risk_score, credit_score)

            # Generate alternatives
            alternatives = self._generate_alternatives(
                recommended_amount, recommended_term, interest_rate
            )

            # Generate reasoning
            reasoning = [
                f"Credit tier: {credit_tier}",
                f"Risk score: {risk_score:.2f}",
                f"Recommended amount is {(recommended_amount/requested_amount)*100:.0f}% of requested"
            ]

            # Generate conditions
            conditions = ["Employment verification required", "Income documentation required"]
            if risk_score > 0.6:
                conditions.append("Additional collateral may be required")

            return LoanRecommendation(
                recommended_amount=recommended_amount,
                recommended_term=recommended_term,
                interest_rate=interest_rate,
                monthly_payment=monthly_payment,
                total_cost=total_cost,
                approval_probability=approval_probability,
                alternative_options=alternatives,
                reasoning=reasoning,
                conditions=conditions
            )

        except Exception as e:
            # Return default recommendation
            return LoanRecommendation(
                recommended_amount=10000,
                recommended_term=60,
                interest_rate=0.10,
                monthly_payment=212.47,
                total_cost=12748.23,
                approval_probability=0.5,
                alternative_options=[],
                reasoning=["Default recommendation due to processing error"],
                conditions=["Complete application review required"]
            )

    def _determine_credit_tier(self, credit_score: int, risk_score: float) -> str:
        """Determine credit tier"""
        adjusted_score = credit_score * (1 - risk_score * 0.2)

        if adjusted_score >= 750:
            return 'excellent'
        elif adjusted_score >= 700:
            return 'very_good'
        elif adjusted_score >= 650:
            return 'good'
        elif adjusted_score >= 600:
            return 'fair'
        else:
            return 'poor'

    def _calculate_interest_rate(self, credit_tier: str, risk_score: float) -> float:
        """Calculate interest rate"""
        base_rate = self.base_rates.get(credit_tier, 0.10)
        risk_adjustment = risk_score * 0.05
        return min(0.30, base_rate + risk_adjustment)

    def _calculate_monthly_payment(self, principal: float, annual_rate: float, term_months: int) -> float:
        """Calculate monthly payment"""
        if annual_rate <= 0:
            return principal / term_months if term_months > 0 else 0

        monthly_rate = annual_rate / 12
        payment = principal * (monthly_rate * (1 + monthly_rate) ** term_months) / ((1 + monthly_rate) ** term_months - 1)
        return payment

    def _calculate_approval_probability(self, risk_score: float, credit_score: int) -> float:
        """Calculate approval probability"""
        risk_prob = 1 - risk_score
        credit_prob = (credit_score - 300) / 550  # Normalize 300-850 to 0-1
        return (risk_prob * 0.6 + credit_prob * 0.4)

    def _generate_alternatives(self, amount: float, term: int, rate: float) -> List[Dict[str, Any]]:
        """Generate alternative loan options"""
        alternatives = []

        # Lower amount option
        lower_amount = amount * 0.75
        lower_payment = self._calculate_monthly_payment(lower_amount, rate, term)
        alternatives.append({
            'option': 'Lower Amount',
            'amount': lower_amount,
            'term': term,
            'rate': rate,
            'monthly_payment': lower_payment,
            'description': 'Reduced amount for easier approval'
        })

        # Shorter term option
        if term > 36:
            shorter_term = 36
            shorter_payment = self._calculate_monthly_payment(amount, rate, shorter_term)
            alternatives.append({
                'option': 'Shorter Term',
                'amount': amount,
                'term': shorter_term,
                'rate': rate,
                'monthly_payment': shorter_payment,
                'description': 'Pay off faster, save on interest'
            })

        return alternatives[:2]
