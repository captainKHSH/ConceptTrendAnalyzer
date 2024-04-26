"""Setup for the package."""
from setuptools import setup, find_packages

setup(
    name="CTA",
    version="1.0.0",
    description="A Python package for concept search and trend analysis using \
    the OpenAlex database.",
    maintainer="Kiran Prasad J P",
    maintainer_email="kjamunap@andrew.cmu.edu",
    license="MIT",
    packages=find_packages(),  # Automatically find packages
    install_requires=["requests", "matplotlib"],  # Dependencies
    long_description="""The Concept Trend Analyzer package provides a Python
    interface for accessing the OpenAlex database to perform concept search
    and trend analysis. With this package, users can easily search for concepts
    using a query parameter, retrieve related concepts, and analyze trends in
    works count and cited by count over ten years.
    Leveraging the OpenAlex database,
    this package aims to facilitate concept exploration and
    trend analysis, enabling
    users to gain valuable insights into research trends and identify emerging
    topics of interest.""",
)
