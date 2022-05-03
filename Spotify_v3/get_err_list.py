#  -*- coding: utf-8 -*-

## Funciones para re_procesar aquellos artista que se encuenten en la lista de errores.

import os
import api_to_csv

def get_err_list():
    
    #Desde archivo TXX
    
    txt_file = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/exec_logs/a_name_error_list.txt'
    
        
    #'''
    #csv_path = '/home/pi/myProjects/Python/Spotify_v2/artists_db/'
    with open(txt_file, 'r') as infile:
        artist_list=[]
        for line in infile.readlines():
            
            artist_list.append(str.strip(line.replace("\n","")))
            
    infile.close()
        
    command = 'mv /home/pi/myProjects/Python/Spotify_v3/exec_logs/a_name_error_list.txt /home/pi/myProjects/Python/Spotify_v3/exec_logs/a_name_error_list.txt.bak'
    returned_value = os.system(command)
    return artist_list 

def main():
        
    #returned_value = separate_csv_bands()
    artist_list = get_err_list()
    api_to_csv.main(artist_list)
    del artist_list

if __name__ == "__main__":
    main()
 
