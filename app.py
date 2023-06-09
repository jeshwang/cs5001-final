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

    Assumptions:
        User says "start" to indicate the start of the list,
        "stop" to indicate the end of the list, and "comma"
        to indicate the end of a list item and the beginning
        of a new one.
    Args:
        filename(str): name of .wav file. Must include
            '.wav' at the end.
    
    Returns:
        str: long string containing the transcription
    """
    # use the audio file as the audio source
    # the Recognizer class recognizes speech!
    r = sr.Recognizer()  # create Recognizer instance
    try:
        grocery = sr.AudioFile(filename)
        with grocery as source:
            audio = r.record(source)

        # Use Google API to return transcription of audio
        # Returns in string type
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
    # 'comma': indicates the end of a list item
    raw = s.find_between(raw)

    # Correct mispellings in transcript using dictionaries:
    #   dict with common mispellings of numbers indicating quantity of item
    #   dict with common mispellings of item names
    #   dict with common spellings of unit measures
    # Note that these dictionaries are meant to be edited over time as the more you
    # use the API with new recordings and mispellings that you'd like to correct.
    quantity = s.load_item("quantity.dat")  
    item = s.load_item("item.dat")
    unit = s.load_item("unit.dat")  

    correct = s.correct_spelling(raw, item)
    correct = s.correct_spelling(correct, quantity)
    correct = s.correct_spelling(correct, unit)
    print(f"Transcript after correcting mispellings: {correct}")

    correct_list = s.split_string(correct)
    print(f"Transcript as list of strings. Each index represents an item and its details: {correct_list}")

    # save list of strings into a ShoppingList
    # default name of ShoppingList is "New List"
    shopping_list = s.save_as_shopping_list(correct_list)
    print(f"ShoppingList details: {shopping_list.__str__()}")
    
    # save ShoppingList to a .txt file
    c.save_list_to_file(shopping_list)
    print("Check out your new grocery list in your file explorer!")


if __name__ == "__main__":
    main()
