from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Todo繼承models的Model
class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    date_copmlated = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)

    # 一對多關聯:Todo的user欄位會與User的user做關聯，如果是要關聯User其他欄位，to_field='ABC'
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    completed = models.BooleanField(default=False)

    # 更改顯示
    def __str__(self):
        return f"{self.id} -{self.title} -({self.user}) -{self.created}"
