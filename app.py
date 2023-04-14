"""
Final
===========================
Student:  Jessica Hwang
Semester: Spring 2023

App that uses the speech_recognition Python library
and Google Web Speech API to transcribe a .wav file
into a .txt file containing a simple, clean shopping list.

Notes:
The execution of this app depends on the availability of this API.
As of April 2023, Google does not require any authentication with an API key
or a username/password combination.
"""
import os
import speech_recognition as sr
import shopping as s
import shopping_classes as c


def transcribe(filename: str) -> str:
    """This function takes in a .wav sound file and 
    uses the speech_recognition package to transcribe
    the audio.

    Args:
        filename(str): name of .wav file. Must include
            '.wav' at the end.
    
    Returns:
        str: long string containing the transcription
    """
    # use the audio file as the audio source
    # the Recognizer class recognizes speech!
    r = sr.Recognizer()
    try:
        grocery = sr.AudioFile(filename)
        with grocery as source:
            audio = r.record(source)

        # Use Google API
        raw = r.recognize_google(audio).lower()
        return raw
    except FileNotFoundError:
        print(f"{filename} not found!")
    except OSError as a:
        print(a)


def main():
    # Transcribe the audio file using Google API
    raw = transcribe('grocery_final.wav')
    print(f"Raw transcription from Google: {raw}")

    # Clip the transcription using keywords.
    # 'start': indicates start of list 
    # 'stop': indicates end of list.
    raw = s.find_between(raw)

    # Correct mispellings in transcript using dictionaries:
    #   dict with common mispellings of numbers indicating quantity of item
    #   dict with common mispellings of item names
    # Note that these dictionaries are meant to be edited over time as the more you
    # use the API with new recordings and mispellings that you'd like to correct.
    quantity = s.load_item("quantity.dat")  
    item = s.load_item("item.dat")  

    correct = s.correct_spelling(raw, item)
    correct = s.correct_spelling(correct, quantity)
    print(f"Transcript after correcting mispellings: {correct}")

    correct_list = s.split_string(correct)
    print(f"Split transcript into a list of strings, where each entry represents an item: {correct_list}")

    # save list of strings into a ShoppingList
    shopping_list = s.save_as_shopping_list(correct_list)
    print(f"Name and total # of items of the resulting ShoppingList: {shopping_list.__str__()}")

    # save ShoppingList to a .txt file
    c.save_list_to_file(shopping_list)


if __name__ == "__main__":
    main()
