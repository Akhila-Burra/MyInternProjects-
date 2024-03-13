def word_count(text):
    """
    Count the number of words in the given text.
    
    Parameters:
    text (str): The input text to count words from.
    
    Returns:
    int: The number of words in the text.
    """
    # Split the text into words using whitespace as delimiter
    words = text.split()
    
    # Return the count of words
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    text = input("Enter a sentence or paragraph: ")
    
    # Check if the input is empty
    if not text:
        print("Error: Empty input. Please enter some text.")
        return
    
    # Call the word_count function to count words
    count = word_count(text)
    
    # Display the word count
    print("Word count:", count)

if __name__ == "__main__":
    main()
