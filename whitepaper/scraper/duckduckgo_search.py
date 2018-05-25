import mechanicalsoup

class DuckDuckGo():
    
    @classmethod
    def _connect(cls):
        browser = mechanicalsoup.StatefulBrowser(
            user_agent='Mozilla/65',
            raise_on_404=True,
        )
        browser.open("https://duckduckgo.com/")
        return browser

    @classmethod
    def search(cls, query):
        browser = cls._connect()
        hits = []
        try:
            browser.select_form('#search_form_homepage')
            browser["q"] = query
            browser.submit_selected()
            hits = browser.get_current_page().select('a.result__a')
        finally:
            browser.close()
        return hits