from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from my_books.books.models import Books
from my_books.books.serializers import BooksSerializer


class BooksListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the books for a requested user
        '''
        book_list = Books.objects.filter(user=request.user.id)
        serializer = BooksSerializer(book_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create a Book for the current user
        '''

        data = {
            'name': request.data.get('name'),
            'author': request.data.get('author'),
            'category': request.data.get('category'),
            'user': request.user.id
        }

        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
