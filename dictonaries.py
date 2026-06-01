car ={"brand":"Ford","model":"Mustang","year":"2024"}
print(car["model"])
print(type(car))

car.update({"color":"red"})
car.pop("brand")
print(car)