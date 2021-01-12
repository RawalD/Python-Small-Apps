# Email slicer

email = input('Please enter your email address\n').strip()

user_name = email[:email.index('@')]
host = email[email.index('@') + 1: email.index('.')]
url_domain = email[email.index('.'):]

print(f'{email} has the following characteristics:\nUsername: {user_name}\nHost: {host}\nURL Domain: {url_domain}')
