from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Task


tasks = {
    0: Task("Task1", "Description 1", datetime.now(), datetime.now()+timedelta(hours=1)),
    1: Task("Task2", "Description 2", datetime.now()-timedelta(hours=1), datetime.now()+timedelta(hours=3)),
    2: Task("Task3", "Description 3", datetime.now(), datetime.now()+timedelta(hours=2, minutes=30))
}
next_id = 3

# Create your views here.
def index(request):
    content = f"""
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Description</th>
            <th>start</th>
            <th>end</th>
        </tr>
    </thead>
    <tbody>
"""
    for task in tasks.values():
        content += f"""
        <tr>
            <td>{task.title}</td>
            <td>{task.description}</td>
            <td>{task.beginning}</td>
            <td>{task.end}</td>
        </tr>
        """
    content += f"""
    </tbody>
</table>
    """
    return HttpResponse(content)

@csrf_exempt
def add_task(request):
    global next_id, tasks
    if request.method == "POST":
        items = [
            request.POST.get("title"),
            request.POST.get("description"),
            request.POST.get("beginning"),
            request.POST.get("end")
        ]
        if all(items):
            tasks[next_id] = Task(*items)
            next_id += 1
        return redirect("/tasks/")
    content = f"""
<form method="POST">
    <input type="text" name="title" id="title" placeholder="Enter title">
    <input type="text" name="description" id="description" placeholder="Enter description">
    <input type="datetime-local" name="beginning" id="beginning">
    <input type="datetime-local" name="end" id="end">
    <button type="submit">Add task</button>
</form>
"""
    return HttpResponse(content)

def delete_task(request, id: int):
    t = tasks[id] if id in tasks else None
    if not t is None:
        del tasks[id]
    return redirect("/tasks/")