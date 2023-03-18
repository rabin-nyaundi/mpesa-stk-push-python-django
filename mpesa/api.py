from rest_framework.decorators import api_view
from rest_framework.response import Response

from payments.views import update_stk_results


@api_view(["POST"])
def stk_push_results(request):
    body = request.data.get("Body")
    body = body["stkCallback"]

    res = update_stk_results(body)
    return Response(res)
