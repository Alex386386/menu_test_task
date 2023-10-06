from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('draw_menu', TemplateView.as_view(template_name='draw_menu.html')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
