"""
URL configuration for estore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from api.views  import Productsview
#from api.views import Addview
#from api.views import Subview
#from api.views import Multiview
# from  api.views import Divview
# from api.views import Cubeviwe
# from api.views import Numchkview
# from api.views import Factview
# from api.views import Wordcountview
# from api.views import Primenumview
# from api.views import Palindromeview
# from api.views import Armstrongview
from api.views import Productsview,Productdetailview
from api.views import Reviewsview,Reviewdetailsview

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("products",Productsview.as_view()),
    # path("add",Addview.as_view()),
    # path("sub", Subview.as_view()),
    # path("mul", Multiview.as_view()),
    # path("div", Divview.as_view()),
    # path("cube",Cubeviwe.as_view()),
    # path("numcheck",Numchkview.as_view()),
    # path("fact",Factview.as_view()),
    # path("wordcount",Wordcountview.as_view()),
    # path("prime",Primenumview.as_view()),
    # path("palindrom",Palindromeview.as_view()),
    # path("armstrong",Armstrongview.as_view()),
    path("products",Productsview.as_view()),
    path("products/<int:id>",Productdetailview.as_view()),
    path("reviews",Reviewsview.as_view()),
    path("reviews/<int:id>",Reviewdetailsview.as_view()),
]