#============================#
# DJANGO VERSION: 3.2.15 LTS #
#============================#
from django.shortcuts import render

def index(request):
    
    return render(request, "index.html", {'content':None})