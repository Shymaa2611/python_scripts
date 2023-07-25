import phonenumbers
from phonenumbers import geocoder,carrier,timezone

number=input("Enter number of phone : ")
#=========== if i dont want to write the key of country =======#
phone_num=phonenumbers.parse(number,None)
#print(phone_num)
#================= determine the location of phone number =============#
print(geocoder.description_for_number(phone_num,"en"))
print(carrier.name_for_number(phone_num,"en"))
print(timezone.time_zones_for_number(phone_num))