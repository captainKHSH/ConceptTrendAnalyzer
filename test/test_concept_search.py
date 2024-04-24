"""Test module for Concept Trend Analyzer."""


def test_concept_search():
    """Test the ConceptSearch class."""
    from CTA.analyze.concept_search import ConceptSearch

    # Create an instance of ConceptSearch
    cs = ConceptSearch()

    # Test searching for a concept
    query = "Computer Science"
    search_results = cs.search(query)

    # Assert that search results are not empty
    assert search_results is not None
    assert "results" in search_results
    assert len(search_results["results"]) > 0


if __name__ == "__main__":
    # Run the test functions
    test_concept_search()

    print("All tests passed!")
