
# File 4: data/__init__.py
data_init = """\"\"\"Data module for loan evaluation system\"\"\"
from .data_processor import DataProcessor
from .validators import InputValidator

__all__ = ['DataProcessor', 'InputValidator']
"""

with open('loan_evaluation_system_complete/data/__init__.py', 'w') as f:
    f.write(data_init)

print("✅ Created data/__init__.py")
