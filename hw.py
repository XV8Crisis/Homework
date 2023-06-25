def palindrome(str):
    str = input("Введите слово, чтобы удостовериться палиндром это или нет:\n")
    return str [::-1] == str
print(palindrome(str))
