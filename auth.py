'''This file gets the Authorization token from the Spotify API.'''
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

AUTH_URL = 'https://accounts.spotify.com/api/token'

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET =  os.getenv('CLIENT_SECRET')

def get_auth():
    '''This function gets the Authorization token from the Spotify API.'''
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    auth_response_data = auth_response.json()
    token = auth_response_data['access_token']
    return token


if __name__ == '__main__':
    t = get_auth()
    print(t)
   