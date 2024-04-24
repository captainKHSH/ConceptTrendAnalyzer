"""Module for extracting name and description."""


import requests


class Conceptname:
    """Class for getting name and description."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"

    def name(self, concept_id):
        """
        Initialize the ConceptName object with a given name.

        Args
        ----
            concept_id (str): The ID of the concept.

        Returns
        -------
            dict: A dictionary containing the display name and description.
        """
        # Construct the URL for the concept
        concept_url = f"{self.base_url}/concepts/{concept_id}"

        # Send a GET request to retrieve information about the concept
        response = requests.get(concept_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            concept_data = response.json()

            # Extract the display name and description
            display_name = concept_data.get("display_name")
            description = concept_data.get("description")

            # Return the extracted information
            return {"display_name": display_name, "description": description}
        else:
            # Print an error message if the request was not successful
            print(
                f"Failed to retrieve information for \
            concept {concept_id}. Status code: {response.status_code}"
            )
            return None
