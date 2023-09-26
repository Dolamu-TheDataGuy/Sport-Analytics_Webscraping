from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(6)
    print(table.dataframe(6))
    table.save(6)

