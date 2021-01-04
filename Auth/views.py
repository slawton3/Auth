from django.views import View
from django.shortcuts import render



class Home(View):
    def get(self, request):
        request.session.set_expiry()
        user = request.session.get('user')
        name = request.session.get('name')
        return render(request, 'Auth/index.html', {
            "user": user,
            "name": name
        })

    #def post(self, request):


