#  -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

def dataframe_transformation():
    df_DM_bands_file = (r'C:\Users\nelso\Desktop\ironhacktareas\ih_datamadpt04222_Final_Project\Spotify_v3\artists_db\DM_bands.csv')
    df_DM_bands = pd.read_csv(df_DM_bands_file, encoding='utf-8')
    df_DM_bands['formed_in'] = df_DM_bands['formed_in'].values.astype(str)
    df_DM_bands['formed_in'] = df_DM_bands['formed_in'].str.slice(0,-2)
    #df_DM_bands['formed_in'] = df_DM_bands['formed_in'].values.astype(int)
    
    #df_DM_bands['name'] = df_DM_bands['name'].str.lower() 
    #df_DM_bands
    #list_artist_file = (r'C:\Users\nelso\Desktop\ironhacktareas\ih_datamadpt04222_Final_Project\Spotify_v3\temp_csv_files\Final_list_artist_v2.csv')
    list_artist_file =(r'C:\Users\nelso\Desktop\ironhacktareas\ih_datamadpt04222_Final_Project\Spotify_v3\files_backups\Final_list_artist_v2.csv')
    df_List_artist_2_2  = pd.read_csv(list_artist_file, encoding='utf-8')
    df_List_artist_2_2 ['genres'] = df_List_artist_2_2['genres'].astype('str')
    for char_value in ["'", "[","]",","]:
        df_List_artist_2_2 ['genres'] = df_List_artist_2_2['genres'].str.replace(char_value, "")
        
    df_List_artist_2_2  = df_List_artist_2_2 .drop(['id','type', 'href'], axis=1)
    df_List_artist_2_2.reset_index(drop=True)
    #df_List_artist_2_2['name'] = df_List_artist_2_2['name'].str.lower() 
    
    df_spot = df_List_artist_2_2 [(df_List_artist_2_2 ['genres'].str.contains('death'))]
    #df_spot

    df_leftjoin = df_DM_bands.merge(df_spot[['name', 'popularity', 'followers.total']], on='name', how='left')
    df_leftjoin.reset_index()
    #df_leftjoin = df_leftjoin.drop(['Unnamed: 8', 'Unnamed: 9'], axis=1)
    #df_leftjoin.loc[df_leftjoin.loc[:, 'name'] == 'cannibal corpse']

    #df_leftjoin['popularity'] = df_leftjoin['popularity'].replace(np.nan,'This band is not available on spotify')
    df_leftjoin['popularity'] = df_leftjoin['popularity'].replace(np.nan,'0')
    df_leftjoin['popularity'] = df_leftjoin['popularity'].values.astype(int)
    
    #df_leftjoin['followers.total'] = df_leftjoin['followers.total'].replace(np.nan,'This band is not available on spotify')
    df_leftjoin['followers.total'] = df_leftjoin['followers.total'].replace(np.nan,'0')
    df_leftjoin['followers.total'] = df_leftjoin['followers.total'].values.astype(int)
    
    df_leftjoin['theme'] = df_leftjoin['theme'].replace(np.nan,'Unknown')
    
    df_drop_2  = df_leftjoin.drop(['id'], axis=1)
    df_drop_2 = df_drop_2.rename({"name":"Name","country":"Country","status":"Status", "formed_in":"Formed In","genre":"Genre" , "theme":"Theme" , "active":"Active" , "popularity":"Spotify Popularity" , "followers.total":"Total Followers On Spotify" }, axis='columns')
    df_drop_2.reset_index(drop=True)
    #df_drop_2 ['Name']= df_drop_2['Name'].str.capitalize()

    path_tbd = r'C:\Users\nelso\Desktop\ironhacktareas\ih_datamadpt04222_Final_Project\dashboard_data.csv'
    df_drop_2.to_csv(path_tbd, index=False,mode='w')
    
    return 0

def main():
    returned_value = dataframe_transformation()
    del returned_value

if __name__ == '__main__':
    returned_value = main()
    del returned_value