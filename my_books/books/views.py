from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from my_books.books.models import Books
from my_books.books.serializers import BooksSerializer


class BooksListApiView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        '''
        List all the books for a requested user
        '''
        books = Books.objects.filter(user=request.user.id)
        serializer = BooksSerializer(books, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create a Book for the current user
        '''

        data = {
            'name': request.data.get('name'),
            'author': request.data.get('author'),
            'pages': request.data.get('pages'),
            'user': request.user.id,
            'category': request.data.get('category'),
        }

        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BooksListViewSet(ModelViewSet):
#     serializer_class = BooksSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
#     def get_queryset(self):
#         current_user = self.request.user
#         return Books.objects.filter(user=current_user)


class BooksDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    #http_method_names = ['get','put','head']

    def get_object(self, book_id, user_id):
        '''
        Helper method to get the object with given book_id and user_id
        '''
        try:
            return Books.objects.get(id=book_id, user=user_id)
        except Books.DoesNotExist:
            return None
    
    def get(self, request, book_id, *args, **kwargs):
        '''
        Retrieves the Book with given book_id
        '''
        book_instance = self.get_object(book_id, request.user.id)
        if not book_instance:
            Response(
                {"res": "Object with book_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = BooksSerializer(book_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, book_id, *args, **kwargs):
        '''
        Updates the Book item with given book_id if exists
        '''
        book_instance = self.get_object(book_id, request.user.id)
        if not book_instance:
            Response(
                {"res": "Object with book_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'author': request.data.get('author'),
            'pages': request.data.get('pages'),
            'user': request.user.id,
            'category': request.data.get('category'),
        }
        serializer = BooksSerializer(
            instance = book_instance, 
            data=data, 
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, book_id, *args, **kwargs):
        '''
        Deletes the Book item with given book_id if exists
        '''
        book_instance = self.get_object(book_id, request.user.id)
        if not book_instance:
            Response(
                {"res": "Object with book_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        book_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
