# myapp/social_save.py

from allauth.socialaccount.signals import social_account_updated, social_account_added
from django.dispatch import receiver
from .models import KakaoUser, NaverUser
import logging

logger = logging.getLogger(__name__)


@receiver(social_account_added)
@receiver(social_account_updated)
def populate_profile(request, sociallogin, **kwargs):
    user = sociallogin.user
    extra_data = sociallogin.account.extra_data
    provider = sociallogin.account.provider

    logger.debug(f"Social login signal received for provider: {provider}")
    logger.debug(f"Extra data received: {extra_data}")

    if provider == "kakao":
        nickname = extra_data.get("properties", {}).get("nickname", user.username)
        email = extra_data.get("kakao_account", {}).get("email", "")
        gender = extra_data.get("kakao_account", {}).get("gender", "")
        age_range = extra_data.get("kakao_account", {}).get("age_range", "")

        # 성별 변환
        if gender == "female":
            gender = "여성"

        logger.debug(
            f"Kakao user details - nickname: {nickname}, email: {email}, gender: {gender}, age_range: {age_range}"
        )

        KakaoUser.objects.update_or_create(
            user=user,
            defaults={
                "nickname": nickname,
                "email": email,
                "gender": gender,
                "age_range": age_range,
            },
        )

    elif provider == "naver":
        nickname = extra_data.get("name", user.username)
        email = extra_data.get("email", "")
        gender = extra_data.get("gender", "")
        age_range = extra_data.get("age", "")

        # 성별 변환
        if gender == "F":
            gender = "여성"

        logger.debug(
            f"Naver user details - nickname: {nickname}, email: {email}, gender: {gender}, age_range: {age_range}"
        )

        NaverUser.objects.update_or_create(
            user=user,
            defaults={
                "nickname": nickname,
                "email": email,
                "gender": gender,
                "age_range": age_range,
            },
        )

    logger.debug(f"User {user} updated or created in the database.")
