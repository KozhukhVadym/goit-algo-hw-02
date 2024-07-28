from collections import deque

def is_palindrome(s: str) -> bool:
    # Функція для очищення рядка: видалення пробілів та приведення до нижнього регістру
    def clean_string(s: str) -> str:
        return ''.join(char.lower() for char in s if char.isalnum())

    # Очищаємо вхідний рядок
    cleaned_s = clean_string(s)
    
    # Створюємо двосторонню чергу
    dq = deque(cleaned_s)
    
    # Порівнюємо символи з обох кінців черги
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
            
    return True

# Приклади використання
print(is_palindrome("No lemon, no melon"))  # Повертає True
print(is_palindrome("Madam, in Eden, I'm Adam"))  # Повертає True
print(is_palindrome("Never odd or even"))              # Повертає True
print(is_palindrome("Hello, World"))                  # Повертає False
