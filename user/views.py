from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# 建立註冊form表單
# Create your views here.


# 登入後會出現profile
def user_profile(request):
    print(request.user)
    return render(request, "user/profile.html", {"user": request.user})


# log in
def user_login(request):
    message = ""
    if request.method == "POST":
        # 註冊
        if request.POST.get("register"):
            return redirect("register")

        # 登入
        elif request.POST.get("login"):
            username = request.POST.get("username")
            password = request.POST.get("password")

            if username == "" or password == "":
                message = "帳號與密碼不能為空"
            else:
                user = authenticate(request, username=username, password=password)

                if user:
                    login(request, user)
                    message = "登入成功"
                    return redirect("todo")

                else:
                    message = "帳號或密碼錯誤"

    return render(request, "user/login.html", {"message": message})


# log out
def user_logout(request):
    logout(request)
    return redirect("login")


# 註冊
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
