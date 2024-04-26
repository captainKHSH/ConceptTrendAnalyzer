"""Module to search for concepts using the Concept Trend Analyzer API."""


import requests
from tabulate import tabulate


class ConceptSearch:
    """Class for searching concepts."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"

    def search(self, query):
        """
        Search for concepts using the Concept Trend Analyzer API.

        First, search using the concepts endpoint.
        If no results are found, search using the autocomplete endpoint.

        Args
        ----
            query (str): The query parameter for concept search.

        Returns
        -------
            dict: A dictionary containing the search results.
        """

        # First search using the concepts endpoint
        concepts_url = f"{self.base_url}/concepts?search={query}"
        concepts_response = requests.get(concepts_url)
        concepts_data = concepts_response.json()

        # If no results are found, search using the autocomplete endpoint
        if concepts_data["meta"]["count"] == 0:
            aut = f"{self.base_url}/autocomplete/concepts?q={query}"
            autocomplete_url = aut
            autocomplete_response = requests.get(autocomplete_url)
            autocomplete_data = autocomplete_response.json()
            # Parse top 5 IDs and display names from autocomplete response
            parsed_results = [
                {
                    "id": concept["id"].split("/")[-1],
                    "display_name": concept["display_name"],
                    "wikipedia": concept.get("ids", {}).get("wikipedia", "N/A"),
                }
                for concept in autocomplete_data["results"][:5]
            ]

        else:
            # Parse id, display_name, and wikipedia from concepts response
            parsed_results = [
                {
                    "id": concept["id"].split("/")[-1],
                    "display_name": concept["display_name"],
                    "wikipedia": concept["ids"]["wikipedia"],
                }
                for concept in concepts_data["results"][:5]
            ]
        table = []
        for item in parsed_results:
            table.append([item['id'], item['display_name'], item['wikipedia']])

        headers = ['ID', 'Display Name', 'Wikipedia Link']
        print(tabulate(table, headers, tablefmt='grid'))
        # Check if table is not empty
        if table:
            return True
        else:
            return None
