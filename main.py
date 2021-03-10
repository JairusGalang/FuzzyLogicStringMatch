from fuzzywuzzy import fuzz

sampleWords = fuzz.ratio("New York","New York")
secondSampleWords = fuzz.partial_ratio("Red Velvet", "Velvet Red")
fuzzyBear = fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")

print(f"Ratio: {sampleWords}")
print(f"Partial Ratio: {secondSampleWords}")
print(f"Token Set Ratio: {fuzzyBear} ")