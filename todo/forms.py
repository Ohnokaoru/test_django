from django.forms import ModelForm
from .models import Todo  # 導出todo的model


class TodoFrom(ModelForm):
    # 表單綁定資料模型(撈出指定model的fields資料)
    class Meta:
        model = Todo
        # 全部欄位都要
        # fields = "__all__"
        fields = ["title", "text", "important", "completed"]
