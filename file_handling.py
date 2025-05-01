# Common modes:
# | Mode | Purpose             |
# | `"r"` | Read (default)       |
# | `"w"` | Write (overwrite)    |
# | `"a"` | Append               |
# | `"rb"`| Read binary (like images) |
# | `"wb"`| Write binary         |


# ✅ open() — Open a File
file = open("example.txt", "r")  # "r" = read mode


# ✅ read() — Read the Content
content = file.read()
print(content)
file.close()

# Other read options:
# file.readline()      # Reads one line
# file.readlines()     # Reads all lines as list


# ✅ write() — Write to a File
file = open("example.txt", "w")
file.write("Hello, world!\n")
file.write("Writing to a file in python")
file.close()

# ⚠️ Note: "w" will overwrite the file if it already exists.

# ✅ Better Way: Use with Block (Auto Close)

with open("example.txt","r") as f:
    data = f.read()
    print(data)
#
with open("example.txt","w") as f:
    f.write("This is safe writing")


# ✅ Small Real-World Use Case

with open("example.txt","r") as r:
    for line in r:
        print(line.strip())

# Write processed data to a new file
with open("cleaned.txt", "w") as f:
    f.write("Cleaned data goes here.")



# Practice with txt file
with open("practice_data.txt","r") as r:
    for line in r:
        print(line.strip())

with open("practice_data.txt","a") as a:
    text = input("Enter a line to add the file")
    a.write(f"{text}\n")


with open("practice_data.txt","r") as r:
    for line in r:
        print(line.strip())


# Practice with csv file using python and pandas

with open("sample_data.csv","r") as r:
    for line in r:
        print(line.strip())