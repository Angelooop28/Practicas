from fastapi import FastAPI
from models.movie import Movie

app = FastAPI()

movies = [
    {
        'id': 1,
        'title': 'Anabelle',
        'description': 'pelicula de terror',
        'genero': 'terror'
    },

       {
        'id': 2,
        'title': 'Fast and furious',
        'description': 'pelicula de Accion',
        'genero': 'accion'
    },


       {
        'id': 3,
        'title': 'El padrino',
        'description': 'pelicula de accion',
        'genero': 'accion'
    }
]

@app.get('/')
def message ():
    return 'Hello world'


@app.get('/movies')
def get_movies ():
    return movies


@app.get('/movies/{id}')
def get_movie(id: int):
   return  list(filter(lambda item: item['id'] == id, movies))


@app.post('/movies')
def create_movie (movie: Movie):
    movies.append(Movie)
    return movies

@app.put ('/movies/{id}')
def update_movie (id: int, movie:Movie):
    for index, item in enumerate(movies):
        if item[id]==id:
            movies[index]['title']= movie.title
            movies[index]['description']= movie.description
            movies[index]['genero']= movie.genero
    return movies


