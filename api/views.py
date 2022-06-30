from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from .models import Book

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/book-list/',
        'Detail-view': '/book-detail/<int:id>',
        'Create': '/book-create/',
        'Update-view': '/book-update/<int:id>',
        'Delete-view': '/book-delete/<int:id>',
    }

    return Response(api_urls)


@api_view(['GET'])
def showAll(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewBook(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createBook(request):
    serializer = BookSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateBook(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=books, data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()

    return Response("Item deleted Successfully")
