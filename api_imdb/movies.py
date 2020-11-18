from imdb import IMDb

class MovieSearcher:
    def __init__(self, movie_name):
        self.api = IMDb()
        try:
            self.search_movie_by_name(movie_name)
        except:
            raise
    
    def search_movie_by_name(self, name):
        self.movies = self.api.search_movie(name)
        self.movie = self.api.get_movie(self.movies[0].movieID)
        self.search_movie_by_id(0)
        return self.movies
    
    def search_movie_by_id(self, id):
        self.movie = self.api.get_movie(self.movies[id].movieID)
        self.get_available_info()
        return self.movie

    def get_available_info(self):
        infoset = self.movie.infoset2keys
        self.info = [str(info) for key in infoset for info in infoset[key]]
        self.extractInfos()
        return self.info

    def getInfo(self, key):
        return self.movie.get(key)

    def extractInfos(self):
        features = [
            'original title', 
            'cast', 
            'genres', 
            'runtimes', 
            'countries', 
            'box office', 
            'original air date', 
            'rating', 
            'languages', 
            'title', 
            'year', 
            'directors', 
            'writers', 
            'producers', 
            'composers', 
            'cinematographers', 
            'editors', 
            'casting directors', 
            'production designers', 
            'art directors', 
            'top 250 rank', 
            'production companies'
        ]
        self.data = {iten: self.__normalize_value__(self.movie.get(iten)) if iten in self.info else None for iten in features}

        fields = [k for k in self.data if type(self.data[k]) == type({})]
        for f in fields:
            for key in self.data[f]:
                self.data['{} - {}'.format(f, key)] = self.data[f][key]
            del self.data[f]


        
        return self.data

    def __normalize_value__(self, data):
        if type(data) == type([]):
            return [str(iten) for iten in data]
        if type(data) == type({}):
            return {k: str(data[k]) for k in data}
        return str(data)
    