# Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

# For example: anti_vowel("Hey You!") should return "Hy Y!". Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels.


def anti_vowel(text):
  anti_lower = ["a", "e", "i", "o", "u"]
  anti_upper = []
  for anti in anti_lower:
    anti_upper.append(anti.upper())
  
  diff = [c for c in text if c not in anti_lower and c not in anti_upper]
  
  return "".join(diff)
