#Search Engine

print("Masukan text yang mau dicari :")

text = input()
word = input()

def search(text, word):
	if word in text:
		return("Word Found!!")
	else:
		return("Word not found!!")


print(search(text,word))
