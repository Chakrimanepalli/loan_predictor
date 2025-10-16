
# Create Dockerfile
dockerfile_content = '''FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
'''

with open('loan_evaluation_system_complete/Dockerfile', 'w') as f:
    f.write(dockerfile_content)

print("✅ Created Dockerfile")

# Now create a comprehensive summary
print("\n" + "=" * 80)
print("📦 PROJECT GENERATION COMPLETE!")
print("=" * 80)

# List all files created
import os
files_created = []
for root, dirs, files in os.walk('loan_evaluation_system_complete'):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, 'loan_evaluation_system_complete')
        files_created.append(relative_path)

files_created.sort()

print(f"\n✅ Created {len(files_created)} files:\n")
for i, file in enumerate(files_created, 1):
    print(f"{i:2d}. {file}")

print("\n" + "=" * 80)
print("📁 PROJECT STRUCTURE:")
print("=" * 80)

# Show directory structure
structure = """
loan_evaluation_system_complete/
├── main.py
├── config.py
├── requirements.txt
├── README.md
├── Dockerfile
├── .gitignore
├── models/
│   ├── __init__.py
│   ├── risk_analyzer.py
│   ├── credit_scorer.py
│   ├── geolocation_analyzer.py
│   └── loan_recommender.py
├── data/
│   ├── __init__.py
│   ├── data_processor.py
│   └── validators.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── constants.py
└── tests/
    ├── __init__.py
    ├── test_models.py
    └── test_data.py
"""

print(structure)
