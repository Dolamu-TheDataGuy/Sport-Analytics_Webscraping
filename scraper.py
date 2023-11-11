from TableScraper import Scraper


if __name__ == "__main__":
    table = Scraper()
    table.extract()
    table.to_json(11)
    print(table.dataframe(11))
    table.save(11)

