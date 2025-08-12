
"""


#method 1
# with open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/my_file.txt")as file_ops:

#     contents = file_ops.read()
#     print(contents)
# method 2
#  file_ops = open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/my_file.txt")
# contents = file_ops.read()
# print(contents)
"""


# with open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/my_file.txt",mode ="a") as file_ops: #"r" - reads the file :"" w" - overwrites file and replaces with new text : "a"- adds to existing text in file
#     file_ops.write("\nTexto de nuevo") #inserts text in new line 
   
with open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/my_file.txt",mode ="a") as file_ops: #"r" - reads the file :"" w" - overwrites file and replaces with new text : "a"- adds to existing text in file
    file_ops.write("\nTexto de nuevo") #inserts text in new line 

# with open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/my_file.txt", mode ="a") as file_ops: 
    
#     file_ops.write("\ndesplazamiento") 

with open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/my_file.txt")as file_ops:

    contents = file_ops.read()
    print(contents)
with open("/Users/kgreen/PycharmProjects/PYLEARNING/day24_files /file_example/nuevo_file.txt", mode ="r") as file_ops: 
    
    file_ops.write("\ndesplazamiento") 

#file_ops.close()