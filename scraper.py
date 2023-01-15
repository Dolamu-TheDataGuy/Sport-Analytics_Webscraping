from TableScraper import Scraper

table = Scraper()
table.extract()
print(table.dataframe(18))
table.save(18)