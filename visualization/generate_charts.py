"""Module for generating line charts to visualize trends."""

import matplotlib.pyplot as plt
from CTA.analyze.concept_trend_analyzer import ConceptTrendAnalyzer
from CTA.visualization.name import Conceptname


class GenChart:
    """Class for generating line charts to visualize trends."""

    @staticmethod
    def chart(concept_id, num_years=10):
        """Generate a line chart to visualize the trend.

        In works count and cited by count over the last
        'num_years' years for a concept.

        Args:
        ----
            concept_id (str): The ID of the concept to retrieve counts for.
            num_years (int): Number of years to retrieve counts
            (default is 10).
        -------------------------------------------------.
        """
        # Create an instance of ConceptTrendAnalyzer
        trend = ConceptTrendAnalyzer()

        # Create an instance of Conceptname to retrieve the concept name
        concept_name_extractor = Conceptname()
        concept_info = concept_name_extractor.name(concept_id)

        # Extract concept name and description
        concept_name = concept_info.get("display_name")
        concept_description = concept_info.get("description")
        print(
            "\n CONCEPT NAME:",
            concept_name,
            "\n \n DESCRIPTION:",
            concept_description,
            "\n",
        )

        # Retrieve counts by year
        extention = trend.year(concept_id, num_years)
        years, works_counts, cited_by_counts = extention

        # Plot works count
        plt.figure(figsize=(10, 5))
        plt.bar(years, works_counts, color="blue", label="Works Count")
        plt.plot(
            years,
            works_counts,
            label="Works Count",
            color="red",
            marker="o",
            linestyle="-",
            linewidth=2,
        )
        plt.title(f"Works Count Trend Analysis for {concept_name}")
        plt.xlabel("Year")
        plt.ylabel("Works Count")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot cited by count
        plt.figure(figsize=(10, 5))
        plt.bar(years, cited_by_counts, color="green", label="Cited By Count")
        plt.plot(
            years,
            cited_by_counts,
            label="Cited By Count",
            color="orange",
            marker="x",
            linestyle="-",
            linewidth=2,
        )
        plt.title(f"Cited By Count Trend Analysis for {concept_name}")
        plt.xlabel("Year")
        plt.ylabel("Cited By Count")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot stacked bar plot
        plt.figure(figsize=(10, 5))
        plt.bar(years, works_counts, color="blue", label="Works Count")
        plt.bar(
            years,
            cited_by_counts,
            bottom=works_counts,
            color="orange",
            label="Cited By Count",
        )

        # Set title, labels, and legend
        plt.title(f"Trend Analysis for {concept_name}")
        plt.xlabel("Year")
        plt.ylabel("Count")
        plt.grid(True)
        plt.legend()

        # Show plot
        plt.show()
