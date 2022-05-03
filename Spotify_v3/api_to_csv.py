
import base64
import time
import requests
import pandas as pd
import _credentials_
import get_artist_list



def get_access_token():

    # URLS
    AUTH_URL    = 'https://accounts.spotify.com/authorize'
    TOKEN_URL   = 'https://accounts.spotify.com/api/token'
    CLIENT_ID   = _credentials_.CLIENT_ID
    CLIENT_SECRET = _credentials_.CLIENT_SECRET

    # Ver Autorization Code Flow: 'https://developer.spotify.com/documentation/general/guides/authorization/code-flow/'
    auth_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': 'http://localhost:8888/callback',
        'scope': 'user-read-private',
    }
        
    auth_code = requests.get(AUTH_URL, auth_params)
    auth_header = base64.urlsafe_b64encode(bytes(CLIENT_ID + ':' + CLIENT_SECRET, 'utf-8'))
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % auth_header.decode('ascii')
    }

    payload = {
        'grant_type': 'client_credentials',
        'code': auth_code,
        'redirect_uri': 'https://open.spotify.com/collection/playlists',
    }

    # request to /token endpoint. aquí obtenermos el token de acceso 
    access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)
    access_token = access_token_request.json()

    return  access_token

def search_artist(atoken, BASE_URL, name):
    pass
    search_headers = {
        'Content-Type': 'application/json',
        'Authorization': (atoken['token_type'] + " " + atoken['access_token'])
    }
    search_pamans = {
        'q': name, 
        'type':'artist',
        'limit':50,
        'offset': 0,
        'include_external': 'FALSE'
        
    }

    new_search_status = requests.get( BASE_URL + 'search?', headers=search_headers, params=search_pamans)
    new_search = new_search_status.json()
    
    line = (name + ',' + atoken['token_type'] + ':' + atoken['access_token'] + ',' + str(new_search_status.status_code) + '\n')
    
    with open('C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/exec_logs/search_status.txt', 'a') as request_status:
        request_status.write(line)
        request_status.close()
    
    return new_search

def write_to_csv(asearch):
    csv_path = 'C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/temp_csv_files/_list_artist.csv'
    csv_data = pd.DataFrame()
    csv_data = pd.json_normalize(asearch['artists']['items'],max_level=1)
    csv_data = csv_data.reset_index(drop=True)
    
    if len(csv_data)==0:
        csv_data = csv_data.reset_index(drop=True)
    else:
        csv_data = csv_data.drop(columns=["images","uri","external_urls.spotify","followers.href"])
        csv_data = csv_data.reset_index(drop=True)
    #print(csv_data)            # imprime el dataframe en pantalla
    csv_data.to_csv(csv_path,index=False,mode='a')
    
    del asearch, csv_data
    
    return 0
 
def validate_token_expire(atoken, token_start_time):
    status = 1
    token_end_time = time.perf_counter() 
        
    try:
        token_actual_time = round((token_end_time-token_start_time),0) 
        
        if (token_actual_time) >= (atoken['expires_in']-100):
        
            del atoken, token_start_time, token_actual_time
            status = 0
    except Exception:
        status = 0
    
    return status
        
    

def main(artist_name):
    
    BASE_URL    = 'https://api.spotify.com/v1/'
    
    status = 1
    
    atoken = get_access_token()
    token_start_time = time.perf_counter() 

    for a_name in artist_name:
        
        time.sleep(0.1)
        try:
            asearch = search_artist(atoken, BASE_URL, a_name)
            returned_value = write_to_csv(asearch)
            status = validate_token_expire(atoken, token_start_time)
            
            if status == 0:
                del atoken, token_start_time
                atoken = get_access_token()
                token_start_time = time.perf_counter() 
            
            del asearch, returned_value
        
        except Exception:
            with open('C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/exec_logs/a_name_error_list.txt', 'a') as error_list:
                error_list.write(a_name + '\r')
                error_list.close()
            continue
        
        else:
            with open('C:/Users/nelso/Desktop/ironhacktareas/ih_datamadpt04222_Final_Project/Spotify_v3/exec_logs/a_name_processed_list.txt', 'a') as processed_list:
                processed_list.write(a_name + '\r')
                processed_list.close()
            continue 
    del BASE_URL, artist_name, atoken
    return 0

if __name__ == "__main__":
    artist_name = get_artist_list.get_artist_list()
    returned_value = main(artist_name)
    del returned_value, artist_name