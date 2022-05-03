#  -*- coding: utf-8 -*-

import api_to_csv
import tunning_csv
import get_artist_list
import dataframe_transformation

def main():
       
    artist_name = get_artist_list.get_artist_list()
    api_to_csv.main(artist_name)
    tunning_csv.main()
    dataframe_transformation.main()
    
    print('\nFinalizado\n')
  
    
        
if __name__ == "__main__":
    returned_value = main()
    del returned_value