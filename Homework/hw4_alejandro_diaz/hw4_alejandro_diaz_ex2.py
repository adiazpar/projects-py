"""
Homework 4 Exercise 2
Name: Alejandro Diaz
Due Date: 10/24/23

Exercise 2:
You have a boring task of finding every phone number and email address in a long web page or
document. If you manually scroll through the page, you might end up searching for a long time.
Implement a phone number extractor and email address extractor as two regexes. Your phone and
email address extractors will need to do the following:

    - Find all phone numbers and email addresses in some text. You can use this link to test
        phone numbers (ignore numbers that contain non-numeric characters like 1–800-U-
        HELP-ME, but your code needs to handle numbers like 911, 1–800–252–2873, 1 (800)
        843–5763, and numbers with an optional area code and extension). You are free to
        manually find some other pages for testing, then define a string variable that contains
        several phone numbers (3-5 numbers in different format), and test your phone number
        regex.

    - An email is typically in this format: username@domain. The username part of the email
        should include upper/lower case letters, numbers, dot (.), underscore, and %, +, - can also
        be included. The domain part we can just consider two levels after @. The first level can
        have upper/lower case letters, numbers, underscore (similar to username but cannot
        include %, +, -). The second level should just be .com, .org, .edu, and so on. Some email
        format like john_doe@python.co.uk can be ignored. Define a string variable containing
        several email addresses (3-5 different emails), and test your email regex.

    - Print all the matches to the screen.

Note that finding a web page and selectively copying its content is not what you need to implement.
"""
import re


def extract_phone_numbers(nums):
    ph_pattern = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'

    ph_list = re.findall(ph_pattern, nums)
    print("Phone Numbers found: \n", ph_list, "\n")


def extract_emails(mails):
    em_pattern = r'\S+@\S+'

    email_list = re.findall(em_pattern, mails)
    print("Emails found: \n" , email_list, "")


if __name__ == "__main__":
    phone_numbers = ("My cellphone number is (719) 510-1818, but it may actually be 720-456-3879. "
                     "A friend of mine owns a business, contact him at 1-800-321-9856. "
                     "Finally, Contact my hedgehog, Odus Flex, at 1 (800) 843-5763, but he can also "
                     "be reached at +1 719-678-5012.")

    emails = ("My personal email address is alexdiaz0923@gmail.com. My school email is adiazpar@uccs.edu. "
              "Contact my friend, Eric, at goofygaf@goof.io or chacha3@gov.org.")

    extract_phone_numbers(phone_numbers)
    extract_emails(emails)
