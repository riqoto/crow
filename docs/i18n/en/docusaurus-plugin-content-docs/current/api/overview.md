---
sidebar_position: 1
---

# API Overview

Crow provides a simple, class-based API for statistical analysis. The library is organized into three main modules:

## Module Structure

```
crow/
├── file.py       # File handling and validation
├── data.py       # Data loading from various formats
└── statistics.py # Statistical analysis methods
```

## Core Classes

### File

Handles file path validation and format detection.

**Key features:**
- Validates file existence
- Detects file format (CSV, Excel, JSON, TXT)
- Provides file path and extension information

[View File API →](./file.mdx)

---

### Data

Loads data from supported file formats into pandas DataFrames.

**Key features:**
- Supports multiple file formats (CSV, Excel, JSON, TXT)
- Automatic format detection
- Provides access to underlying DataFrame

[View Data API →](./data.mdx)

---

### Statistics

Performs statistical calculations on loaded data.

**Key features:**
- Mean (arithmetic average)
- Variance (measure of spread)
- Median (middle value)

[View Statistics API →](./statistics.mdx)

---

## Basic Workflow

The typical workflow when using Crow:

```mermaid
graph LR
    A[Create File] --> B[Validate File]
    B --> C[Load Data]
    C --> D[Create Statistics]
    D --> E[Analyze]
```

### Step-by-Step

1. **Create File Object**
   ```python
   from crow.file import File
   file = File("data.csv")
   ```

2. **Validate File** (Optional but recommended)
   ```python
   if file.Validate():
       print("File is valid")
   ```

3. **Load Data**
   ```python
   from crow.data import Data
   data = Data()
   data.Load(file)
   ```

4. **Perform Analysis**
   ```python
   from crow.statistics import Statistics
   stats = Statistics()
   stats.Load(data)
   
   mean = stats.Mean('column_name')
   ```

## Quick Reference

| Class | Purpose | Key Methods |
|-------|---------|-------------|
| `File` | File handling | `Validate()`, `GetPath()`, `GetSuffix()` |
| `Data` | Data loading | `Load()`, `GetData()` |
| `Statistics` | Statistical analysis | `Load()`, `Mean()`, `Variance()`, `Median()` |

## Type Hints

Crow is fully typed with type hints for better IDE support:

```python
from crow.file import File, FileExtension
from crow.data import Data
from crow.statistics import Statistics
import pandas as pd

file: File = File("data.csv")
suffix: FileExtension | None = file.GetSuffix()

data: Data = Data()
df: pd.DataFrame | None = data.GetData()

stats: Statistics = Statistics()
mean: pd.Series | float | int | None = stats.Mean('column')
```

## Next Steps

Explore the detailed API documentation for each class:

- [File Class](./file.mdx) - File handling and validation
- [Data Class](./data.mdx) - Data loading and access
- [Statistics Class](./statistics.mdx) - Statistical calculations
