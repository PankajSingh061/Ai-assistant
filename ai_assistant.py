import webbrowser

def open_website(website):
    """
    Opens a specified website in the default web browser.
    
    Args:
        website (str): The URL of the website to open.
    """
    webbrowser.open(website)

def main():
    while True:
        user_input = input("Hello! How can I assist you today? (Type 'exit' to quit) ").lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif 'youtube' in user_input:
            open_website("https://www.youtube.com")
        elif 'instagram' in user_input:
            open_website("https://www.instagram.com")
        elif 'linkedin' in user_input:
            open_website("https://www.linkedin.com")
        elif 'facebook' in user_input:
            open_website('https://www.facebook.com')
        else:
            print("I'm not sure how to help with that. Try asking to open YouTube, Instagram, or LinkedIn.")

if __name__ == "__main__":
    main()
