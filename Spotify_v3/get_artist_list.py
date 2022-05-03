#  -*- coding: utf-8 -*-

import csv

def get_artist_list():
 
    #csv_file = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/artists_db/DM_bands.csv' 
    csv_file = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/artists_db/F_10_bands.csv' 
        
    with open(csv_file, 'r') as infile:
        reader = csv.reader(infile)
        artist_list=[]
        for col in reader:
            artist_list.append((col[1]))
            
    infile.close()
    artist_list.pop(0)
    #'''
    
    del reader, col
    
    return artist_list 

def main():
        
    #returned_value = separate_csv_bands()
    artist_list = get_artist_list()
    del artist_list

if __name__ == "__main__":
    main()
 
