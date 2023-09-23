from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(5)
    print(table.dataframe(5))
    table.save(5)

