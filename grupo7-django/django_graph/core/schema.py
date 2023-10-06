import graphene
from graphene_django import DjangoObjectType
from movies.models import Movie

class MovieType (DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "created_at")


class CreateMovieMutation (graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
    movie = graphene.Field(MovieType)
    
    def mutate (self, info, title, description):
        movie = Movie(title = title, description = description)
        movie.save()
        return CreateMovieMutation(movie = movie)
    

class DeleteMovieMutation (graphene.Mutation):
    class Arguments:
        id = graphene.ID(required = True)
    message = graphene.String()
    def mutate (self, info, id):
        movie = Movie.objects.get(pk = id)
        movie.delete()
        return DeleteMovieMutation(message ="Movie deleted")


class Query (graphene.ObjectType):
    movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, id = graphene.ID())

    def resolve_movies (self, info):
        return Movie.objects.all()
    def resolve_movie (self, info, id):
        return Movie.objects.get(pk = id)

class Mutation (graphene.ObjectType):
    create_movie = CreateMovieMutation.Field()
    delete_movie = DeleteMovieMutation.Field()

schema = graphene.Schema(query = Query, mutation = Mutation)