from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'pais', views.PaisView, basename='Pais')
router.register(r'universidad', views.UniversidadView, basename='Universidad')
router.register(r'institucion', views.InstitucionView, basename='Institucion')
router.register(r'plan', views.PlanEstudioView, basename='PlanEstudio')
router.register(r'guia', views.GuiaView, basename='Guia')
router.register(r'nodocurso', views.NodoCursoView, basename='NodoCurso')
router.register(r'enlacecurso', views.EnlaceCursoView, basename='EnlaceCurso')
router.register(r'nodomodcurso', views.NodoModCursoView, basename='NodoModCurso')
router.register(r'enlacemodcurso', views.EnlaceModCursoView, basename='EnlaceModCurso')
#router.register(r'comparagraph/<int:guia>/<int:plan>/', views.ComparaGraphView, basename='comparagraph')

urlpatterns = [
    path('', include(router.urls)),
    path(r'comparagraph/<int:guia>/<int:plan>/', views.ComparaGraphView.as_view(), name='comparagraph'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]