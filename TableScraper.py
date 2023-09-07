from requests_html import HTMLSession
from requests import Response
from bs4 import BeautifulSoup as bs

import pandas as pd
from typing import Optional
from pandas import DataFrame
import json


class Scraper:
    """Scraper class that embeds functionalities of my Premier league Table Scraper
    """

    def __init__(self):
        self.session: HTMLSession = HTMLSession()
        self.headers: dict = {'Access-Control-Allow-Origin': 'www.skysports.com', 'Access-Control-Allow-Credentials': 'true',
                        'ETag': 'a512df7a54821b88b7feee77a68304ddfe9e3d4a', 'Content-Type': 'text/html',
                        'Vary': 'Accept-Encoding',
                        'Content-Encoding': 'gzip', 'Cache-Control': 'max-age=211, s-maxage=300',
                        'Expires': 'Thu, 21 Oct 2021 11:05:34 GMT',
                        'Date': 'Thu, 21 Oct 2021 11:02:03 GMT', 'Content-Length': '32362', 'Connection': 'keep-alive',
                        'Content-Security-Policy': 'frame-ancestors https://*.skysports.com http://*.skysports.com *.livefyre.com *.norkon.net *.google.com *.google.co.uk *.ampproject.org;'}
        self.baseurl: str = 'https://www.skysports.com/premier-league-table'
        self.goals_against: Optional[list] = None
        self.goals_for: Optional[list]  = None
        self.goal_diff: Optional[list] = None
        self.games_lost: Optional[list] = None
        self.game_drawn: Optional[list] = None
        self.pl_points: Optional[list] = None
        self.games_won: Optional[list] = None
        self.games_played: Optional[list] = None
        self.position: Optional[list] = None
        self.teams: Optional[list] = None
        self.table: Optional[list] = None
        self.json_data: dict = None

    def extract(self):
        """Function to extract Premier League table information
        """
        r: Response = self.session.get(self.baseurl, headers=self.headers)
        soup: bs = bs(r.text, 'html.parser')
        league_table = soup.find('table', class_='standing-table__table')
        rows = [team.find_all('tr') for team in league_table.find_all('tbody')][0]
        self.teams = [row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip() for row in
                      rows]
        self.position = [row.find_all('td', class_='standing-table__cell')[0].text for row in rows]
        self.games_played = [row.find_all('td', class_='standing-table__cell')[2].text for row in rows]
        self.games_won = [row.find_all('td', class_='standing-table__cell')[3].text for row in rows]
        self.game_drawn = [row.find_all('td', class_='standing-table__cell')[4].text for row in rows]
        self.games_lost = [row.find_all('td', class_='standing-table__cell')[5].text for row in rows]
        self.goals_for = [row.find_all('td', class_='standing-table__cell')[6].text for row in rows]
        self.goals_against = [row.find_all('td', class_='standing-table__cell')[7].text for row in rows]
        self.goal_diff = [row.find_all('td', class_='standing-table__cell')[8].text for row in rows]
        self.pl_points = [row.find_all('td', class_='standing-table__cell')[9].text for row in rows]

    def dataframe(self, i: int):
        """Function to put the information into a structured Table"""
        self.table: DataFrame = pd.DataFrame({'Position': self.position, 'Teams': self.teams,
                                   'Games_Played': self.games_played, 'Games_Won': self.games_won,
                                   'Games_Drawn': self.game_drawn, 'Games_Lost': self.games_lost, 'GF': self.goal_diff,
                                   'GA': self.goals_against, 'GD': self.goal_diff, 'Points': self.pl_points
                                   })
        self.table['Game_Week'] = 'GW' + str(i)
        self.table.set_index('Game_Week', inplace=True)
        return self.table

    def to_json(self, gw: int):
        self.club_content: dict = {}

        for i in range(20):
            self.club_content[i + 1] = {}
            self.club_content[i + 1]["Position"] = self.position[i]
            self.club_content[i + 1]['Club_Name'] = self.teams[i]
            self.club_content[i + 1]['Games_Played'] = self.games_played[i]
            self.club_content[i + 1]['Games_Won'] = self.games_won[i]
            self.club_content[i + 1]['Games_Lost'] = self.games_lost[i]
            self.club_content[i + 1]['Goals_Scored'] = self.goals_for[i]
            self.club_content[i + 1]['Goals_Conceded'] = self.goals_against[i]
            self.club_content[i + 1]['Goal_difference'] = self.goal_diff[i]
            self.club_content[i + 1]['Points'] = self.pl_points[i]
        print(self.club_content)

        with open(f'Json_files/data_GW{gw}.json', 'w') as f:
            json.dump(self.club_content, f, indent=5)

    def save(self, i: int):
        """Function to save Premier league table to a csv file"""
        self.table.to_csv(f'files/PL_GW{i}.csv', index=False)
