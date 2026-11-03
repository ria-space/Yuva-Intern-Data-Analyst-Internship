# Assessment 02 – Hands-On Data Lab Implementation

## Overview
A practical Python data analysis lab covering environment setup, data loading, inspection, cleaning, manipulation, visualization, and basic analysis.

## Tools
Python 3, Jupyter Notebook, Pandas, NumPy, Matplotlib, and Seaborn.

## Structure
- `data/`: illustrative sales CSV
- `notebooks/`: step-by-step Jupyter analysis
- `python/`: reusable Python analysis script
- `outputs/`: generated analysis files

## Setup
```bash
python -m venv .venv
```
Windows activation:
```bash
.venv\Scripts\activate
```
Install dependencies and launch:
```bash
pip install -r requirements.txt
jupyter notebook
```
Open `notebooks/Hands_On_Data_Lab.ipynb` and run cells from top to bottom.

## Exercises
1. Load and inspect the dataset.
2. Check missing values and duplicates.
3. Clean and validate records.
4. Filter, sort, group, and aggregate data.
5. Calculate summary metrics and correlations.
6. Create bar, line, and scatter plots.
7. Export the cleaned dataset.

## Dataset note
The included 20-row sales dataset is synthetic and made for demonstration. It was not supplied by the internship provider. Replace it with an assigned dataset if one is provided.

## Before submission
Run the notebook in your own environment, verify outputs, and add your name and submission date to the report. The small synthetic dataset demonstrates methods only and does not support real business conclusions.
