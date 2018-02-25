# Name of dataset: American Movies Scraped from Wikipedia
# Description: Name and related info about American Movies that are listed on Wikipedia
# Hyperlink: https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json
# Import mechanism:

import pymongo, requests, json

connection = pymongo.MongoClient("homer.stuy.edu")
db = connection["freudenbergJ-zorinM"]
movies = db["movies"]

# r = requests.get("https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json")
# data = r.json()

# for doc in data:
#     movies.insert_one(doc)


def get_year(year):
    year_cursor = movies.find({"year" : year})
    L = list()
    for movie in year_cursor:
        L.append(movie)
    return L

def get_director(director):
    direct_cursor = movies.find({"director" : director})
    L = list()
    for movie in direct_cursor:
        L.append(movie)
    return L

def director_genre(director, genre):
    cursor = movies.find({"director" : director, "genre" : genre})
    L = list()
    for movie in cursor:
        L.append(movie)
    return L

def director_year(director, year):
    cursor = movies.find({"director" : director, "year" : year})
    L = list()
    for movie in cursor:
        L.append(movie)
    return L

def get_movie(title):
    cursor = movies.find({"title" : title})
    L = list()
    for movie in cursor:
        L.append(movie)
    return L

if __name__ == '__main__':
    print "\nMovies from 2016:\n"
    print get_year(2016)
    print
    print "Movies by Christopher Nolan"
    print
    print get_director("Christopher Nolan")
    print
    print "Science Fiction Movies by Christopher Nolan"
    print
    print director_genre("Christopher Nolan", "Science fiction")
    print
    print "2014 movies by Christopher Nolan"
    print
    print director_year("Christopher Nolan", 2014)
    print
    print "Info about Interstellar"
    print
    print get_movie("Interstellar")
