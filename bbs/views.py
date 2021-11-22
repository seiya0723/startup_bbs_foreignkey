from django.shortcuts import render,redirect

from django.views import View
from .models import Category,Topic,Reply
from .forms import TopicForm,ReplyForm


class BbsView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["topics"]       = Topic.objects.all()
        context["categories"]   = Category.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:index")

index   = BbsView.as_view()



class BbsReplyView(View):

    def get(self, request, pk, *args, **kwargs):

        context = {}
        context["topic"]    = Topic.objects.filter(id=pk).first()
        context["replies"]  = Reply.objects.filter(target=pk)

        return render(request,"bbs/reply.html",context)

    def post(self, request, pk, *args, **kwargs):

        #request.POSTの辞書型のコピーを手に入れる。(そのままでは書き換えはできないため)
        copied              = request.POST.copy()
        copied["target"]    = pk

        form    = ReplyForm(copied)

        if form.is_valid():
            form.save()
        else:
            print("バリデーションNG")

        return redirect("bbs:reply",pk)

reply   = BbsReplyView.as_view()

