movie_ratings = {
    "Varsity Blues": 10,
    "Last Airbender": 2,
    "Devil Wears Prada": 6,
    "Into the Spiderverse": 9.5,
    "Avengers": 8
}
movie_title = input('Please input a movie title: ')

def recommended_movie (movie_ratings, movie_title):
    for movie_ratings, movie_title in movie_ratings.items:
        if movie_title in motive_ratings:
            if movie_ratings(movie_title) >= 8:
                print (f'{movie_title} is a good movie with a rating of {v}.')
        else:
                print(f'{movie_title} does not have a rating over 8.')
                for movie_ratings, movie_title in movie_ratings.items: 
                    print(f'Movies over a rating of 8 are {k}.')
    else:
        print('Movie is not in database')
        if movie_title >= 8:
            print (f'Movies we recommend are {k}')

            
recommended_movie(movie_ratings, movie_title)


