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

    # user_id <=> todo_id
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 更改顯示
    def __str__(self):
        return f"{self.id} -{self.title} -({self.user}) -{self.created}"