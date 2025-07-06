from difflib import SequenceMatcher

with open('untitled1.txt') as one_file, open('untitled2.txt') as two_file:
    data_file1 = one_file.read().strip().replace('\r\n', '\n')
    data_file2 = two_file.read().strip().replace('\r\n', '\n')

matches = SequenceMatcher(None, data_file1, data_file2).ratio() * 100

print(f"The plagiarized content is {matches:.2f}%")






