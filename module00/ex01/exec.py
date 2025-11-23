import sys

# recuperer les arguments a partir du 1er
# text = sys.argv[1::]

# join la liste avec " " entre
# text = " ".join(text)

# swapcase la str
# text = text.swapcase()

# afficher a l'envers
# print (text[::-1])

print(" ".join(sys.argv[1::]).swapcase()[::-1])