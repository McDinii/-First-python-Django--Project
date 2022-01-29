from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page!!',
        'values' : ['Some','Hello','123'],
        'obj':{
            'car' : ' porsche',
            'age' : '18',
            'hobby' : 'backetball',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')
