from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    # obj = Article.objects.all()
    # for article in obj:
    #     print('!!!!!')
    #     print(article.scopes.all())
    #     scopes = article.scopes.all()
    #
    #
    #     for scope in scopes:
    #         if scope.is_main:
    #             print('IS MAIN!!!!')
    #         print(scope.scope.name)

    context = {'object_list': Article.objects.all()}


    return render(request, template, context)
