movie_ratings = {
    "Varsity Blues": 10,
    "Last Airbender": 2,
    "Devil Wears Prada": 6,
    "Into the Spiderverse": 9.5,
    "Avengers": 8
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
                for k, v in movie_ratings.items():
                    if v >= 8:
                        
                        print (k)
                        print('\n')
    else:
        print('Movie is not in database')
        print ('Movies we recommend are: ')
        print('\n') 
        for k, v in movie_ratings.items():
            if v >= 8:
                print (k)
                print('\n')

            
recommended_movie(movie_ratings, movie_title)


