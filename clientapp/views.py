from django.shortcuts import render,redirect
import requests
import base64

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def upload(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        file = {'file': image}
        response = requests.post('http://127.0.0.1:8000/recognition', files= file)

        context = response.json()

        image.seek(0)
        image_data = base64.b64encode(image.read()).decode('utf-8')
        context['link_image'] = f"data:image/png;base64,{image_data}"

        
        return render(request, 'app/index.html', context= context)