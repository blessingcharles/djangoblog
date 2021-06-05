
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path , include
from . import settings
from django.conf.urls.static import static 

#dummy homepage
def main_page(request):
    return HttpResponse('''<h1>VISIT TH3H04X BLOG</h1>
                            <a href="/blog">blog</a>''')


urlpatterns = [
    path('',main_page),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls',namespace='blog')),
    path('auth/',include('Authentication.urls',namespace='Authentication')),
    path('user/',include('user.urls',namespace='user')),
   
]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 