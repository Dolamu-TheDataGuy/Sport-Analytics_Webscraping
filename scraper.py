from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(9)
    print(table.dataframe(9))
    table.save(9)

