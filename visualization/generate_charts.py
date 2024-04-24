"""Module to generate line charts for visualizing trends."""

import matplotlib.pyplot as plt

def generate_line_chart(years, works_counts, cited_by_counts, concept_name):
    """
    Generate a line chart to visualize the trend in works count and cited by count over the last ten years for a concept.
    
    Args:
        years (list): List of years.
        works_counts (list): List of works counts corresponding to each year.
        cited_by_counts (list): List of cited by counts corresponding to each year.
        concept_name (str): Name of the concept.
    """
    # Plot works count
    plt.plot(years, works_counts, label='Works Count')
    
    # Plot cited by count
    plt.plot(years, cited_by_counts, label='Cited By Count')
    
    # Set title and labels
    plt.title(f'Trend Analysis for {concept_name}')
    plt.xlabel('Year')
    plt.ylabel('Count')
    
    # Add legend
    plt.legend()
    
    # Show plot
    plt.show()
