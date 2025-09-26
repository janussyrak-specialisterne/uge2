
# Delopgave 1: Intro til Python
This exercise is solved in the file delopgave1.py. It requires no external libraries, and so can be run like you would any python file, eg
```powershell
# Create and activate a virtual environment
python delopgave1.py
```

# Delopgave 2: Logfil-analyse
## How to run
1.  Put your log file in a `data/` folder.
2.  Run:
`python logfilter.py SOURCE_LOG.txt DESTINATION_PREFIX --type ERROR` 
Example:
`python logfilter.py app_log.txt filtered --type ERROR` 
This will create a file called:
`filtered_ERROR` 
containing only the `ERROR` log lines.

# Delopgave 3: Data Migration Script
This exercise is solved in logfilter.py, and contains a small Python script that copies a CSV file from a \*\*source\*\* path to a \*\*destination\*\* path with basic error handling.
## Setup (Windows)
```powershell
# Create and activate a virtual environment
python -m venv venv
venv\\Scripts\\Activate.ps1
# Install dependency
pip install pandas
```
---
## Usage
```powershell
python logfilter.py data\\source\_data.csv random.csv
```
- First argument: path to the source `.csv`
- Second argument: path to the destination `.csv`
The script prints either a success message or an error explanation.
---
## Deactivate the environment
Afterwards, ensure to shut down the virtual environment by using
```powershell
deactivate
```

# Delopgave 4: Introduktion til Pandas
This exercise is solved in the Jupyter notebook Delopgave4.ipynb.