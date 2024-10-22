from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),  # Certifique-se de que a aplicação 'books' está incluída nas rotas
]
