import pyotp
import qrcode
from app_consts import PY_HUMAN_OPT_APP

from user_store.user_store import add_user, init_user_store


def generate_qr_code(totp_uri: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(totp_uri)
    qr.make(fit=True)

    qr.print_ascii()


def main():
    print('Onboarding new user')
    user_email = input('Enter new user email: ')

    init_user_store()

    secret = pyotp.random_base32()
    totp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=user_email, issuer_name=PY_HUMAN_OPT_APP)

    add_user(user_email, secret)

    generate_qr_code(totp_uri)
    print(f'User code: {secret}')

if __name__ == "__main__":
    main()
