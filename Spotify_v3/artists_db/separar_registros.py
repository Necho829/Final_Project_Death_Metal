#  -*- coding: utf-8 -*-

import os


def separate_csv_bands():
    # Esta función es para separar la BD original en archivos más pequeños
    # La deje en 1000 por registros, pero la puedes cambiar a lo que quieras
    
    csv_path = '/home/pi/myProjects/Python/Spotify_v2/artists_db/'
    with open(csv_path + 'DM_bands.csv', 'r') as infile: 
        i=1
        for line in infile:
            if i == 1:
                head = line
            if i<=1001:
                with open(csv_path + 'F_1000_bands.csv','a') as f_1000:
                   f_1000.write(line)
                i = i + 1
            elif i in range(1002,2002):
                with open(csv_path + 'F_2000_bands.csv','a') as f_2000:
                    if i == 1002:
                        f_2000.write(head)
                        f_2000.write(line)
                    else:
                        f_2000.write(line)
                i = i + 1
            elif i in range(2002,3002):
                with open(csv_path + 'F_3000_bands.csv','a') as f_3000:
                    if i == 2002:
                        f_3000.write(head)
                        f_3000.write(line)
                    else:
                        f_3000.write(line)
                i = i + 1
        
        infile.close()
        f_1000.close()
        f_2000.close()
        f_3000.close()
                
    del csv_path, infile, line, i
    return 0



def main():
        
    returned_value = separate_csv_bands()
    del returned_value

if __name__ == "__main__":
    main()