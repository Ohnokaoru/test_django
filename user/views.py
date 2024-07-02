from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 建立註冊form表單
# Create your views here.


def user_register(request):
    message = ""
    form = UserCreationForm()
    # 取得所有
    print(User.objects.all())

    # 取得為一
    # print(User.objects.get(username="ohnog"))

    # 篩選
    # print(User.objects.filter(username="ohnog"))

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username, password1, password2)

        try:
            if password1 != password2:
                message = "與前面密碼不相同"

            elif len(password1) < 8:
                message = "密碼至少包含至少 8 個字元"

            elif password1.isdigit():
                message = "密碼不能完全是數字"

            else:
                # 檢查使用者是否存在
                user = User.objects.filter(username=username)
                if user.exists():
                    message = "帳號已存在"
                else:
                    User.objects.create_user(
                        username=username, password=password1
                    ).save()
                    message = "帳號註冊成功!"

        except Exception as e:
            print(e)
            message = "不明錯誤發生"

    return render(request, "user/register.html", {"form": form, "message": message})
