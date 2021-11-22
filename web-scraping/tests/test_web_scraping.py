from web_scraping import __version__


def test_version():
    assert __version__ == '0.1.0'

from web_scraping.web_scraping import *


def test_get_citations_needed_count():
    assert get_citations_needed_count

def test_get_citations_needed_report():
    assert test_get_citations_needed_report

