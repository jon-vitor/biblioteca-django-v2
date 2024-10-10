from rest_framework import generics
from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from core.filters import LivroFilter


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    search_fields = ('^titulo',)
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    name = 'livro-list'


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-detail'


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    name = 'categoria-list'


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = 'categoria-detail'


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-list'


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = 'autor-detail'


# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Livro
# from .serializers import LivroSerializer


# @csrf_exempt
# def livro_list_create(request):
#    if request.method == 'GET':
#        livros = Livro.objects.all()
#        serializer = LivroSerializer(livros, many=True)
#        return Response(serializer.data)

#    if request.method == 'POST':
#        serializer = LivroSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# 3@csrf_exempt
# def livro_detail(request, pk):
#    livro = Livro.objects.get(pk=pk)
#
#    if request.method == 'GET':
#        serializer = LivroSerializer(livro)
#        return Response(serializer.data)
#
#    if request.method == 'PUT':
#        serializer = LivroSerializer(livro, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    if request.method == 'DELETE':
#        livro.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
# from core.filters import CategoriesFilter, BooksFilter, AuthorsFilter
