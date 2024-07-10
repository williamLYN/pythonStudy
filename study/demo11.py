game_roles = {
    '战士': {
        'health_value': 120,
        'magic_value': 50,
        'aggressive_value': 12,
        'magic_power_value': 12
    },
    '弓箭手': {
        'health_value': 80,
        'magic_value': 70,
        'aggressive_value': 16,
        'magic_power_value': 6
    },
    '野蛮人': {
        'health_value': 110,
        'magic_value': 60,
        'aggressive_value': 14,
        'magic_power_value': 10
    }
}

for role_name in game_roles.keys():
    print(role_name)

for role_value in game_roles.values():
    print(role_value)

for role_name, role_value in game_roles.items():
    print(role_name, role_value)

for role_name, role_value in game_roles.items():
    print(role_name, role_value['health_value'])