#work with a collection of files
import os
import glob

import pandas as pd

game_files = glob.glob(os.path.join('F:\\Python-Baseball\\','games', '*.EVE')) #gets name of files, path from lesson is wrong
game_files.sort() #sort list of files by name

game_frames = []
#read content of files
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type','multi2','multi3','multi4','multi5','multi6','event']) #read current file in pandas data frame
    game_frames.append(game_frame) #add frame to game frames

games = pd.concat(game_frames) #what does this do

games.loc[games['multi5'] == '??', 'multi5'] = '' #replace rows with ?? with empty space in multi5 column. not working

identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})') #extract ids
identifiers = identifiers.fillna(method='ffill') #fill identifiers
identifiers.columns = ['game_id','year'] #change column labels

games = pd.concat([games, identifiers], axis=1, sort=False) #what does this do

games = games.fillna(' ') #fill Nan with empty space

games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type']) #reduce memory used by frame

print(games.head())
