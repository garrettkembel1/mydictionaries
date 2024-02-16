movie_ratings = {
    "Varsity Blues": 10,
    "Last Airbender": 2,
    "Devil Wears Prada": 6,
    "Into the Spiderverse": 9.5,
    "Days of Thunder": 8
}
print('\n')
movie_title = input('Please input a movie title: ')
print('\n')

def recommended_movie (movie_ratings, movie_title):
    if movie_title in movie_ratings:
            if movie_ratings[movie_title] >= 8:
                print (f'{movie_title} is a good movie with a rating of {movie_ratings[movie_title]}.')
                print('\n')
            else:
                print(f'{movie_title} does not have a rating over 8.')
                print('\n')
                print(f'Movies over a rating of 8 are: ')
                print('\n')
                for movie_ratings, movie_title in movie_ratings.items():
                    if movie_title >= 8:
                        print (movie_ratings)
                        print('\n')
    else:
        print('Movie is not in database')
        print('\n')
        print ('Movies we recommend are: ')
        print('\n') 
        for movie_ratings, movie_title in movie_ratings.items():
            if movie_title >= 8:
                print (movie_ratings)
                print('\n')

            
recommended_movie(movie_ratings, movie_title)


