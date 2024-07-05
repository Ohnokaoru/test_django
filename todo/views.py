from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoFrom
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def create_todo(request):
    message = ""

    # 第一次進來，一定是get
    form = TodoFrom()

    if request.method == "POST":
        try:
            form = TodoFrom(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            message = "建立成功"
            return redirect("todo")

        except Exception as e:
            print(e)
            message = "建立失敗"
    return render(request, "todo/create-todo.html", {"form": form, "message": message})


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user).order_by("-created")
        print(todos)
    return render(request, "todo/todo.html", {"todos": todos})


@login_required
def view_todo(request, id):
    todo = None
    message = ""
    try:
        todo = Todo.objects.get(id=id)
        form = TodoFrom(instance=todo)

        if request.method == "POST":
            print(request.POST)

            # 更新
            if request.POST.get("update"):

                todo.date_copmlated = (
                    datetime.now() if request.POST.get("completed") else None
                )

                form = TodoFrom(request.POST, instance=todo)
                # 是否有效
                if form.is_valid():
                    form.save()
                    message = "更新成功"

            # 刪除
            elif request.POST.get("delete"):
                todo.delete()

                # 回列表
                return redirect("todo")

    except Exception as e:
        print(e)
        message = "更新或修改失敗"

    return render(
        request, "todo/view-todo.html", {"todo": todo, "form": form, "message": message}
    )


# 已完成事項
@login_required
def completed_todo(request):
    todos = None
    completed = True
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user, completed=True).order_by(
            "-created"
        )

    return render(request, "todo/todo.html", {"todos": todos, "completed": completed})


@login_required
def delete_todo(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()

    except Exception as e:
        print(e)

    return redirect("todo")
