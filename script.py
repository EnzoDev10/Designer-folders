import os, shutil

while True:
    try:
        # 1 Ask for the path to a folder
        folder_path = input("Dirección de la carpeta: ")

        # 2 Create a list that contains the names of the files
        file_list = [
            "Iconos",
            "Logos",
            "imágenes",
            "Ideas y Ejemplos",
            "Fuentes.txt",
            "Textos.txt",
        ]

        # 3 Loop the list and:
        for file in file_list:
            # 4 For each item in the list create a file path
            file_path = folder_path + "\\" + file

            # 5 If the file doesn't exists create it and move it to the folder and:
            if not os.path.exists(file_path):
                
                #6 If the file_path doesn't ends with .txt create a folder
                if not file_path.endswith(".txt"):    
                    os.mkdir(file_path)

                #7 Else, create a .txt file
                else:
                    with open(file_path, 'w') as fp:
                        pass

            # 6 Else, check the next one
            else:
                pass

        break
    except FileNotFoundError:
        print("La dirección es incorrecta o no existe.")



# Regex for a folder path: /^[a-zA-Z]:\(?:\w+\?)*$/

# MVP:
# + Ask for a path to an existent folder.
# + Create 7 different folders and 2 .txt files.
# + The organization should be the next:
# 	+ 📁 Iconos
# 	+ 📁Logos
# 	+ 📁Imágenes
# 		+ 📁 Vectores
# 		+ 📁 Fondos
# 		+ 📁 Overlays
# 	 + 📁 Ideas y Ejemplos
# 	 + 📄 Fuentes.txt
# 	 + 📄Textos.txt
