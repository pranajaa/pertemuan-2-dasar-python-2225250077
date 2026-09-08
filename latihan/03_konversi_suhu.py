KELVIN_OFFSET = 273.15

celcius = float(input("Suhu celcius : "))

fahrenheit = (9/5) * celcius + 32
kelvin = celcius + KELVIN_OFFSET

print (f"celcius    : {celcius} °C")
print (f"fahrenheit : {fahrenheit} °F")
print (f"kelvin     : {kelvin} K")