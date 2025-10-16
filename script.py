
import os
import shutil

# Create a fresh directory for the complete project
project_dir = "loan_evaluation_system_complete"

# Remove if exists
if os.path.exists(project_dir):
    shutil.rmtree(project_dir)

# Create main directory
os.makedirs(project_dir)

# Create subdirectories
os.makedirs(f"{project_dir}/models")
os.makedirs(f"{project_dir}/data")
os.makedirs(f"{project_dir}/utils")
os.makedirs(f"{project_dir}/tests")

print("✅ Created directory structure:")
print(f"   {project_dir}/")
print(f"   ├── models/")
print(f"   ├── data/")
print(f"   ├── utils/")
print(f"   └── tests/")
