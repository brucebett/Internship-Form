from django.shortcuts import render, redirect
from django.contrib import messages
from myapp.models import Internship

# Create your views here.
def internshipdetails(request):    
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')    
        fusn=request.POST.get('usn')    
        fcolege=request.POST.get('cname')    
        foffer=request.POST.get('offer')    
        fstartdate=request.POST.get('sartdate')    
        fenddate=request.POST.get('enddate')    
        fprojreport=request.POST.get('projreport')  

# conecting to uppercase
        fname=fname.upper()  
        fusn=fusn.upper()  
        fcolege=fcolege.upper()  
        foffer=foffer.upper()  
        fprojreport=fprojreport.upper()  

        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request, "Your Details are already Present")
            return redirect("/internshipdetails")

        query=Internship(fullname=fname,usn=fusn,email=femail,college_name=fcolege,offer_status=foffer,
                         start_date=fstartdate,end_date=fenddate,project_report=fprojreport)
        query.save()
        messages.success(request, "Form is Submitted Successfuly!")
        return redirect('/internshipdetails')

    return render(request, 'internship.html') 