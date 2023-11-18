from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(12)
    print(table.dataframe(12))
    table.save(12)

