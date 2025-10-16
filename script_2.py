
# File 2: .gitignore
gitignore = """__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.env
.venv
venv/
*.log
.DS_Store
.streamlit/
logs/
temp/
*.db
*.sqlite
"""

with open('loan_evaluation_system_complete/.gitignore', 'w') as f:
    f.write(gitignore)

print("✅ Created .gitignore")
