def main():
    print("--- Проверка банковской карты ---")
    card = input("Введите номер карты (своей): ").strip().replace(" ", "").replace("-", "")

    if not card.isdigit():
        print("Ошибка: Номер карты должен содержать только цифры!")
        return

    card_type = check_card_type(card)
    if card_type == "Неизвестный тип карты":
        print("Карта недействительна: не соответствует условиям длины или начальным цифрам для Visa, MasterCard, American Express.")
        return

    if luhn_checksum(card):
        print(f"\nРезультат:")
        print(f"Карта: Действительна")
        print(f"Тип платежной системы: {card_type}")
    else:
        print(f"\nРезультат:")
        print(f"Карта: НЕдействительна")
        print(f"(Контрольная сумма алгоритма Луна не заканчивается на 0)")

def check_card_type(card):
    length = len(card)
    
    if (card.startswith('34') or card.startswith('37')) and length == 15:
        return "American Express"
    
    elif any(card.startswith(prefix) for prefix in ['51', '52', '53', '54', '55']) and length == 16:
        return "MasterCard"
    
    elif card.startswith('4') and (length == 13 or length == 16):
        return "Visa"
    
    return "Неизвестный тип карты"

def luhn_checksum(card_number):
    digits = [int(char) for char in card_number]
    
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
        
    return sum(digits) % 10 == 0

if __name__ == "__main__":
    main()