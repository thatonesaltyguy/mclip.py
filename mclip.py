import sys, pyperclip

text = {"agree": "sure lets do this but later i am very busy right now ",
"busy": "hey sorry but looks like i wont be able to help you,my schedule is super packed right now maybe we can do this later? ",
"lessgo": "lets do this whenever you are free, super exited about this project "
}
keyphrase = sys.argv[1]
if keyphrase in text:
 pyperclip.copy(text[keyphrase])
 print("the praragraph for" " " + keyphrase + " " "has been pasted")
else:
    print("your request is invalid")

 



