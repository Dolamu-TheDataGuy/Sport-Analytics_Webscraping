from Table_Scraper import Scraper

table = Scraper()
table.extract()
print(table.dataframe(3))
table.save(3)