from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^pokemon/', include('pokemon.urls', namespace='pokemon')),
    url(r'^webtoon/', include('webtoon.urls', namespace='webtoon')),

]
