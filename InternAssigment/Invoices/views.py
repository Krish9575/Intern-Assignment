from .models import Invoices,InvoicesDetails
from .serializer import InvoiceSerializer,InvoiceDetailSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class InvoiceGetAndCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
class Invoice_Put_PATCH_and_Delete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    

class InvoiceDetailsGetAndCreate(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset=InvoicesDetails.objects.all()
    serializer_class = InvoiceDetailSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class InvoiceDetails_Put_PATCH_and_Delete(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = InvoicesDetails.objects.all()
    serializer_class = InvoiceDetailSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def patch(self,request,*args, **kwargs):
        return self.partial_update(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    

