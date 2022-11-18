from django.shortcuts import render
def home_view(request):
    context={
        'first_name':'siva','last_name':'ganesh'
    }
    return render(request,'index.html',context)