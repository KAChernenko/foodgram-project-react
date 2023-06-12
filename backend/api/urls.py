from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import UserViewSet, TagViewSet, IngredientViewSet, RecipeViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('tags', TagViewSet, basename='tags')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
