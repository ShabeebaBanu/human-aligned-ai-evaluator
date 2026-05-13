# human-aligned-ai-evaluator

## 1. What this project does

This project builds an automated  grading system using NLP and machine learning. It replaces keyword matching with genuine meaning comparison, catches logical contradictions, distributes partial credit fairly, and explains every score in plain English.

| Module | Owner | Responsibility |
|--------|-------|---------------|
| Module 1 | Member A | Semantic understanding — reads and understands the student answer |
| Module 2 | Member B | Intelligent scoring engine — assigns human-aligned marks using machine learning |
| Module 3 | Member C | Fairness and explanation — validates scores against human marks and reasoning|

---

## 2. Prerequisites

Every team member must install all four tools below on their own laptop before cloning the project.

### 2.1 Python 3.10 or higher
Download from [python.org](https://python.org).
> **Windows:** During installation, tick the checkbox **"Add Python to PATH"** — easy to miss, causes problems if skipped.
> **Mac:** Python may already be installed. Check with `python3 --version`.

```bash
# Verify installation
python --version
# Expected: Python 3.10.x or higher
```

### 2.2 VS Code
Download from [code.visualstudio.com](https://code.visualstudio.com). After installing, open VS Code and install these two extensions from the Extensions panel (left sidebar):
- **Python** (publisher: Microsoft)
- **Jupyter** (publisher: Microsoft)


## 3. Cloning the repository
```bash
# Clone the repository to your laptop
git clone https://github.com/MEMBER-A-USERNAME/automated-answer-grader.git

# Move into the project folder
cd automated-answer-grader
```

## 4. Setting up the Python environment

### 4.1 Create and activate the virtual environment

```bash
# Create the virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac / Linux
source venv/bin/activate
```

> **Important:** You will see `(venv)` at the start of your terminal line when it is active. You must activate the virtual environment **every time you open a new terminal window** before running any Python files.

### 4.2 Install all required libraries

```bash
# Install everything from requirements.txt
pip install -r requirements.txt

# Download the spaCy English language model
python -m spacy download en_core_web_sm

# Verify key libraries installed correctly
python -c "import sentence_transformers, spacy, sklearn, pandas; print('All OK')"
# Expected output: All OK
```

> **Troubleshooting:** If you see `ModuleNotFoundError`, make sure `(venv)` is showing in your terminal, then run `pip install -r requirements.txt` again.

---

## 5. Project folder structure
```bash
# Each module has a seperate folder 

# Dataset is linked to drive sheet, any update made to sheet will be reflected in local repo as a csv file
```

## 6. Verify the data accessibility 
```bash
# after setting up everything run the file 'pipeline.py'
# To run pre-processing 
python pipeline.py preprocess


# if everything are ok, you are good to go with your development works
```

## 7. Project Structure Overview

This section briefly explains the purpose of each folder and key files in the project.

### 📁 Folders

- **data/**  
  Stores all datasets used in the project  
  - `raw/` → original dataset (from Google Sheets)  
  - `processed/` → cleaned data after preprocessing  
  - `features/` → outputs from each feature process (sementic-similarity, contradiction etc)   

- **utils/**  
  Common helper functions used across modules  
  - `data_loader.py` → handles loading and saving of various datasets  
  - `config.py` → stores file paths and configuration variables  

- **models/**  
  Stores trained machine learning models  

---

### 📄 Key Files

- **modules**  
  implementation of each module  
  - `module1/` → preprocessing and semantic analysis etc  
  - `module2/` → scoring models and training logic  
  - `module3/` → feedback generation and evaluation  

- **pipeline.py**  
  Main entry point of the system — used to run preprocessing, training, and prediction commands  

- **requirements.txt**  
  List of all Python libraries required for the project 

- **train_pipeline.py & predict_pipeline.py**
  Future use........ 

- **README.md**  
  Project documentation and setup instructions  

---

### 🧠 Summary

- Data flows from `data/raw` → `processed` → `features` → `outputs`  
- Each module performs a specific task in the pipeline  
- `pipeline.py` controls the overall workflow  
 