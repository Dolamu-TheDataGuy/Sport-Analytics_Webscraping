from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(7)
    print(table.dataframe(7))
    table.save(7)

