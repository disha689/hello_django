from django.contrib import admin
from django.urls import path
from home.views import index   # 👈 ye line add karo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # 👈 ye line add karo (homepage pe chalega)
]
