from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(4)
    print(table.dataframe(4))
    table.save(4)

