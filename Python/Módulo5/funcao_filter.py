emails = ['andre.perez@gmail.com', 'andre.perez@live.com', 'andre.perez@yahoo.com']
provedor_da_google = lambda email: 'gmail' in email

emails_google = []
for email in emails:
  if provedor_da_google(email) == True:
    emails_google.append(email)

print(emails_google)

emails_google = filter(provedor_da_google, emails)
print(emails_google)

emails_google = list(filter(provedor_da_google, emails))
print(emails_google)

emails_google = filter(lambda email: 'gmail' in email, emails)
...
print(list(emails_google))