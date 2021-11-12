from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
import pandas as pd

class Scraper:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'Access-Control-Allow-Origin': 'www.skysports.com', 'Access-Control-Allow-Credentials': 'true', 
                        'ETag': 'a512df7a54821b88b7feee77a68304ddfe9e3d4a', 'Content-Type': 'text/html', 'Vary': 'Accept-Encoding',
                        'Content-Encoding': 'gzip', 'Cache-Control': 'max-age=211, s-maxage=300', 'Expires': 'Thu, 21 Oct 2021 11:05:34 GMT', 
                        'Date': 'Thu, 21 Oct 2021 11:02:03 GMT', 'Content-Length': '32362', 'Connection': 'keep-alive',
                        'Content-Security-Policy': 'frame-ancestors https://*.skysports.com http://*.skysports.com *.livefyre.com *.norkon.net *.google.com *.google.co.uk *.ampproject.org;'}
        self.baseurl = 'https://www.skysports.com/premier-league-table'
        
    def extract(self):
        self.Positions = []
        self.Teams = []
        self.played = []
        self.Won = []
        self.Drawn = []
        self.Lost = []
        self.GF= []
        self.GA = []
        self.GD = []
        self.Points = []
        r = self.session.get(self.baseurl, headers = self.headers)
        soup = bs(r.text, 'html.parser')
        league_table = soup.find('table', class_ = 'standing-table__table')
        for team in league_table.find_all('tbody'):
            rows = team.find_all('tr')
        for row in rows:
            pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
            self.Teams.append(pl_team)
            Position = row.find_all('td', class_='standing-table__cell')[0].text
            self.Positions.append(Position)
            games_played = row.find_all('td', class_='standing-table__cell')[2].text
            self.played.append(games_played)
            games_won = row.find_all('td', class_='standing-table__cell')[3].text
            self.Won.append(games_won)
            games_drawn = row.find_all('td', class_='standing-table__cell')[4].text
            self.Drawn.append(games_drawn)
            games_lost = row.find_all('td', class_='standing-table__cell')[5].text
            self.Lost.append(games_lost)
            goals_for = row.find_all('td', class_='standing-table__cell')[6].text
            self.GF.append(goals_for)
            goals_against = row.find_all('td', class_='standing-table__cell')[7].text
            self.GA.append(goals_against)
            goal_diff = row.find_all('td', class_='standing-table__cell')[8].text
            self.GD.append(goal_diff)
            pl_points = row.find_all('td', class_='standing-table__cell')[9].text
            self.Points.append(pl_points)
    
    def dataframe(self, i):
            self.table = pd.DataFrame({'Position': self.Positions, 'Teams': self.Teams,
                      'Games_Played': self.played, 'Games_Won': self.Won,
                      'Games_Drawn': self.Drawn, 'Games_Lost': self.Lost, 'GF': self.GF,
                      'GA': self.GA, 'GD': self.GD, 'Points': self.Points   
                     })
            self.table['Game_Week'] = 'GW' + str(i)
            self.table.set_index('Game_Week', inplace = True)
            return self.table
            
    def save(self,i):
            self.table.to_csv(f'pl_GW{i}.csv', index = False)        
        
        