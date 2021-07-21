import phonenumbers
from phonenumbers import geocoder

telefone = input('Digite o telefone no formato +551140028922: ')

phone_number = phonenumbers.parse(telefone)

print(geocoder.description_for_number(phone_number, 'pt'))