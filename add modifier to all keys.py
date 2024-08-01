import json

vendor_id = 1539
product_id = 245

keys = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
    'escape', 'tab', 'caps_lock', 'return_or_enter', 'spacebar', 'delete_or_backspace', 'delete_forward',
    'hyphen', 'equal_sign', 'open_bracket', 'close_bracket', 'backslash', 'semicolon', 'quote', 'grave_accent_and_tilde',
    'comma', 'period', 'slash',
    'left_arrow', 'right_arrow', 'up_arrow', 'down_arrow',
    'keypad_num_lock', 'keypad_slash', 'keypad_asterisk', 'keypad_hyphen', 'keypad_plus', 'keypad_enter',
    'keypad_1', 'keypad_2', 'keypad_3', 'keypad_4', 'keypad_5', 'keypad_6', 'keypad_7', 'keypad_8', 'keypad_9', 'keypad_0', 'keypad_period',
    'print_screen', 'scroll_lock', 'pause', 'insert', 'home', 'page_up', 'page_down', 'end'
]

manipulators = []

for key in keys:
    manipulators.append({
        "type": "basic",
        "from": {
            "key_code": key,
            "modifiers": {
                "optional": ["any"]
            }
        },
        "to": [
            {
                "key_code": key,
                "modifiers": ["left_command", "left_shift", "left_control", "left_option"]
            }
        ],
        "conditions": [
            {
                "type": "device_if",
                "identifiers": [
                    {
                        "vendor_id": vendor_id,
                        "product_id": product_id
                    }
                ]
            }
        ]
    })

rule = {
    "description": "Map all non-modifier keys to cmd+shift+ctrl+option+key for a specific device",
    "manipulators": manipulators
}

profile = {
    "name": "Default profile",
    "complex_modifications": {
        "rules": [rule]
    }
}

config = {
    "profiles": [profile]
}

with open("script.json", "w") as f:
    json.dump(config, f, indent=2)
