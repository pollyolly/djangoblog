from .models import Setting, SocialMedia

def site_setting(request):
    setting = Setting.objects.all().first()
    socmed = SocialMedia.objects.all()
    context = { 'sitesetting':setting, 'socmed': socmed, 'user_auth':request.user.is_authenticated}
    return context
