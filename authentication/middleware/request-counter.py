from authentication.models import VisitorCount


# class VisitorCountMiddleware:
#     def process_request(self, request):
#         try:
#             obj = VisitorCount.objects.get_or_create()
#             obj.increment()
#         except:
#             pass
#         return None


class VisitorCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            obj = VisitorCount.objects.first()
            if not obj:
                obj = VisitorCount.objects.create()
            obj.increment()
        except Exception:
            pass
        response = self.get_response(request)
        return response
