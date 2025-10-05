name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(f"Name: {name}", file=out_file)
out_file.close()


in_file = open("name.txt", 'r')
text = in_file.read()
in_file.close()
print(text)

