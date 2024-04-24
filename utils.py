"""Utility functions for the Concept Trend Analyzer package."""

# Import necessary classes from their respective modules
from Concept-Trend-Analyzer.analyze.concept_search import ConceptSearch
from Concept-Trend-Analyzer.analyze.RelatedConcepts import RelatedConcepts
from Concept-Trend-Analyzer.analyze.concept_trend_analyzer import ConceptTrendAnalyzer
from Concept-Trend-Analyzer.visualization.generate_charts import GenChart

print("Importing utilities for the Concept Trend Analyzer package...")

# Create instances of classes and store them in a dictionary
CS = ConceptSearch()
RC = RelatedConcepts()
CAT = ConceptTrendAnalyzer()
chart = GenChart()
