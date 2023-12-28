from django.shortcuts import render
from django.http import HttpResponse
import os
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
    try:
        base_path = os.path.dirname(os.path.abspath('eralink'))
        data_file_paths = [
            os.path.join(base_path, 'eralink', 'BrainData', 'physics_definitions.txt'),
            os.path.join(base_path, 'eralink', 'BrainData', 'qa_data.txt'),
            os.path.join(base_path, 'eralink', 'BrainData', 'gk_que.txt'),
            os.path.join(base_path, 'eralink', 'BrainData', 'interesting.txt'),
            # 'additional-file.txt',
            # Add more file paths here
        ]
        userMessage = request.GET.get('userMessage')
        response = chatbot_response(userMessage, data_file_paths)
        return HttpResponse(response)
    except Exception as e:
        # Log the exception details
        print(f"Error in getResponse: {e}")
        # You may want to log to a file or use Django's logging framework
        return HttpResponse("Internal Server Error", status=500)
