"""Module to search for concepts using the Concept Trend Analyzer API."""
import requests

class relatedconcepts:
    def __init__(self):
        self.base_url = "https://api.openalex.org"

    def fetch_related_concepts(self, concept_id):
        """
        Fetch the top ten related concepts for a given concept ID.
        
        Args:
            concept_id (str): The ID of the concept to fetch related concepts for.
        
        Returns:
            list: A list containing the top ten related concepts with their IDs and display names.
        """
        related_concepts_url = f"{self.base_url}/concepts/{concept_id}?select=related_concepts"
        related_concepts_response = requests.get(related_concepts_url)
        related_concepts_data = related_concepts_response.json()
        related_concepts = related_concepts_data.get("related_concepts", [])[:10]  # Extract top ten related concepts
        return [{"id": related_concept["id"].split("/")[-1], "display_name": related_concept["display_name"]} for related_concept in related_concepts]
