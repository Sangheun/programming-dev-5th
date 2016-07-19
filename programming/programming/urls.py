from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^pokemon/', include('pokemon.urls')),
    url(r'^webtoon/', include('webtoon.urls')),

]
