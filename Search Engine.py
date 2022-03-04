#Search Engine

print("Masukan text yang mau dicari : ")

text = input()
word = input()

def search(text, word):
	if word in text:
		return("Keyword ditemukan!!")
	else:
		return("Keyword tidak ditemukan!!")


print(search(text,word))
