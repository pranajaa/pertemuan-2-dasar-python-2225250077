print ("Kalkulator Koordinat Dua Titik")

x1 = float(input("x titik A : "))
y1 = float(input("y titik A : "))
x2 = float(input("x titik B : "))
y2 = float(input("y titik B : "))

jarak = ((x2 - x1) **2 + (y2 - y1) **2) **0.5

dx = x2 - x1
dy = y2 - y1

titiktengah_x = (x1 + x2) / 2
titiktengah_y = (y1 + y2) / 2

print (f"Titik A                    : ({x1:.2f}, {y1:.2f})")
print (f"Titik B                    : ({x2:.2f}, {y2:.2f})")
print (f"Perubahan koordinat        : dx: {dx:.2f}, dy: {dy:.2f}")
print (f"Jarak antara titik A dan B : {jarak: .2f}")
print (f"Titik tengah               : ({titiktengah_x:.2f}, {titiktengah_y:.2f})")