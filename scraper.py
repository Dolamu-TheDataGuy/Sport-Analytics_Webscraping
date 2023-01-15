from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    print(table.dataframe(18))
    table.save(18)
