from smarthone import Smartphone
catalog = []

phone1 = Smartphone("Apple", "IPhone13", "+7963 258 7432")
phone2 = Smartphone("Samsung", "Galaxy A5556", "+7900 7412589")
phone3 = Smartphone("Xiaomi", "Redmi 13C8", "+7999 236 1236")
phone4 = Smartphone("Honor", "Honor 100", "+7921 252 4152")
phone5 = Smartphone("Huawei", "Pura 70", "+7 852 471 2145")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.mobile_phone} - {phone.model_phone}, {phone.number}")