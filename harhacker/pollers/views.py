from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

@login_required
def index(request):
    return render(request, 'pollers/index.html', {})
