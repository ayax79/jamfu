from django.shortcuts import render_to_response

def index(Request):
    return render_to_response('artist/index.html')