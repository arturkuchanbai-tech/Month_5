from rest_framework import serializers
from .models import Film, Director, Review, Genre

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'stars']

class GenreSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, genre):
        return genre.film_set.count()

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'fio']

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class FilmReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Film
        fields = ['id', 'title', 'rating', 'reviews']

    def get_rating(self, film):
        reviews = film.reviews.all()
        if not reviews:
            return 0
        return round(sum(i.stars for i in reviews) / reviews.count(), 1)

class FilmListSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    genres = serializers.SerializerMethodField()  

    class Meta:
        model = Film
        fields = ['id', 'title', 'rating', 'release_year', 'director', 'genres', 'reviews']
        depth = 1

    def get_genres(self, film):
        return film.genre_names()[0:2]