---
sidebar_position: 1
---

# Introduction to Crow

Welcome to **Crow** - a Python library designed for statistical analysis across multiple data formats.

## What is Crow?

Crow is a lightweight statistical analysis library that simplifies working with data from various file formats. Whether you're analyzing CSV files, Excel spreadsheets, JSON data, or text files, Crow provides a unified interface for loading and analyzing your data.

## Key Features

### 📊 Multi-Format Support

Crow supports reading data from:
- **CSV** files (`.csv`)
- **Excel** files (`.xlsx`, `.xls`)
- **JSON** files (`.json`)
- **Text** files (`.txt`)

### 🧮 Statistical Analysis

Perform essential statistical calculations:
- **Mean** (arithmetic average)
- **Variance** (measure of data spread)
- **Median** (middle value)

### 🚀 Simple API

Built with simplicity in mind:
- Easy-to-use class-based interface
- Powered by pandas for reliable data processing
- Type hints for better IDE support

## Quick Example

```python
from crow.file import File
from crow.data import Data
from crow.statistics import Statistics

# Load data from a CSV file
file = File("data.csv")
data = Data()
data.Load(file)

# Perform statistical analysis
stats = Statistics()
stats.Load(data)

# Get results
print(f"Mean: {stats.Mean('column_name')}")
print(f"Variance: {stats.Variance('column_name')}")
print(f"Median: {stats.Median('column_name')}")
```

## Why Crow?

- **Unified Interface**: Work with different file formats using the same API
- **Type Safe**: Built with type hints for better development experience
- **Pandas-Powered**: Leverages the battle-tested pandas library
- **Extensible**: Easy to extend with additional statistical methods

## Next Steps

- [Getting Started](./getting-started.md) - Installation and setup guide
- [User Guide](./user-guide.md) - Comprehensive usage guide
- [API Reference](./api/overview.md) - Detailed API documentation
