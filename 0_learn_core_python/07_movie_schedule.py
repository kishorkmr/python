current_movies = {'movie1':'10:00am','movie2':'01:00pm','movie3':'03:00pm',
                    'movie4':'06:00pm','movie5':'08:00pm'}

#print the disctionary
print(current_movies)

print("We're playing the following movies:")

for key in current_movies:
    print(key)

movie = input('What moviw would you like the showtime for?\n')

#method 1 to get the value for a key
#show_time = current_movies[movie]
#print(show_time)

#input - movie, output - 10:00am
#input - worng_movie, output - KeyError: 'worng_movie'

#method 2 to get the value for a key
show_time = current_movies.get(movie)
if show_time == None:
    print("Requested movie isn't playing")
else:
    print(movie, 'is playing at', show_time)

#input - movie, output - Requested movie isn't playing
#input - movie5, output - movie5 is playing at 08:00pm
