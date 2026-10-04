# Python Environment Setup & Machine Learning Starter

This repository contains my personal setup for learning Python, managing virtual environments, and working on Machine Learning projects (including Kaggle competitions like Titanic).

---

## 🛠️ Prerequisites

Before starting, ensure you have Python 3 installed on your system.

* macOS / Linux: python3
* Windows: python

---

## 🚀 Quick Start & Environment Setup

Follow these steps to set up and run this project on any machine (Local Mac/Linux, Windows, or Cloud Services like GitHub Codespaces).

### 1. Clone the Repository

git clone <YOUR-REPOSITORY-URL>
cd <YOUR-REPOSITORY-NAME>

### 2. Create a Virtual Environment

* macOS / Linux / GitHub Codespaces: python3 -m venv .venv
* Windows (Command Prompt / PowerShell): python -m venv .venv

### 3. Activate the Virtual Environment

* macOS / Linux / GitHub Codespaces: source .venv/bin/activate
* Windows (Command Prompt): .venv\Scripts\activate.bat
* Windows (PowerShell): .\.venv\Scripts\Activate.ps1

> Note: When active, you will see (.venv) at the beginning of your terminal prompt.

---

## 📦 Managing Dependencies & pip

### Install pip (If not available by default)

If pip is missing in your environment, download and execute the official installer script:

`curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py`

### Install Project Requirements

Install all required libraries for the project:

pip install -r requirements.txt

*(If you add new libraries, save them to the requirements file using: pip freeze > requirements.txt)*

---

## 💻 Working with VS Code & Extensions

When opening this repository in Visual Studio Code or GitHub Codespaces:

1. Install the recommended Python Extension from Microsoft.
2. Select your interpreter: Open Command Palette (Cmd+Shift+P on Mac or Ctrl+Shift+P on Windows/Linux) -> Search for Python: Select Interpreter -> Choose ./mi_entorno.

---

## 📝 Project Workflow & Notes

* mi_entorno/: Local virtual environment directory (excluded from Git version control).
* get-pip.py: Utility script used for manual pip bootstrapping if needed.
* Kaggle Workflow: Notebooks are designed to run locally using this environment or directly in Kaggle/Google Colab.