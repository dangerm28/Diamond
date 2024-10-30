from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {
            "status": renderer_context['response'].status_code < 400,
            "code": renderer_context['response'].status_code,
            "data": data
        }
        return super().render(response_data, accepted_media_type, renderer_context)
