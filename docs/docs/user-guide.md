---
sidebar_position: 3
---

# User Guide

Comprehensive guide to using Crow for statistical analysis.

## Working with Files

The `File` class handles file path validation and format detection.

### Creating a File Object

```python
from crow.file import File

# Create a file object
file = File("data.csv")
```

### Validating Files

```python
# Check if file exists and has a supported format
if file.Validate():
    print("File is ready for processing")
else:
    print("File validation failed")
```

### Getting File Information

```python
# Get file path
path = file.GetPath()
print(f"File path: {path}")

# Get file extension
from crow.file import FileExtension

suffix = file.GetSuffix()
if suffix == FileExtension.CSV:
    print("This is a CSV file")
elif suffix == FileExtension.EXCEL:
    print("This is an Excel file")
```

### Supported File Extensions

```python
from crow.file import FileExtension

# All supported formats
FileExtension.CSV        # .csv
FileExtension.EXCEL      # .xlsx  
FileExtension.EXCEL_OLD  # .xls
FileExtension.JSON       # .json
FileExtension.TXT        # .txt
```

## Loading Data

The `Data` class handles loading files into pandas DataFrames.

### Basic Data Loading

```python
from crow.data import Data
from crow.file import File

# Create and load data
file = File("sales_data.csv")
data = Data()
data.Load(file)
```

### Accessing the DataFrame

```python
# Get the underlying pandas DataFrame
df = data.GetData()

# Now you can use pandas operations
print(df.head())
print(df.columns)
print(df.info())
```

### Loading Different Formats

Crow automatically handles different file formats:

#### CSV Files

```python
file = File("data.csv")
data = Data()
data.Load(file)  # Automatically uses pd.read_csv()
```

#### Excel Files

```python
# Modern Excel (.xlsx)
file = File("data.xlsx")
data = Data()
data.Load(file)  # Uses pd.read_excel()

# Legacy Excel (.xls)
file = File("legacy_data.xls")
data.Load(file)  # Also works
```

#### JSON Files

```python
file = File("data.json")
data = Data()
data.Load(file)  # Uses pd.read_json()
```

#### Text Files

```python
file = File("data.txt")
data = Data()
data.Load(file)  # Treats as CSV
```

## Statistical Analysis

The `Statistics` class provides methods for statistical calculations.

### Setting Up Statistics

```python
from crow.statistics import Statistics

# Create statistics object
stats = Statistics()

# Load your data
stats.Load(data)
```

### Calculating Statistics

#### Mean (Arithmetic Average)

```python
# Get mean of a column
mean_value = stats.Mean('sales_amount')
print(f"Average sales: ${mean_value:.2f}")
```

#### Variance

```python
# Get variance of a column
variance_value = stats.Variance('test_score')
print(f"Score variance: {variance_value:.2f}")
```

#### Median

```python
# Get median of a column
median_value = stats.Median('age')
print(f"Median age: {median_value}")
```

### Handling Multiple Columns

```python
# Analyze different columns
columns = ['math_score', 'science_score', 'english_score']

for col in columns:
    mean = stats.Mean(col)
    variance = stats.Variance(col)
    median = stats.Median(col)
    
    print(f"\n{col}:")
    print(f"  Mean: {mean:.2f}")
    print(f"  Variance: {variance:.2f}")
    print(f"  Median: {median:.2f}")
```

## Complete Workflow Example

Here's a complete example analyzing student test scores:

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics

def analyze_test_scores(filepath: str):
    """
    Analyze student test scores from a data file.
    
    Args:
        filepath: Path to the data file
    """
    # Step 1: Load the file
    try:
        file = File(filepath)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
        return
    
    # Step 2: Validate file format
    if not file.Validate():
        print("Error: Unsupported file format")
        print("Supported formats: .csv, .xlsx, .xls, .json, .txt")
        return
    
    # Step 3: Load data
    data = Data()
    data.Load(file)
    
    # Step 4: Preview the data
    df = data.GetData()
    if df is None:
        print("Error: Failed to load data")
        return
    
    print("Data loaded successfully!")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
    print(f"\nAvailable columns: {', '.join(df.columns)}")
    
    # Step 5: Perform statistical analysis
    stats = Statistics()
    stats.Load(data)
    
    # Analyze numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns
    
    for col in numeric_columns:
        print(f"\n{'='*50}")
        print(f"Statistics for: {col}")
        print(f"{'='*50}")
        print(f"Mean:     {stats.Mean(col):.2f}")
        print(f"Variance: {stats.Variance(col):.2f}")
        print(f"Median:   {stats.Median(col):.2f}")

# Usage
analyze_test_scores("students.csv")
```

## Best Practices

### 1. Always Validate Files

```python
file = File("data.csv")
if not file.Validate():
    print("Invalid file!")
    return
```

### 2. Handle Errors Gracefully

```python
try:
    file = File("data.csv")
    data = Data()
    data.Load(file)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")
```

### 3. Check for Null Data

```python
df = data.GetData()
if df is None:
    print("No data loaded")
    return
```

### 4. Verify Column Existence

```python
df = data.GetData()
if 'column_name' not in df.columns:
    print("Column not found in dataset")
    return

result = stats.Mean('column_name')
```

## Advanced Usage

### Using Pandas Operations

Since Crow is built on pandas, you can use the full power of pandas:

```python
# Get the DataFrame
df = data.GetData()

# Filter data
filtered_df = df[df['age'] > 18]

# Group by operations
grouped = df.groupby('category')['value'].mean()

# Custom calculations
df['normalized'] = (df['value'] - df['value'].mean()) / df['value'].std()
```

### Combining with Other Libraries

```python
import matplotlib.pyplot as plt

# Load and analyze data
file = File("data.csv")
data = Data()
data.Load(file)

stats = Statistics()
stats.Load(data)

# Get statistics
mean = stats.Mean('value')
median = stats.Median('value')

# Visualize
df = data.GetData()
df['value'].hist()
plt.axvline(mean, color='r', label='Mean')
plt.axvline(median, color='g', label='Median')
plt.legend()
plt.show()
```

## Troubleshooting

### Common Issues

**Issue**: `FileNotFoundError`
```python
# Solution: Check file path
import os
if not os.path.exists("data.csv"):
    print("File does not exist at this path")
```

**Issue**: Column not found
```python
# Solution: Check available columns
df = data.GetData()
print("Available columns:", df.columns.tolist())
```

**Issue**: Statistics return None
```python
# Solution: Ensure data is loaded first
stats = Statistics()
stats.Load(data)  # Don't forget this step!
```

## Next Steps

- [API Overview](./api/overview.md) - Explore all classes and methods
- [Statistics Class](./api/statistics.mdx) - Detailed Statistics API
- [File Class](./api/file.mdx) - Detailed File API
- [Data Class](./api/data.mdx) - Detailed Data API
