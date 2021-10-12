from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Informatica Tool'
admin.site.index_title = 'Herramienta para comparar planes y guias'
admin.site.site_title = 'Informatica Tool' 

urlpatterns = [
    path('compara/', include('pro_compara_api.urls')),
    path('admin/', admin.site.urls),
]
