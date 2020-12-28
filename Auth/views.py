from django.views import View
from django.shortcuts import render



class Home(View):
    def get(self, request):
        request.session.set_expiry(300)
        user = request.session.get('user')
        name = request.session.get('name')
        return render(request, 'Main/index.html', {
            "user": user,
            "name": name
        })

    #def post(self, request):


