from django.shortcuts import render

def index(reqeust):
    return render(reqeust, 'blog/index.html', {})