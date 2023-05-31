from typing import Any, Dict
from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Article

# Create your views here.


class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by("-date")
    template_name = "blog/index.html"
    paginate_by = 1


class DetailArticleView(DetailView):
    model = Article
    template_name = "blog/detail_article.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """let's override this method to add more template context 'liked_by_user'"""
        context = super(DetailArticleView, self).get_context_data(**kwargs)
        article = Article.objects.get(id=self.kwargs.get("pk"))

        context["liked_by_user"] = False

        if article.likes.filter(pk=self.request.user.id).exists():
            context["liked_by_user"] = True

        return context


class LikeArticle(View):
    """user can hit like button => send POST request and redirected into DetailArticleView"""

    def post(self, request, pk):
        """pk: primary key to the specific article"""
        article = Article.objects.get(id=pk)

        # 해당 게시글에 좋아요 누른 유저가 현재 세션의 유저인지 판별
        if article.likes.filter(pk=request.user.id).exists():
            # toggle off
            article.likes.remove(request.user.id)
        else:
            # toggle on
            article.likes.add(request.user.id)

        # save the article and redirect to itself
        article.save()
        return redirect("detail_article", pk)
