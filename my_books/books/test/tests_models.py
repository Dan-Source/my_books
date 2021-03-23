from django.test import TestCase

from my_books.books.models import Books, Category, User

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Teste')
        self.category.save()

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEquals(str(self.category), 'Teste')
    
    def test_name_can_not_be_blank_and_null(self):
        field = Category._meta.get_field('name')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_name_value(self):
        self.assertEquals(self.category.name, 'Teste')

class BooksModelTest(TestCase):
    def setUp(self):
        self.user = User(username='test')
        self.user.set_password('#pass123')
        self.user.save()
        self.category = Category.objects.create(name='Teste')
        self.category.save()
        self.books = Books.objects.create(
            name='Books Teste',
            author='Author',
            user=self.user,
            pages=777,
            category=self.category
        )
    
    def test_create(self):
        self.assertTrue(Books.objects.exists())
    
    def test_str(self):
        self.assertEquals(str(self.books), 'Books Teste')

    def test_category_has_category(self):
        field = Books._meta.get_field('category')
        self.assertTrue(field.blank)
        self.assertFalse(field.null)
    
    def test_name_can_not_be_blank_and_null(self):
        field = Books._meta.get_field('name')
        self.assertFalse(field.blank)
        self.assertFalse(field.null)
    
    def test_category_value(self):
        self.assertEquals(self.books.category, self.category)

    def test_name_value(self):
        self.assertEquals(self.books.name, 'Books Teste')

    def test_pages_value(self):
        self.assertEquals(self.books.pages, 777)

    def test_description_value(self):
        self.assertEquals(self.books.author, 'Author')

