def toRomanLazy(num):
    output = ""
    romanNumeralToArabic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    romanNumeralPriorityOrder = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    for numeral in romanNumeralPriorityOrder:
        while num >= romanNumeralToArabic[numeral]:
            output += numeral
            num -= romanNumeralToArabic[numeral]

    return output


def toRoman(num):
    output = ""
    romanNumeralToArabic = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    romanNumeralPriorityOrder = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    for numeral in romanNumeralPriorityOrder:
        while num >= romanNumeralToArabic[numeral]:
            output += numeral
            num -= romanNumeralToArabic[numeral]

    return output
