import CellPhoneClass as c


iPhone = c.Cellphone('Apple', 'iPhone16', 1600)
Samsung = c.Cellphone('Samsung','Galaxy10',1500)


print(f"The {iPhone.get_model()} is produced by {iPhone.get_manufact()} and retails for ${iPhone.get_retail_price()}")
print(f"The {Samsung.get_model()} is produced by {Samsung.get_manufact()} and retails for ${Samsung.get_retail_price()}")

iPhone.set_retail_price(sum({iPhone.get_retail_price()} - {Samsung.get_retail_price()}))

print(f"The {iPhone.get_model()} is produced by {iPhone.get_manufact()} and retails for ${iPhone.get_retail_price()}")
print(f"The {Samsung.get_model()} is produced by {Samsung.get_manufact()} and retails for ${Samsung.get_retail_price()}")