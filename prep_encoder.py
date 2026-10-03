def encode_word(word, prefix, suffix):
    if len(prefix) > 3 or not prefix.isalpha():
        raise ValueError("Prefix must contain only alphabets and be at most 3 characters long.")
    if len(suffix) > 3 or not suffix.isalpha():
        raise ValueError("Suffix must contain only alphabets and be at most 3 characters long.")

    if len(word) <= 3:
        return word[::-1]

    return prefix + word[1:] + word[0] + suffix


def main():
    try:
        count = int(input("Enter the number of words you want to encode: "))
        encoded_words = []

        prefix = input("Enter a prefix (up to 3 alphabets): ")
        suffix = input("Enter a suffix (up to 3 alphabets): ")

        for _ in range(count):
            word = input("Enter your word: ").strip()
            encoded_words.append(encode_word(word, prefix, suffix))

        print(" ".join(encoded_words))

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()