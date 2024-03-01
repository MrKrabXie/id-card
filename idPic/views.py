from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import os
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.http import JsonResponse
from idPic import utils


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        base64_image = body_data['image']
        # format, imgstr = base64_image.split(';base64,')
        # ext = format.split('/')[-1]

        # data = BytesIO(base64.b64decode(imgstr))
        # img = Image.open(data)
        # img.save(os.path.join(settings.MEDIA_ROOT, 'image.' + ext))  # 将图像保存至 MEDIA_ROOT

        result = utils.extract_id_info(base64_image)

        return JsonResponse(result)

    return JsonResponse({"status": "failure", "message": "Only POST request is allowed."})
