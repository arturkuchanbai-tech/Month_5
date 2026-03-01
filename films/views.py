from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Film
from .serializers import FilmDetailSerializer, FilmListSerializer,FilmReviewSerializer
@api_view(['GET'])
def film_reviews_list(request):
    film =Film.objects.prefetch_related('reviews').all()
    serialiser = FilmReviewSerializer(film,many=True)
    return Response(serialiser.data)
@api_view(['GET'])
def film_detail_api_view(request, id):
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        return Response(data={'error':'film does in not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    data=FilmDetailSerializer(film, many=False).data
    return Response(data=data)
@api_view(['GET'])
def film_list_api_view(request):
    film=Film.objects.select_related('director').prefetch_related('genre','reviews').all()
    data = FilmListSerializer(film,many=True).data
    return Response(data=data, status= status.HTTP_200_OK)
