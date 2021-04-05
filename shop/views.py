from django.shortcuts import render
from .models import Banner,Product,Order,updateOrder
from django.http import HttpResponse
# Create your views here.
#home view
def home(request):
    image=Banner.objects.all()
    product = Product.objects.all()[0:12]
    return render(request,'base.html',{'banner':image,'product':product})

#show product by category
def Category(request):
    category=request.GET.get('category')
    product = Product.objects.filter(category=category)
    return render(request,'category.html',{'category':category,'product':product})
#search product
def search(request):
    try:
        query=request.GET.get("search")
    except:
        query=None 
    products=Product.objects.filter(name__icontains=query) 
    params={'product':products}
    return render(request,'search.html',params)    

#product view
def product(request,id):
    product=Product.objects.get(id=id) 
    return render(request,'product.html',{'product':product})   

#checkout view
def checkout(request,id):
    if request.method=="POST":
        name=request.POST.get('name','')
        size=request.POST.get('size','')
        Landmark=request.POST.get('landhouse')
        address=request.POST.get('address','')
        district=request.POST.get('district','')
        state=request.POST.get('state','')
        phone=request.POST.get('phone','')
        pin_code=request.POST.get('pincode','')
        itemjson=request.POST.get('itemjson','')
        order =Order(name=name,size=size,address=address,district=district,phone=phone,state=state,pin_code=pin_code,item=itemjson,Landmark=Landmark)
        order.save()
        update=updateOrder(order_id=order.order_id,update_desc="order has been placed,You will get tracking link after 3-4 days")
        update.save()
        return render(request,'success.html',{'order_id':order.order_id,'name':name})
#view for get request
    product=Product.objects.get(id=id) 
    return render(request,'checkout.html',{'product':product}) 


#add to cart checkout
def cart_checkout(request):
    if request.method=="POST":
        itemjson=request.POST.get('itemjson','')
        name=request.POST.get('name','')
        Landmark=request.POST.get('landhouse')
        address=request.POST.get('address','')
        district=request.POST.get('district','')
        state=request.POST.get('state','')
        phone=request.POST.get('phone','')
        pin_code=request.POST.get('pincode','')
        order =Order(name=name,address=address,district=district,phone=phone,state=state,pin_code=pin_code,item=itemjson,Landmark=Landmark)
        order.save()
        update=updateOrder(order_id=order.order_id,update_desc="order has been placed,You will get tracking link after 3-4 days")
        update.save()
        return render(request,'success.html',{'order_id':order.order_id,'name':name})
    return render(request,'cart_checkout.html')


    
#track the order
def tracker(request):
    if request.method=="POST":
        orderid=request.POST.get('orderid','')
        try:
            order=updateOrder.objects.filter(order_id=orderid)
            if len(order)>0:
                update=updateOrder.objects.filter(order_id=orderid)
                return render(request,'tracker.html',{'update':update})  
            else:
                return render(request,'tracker.html',{'nothing':'nothing'})
        except Exception as e:        
                return render(request,'tracker.html',{'nothing':'nothing'})
    return render(request,'tracker.html') 
