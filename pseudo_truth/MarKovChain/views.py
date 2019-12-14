from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Markov import MarkovChain
from .Markov import resourceSelector

class Poems(APIView):
    def get(self,request, *args, **kwargs):
        poem={}
        if 'id' in request.GET:
            poemType=request.GET['id']
            markov=MarkovChain(resourceSelector(poemType))
            poem={'Poem':markov.generateText()}
        else:
            markov=MarkovChain()
            poem={'Poem':markov.generateText()}
        return Response(poem)        
        pass