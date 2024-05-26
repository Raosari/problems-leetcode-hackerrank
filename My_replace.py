def customRep(text, old, new):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    return result

a = customRep("Hola que hace que", 'que', 'como')
print(a)









# def replace(input_string, old_substring, new_substring):
#     # Initialize an empty string to store the result
#     result = ""
#     # Initialize a variable to store the starting index of the next search
#     start_index = 0
    
#     # Iterate through the input string
#     while start_index < len(input_string):
#         # Find the index of the next occurrence of the old substring
#         next_index = input_string.find(old_substring, start_index)
        
#         # If the old substring is not found from the current start_index onwards,
#         # append the remaining part of the input string to the result and exit the loop
#         if next_index == -1:
#             result += input_string[start_index:]
#             break
        
#         # Append the part of the input string from the current start_index to the next_index
#         # (i.e., the part before the old substring)
#         result += input_string[start_index:next_index]
        
#         # Append the new substring to the result
#         result += new_substring
        
#         # Update the start_index to the index after the old substring
#         start_index = next_index + len(old_substring)
    
#     return result


# a = replace("Hola como estan como estan","como estan","ke pasa")
# print(a)


