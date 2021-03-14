from all_classes_module import User, EmailUser


def test_abstract_class():
    try:
        User('abc123')
    except Exception as e:
        print('['+str(e)+']\n')


test_abstract_class()

selected_option = input('how do you want to sign in? [Email: e, Phone: p] ')

if selected_option == 'e':
    email_input = input('your email please: ')
    user = EmailUser('abc123', email_input)
elif selected_option == 'p':
    phone_input = input('your phone-number please: ')
    user = EmailUser('abc123', phone_input)
else:
    print('Error! invalid option selected.')
    exit(0)

print('\nvalidating credentials...\n')

if user.validate_credentials():
    print('user successfully signed in!')
else:
    print('user validation failed')

print(user.__str__())
