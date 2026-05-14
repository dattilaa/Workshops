class RomanNumber:
    """
    Class that supports both roman and decimal interpretations
    """

    roman_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    def __init__(self, num=None, int_num=None):
        self.rom_value = num
        self.int_value = int_num
        if not RomanNumber.is_roman(num):
            print('Ошибка')
            self.rom_value = None

        if not RomanNumber.is_int(int_num):
            print('Ошибка')
            self.rom_value = None


    def __repr__(self):
        return f'{self.rom_value}' if self.rom_value else f'{self.int_value}'


    @staticmethod
    def is_roman(value: str):
        if not isinstance(value, str):
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


    @staticmethod
    def is_int(value: int):
        return isinstance(value, int) and 1 <= value <= 3999



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


    def roman_number(self):
        if self.int_value is None:
            return None

        num = self.int_value
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        result = ''
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result

num_1 = RomanNumber(214)
print(num_1.int_value)
print(num_1.roman_number())
print(num_1.rom_value)
print(num_1)
num_2 = RomanNumber(5690)
print(num_2.int_value)
num_3 = RomanNumber('DXCVII')
print(num_3.int_value)
print(num_3.rom_value)
print(num_3)
print(RomanNumber.is_int(-614))
print(RomanNumber.is_int(3758))








