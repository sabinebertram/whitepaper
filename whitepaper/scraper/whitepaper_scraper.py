import os

import requests
import tika
from tika import parser

from scraper.duckduckgo_search import DuckDuckGo


class WhitepaperScraper():

    def __init__(self):
        tika.initVM()

    def scrape_many(self, companies, output_path):
        c = 0
        companies_to_scrape = companies.copy()
        while companies_to_scrape:
            company = companies_to_scrape[0]
            companies_to_scrape.pop(0)
            success = self.scrape(company, output_path)
            if success:
                c = 0
            else:
                companies_to_scrape.append(company)
                c +=1
            if c > len(companies):
                break
        successful_downloads = list(set(companies)-set(companies_to_scrape))
        return(successful_downloads, companies_to_scrape)

    def scrape(self, company, output_path):
        query = self._build_query(company)
        hits = DuckDuckGo.search(query)
        if hits:
            for hit in hits:
                pdf = self._download(hit)
                if pdf:
                    if self._is_whitepaper(pdf, company):
                        self._save(pdf, company, output_path)
                        break
                    else:
                        continue
                else:
                    continue
            return True
        else:
            return False

    def _build_query(self, company):
        return company + " whitepaper filetype:pdf"

    def _download(self, hit):
        href = hit.attrs['href']
        try:
            r = requests.get(href)
            r.raise_for_status()
            return r.content
        except:
            return None

    def _is_whitepaper(self, pdf, company):
        raw_pdf = parser.from_buffer(pdf)
        raw_text = raw_pdf['content']
        if raw_text and company.lower() in raw_text.lower() and ('whitepaper' in raw_text.lower() or 'white paper' in raw_text.lower()):
            return True
        else:
            return False

    def _save(self, pdf, company, output_path):
        with open(os.path.join(output_path, company + ".pdf"), 'wb') as f:
            f.write(pdf)
