# myapp/views.py
# views.py
from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .forms import CommentForm
from .models import Comment

def apod_view(request):
    date = request.GET.get('date')
    apod_data = None
    error = None
    comments = []

    try:
        if date:
            url = f'https://api.nasa.gov/planetary/apod?api_key={settings.NASA_API_KEY}&date={date}'
        else:
            url = f'https://api.nasa.gov/planetary/apod?api_key={settings.NASA_API_KEY}'
        
        response = requests.get(url)
        response.raise_for_status() 
        apod_data = response.json()
        
        if 'error' in apod_data:
            error = apod_data['error'].get('message', 'An error occurred while fetching data.')
            apod_data = None
        else:
            comments = Comment.objects.filter(apod_date=apod_data['date']).order_by('-created_at')

    except requests.exceptions.RequestException as e:
        error = f"An error occurred: {str(e)}"

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.apod_date = apod_data['date']
            comment.save()
            return redirect('apod')
    else:
        form = CommentForm()

    context = {
        'apod_data': apod_data,
        'error': error,
        'form': form,
        'comments': comments,
    }
    return render(request, 'apod.html', context)