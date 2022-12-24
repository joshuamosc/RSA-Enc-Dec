
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡', ',', '.', '-', ';', ':', '_', 'º', '|', '¬', '™', '£', '¢', '∞', '§', '¶', '•', 'ª', '≠', '´', '+', '{', '}', '¨', '*', '[', ']', '“', '~', 'ˆ', '`', '@', ' ']

def parse_message(message):

    final_message = []


    message_splitted = [i.lower() for i in message]

    for i in message_splitted:
        final_message.append(chars.index(i))

    return final_message

def parse_numbers(numbers):

    final_message = []

    for i in numbers:
        final_message.append(chars[i])

    return "".join(final_message)

