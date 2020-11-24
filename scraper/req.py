import sqlite3
import requests

#create and connect to DB
fightconn = sqlite3.connect('fightcade.db')

c = fightconn.cursor()

#create matches table
c.execute('''CREATE TABLE IF NOT EXISTS matches
            (
            match_id text,
            datetime integer,
            game_duration integer, 
            rom_id text,
            game_name text,
            first_to integer, 
            player_1_name text,
            player_1_country text,
            player_1_rank integer,
            player_1_wins integer, 
            player_2_name text,
            player_2_country text,
            player_2_rank integer,
            player_2_wins integer,
            live_views integer,
            game_replays integer
            )''')

#define http request for api data
url = 'https://www.fightcade.com/api/'
headers = {
    'authority': 'www.fightcade.com',
    'accept': 'application/json, text/plain, */*',
    'dnt': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 13421.73.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.112 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.fightcade.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.fightcade.com/replay',
    'accept-language': 'en-US,en;q=0.9,la;q=0.8,fi;q=0.7',
    'cookie': '__cfduid=d7b0cbb63ecf19048bbad28e9d390402a1605497854', 
    'sec-gpc': '1'
    }


offset = 0 #initial offset ie, start at the beginning. api only returns 15 at a time
matches = [] #will hold all the data to be stored in the db

while offset < 1000:

    #modifying the request to get the next 15 matches
    payload='{"req":"searchquarks","best":"true","offset":'+ str(offset) + ',"limit":15}'
    r = requests.post(url, headers=headers, data=payload)
    res = r.json()
    

    for match in res['results']['results']:
        p1 = match['players'][0]
        p2 = match['players'][1]

        matches.append(
            (
                match['quarkid'],
                match['date'],
                int(match['duration']),
                match['gameid'],
                match['channelname'],
                match['ranked'],
                p1['name'],
                p1['country'],
                p1['rank'],
                p1['score'],
                p2['name'],
                p2['country'],
                p2['rank'],
                p2['score'],
                match['realtime_views'] if 'realtime_views' in match else 0,
                match['saved_views'] if 'saved_views' in match else 0
            )
        )
    
    offset=res['results']['count']-1


c.executemany('INSERT INTO matches VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', matches)

fightconn.commit()
fightconn.close()