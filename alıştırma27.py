import re
[print('YES' if re.match(r'[5]\d{9}$',input("Telefon numarası:")) else 'NO') for _ in range(int(input("Kontrol edilecek numara sayısı:")))]