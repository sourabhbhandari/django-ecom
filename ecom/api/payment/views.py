from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="g98pgknrcftmfk9t",
        public_key="hcxfqqyzvkf57f4k",
        private_key="d5b07d54295e9aef2437e13d5acc8ac7"
    )
)

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False

    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid Session, Please Login Again :('})
    return JsonResponse({'client_token': gateway.client_token.generate(), 'Success':True})
    
@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid Session, Please Login Again :('})
    
    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = gateway.transaction.sale({
        "amount":amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {"submit_for_settlement": True}
    })

    if result.is_success:
        return JsonResponse({
            "Success":result.is_success,
            "Transaction": {'id': result.transaction.id, 'amount': result.transaction_amount}})
    else:
        return JsonResponse({"error": True, 'Success': False})
