import requests # Import library request
import json # Import library json

try: # Case movie or series exist
    request_type = int(input('Deseja um retorno completo ou simplificado? [0] para completo [1] para simplificado: ')) # User insert 1 for simplify return or 2 for complete return
    movie_serie = input('Digite o filme ou serie: ') # User insert movie or serie
    API_KEY = 'TOKEN_HERE' # Insert your token omdbapi in string format, example: 'f31sade'
    movie_serie = movie_serie.replace(' ', '+') # Space replace for + , used in method get api
    result_request = requests.get(f'http://www.omdbapi.com/?t={movie_serie}&plot=full&apikey={API_KEY}') # requests method get for api omdbapi

    request_dic = result_request.json() # Getting return from api in json file

    if request_type == 0: # Case in user choice is 0
        for key_dic in request_dic: # for all keys in dictionary json getting in api
            
            if key_dic == 'Poster': # Skip key 'Poster'
                continue

            if key_dic == 'Ratings': # Case key it is 'Ratings'
                print('Ratings : ', end=' ')
                for ratings in request_dic[key_dic]: # for all keys and content in dictionary 'Ratings'
                    for key_ratings_dic in ratings:
                        print(ratings[key_ratings_dic], end=' ')
                print()

            else: # Case not key it is 'Ratings'
                print(f'{key_dic} : {request_dic[key_dic]}') # Print content in dictionary
    
    else: # Case in user choice not is 0
        result_genre = request_dic['Genre'] # Saving content in key 'Genre' obtained in json file
        result_plot = request_dic['Plot'] # Saving content in key 'Plot' obtained in json file
        result_title = request_dic['Title'] # Saving content in key 'Title' obtained in json file

        print(f'Title : {result_title}') # Print content in key 'Title' for displays title
        print(f'Genre : {result_genre}') # Print content in key 'Genre' for displays genre
        print(f'Plot : {result_plot}') # Print content in key 'Plot' for displays plot

except: # Case movie or series dont exist
    print('Não foi possivel localizar este filme ou série!') # Print alert for movie or serie dont exist