function toRomanLazy(num) {
  let output = "";
  const romanNumeralToArabic = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
  };
  const romanNumeralPriorityOrder = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];

  for (let numeral of romanNumeralPriorityOrder) {
      while (num >= romanNumeralToArabic[numeral]) {
          output += numeral;
          num -= romanNumeralToArabic[numeral];
      }
  }
  return output;
}


function toRoman(num) {
  let output = "";
  const romanNumeralToArabic = {
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
  };
  const romanNumeralPriorityOrder = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];

  for (let numeral of romanNumeralPriorityOrder) {
      while (num >= romanNumeralToArabic[numeral]) {
          output += numeral;
          num -= romanNumeralToArabic[numeral];
      }
  }
  return output;
}

module.exports = { toRomanLazy, toRoman };