name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(f"Name: {name}", file=out_file)
out_file.close()