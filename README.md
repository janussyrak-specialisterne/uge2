# \# Data Migration Script

# 

# This repository contains a small Python script that copies a CSV file from a \*\*source\*\* path to a \*\*destination\*\* path with basic error handling.

# 

# ---

# 

# \## Setup (Windows)

# 

# ```powershell

# \# Create and activate a virtual environment

# python -m venv venv

# venv\\Scripts\\Activate.ps1

# 

# \# Install dependency

# pip install pandas

# ```

# 

# ---

# 

# \## Usage

# 

# ```powershell

# python migrator.py data\\source\_data.csv random.csv

# ```

# 

# \- First argument: path to the source `.csv`

# \- Second argument: path to the destination `.csv`

# 

# The script prints either a success message or an error explanation.

# 

# ---

# 

# \## Deactivate the environment

# 

# ```powershell

# deactivate

# ```

# 

