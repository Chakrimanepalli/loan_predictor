
# File 14: models/geolocation_analyzer.py
geolocation_content = '''"""Geolocation analysis module"""
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class LocationRisk:
    """Location risk assessment results"""
    overall_risk: float
    economic_risk: float
    demographic_risk: float
    environmental_risk: float
    crime_risk: float
    risk_factors: List[str]
    risk_mitigation: List[str]

class GeolocationAnalyzer:
    """Geographic risk assessment system"""
    
    def __init__(self):
        # Risk data by state (simplified)
        self.state_risk_data = {
            'CALIFORNIA': {'unemployment': 4.2, 'median_income': 80000, 'crime_rate': 400},
            'NEW YORK': {'unemployment': 4.1, 'median_income': 71000, 'crime_rate': 500},
            'TEXAS': {'unemployment': 3.6, 'median_income': 64000, 'crime_rate': 450},
            'FLORIDA': {'unemployment': 3.8, 'median_income': 55000, 'crime_rate': 480}
        }
    
    def assess_location_risk(self, location_data: Dict[str, str]) -> float:
        """Assess risk based on geographic location"""
        try:
            state = location_data.get('state', '').upper()
            
            # Get state data or use defaults
            state_data = self.state_risk_data.get(
                state,
                {'unemployment': 5.0, 'median_income': 60000, 'crime_rate': 400}
            )
            
            # Calculate risk components
            unemployment_risk = min(state_data['unemployment'] / 10, 1.0)
            income_risk = max(0, 1 - (state_data['median_income'] / 100000))
            crime_risk = min(state_data['crime_rate'] / 1000, 1.0)
            
            # Overall risk
            overall_risk = (unemployment_risk * 0.4 + income_risk * 0.3 + crime_risk * 0.3)
            return min(1.0, overall_risk)
            
        except Exception as e:
            return 0.3  # Default moderate risk
    
    def get_comprehensive_location_analysis(self, location_data: Dict[str, str]) -> LocationRisk:
        """Get comprehensive location risk analysis"""
        overall_risk = self.assess_location_risk(location_data)
        
        # Calculate component risks
        economic_risk = overall_risk * 0.4
        demographic_risk = overall_risk * 0.25
        environmental_risk = overall_risk * 0.20
        crime_risk = overall_risk * 0.15
        
        # Identify risk factors
        risk_factors = []
        if overall_risk > 0.6:
            risk_factors.append("High geographic risk area")
        if economic_risk > 0.3:
            risk_factors.append("Economic instability in region")
        
        # Risk mitigation
        risk_mitigation = []
        if overall_risk > 0.5:
            risk_mitigation.append("Consider additional collateral requirements")
            risk_mitigation.append("Verify local employment stability")
        else:
            risk_mitigation.append("Standard loan terms appropriate")
        
        return LocationRisk(
            overall_risk=overall_risk,
            economic_risk=economic_risk,
            demographic_risk=demographic_risk,
            environmental_risk=environmental_risk,
            crime_risk=crime_risk,
            risk_factors=risk_factors,
            risk_mitigation=risk_mitigation
        )
'''

with open('loan_evaluation_system_complete/models/geolocation_analyzer.py', 'w') as f:
    f.write(geolocation_content)

print("✅ Created models/geolocation_analyzer.py")
