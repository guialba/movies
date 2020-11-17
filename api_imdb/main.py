import sys
from imdb import IMDb


def search_movie_by_name(name):
    ia = IMDb()

    movies = ia.search_movie(name)

    for movie in movies:
        print(movie)

    i = input()

    movie = ia.get_movie(movies[int(i)-1].movieID)

    for k in movie.infoset2keys:
        print(k)
    
    # print("Cast: ",movie.get('cast'))
    # print("Genres: ",movie.get('genres'))
    # print("Runtimes: ",movie.get('runtimes'))
    # print("Countries: ",movie.get('countries'))
    # print("country codes: ",movie.get('country codes'))
    # print("language codes: ",movie.get('language codes'))
    # print("color info: ",movie.get('color info'))
    # print("aspect ratio: ",movie.get('aspect ratio'))
    # print("sound mix: ",movie.get('sound mix'))
    # print("certificates: ",movie.get('certificates'))
    # print("Original Date: ",movie.get('original air date'))
    # print("Rating: ",movie.get('rating'))
    # print("Plot outline: ",movie.get('plot outline'))
    # print("Title: ",movie.get('title'))
    # print("Year: ",movie.get('year'))
    # print("Kind: ",movie.get('kind'))
    # print("Directors: ",movie.get('directors'))
    # print("Writers: ",movie.get('writers'))
    # print("Producers: ",movie.get('producers'))
    # print("Composers: ",movie.get('composers'))
    # print("Cinematographers: ",movie.get('cinematographers'))
    # print("Editors: ",movie.get('editors'))
    # print("editorial department: ",movie.get('editorial department'))
    # print("casting directors: ",movie.get('casting directors'))
    # print("production designers: ",movie.get('production designers'))
    # print("art directors: ",movie.get('art directors'))
    # print("set decorators: ",movie.get('set decorators'))
    # print("costume designers: ",movie.get('costume designers'))
    # print("make up department: ",movie.get('make up department'))
    # print("production managers: ",movie.get('production managers'))
    # print("assistant directors: ",movie.get('assistant directors'))
    # print("art department: ",movie.get('art department'))
    # print("sound department: ",movie.get('sound department'))
    # print("special effects: ",movie.get('special effects'))
    # print("visual effects: ",movie.get('visual effects'))
    # print("camera department: ",movie.get('camera department'))
    # print("casting department: ",movie.get('casting department'))
    # print("costume departmen: ",movie.get('costume departmen'))
    # print("location management: ",movie.get('location management'))
    # print("music department: ",movie.get('music department'))
    # print("script department: ",movie.get('script department'))
    # print("transportation department: ",movie.get('transportation department'))
    # print("miscellaneous: ",movie.get('miscellaneous'))
    # print("thanks: ",movie.get('thanks'))
    # print("akas: ",movie.get('akas'))
    # print("writer: ",movie.get('writer'))
    # print("director: ",movie.get('director'))
    # print("top 250 rank: ",movie.get('top 250 rank'))
    # print("production companies: ",movie.get('production companies'))
    # print("distributors: ",movie.get('distributors'))
    # print("special effects companies: ",movie.get('special effects companies'))
    # print("other companies: ",movie.get('other companies'))
    # print("plot: ",movie.get('plot'))
    # print("synopsis: ",movie.get('synopsis'))



def main(params):
    params = params[1:]
    search_movie_by_name(params[0])


if __name__ == "__main__":
    params = sys.argv[1:]
    main(sys.argv)

