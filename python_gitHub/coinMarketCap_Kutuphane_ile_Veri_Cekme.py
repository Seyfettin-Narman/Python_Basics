from cryptocmd import CmcScraper
scraper=CmcScraper("TRX","12-01-2022","15-01-2022")
basliklar,veriler=scraper.get_data()
json_veri=scraper.get_data("json")
scraper.export("csv")
vk=scraper.get_dataframe()
