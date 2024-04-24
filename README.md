# Concept-Trend-Analyzer

![GitHub repo size](https://img.shields.io/github/repo-size/Systems-and-Toolchains-Fall-2023/course-project-option-2-captainKHSH)
![GitLab last commit](https://img.shields.io/gitlab/last-commit/Systems-and-Toolchains-Fall-2023/course-project-option-2-captainKHSH)

The Concept Trend Analyzer (CTA) is a Python package designed to analyze trends related to various concepts using the Concept Trend Analyzer API. It provides functionality to search for concepts, retrieve related concepts, analyze trends over time, and visualize the trends using line charts.

## Features

- Concept Search: Search for concepts using keywords and retrieve relevant information such as display name, Wikipedia link, and related concepts.
- Related Concepts: Retrieve the top related concepts for a given concept ID.
- Concept Trend Analysis: Analyze trends in works count and cited by count over a specified number of years for a given concept.
- Visualization: Generate line charts to visualize trends in works count and cited by count for a given concept over time.

## Installation

To install the Concept Trend Analyzer package, simply use pip:
`pip install concept-trend-analyzer`

Usage
Here's how you can use the concept-trend-analyzer package:
`from CTA.utils import CS, RC, CAT, chart

# Search for concepts
search_results = CS.search('CONCEPT')

# Retrieve related concepts
related_concepts = RC.related('concept_id')

# Analyze concept trends
years, works_counts, cited_by_counts = CAT.year('concept_id', num_years=10)

# Generate line charts to visualize trends
chart.chart('concept_id', num_years=10)
`
