# project_ether

If you need to run the script to pull the data again, from the project_ether directory, run:
```
virtualenv --python=python3.7.3 env
source env/bin/activate
pip install -r requirements.txt
python scraper/req.py
```

## DB Schema

| Column Name     | Data Type  | What is?                 |
|-----------------|------------|--------------------------|
| match_id        | text       | unique id for that match |
| datetime        | int        | millisecond unix time    |
| game_duration   | int        | match duration, seconds  |
| rom_id          | text       | FC id for game played    |
| game_name       | text       | full name of game played |
| first_to        | int        | number of wins required  |
| player_1_name   | text       | p1 name                  |
| player_1_country| text       | 2-letter country code    |
| player_1_rank   | int        | p1 numeric rank          |
| player_1_wins   | int        | rounds won in this match |
| player_2_name   | text       | p1 name                  |
| player_2_country| text       | 2-letter country code    |
| player_2_rank   | int        | p1 numeric rank          |
| player_2_wins   | int        | rounds won in this match |
| live_views      | int        | how many watched live    |
| match_replays   | int        | how many have replayed   |