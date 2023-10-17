price_dict = {
    'Жесткие диски SSD': {
        600: 1.090,
        1000: 1.087,
        2000: 1.085,
        4000: 1.075,
        4001: 1.070,
        'top': 55,
        'other': 65,
        'top_rivals': ['Rozetka', 'Telemart', 'Brain'],
        'stop_brands': ['Kingston'],
        'stop_id': [1222234234, 363442344]
    },
    'Жесткие диски': {
        2300: 1.085,
        3000: 1.080,
        6000: 1.075,
        6001: 1.072,
        'top': 55,
        'other': 65,
        'top_rivals': ['Rozetka', 'Telemart', 'Brain']
    },
    'Видео адаптеры': {
        3000: 1.075,
        6000: 1.070,
        15000: 1.067,
        20000: 1.065,
        60000: 1.063,
        60001: 1.060,
        'top': 55,
        'other': 65,
        'top_rivals': ['Rozetka', 'Telemart', 'Brain']
    },
    'Материнские платы': {
        600: 1.10,
        1000: 1.090,
        2000: 1.087,
        4000: 1.085,
        4001: 1.070,
        'top': 55,
        'other': 65,
        'top_rivals': ['Rozetka', 'Telemart', 'Brain']
    },
    'Модули памяти': {
        600: 1.095,
        1000: 1.090,
        2000: 1.085,
        4000: 1.080,
        4001: 1.070,
        'top': 55,
        'other': 65,
        'top_rivals': ['Rozetka', 'Telemart', 'Brain']
    },
    'Процессоры': {
        1030: 1.12,
        3080: 1.08,
        5130: 1.075,
        8200: 1.070,
        10250: 1.067,
        15400: 1.065,
        21500: 1.060,
        21501: 1.055,
        'top': 55,
        'other': 65,
        'top_rivals': ['Rozetka', 'Telemart', 'Brain']
    }
}


def find_purchase_price(name):
    return price_dict[name]
