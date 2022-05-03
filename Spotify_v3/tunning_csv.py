#  -*- coding: utf-8 -*-


from datetime import timedelta
import os
import time

def clean_csv_duplicated():
    #Elimina los registros duplicados
    csv_file_in = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/temp_csv_files/_list_artist.csv'
    csv_file_out = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/temp_csv_files/Final_list_artist.csv'
    
    with open(csv_file_in, 'r',  encoding='utf-8') as infile, open(csv_file_out,'w', encoding='utf-8') as outfile:
        seen = set()
        for line in infile:
            if line in seen: continue
            
            seen.add(line)
            outfile.write(line)
        
        infile.close()
        outfile.close()
                
    del csv_file_in, csv_file_out, infile, line, seen
    return 0

def remove_csv_columns():
    # Elimina los registros con los generos vacios ([])
    csv_file_in = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/temp_csv_files/Final_list_artist.csv'
    csv_file_out ='C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/temp_csv_files/Final_list_artist_v2.csv'
    with open(csv_file_in, 'r', encoding='utf-8') as infile, open(csv_file_out,'w', encoding='utf-8') as outfile:
        
        count = 0
        for line in infile:
            if line[0:3] == '[],':
                count = count + 1
            else:         
                outfile.write(line)
        
        infile.close()
        outfile.close()
                
    del csv_file_in, csv_file_out, infile, line
    return 0
    

def remove_csv_files():
    csv_file_in = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/temp_csv_files/Final_list_artist.csv'
    os.remove(csv_file_in)
            
    return 0

def main():
    
    returned_value = clean_csv_duplicated()
    time.sleep(0.01)
    returned_value = remove_csv_columns()
    #returned_value = remove_csv_files()
    del returned_value
    return 0

if __name__ == "__main__":
    returned_value = main()
    del returned_value
    