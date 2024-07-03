from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import BoardPost
from django.views.decorators.http import require_POST
import json


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
@require_POST
def like_post(request, post_id):
    data = json.loads(request.body.decode("utf-8"))
    post = get_object_or_404(BoardPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({"likes": post.likes.count(), "liked": liked})


@login_required
@require_POST
def dislike_post(request, post_id):  # Ensure post_id is accepted as an argument
    data = json.loads(request.body.decode("utf-8"))
    post = get_object_or_404(BoardPost, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
        disliked = False
    else:
        post.dislikes.add(request.user)
        disliked = True
    return JsonResponse({"dislikes": post.dislikes.count(), "disliked": disliked})


@login_required
def board_list(request):
    # 게시물 목록을 가져오는 로직
    return render(request, "board_list.html")



@login_required
def grow_1(request):
    user = request.user
    user_posts = BoardPost.objects.filter(user=user)
    total_posts = user_posts.count()
    
    # Sum the count of likes for each post
    total_likes = sum(post.likes.count() for post in user_posts)

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

from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import BoardPost  

# @login_required
# def update(request, post_id):
#     post = get_object_or_404(BoardPost, id=post_id)
    
#     if request.method == "POST":
#         post.title = request.POST['title']
#         post.content = request.POST['content']
#         post.development_period=request.POST['development_period']
#         post.participants=request.POST['participants']
#         post.language=request.POST['language']
#         post.updated_at = timezone.now()
        
#         # Handle image upload
#         try:
#             post.file = request.FILES['file']
#         except KeyError:
#             pass  
        
#         post.save()
        
#         # Redirect to the post detail page
#         return redirect('/detail/' + str(post.id))
    
#     # Render the update form for GET requests
#     context = {
#         'post': post,
#     }
#     return render(request, 'board_update.html', context)

def update(request, post_id):
    if request.method == 'POST':
        post = BoardPost.objects.get(pk=post_id)  # 예시로 사용할 모델에 맞게 수정해야 합니다.


        # 새로운 데이터 저장
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.participants = request.POST.get('participants')
        post.development_period = request.POST.get('development_period')
        post.language = request.POST.get('language')
        post.updated_at = timezone.now()
        

        # 파일 업로드 처리 (필요시)
        if 'file' in request.FILES:
            file = request.FILES['file']
            # 파일 처리 로직 추가
        
        new_language = request.POST.get('language')
        if new_language:
            post.language = new_language

        # 저장
        post.save()
        return redirect('/detail/' + str(post.id))

    # GET 요청 처리 (옵션)
    else:
        post = BoardPost.objects.get(pk=post_id)
        context = {'post': post}
        return render(request, 'board_update.html', context)


def delete(request, post_id):
    post = BoardPost.objects.get(id=post_id)
    post.delete()
    return redirect('main') 
