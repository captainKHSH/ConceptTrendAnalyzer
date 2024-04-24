# Concept-Trend-Analyzer

![GitHub repo size](https://img.shields.io/github/repo-size/captainKHSH/Concept-Trend-Analyzer)
![GitLab last commit](https://img.shields.io/gitlab/last-commit/captainKHSH/Concept-Trend-Analyzer)

The Concept Trend Analyzer (CTA) is a Python package designed to analyze trends related to various concepts using the Concept Trend Analyzer API. It provides functionality to search for concepts, retrieve related concepts, analyze trends over time, and visualize the trends using line charts.

## Features

- Concept Search: Search for concepts using keywords and retrieve relevant information such as display name, Wikipedia link, and related concepts.
- Related Concepts: Retrieve the top related concepts for a given concept ID.
- Concept Trend Analysis: Analyze trends in works count and cited by count over a specified number of years for a given concept.
- Visualization: Generate line charts to visualize trends in works count and cited by count for a given concept over time.

## Installation

To install the Concept Trend Analyzer package, simply use pip:
```bash
pip install concept-trend-analyzer
```

## Usage

Here's how you can use the concept-trend-analyzer package:
```python
from .main import *
```

If you execute the `main.py` file, it will print the example usage code to the console. Then import the `utils.py`

```python
from .utils import *
```

### Search for concepts
```python
search_results = CS.search('CONCEPT')
```
### Retrieve related concepts
```python
related_concepts = RC.related('concept_id')
```
### Analyze concept trends
```python
years, works_counts, cited_by_counts = CAT.year('concept_id', num_years=10)
```
### Generate line charts to visualize trends
```python
chart.chart('concept_id', num_years=10)
```

## Requirements

The Concept Trend Analyzer package requires the following dependencies:

- Python 3.x
- requests
- matplotlib

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/captainKHSH/Concept-Trend-Analyzer/blob/main/LICENSE) file for details.

