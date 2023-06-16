from django.contrib import admin
from django.urls import include, path


from rest_framework.routers import DefaultRouter


from garagem.views import MarcaViewSet, CategoriaViewSet, CorViewSet, AcessorioViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"marcas", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessórios", AcessorioViewSet)
router.register(r"veículos", VeiculoViewSet)


urlpatterns = [
   path("admin/", admin.site.urls),
   path("", include(router.urls)),
]
