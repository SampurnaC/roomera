from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

User = get_user_model()

def generate_verification_token(user):
    signer = TimestampSigner()
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = signer.sign(uid)
    return token, uid

def verify_verification_token(uidb64, token):
    signer = TimestampSigner()
    try:
        uid = signer.unsign(token, max_age=2)
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        return user
    except (BadSignature, SignatureExpired, User.DoesNotExist):
        return None
