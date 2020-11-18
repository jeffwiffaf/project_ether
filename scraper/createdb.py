import sqlite3

fightconn = sqlite3.connect('fightcade.db')

c = fightconn.cursor()

c.execute('''CREATE TABLE players
             (name text PRIMARY KEY, date_joined integer, time_played integer, ranked text, country text)''')

c.execute('''CREATE TABLE games
             (rom text PRIMARY KEY, emulator text, game_name text, ranked_game text)''')

c.execute('''CREATE TABLE play_times
            (rom text,
            player text ,
            hours integer, 
            player_rank text, 
            ranked_matches integer)''')

c.execute('''CREATE TABLE matches
            (
            datetime integer, 
            rom text,
            first_to integer, 
            player1 text,
            player_1_wins integer, 
            player2 text,
            player_2_wins, 
            game_duration integer, 
            game_replays integer)''')



fightconn.commit()
fightconn.close()
