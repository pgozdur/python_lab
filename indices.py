greeting = "Hello, Python!"
sub_greeting = greeting[0:5]  # Extracts 'Hello'
print(sub_greeting)


language = greeting[7:]  # Extracts 'Python!'
print(language)


skip_chars = greeting[::2]  # Extracts 'Hlo yhn'
print(skip_chars)

reversed_greeting = greeting[::-1]  # Reverses the string
print(reversed_greeting)  # Output: '!nohtyP ,olleH'

last_chars = greeting[-7:]  # Extracts 'Python!'
print(last_chars)

middle_chars = greeting[2:-1]  # Extracts 'llo, Python'
print(middle_chars)

nth_chars = greeting[1:10:3]  # Starts at 'e', ends before 'o', taking every 3rd character
print(nth_chars)  # Output: 'e,Ph'
