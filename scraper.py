from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(10)
    print(table.dataframe(10))
    table.save(10)

