from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(8)
    print(table.dataframe(8))
    table.save(8)

