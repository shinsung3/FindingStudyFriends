from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("장고 웹 프로젝트 시작했습니다.")