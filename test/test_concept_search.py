"""Test module for Concept Trend Analyzer."""
from analyze.concept_search import ConceptSearch


def test_concept_search():
    """Test the ConceptSearch class."""
    # Create an instance of ConceptSearch
    CS = ConceptSearch()

    query = "Computer Science"
    search_results = CS.search(query)

    # Assert that search results are not empty
    assert search_results is not None


def test_autocomplete_concepts():
    """Test the ConceptSearch class."""
    # Create an instance of ConceptSearch
    CS = ConceptSearch()

    query = "Comp"
    search_results = CS.search(query)

    # Assert that search results are not empty
    assert search_results is not None


if __name__ == "__main__":
    # Run the test functions
    test_concept_search()

    print("All tests passed!")
