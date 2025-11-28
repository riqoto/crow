---
sidebar_position: 2
---

# Getting Started

This guide will help you get started with Crow.

## Installation

:::info
Crow is currently under development. Once published to PyPI, you'll be able to install it using pip.
:::

### From Source

Clone the repository and install:

```bash
git clone https://github.com/riqoto/stat.git
cd stat
pip install -e .
```

## Dependencies

Crow requires:
- **Python 3.10+**
- **pandas** - For data manipulation and analysis
- **openpyxl** - For Excel file support

Dependencies will be automatically installed when you install Crow.

## Basic Usage

Here's a complete example to get you started:

### 1. Import Required Modules

```python
from crow.file import File
from crow.data import Data  
from crow.statistics import Statistics
```

### 2. Load Your Data File

```python
# Create a File object with your file path
file = File("students.csv")

# Validate the file (optional but recommended)
if file.Validate():
    print("File is valid!")
```

### 3. Load Data

```python
# Create a Data object and load the file
data = Data()
data.Load(file)

# Get the loaded DataFrame (optional)
df = data.GetData()
print(df.head())
```

### 4. Perform Statistical Analysis

```python
# Create a Statistics object and load your data
stats = Statistics()
stats.Load(data)

# Calculate statistics for a specific column
mean_score = stats.Mean('math_score')
variance_score = stats.Variance('math_score')
median_score = stats.Median('math_score')

print(f"Mean: {mean_score}")
print(f"Variance: {variance_score}")
print(f"Median: {median_score}")
```

## Complete Example

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics

def analyze_student_data(filepath: str, column: str):
    """Analyze student test scores."""
    try:
        # Load file
        file = File(filepath)
        
        if not file.Validate():
            print("Invalid file format!")
            return
        
        # Load data
        data = Data()
        data.Load(file)
        
        # Perform analysis
        stats = Statistics()
        stats.Load(data)
        
        # Display results
        print(f"Analysis for column: {column}")
        print(f"Mean: {stats.Mean(column)}")
        print(f"Variance: {stats.Variance(column)}")
        print(f"Median: {stats.Median(column)}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run analysis
analyze_student_data("students.csv", "math_score")
```

## Supported File Formats

Crow automatically detects and handles different file formats:

| Format | Extension | Notes |
|--------|-----------|-------|
| CSV | `.csv` | Standard comma-separated values |
| Excel (Modern) | `.xlsx` | Microsoft Excel 2007+ |
| Excel (Legacy) | `.xls` | Microsoft Excel 97-2003 |
| JSON | `.json` | JavaScript Object Notation |
| Text | `.txt` | Treated as CSV |

## Error Handling

Crow will raise `FileNotFoundError` if the specified file doesn't exist:

```python
try:
    file = File("nonexistent.csv")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

Invalid file extensions are handled during validation:

```python
file = File("data.pdf")  # Will be created
if not file.Validate():  # Returns False for unsupported formats
    print("Unsupported file format!")
```

## Next Steps

- [API Reference](./api/overview.md) - Explore the complete API
