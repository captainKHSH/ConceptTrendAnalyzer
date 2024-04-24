"""Module for analyzing concept trends using the Concept Trend Analyzer API."""


import requests


class ConceptTrendAnalyzer:
    """Class for searching concepts and Trend-Analyzer."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"

    def year(self, concept_id, num_years=10):
        """
        Retrieve the values of works count.

        Cited by count for the last 'num_years' years, binned by year.

        Args
        ----
            concept_id (str): The ID of the
            concept to retrieve counts for.
            num_years (int): Number of years to
            retrieve counts for (default is 10).

        Returns
        -------
            tuple: A tuple containing lists of
            years, works counts, and cited counts.
        """
        cy = f"{self.base_url}/concepts/{concept_id}?select=counts_by_year"
        counts_by_year_url = cy
        counts_by_year_response = requests.get(counts_by_year_url)
        counts_by_year_data = counts_by_year_response.json()

        # Check if counts_by_year_data is None or empty
        if not counts_by_year_data:
            if "counts_by_year" not in counts_by_year_data:
                print("No data available for the specified concept.")
                return None, None, None

        # Extract and store year, work counts, and cited counts
        years = []
        works_counts = []
        cited_by_counts = []
        for entry in counts_by_year_data["counts_by_year"][:num_years]:
            year = entry.get("year")
            works_count = entry.get("works_count")
            cited_by_count = entry.get("cited_by_count")
            years.append(year)
            works_counts.append(works_count)
            cited_by_counts.append(cited_by_count)
        return years, works_counts, cited_by_counts

    @staticmethod
    def ytable(years, works_counts, cited_by_counts):
        """
        Print the search results as a table.

        Args
        ----
            years (list): List of years.
            works_counts (list): List of works
            counts corresponding to each year.
            cited_by_counts (list): List of cited
            by counts corresponding to each year.
        """
        # Print table header
        ini = "{:<10} {:<15} {:<15}"
        print(ini.format("Year", "Works Count", "Cited Count"))
        print("=" * 45)

        # Iterate over results and print each row
        for y, w, c in zip(years, works_counts, cited_by_counts):
            print(ini.format(y, w, c))
