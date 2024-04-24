"""Module to search for concepts using the Concept Trend Analyzer API."""
import requests

class ConceptTrendAnalyzer:
    def __init__(self):
        self.base_url = "https://api.openalex.org"

    def get_counts_by_year(self, concept_id):
        """
        Retrieve the values of works count and cited by count for the last ten years, binned by year.
        
        Args:
            concept_id (str): The ID of the concept to retrieve counts for.
        
        Returns:
            list: A list of dictionaries containing year, work counts, and cited counts.
        """
        counts_by_year_url = f"{self.base_url}/concepts/{concept_id}?select=counts_by_year"
        counts_by_year_response = requests.get(counts_by_year_url)
        counts_by_year_data = counts_by_year_response.json()
        
        # Extract and store year, work counts, and cited counts
        counts_data = []
        for entry in counts_by_year_data.get("counts_by_year", []):
            year = entry.get("year")
            works_count = entry.get("works_count")
            cited_by_count = entry.get("cited_by_count")
            counts_data.append({"year": year, "works_count": works_count, "cited_by_count": cited_by_count})
        
        return counts_data
