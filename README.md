# Smart-Resume-Analyzer

***

# Smart Resume Insights & Placement Analyzer

A collaborative, cross-platform application for parsing resumes, extracting skills, and visualizing placement readiness through a modular Python backend and an interactive dashboard frontend.

***

## Features

- **Resume PDF Parsing** – Extract and clean text from uploaded resumes.
- **Skill Extraction** – Detect and map skills from resume content.
- **Placement Scoring** – Rate candidate readiness for roles/domains.
- **Dashboard Visualization** – Interactive insights and recommendations.
- **Cross-OS Workflow** – Seamless development for macOS and Windows.

***

## Prerequisites

- Python 3.9 or higher
- Git
- VS Code (recommended)
- (Extensions: Python, Pylance, GitLens, Jupyter, Prettier/Black)

***

## Setup

### 1. Clone the Repository

```sh
# Raghav (macOS)
cd ~/Projects
git clone https://github.com/raghavkapoor31/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer

# Ananya (Windows)
cd C:\Users\Ananya\Projects
git clone https://github.com/raghavkapoor31/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer
```

### 2. Create and Activate Virtual Environment

```sh
# macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

_Add initial packages to requirements.txt if empty:_
```
pandas
numpy
matplotlib
seaborn
PyPDF2
wordcloud
streamlit
flask
```

***

## Folder Structure

```
Smart-Resume-Analyzer/
├── backend/
│   ├── resume_parser.py
│   ├── skill_extraction.py
│   ├── placement_scoring.py
│   └── nlp_utils.py
├── frontend/
│   ├── app.py
│   └── visualizations.py
├── data/
│   └── sample_resumes/
├── docs/
├── requirements.txt
└── README.md
```

***

## Development Workflow

- **Pull latest main before starting work:**
  ```sh
  git checkout main
  git pull origin main
  ```
- **Create a feature branch:**
  ```sh
  git checkout -b feature/<feature-name>
  ```
- **Commit and push changes to branch:**
  ```sh
  git add .
  git commit -m "Describe the change"
  git push origin feature/<feature-name>
  ```
- **Open a Pull Request for review and merging.**
- **Sync dependencies:** After installing new packages,
  ```sh
  pip freeze > requirements.txt
  git add requirements.txt
  git commit -m "Update requirements"
  git push origin <branch>
  ```

***

## Running the Dashboard

```sh
streamlit run frontend/app.py
```
_This will launch the interactive resume analytics dashboard in your browser._

***

## Usage

- Upload resumes (PDF) to the dashboard to extract and visualize insights.
- Sample resumes for testing should be placed in `data/sample_resumes/`.

***

## Contribution

- Use feature branches for each task.
- Write clear commit messages.
- Add docstrings to all major functions.
- Update documentation (`/docs`, `README.md`) as the project evolves.

***

## Authors

- Raghav Kapoor (macOS)
- Ananya (Windows)

***

Copy and paste this into your `README.md` for a complete, professional, and collaborative open-source project introduction and guide.Here is a complete `README.md` you can directly copy-paste into your repository:

***

# Smart Resume Insights & Placement Analyzer

A collaborative cross-platform tool (Python + Streamlit/Flask) to parse resumes, extract skills, rate placement readiness, and visualize career insights. Built by Raghav (macOS) and Ananya (Windows) for efficient teamwork and maximum compatibility.

***

## Features

- PDF Resume Parsing and Cleaning
- Skill Extraction and Mapping
- Placement Scoring/Domain Analysis
- Interactive Dashboard (Streamlit)
- Data Visualization (Charts, WordClouds)
- Modular Backend/Frontend Code Organization

***

## Prerequisites

- Python 3.9+
- Git
- VS Code (recommended)
- VS Code extensions: Python, Pylance, Jupyter, Prettier/Black, GitLens

***

## Setup Instructions

### 1. Clone the Repository

```sh
# Raghav (macOS)
cd ~/Projects
git clone https://github.com/raghavkapoor31/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer

# Ananya (Windows)
cd C:\Users\Ananya\Projects
git clone https://github.com/raghavkapoor31/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer
```

### 2. Create and Activate Virtual Environment

```sh
# macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python Packages

```sh
pip install -r requirements.txt
```

_Add if requirements.txt is empty:_
```
pandas
numpy
matplotlib
seaborn
PyPDF2
wordcloud
streamlit
flask
```

### 4. Open in VS Code and Set Interpreter

- Open folder in VS Code
- Cmd+Shift+P (macOS) / Ctrl+Shift+P (Windows) > `Python: Select Interpreter` > choose your venv

***

## Project Structure

```
Smart-Resume-Analyzer/
├── backend/
│   ├── resume_parser.py
│   ├── skill_extraction.py
│   ├── placement_scoring.py
│   └── nlp_utils.py
├── frontend/
│   ├── app.py
│   └── visualizations.py
├── data/
│   └── sample_resumes/
├── docs/
├── requirements.txt
└── README.md
```

***

## Development Workflow

- Always pull latest main:
  ```sh
  git checkout main
  git pull origin main
  ```
- Create a feature branch:
  ```sh
  git checkout -b feature/<your-feature>
  ```
- Regularly commit, push, and create Pull Requests.
- Update requirements.txt after new installs:
  ```sh
  pip freeze > requirements.txt
  git add requirements.txt
  git commit -m "Update requirements"
  git push
  ```

***

## Running the App

```sh
streamlit run frontend/app.py
```

***

## Contribution

- Work in branches; propose PRs for main changes.
- Use clear commit messages and code docstrings.
- Store sample PDFs in `data/sample_resumes/`.

***

## Authors

- Raghav Kapoor (macOS)
- Ananya (Windows)

***

