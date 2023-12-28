from django.shortcuts import render
from django.http import HttpResponse

# import sk learn chatbot
from eralink.Brain import chatbot_response


# Create your views here.
def index(request):
    return render(request, 'index.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def login(request):
    return render(request, 'login.html')

# def article(requests, article_id):
#     # http://127.0.0.1:8000/blog/article/2
#     # return HttpResponse(article_id)
#     return render(requests, 'blog/index.html', {'article_id': articl

def getResponse(request):
    # Example usage
    data_file_paths = [
        'eralink\\BrainData\\physics-a-level-definitions.txt',
        'eralink\\BrainData\\qa_data.txt',
        'eralink\\BrainData\\gk_que.txt',
        'eralink\\BrainData\\interesting.txt',
        # 'additional-file.txt',
        # Add more file paths here
    ]
    userMessage = request.GET.get('userMessage')
    response = chatbot_response(userMessage, data_file_paths)
    return HttpResponse(response)