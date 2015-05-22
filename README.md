# Paper-Scraper
Gets bibtex entries from spires and stores them in a convenient format.

## Basic setup
Requirements:
- Python 2.7
- Pip

First run 'python setup.py'

## Basic use
At present only arxiv numbers can be used to index.

Run 'python PaperScraper.py <ARXIVNUMBER>'


## Known issues
Need to ensure that all possible bibtex entries are in Article model. There will be a clever to do this with post_init signals that I'll look into.

Need to add search features and DOI lookups.
