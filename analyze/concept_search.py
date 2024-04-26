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
        # Print table header
        ini = "{:<15} {:<30} {:<50}"
        print(ini.format("ID", "Concept Display Name", "Wikipedia Link"))
        print("=" * 95)

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
        # Initialize an empty string to store the formatted table
        formatted_table = ""

        # Add the table headers
        formatted_table += "ID\t\t\tDisplay Name\t\t\tWikipedia Link\n"
        formatted_table += "-" * 70 + "\n"

        # Add each row of the table
        for item in parsed_results:
            id_str = item['id']
            display_name_str = item['display_name']
            wikipedia_link_str = item.get('wikipedia', '')

            # Adjust tabs for better alignment
            tabs_id = '\t' * (3 - len(id_str) // 8)
            tabs_display_name = '\t' * (3 - len(display_name_str) // 8)

            # Add the formatted row to the table
            formatted_table += f"{id_str}{tabs_id}{display_name_str}{tabs_display_name}{wikipedia_link_str}\n"

        return formatted_table
