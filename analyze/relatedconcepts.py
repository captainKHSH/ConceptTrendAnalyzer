"""Module to search for concepts using the Concept Trend Analyzer API."""


import requests


class RelatedConcepts:
    """Class for searching related concepts."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"

    def related(self, concept_id):
        """
        Fetch the top ten related concepts for a given concept ID.

        Args
        ----
            concept_id (str): The ID of the concept
            to fetch related concepts for.

        Returns
        -------
            list: A list containing the top ten related
            concepts with their IDs and display names.
        """
        rc = f"{self.base_url}/concepts/{concept_id}?select=related_concepts"
        related_concepts_url = rc
        related_concepts_response = requests.get(related_concepts_url)
        related_concepts_data = related_concepts_response.json()
        relatedconcept = related_concepts_data.get("related_concepts", [])[:10]
        Results = [
            {
                "id": related_concept["id"].split("/")[-1],
                "display_name": related_concept["display_name"],
            }
            for related_concept in relatedconcept
        ]
        self.print_results_table({"results": Results})

    @staticmethod
    def print_results_table(results):
        """
        Print the search results in a table format.

        Args
        ----
            results (dict): A dictionary containing the search results.
        """
        # Print table header
        print("{:<15} {:<30}".format("ID", "Related Concept Names"))
        print("=" * 45)

        # Iterate over related concepts and print each row
        for related_concept in results["results"]:
            concept_id = related_concept["id"]
            display_name = related_concept["display_name"]
            print("{:<15} {:<30}".format(concept_id, display_name))
