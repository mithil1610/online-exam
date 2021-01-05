from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Questions,Answer,Course,Paper
from.forms import AddQFrm
from accounts.models import User
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def exam_admin_home(request):
    return render(request,'exam_admin_home.html')

@staff_member_required
def new_question(request):
    msg=""
    if request.method=="POST":
        frm=AddQFrm(request.POST or None)
        if frm.is_valid():
            a=frm.save()
            if a:
                msg="Question Added Successfully"
    frm=AddQFrm()
    context={
        'frm':frm,
        'msg':msg,
    }
    return render(request,'add_question.html',context)

@staff_member_required
def view_question(request):
    qts=Questions.objects.all()
    context={
        'qts':qts,
    }
    return render(request,'view_questions.html',context)

@staff_member_required
def edit_questions(request,qid):
    qi=Questions.objects.get(id=qid)
    if request.method=='POST':
        frm=AddQFrm(request.POST,instance=qi)
        if frm.is_valid():
            frm.save()
            return redirect('view_question')
    frm=AddQFrm(instance=qi)
    context={
        'frm':frm,
    }
    return render(request,'add_question.html',context)

@staff_member_required
def delete_questions(request,qid):
    Questions.objects.filter(id=qid).delete()
    return redirect('view_question')

@staff_member_required
def students(request):
    students=User.objects.filter(is_staff=False,is_admin=False)
    context={
        'stds':students
    }
    return render(request,'student_list.html',context)

@staff_member_required
def answerd_questions(request,stdid):
    ans=Answer.objects.filter(student=stdid)
    context={
        'ans':ans
    }
    return render(request,'answers.html',context)