from django.contrib import admin

# 本地的模型
from .models import Todo

# Register your models here.
# 註冊模型
admin.site.register(Todo)
