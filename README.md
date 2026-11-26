# Python Environment Setup & Machine Learning Starter

This repository contains my personal setup for learning Python, managing virtual environments, and working on Machine Learning projects with scikit-learn (and Kaggle competitions like Titanic).

---

## 🛠️ Prerequisites

Make sure Python 3 is installed on your system.

* macOS / Linux / GitHub Codespaces: `python3`
* Windows: `python`

---

## 🚀 Quick Start & Environment Setup

Follow these steps to run this project on any machine (local Mac/Linux, Windows, or cloud services like GitHub Codespaces).

### 1. Clone the Repository

```bash
git clone <YOUR-REPOSITORY-URL>
cd <YOUR-REPOSITORY-NAME>
```

### 2. Create a Virtual Environment

* macOS / Linux / GitHub Codespaces:

  ```bash
  python3 -m venv .venv
  ```

* Windows (Command Prompt / PowerShell):

  ```bash
  python -m venv .venv
  ```

### 3. Activate the Virtual Environment

* macOS / Linux / GitHub Codespaces:

  ```bash
  source .venv/bin/activate
  ```

* Windows (Command Prompt):

  ```bash
  .venv\Scripts\activate.bat
  ```

* Windows (PowerShell):

  ```bash
  .\.venv\Scripts\Activate.ps1
  ```

> Note: when active, you will see `(.venv)` at the beginning of your terminal prompt.
> This alone does NOT guarantee the right Python is running. Always verify with `which python`.

### 4. Install the Requirements

```bash
python -m pip install -r requirements.txt
```

---

## 📦 Managing Dependencies & pip

### Install pip (if not available by default)

If pip is missing in your environment, download and run the official installer script:

```bash
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
```

### Save new libraries

After installing something new, update the requirements file and push it to GitHub:

```bash
python -m pip freeze > requirements.txt
git add requirements.txt
git commit -m "update requirements"
git push
```

> `requirements.txt` is only a list of what to install. It does not install anything by itself.

---

## 🩺 Troubleshooting: when the .venv doesn't work

**Typical symptom:** `ModuleNotFoundError: No module named 'pandas'` (or sklearn, matplotlib...)

**Why it happens:** libraries live *inside* `.venv/`, which is not uploaded to GitHub (it is in `.gitignore`).
A new or rebuilt Codespace starts without it. Also, a different Python (for example the global one) may be running instead of the one in `.venv`.

### Fix, step by step

1. Check which Python is running:

   ```bash
   which python
   ```

   It must show `/workspaces/<repo-name>/.venv/bin/python`.

2. If it points somewhere else, reactivate the environment:

   ```bash
   deactivate
   source .venv/bin/activate
   which python
   ```

3. Check whether the libraries are installed:

   ```bash
   python -m pip list
   ```

4. If they are missing, install them:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. If `.venv` doesn't exist at all (new Codespace), recreate everything:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

### Good habits

* Always use `python -m pip` (it installs into the Python that runs your scripts).
* Stop the Codespace, don't delete it. Deleting loses everything not pushed to GitHub.
* Run scripts from the project root so paths like `./data/heart.csv` work.
* Commit and push often, including `notes.md`.

---

## 📊 Data Files

* Save datasets as a real `.csv` file (not Excel, and not pasted content). Otherwise pandas fails with `Error tokenizing data`.
* Check a file quickly with:

  ```bash
  head -n 5 data/<file>.csv
  ```

* Make sure the target column name matches your code (e.g. `'target'` in `heart.csv`). Check it with `print(df.columns)`.

---

## 💻 Working with VS Code & Codespaces

1. Install the recommended Python extension from Microsoft.
2. Select your interpreter: open the Command Palette (`Cmd+Shift+P` on Mac or `Ctrl+Shift+P` on Windows/Linux) → **Python: Select Interpreter** → choose `./.venv/bin/python`.

### Automatic setup with devcontainer (optional)

A `.devcontainer/devcontainer.json` file can create the `.venv` and install the requirements automatically whenever a Codespace is created:

```json
{
  "name": "ML scikit-learn",
  "image": "mcr.microsoft.com/devcontainers/python:3",
  "postCreateCommand": "python3 -m venv .venv && .venv/bin/python -m pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python"],
      "settings": {
        "python.defaultInterpreterPath": "${containerWorkspaceFolder}/.venv/bin/python"
      }
    }
  }
}
```

For an existing Codespace, run **Codespaces: Rebuild Container** from the Command Palette. You may still need `source .venv/bin/activate` in new terminals.

---

## 📝 Project Structure & Notes

```
.
├── .venv/               # Virtual environment (excluded from Git)
├── .devcontainer/       # Optional Codespaces auto-setup
├── data/
│   ├── heart.csv
│   └── whr2017.csv
├── pca.py               # PCA and IncrementalPCA + logistic regression
├── kpca.py              # Kernel PCA + logistic regression
├── regularization.py    # Ridge / Lasso on the WHR 2017 dataset
├── requirements.txt
├── get-pip.py           # Utility for manual pip bootstrapping
└── README.md
```

* Each model lives in its own `.py` file; all of them share the same `.venv` and `data/` folder.
* Don't name a file after a library you import (e.g. `sklearn.py`, `pandas.py`), or the imports will break.
* Python is case-sensitive: it's `sklearn`, not `skLearn`.
* Kaggle workflow: notebooks run locally with this environment or directly in Kaggle/Google Colab.