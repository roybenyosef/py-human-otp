import pyotp

from user_store.user_store import get_user_secret, list_users


PY_HUMAN_OPT_APP = 'HumanOPT'


def main():
    print(list_users())

    user_email = input('Enter new user email: ')
    user_secret = get_user_secret(user_email)

    totp = pyotp.TOTP(user_secret)
                      
    while user_input := input('Enter OTP (enter to exit): '):
        if totp.verify(user_input):
            print('OK! The OTP is valid.')
            break
        else:
            print('XXX DANGER! The OTP is invalid. XXX')


if __name__ == "__main__":
    main()
