from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import BoardPost


def main(request):
    context = {}

    if request.user.is_authenticated:
        try:
            kakao_user = KakaoUser.objects.get(user=request.user)
            context["username"] = kakao_user.nickname
        except KakaoUser.DoesNotExist:
            try:
                naver_user = NaverUser.objects.get(user=request.user)
                context["username"] = naver_user.nickname
            except NaverUser.DoesNotExist:
                # 로그인은 되어 있으나, 어느 쪽 데이터베이스에도 사용자 정보가 없는 경우
                context["username"] = None
    else:
        # 사용자가 로그인하지 않은 경우
        context["username"] = None

    recent_posts = BoardPost.objects.order_by("-created_at")[:15]
    most_viewed_posts = BoardPost.objects.order_by("-likes")[:15]
    popular_posts = BoardPost.objects.order_by("-likes")[:15]

    context.update(
        {
            "recent_posts": recent_posts,
            "most_viewed_posts": most_viewed_posts,
            "popular_posts": popular_posts,
        }
    )

    return render(request, "main.html", context)


def board_list(request):
    return render(request, "board_list.html")


from django.contrib.auth.decorators import login_required
from .models import BoardPost
from .models import KakaoUser, NaverUser


def board_create(request):
    return render(request, "board_create.html")


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "login_create.html"


def grow_1(request):
    return render(request, "grow_1.html")


def login(request):
    return render(request, "login.html")


def mypage_share(request):
    return render(request, "mypage_share.html")


@login_required
def board_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        development_period = request.POST.get("development_period")
        participants = request.POST.get("participants")
        language = request.POST.get("language")
        file = request.FILES.get("file")

        BoardPost.objects.create(
            title=title,
            content=content,
            development_period=development_period,
            participants=participants,
            language=language,
            file=file,
            user=request.user,
        )
        return redirect("board_list")
    return render(request, "board_create.html")


@login_required
def like_post(request, post_id):
    post = get_object_or_404(BoardPost, id=post_id)
    post.likes += 1
    post.save()
    return JsonResponse({"likes": post.likes})


@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(BoardPost, id=post_id)
    post.dislikes += 1
    post.save()
    return JsonResponse({"dislikes": post.dislikes})


@login_required
def board_list(request):
    # 게시물 목록을 가져오는 로직
    return render(request, "board_list.html")


@login_required
def grow_1(request):
    user = request.user
    user_posts = BoardPost.objects.filter(user=user)
    total_posts = user_posts.count()
    total_likes = sum(post.likes for post in user_posts)

    context = {
        "total_posts": total_posts,
        "total_likes": total_likes,
        "user_posts": user_posts,
    }
    return render(request, "grow_1.html", context)


@login_required
def board_detail(request, post_id):
    post = get_object_or_404(BoardPost, id=post_id)

    context = {
        "post": post,
    }
    return render(request, "board_detail.html", context)
