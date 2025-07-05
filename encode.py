import parameters

amountPass = 0

newText = ""

with open(parameters.outputFile,"r") as file:
    text = file.read()

def compress_binary_image(string):

    result = []
    current_char = string[0]
    count = 1
    
    for letter in string[1:]:
        
        if letter == current_char:
            count +=1
        else:
            if count != 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = letter
            count = 1

    result.append(f"{count}{current_char}")
    return "".join(result)

compressed_output = compress_binary_image(text)
print(compressed_output)

with open(parameters.outputFile,"w") as file:
    file.write(compressed_output)