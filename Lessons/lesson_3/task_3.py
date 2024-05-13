from adress import Address
from mailing import Mailing

to_address = Address("162626", "Череповец", "Ленинградская", "45", "29")
from_address = Address("162600", "Вологда", "Советский", "23", "15")
mailing = Mailing(to_address, from_address, 1000, "TR123")

print(f"Отправление {mailing.track} из {mailing.from_address.index} "
      f"{mailing.from_address.town}, {mailing.from_address.street} "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index} {mailing.to_address.town}"
      f" {mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}.Стоимость {mailing.cost} рублей.")
