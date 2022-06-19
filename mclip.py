import sys, pyperclip

text = {"agree": "sure lets do this but later i dont want to waste your precious time ",
"busy": "nah i am not interested in this shitshow that you call your life ",
"lessgo": "lets do this shit cuz why not lol "
}
keyphrase = sys.argv[1]
if keyphrase in text:
 pyperclip.copy(text[keyphrase])
 print("the praragraph for" " " + keyphrase + " " "has been pasted")
else:
    print("your request is invalid")

 



