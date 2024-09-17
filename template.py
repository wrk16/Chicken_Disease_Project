import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s :')

project_name = "Chicken Disease Detection"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__(link unavailable)",
    f"src/{project_name}/components/__(link unavailable)",
    f"src/{project_name}/utils/__(link unavailable)",
    f"src/{project_name}/config/__(link unavailable)",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/pipeline/__(link unavailable)",
    f"src/{project_name}/entity/__(link unavailable)",
    f"src/{project_name}/constants/__(link unavailable)",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "(link unavailable)",
    "research/trials.ipynb",
    "test.py"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created at {filedir} for file {filename}")
    
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Empty File created at {filepath}")
    else:
        logging.info(f"File already exists at {filepath}")
