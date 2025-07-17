from django.shortcuts import render

def home(req):
    if req.method=="POST" and req.POST.get('arm') == "":
        data = int(req.POST.get('number'))
        temp = data
        sum = 0
        length = len(req.POST.get('number'))
        while (data > 0):
            last = data % 10
            sum = sum +  last**length
            data = data // 10
        if sum == temp :
            result = "yes it is a armstrong number "
        else:
            result = "no  it is not  a armstrong number "
        return  render(req,"determiner/index.html",{'result':result})
    if req.method=="POST" and req.POST.get('prime') == "":
        data = req.POST.get('number')
        
        return  render(req,"determiner/index.html")
    if req.method=="POST" and req.POST.get('pal') == "":
        data = int(req.POST.get('number'))
        temp = data
        sum = 0
        while (data>0):
            num1 = data % 10
            sum = (sum*10) + num1
            data = data//10
        if temp == sum:
            result = "It is a pallindrome."
        else:
            result = "No, It's not a pallindrome."
        return render(req,"determiner/index.html",{'result':result})
    





    return render(req,"determiner/index.html")