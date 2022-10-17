import math

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne import rpc, Double, Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

# Create your views here.
class mathserv(ServiceBase):
    @rpc (Double(nillable=False),Double(nillable=False),_return=Double)
    def min(self,x,y):
       if (x<y):
           return x

    @rpc (Double(nillable=False),Double(nillable=False),_return=Double)
    def max(self,x,y):
        if(x>y):
            return x

    @rpc (Double(nillable=False),_return=Double)
    def sin(self,x):
        return math.sin(x)

    @rpc (Double(nillable=False),_return=Double)
    def cos(self,x):
        return math.cos(x)
## validator doit etre dans input mais output non
soap_app= Application([mathserv],tns=math.isg.tn,in_protocol=Soap11(validator='lxml'),out_protocol=Soap11)##tns est un url et ajoueter le protocole soap
django_app=DjangoApplication(soap_app)
My_maths_app= csrf_exempt(django_app)




