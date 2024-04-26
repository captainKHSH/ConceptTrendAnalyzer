"""Module to search for concepts using the Concept Trend Analyzer API."""


import requests


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
        
        # Print table header
        ini = "{:<15} {:<30} {:<50}"
        print(ini.format("ID", "Concept Display Name", "Wikipedia Link"))
        print("=" * 95)

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
                }
                for concept in autocomplete_data["results"][:5]
            ]

            # Print the results in table format
            R = self.print_results_table({"results": parsed_results})

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

            # Print the results in table format
            R = self.print_results_table({"results": parsed_results})
            return R

    @staticmethod
    def print_results_table(results):
        """
        Print the search results in a table format.

        Args
        ----
            results (dict): A dictionary containing the search results.
        """

        # Iterate over results and print each row
        for result in results["results"]:
            concept_id = result["id"]
            display_name = result["display_name"]
            wikipedia_link = result.get("wikipedia", "N/A")
            print(ini.format(concept_id, display_name, wikipedia_link))
