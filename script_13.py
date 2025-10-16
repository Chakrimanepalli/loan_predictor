
# File 13: models/credit_scorer.py
credit_scorer_content = '''"""Credit scoring module"""
from typing import Dict, Any, List
from dataclasses import dataclass

@dataclass
class CreditAnalysis:
    """Credit analysis results"""
    score: int
    grade: str
    factors: Dict[str, float]
    strengths: List[str]
    weaknesses: List[str]
    recommendations: List[str]

class CreditScorer:
    """Credit scoring system"""
    
    def __init__(self):
        self.score_grades = {
            (800, 850): 'Exceptional',
            (740, 799): 'Very Good',
            (670, 739): 'Good',
            (580, 669): 'Fair',
            (300, 579): 'Poor'
        }
    
    def calculate_credit_score(self, application_data: Dict[str, Any]) -> int:
        """Calculate credit score"""
        credit = application_data.get('credit', {})
        base_score = credit.get('credit_score', 600)
        
        # Adjustments based on other factors
        adjustments = 0
        
        # Payment history
        defaults = credit.get('previous_defaults', 0)
        if defaults == 0:
            adjustments += 20
        else:
            adjustments -= 30 * defaults
        
        # Credit history length
        history_length = credit.get('credit_history_length', 0)
        if history_length >= 10:
            adjustments += 15
        elif history_length >= 5:
            adjustments += 10
        
        final_score = int(base_score + adjustments)
        return max(300, min(850, final_score))
    
    def analyze_creditworthiness(self, application_data: Dict[str, Any]) -> CreditAnalysis:
        """Perform comprehensive credit analysis"""
        score = self.calculate_credit_score(application_data)
        grade = self._get_credit_grade(score)
        
        # Analyze factors
        credit = application_data.get('credit', {})
        factors = {
            'payment_history': 1.0 if credit.get('previous_defaults', 0) == 0 else 0.5,
            'credit_history': min(1.0, credit.get('credit_history_length', 0) / 10),
            'current_loans': 0.8 if credit.get('current_loans', 0) <= 3 else 0.5
        }
        
        # Identify strengths and weaknesses
        strengths = []
        weaknesses = []
        
        if credit.get('previous_defaults', 0) == 0:
            strengths.append("No payment defaults")
        else:
            weaknesses.append("History of payment defaults")
        
        if score >= 700:
            strengths.append("Good credit score")
        elif score < 600:
            weaknesses.append("Low credit score")
        
        # Recommendations
        recommendations = []
        if score < 670:
            recommendations.append("Work on improving credit score")
            recommendations.append("Make all payments on time")
        else:
            recommendations.append("Maintain good credit practices")
        
        return CreditAnalysis(
            score=score,
            grade=grade,
            factors=factors,
            strengths=strengths,
            weaknesses=weaknesses,
            recommendations=recommendations
        )
    
    def _get_credit_grade(self, credit_score: int) -> str:
        """Get credit grade based on score"""
        for (min_score, max_score), grade in self.score_grades.items():
            if min_score <= credit_score <= max_score:
                return grade
        return 'Unknown'
'''

with open('loan_evaluation_system_complete/models/credit_scorer.py', 'w') as f:
    f.write(credit_scorer_content)

print("✅ Created models/credit_scorer.py")
