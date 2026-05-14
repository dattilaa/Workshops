class RomanNumber:
    """
    Class that supports both roman and decimal interpretations
    """

    roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    def __init__(self, num: str):
        self.rom_value = num
        if not RomanNumber.is_roman(num):
            print('Ошибка')
            self.rom_value = None


    def __repr__(self):
        return f'{self.rom_value}'


    @staticmethod
    def is_roman(value: str):
        if not isinstance(value, str) or not value:
            return False

        for char in value:
            if char not in RomanNumber.roman_symbols:
                return False

        invalid_patterns = [
            'IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM',
            'IVI', 'IXI', 'XLX', 'XCX', 'CDC', 'CMC',
            'IL', 'IC', 'ID', 'IM', 'VX', 'VL', 'VC', 'VD', 'VM',
            'XD', 'XM', 'LC', 'LD', 'LM', 'DM'
        ]

        for pattern in invalid_patterns:
            if pattern in value:
                return False

        prev_value = 0
        count = 0

        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for ch in reversed(value):
            curr_value = roman_map[ch]

            if curr_value < prev_value:
                if ch in ['V', 'L', 'D']:
                    return False
                if count > 1:
                    return False

            if curr_value == prev_value:
                count += 1
                if ch in ['V', 'L', 'D']:
                    return False
            else:
                count = 1

            prev_value = curr_value

        return True

    def decimal_number(self):
        if self.rom_value is None:
            return None

        roman_map = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        result = 0
        prev = 0

        for char in reversed(self.rom_value):
            current = roman_map[char]
            if current < prev:
                result -= current
            else:
                result += current
            prev = current

        return result





