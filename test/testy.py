"""Test module for Concept Trend Analyzer."""


def test_concept_search():
    """Test the ConceptSearch class."""
    from CTA.analyze.concept_search import ConceptSearch

    # Create an instance of ConceptSearch
    cs = ConceptSearch()

    # Test searching for a concept
    query = "computer"
    search_results = cs.search(query)

    # Assert that search results are not empty
    assert search_results is not None
    assert "results" in search_results
    assert len(search_results["results"]) > 0


def test_related_concepts():
    """Test the RelatedConcepts class."""
    from CTA.analyze.RelatedConcepts import RelatedConcepts

    # Create an instance of RelatedConcepts
    rc = RelatedConcepts()

    # Test retrieving related concepts
    concept_id = "C41008148"  # Replace with a valid concept ID
    related_concepts = rc.related(concept_id)

    # Assert that related concepts are not empty
    assert related_concepts is not None
    assert len(related_concepts) > 0


def test_concept_trend_analyzer():
    """Test the ConceptTrendAnalyzer class."""
    from CTA.analyze.concept_trend_analyzer import ConceptTrendAnalyzer

    # Create an instance of ConceptTrendAnalyzer
    cta = ConceptTrendAnalyzer()

    # Test analyzing trends for a concept
    concept_id = "C41008148"  # Replace with a valid concept ID
    years, works_counts, cited_by_counts = cta.year(concept_id)

    # Assert that trends data is not empty
    assert years is not None
    assert works_counts is not None
    assert cited_by_counts is not None


if __name__ == "__main__":
    # Run the test functions
    test_concept_search()
    test_related_concepts()
    test_concept_trend_analyzer()

    print("All tests passed!")
