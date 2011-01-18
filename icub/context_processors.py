from settings import CSS_PATH, JS_PATH, MEDIA_URL

def urls(request):
    return {'CSS_PATH': CSS_PATH, 'JS_PATH': JS_PATH, 'MEDIA_PATH': MEDIA_URL}
