from council_scrapers.base import BaseScraper, ScraperReturn, register_scraper
from bs4 import BeautifulSoup
import re

_STRATHFIELD_BASE_URL="https://www.strathfield.nsw.gov.au/"

@register_scraper
class StrathfieldNSWScraper(BaseScraper):
    current_year: int

    def __init__(self, current_year: int, **kwargs):
        self.current_year = current_year
        super.__init__(council_name="strathfield",
                       state="nsw",
                       base_url=_STRATHFIELD_BASE_URL)

    def scraper(self) -> ScraperReturn:
        self.logger.info(f"Starting {self.council_name} scraper")

        output = self.fetcher.fetch_with_requests(webpage_url)
        soup = BeautifulSoup(output, "html.parser")

if __name__ == "__main__":
    scraper = CamdenScraper()
    scraper.scraper()
