# NadoshaDev | Stepik Task: Фильтрация iPhone
smartphones = [
    'iPhone 15 Pro Max',
    'Samsung Galaxy S23 Ultra',
    'Google Pixel 8 Pro',
    'iPhone 14',
    'Xiaomi 13 Pro'
]

# Фильтрация через list comprehension (case-insensitive)
iphone_smartphones = [
    phone for phone in smartphones if 'iphone' in phone.lower()
]

print(iphone_smartphones)
