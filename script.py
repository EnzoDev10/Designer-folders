import os, shutil


def create_files(folder_path):
    # 1 Creates a list that contains the names of the files
    file_list = [
        "Iconos",
        "Logos",
        "Imágenes",
        "Ideas y Ejemplos",
        "Fuentes.txt",
        "Textos.txt",
    ]

    # A list for the name of the subfolders
    subfolders_list = ["Vectores", "Fondos", "Overlays"]

    # 2 Loop the list and:
    for file in file_list:
        # 3 For each item in the list create a file path
        file_path = folder_path + "\\" + file

        # 4 If the file doesn't exists create it and move it to the folder and:
        if not os.path.exists(file_path):

            # 5 If the file_path ends with .txt create the file
            if file_path.endswith(".txt"):
                with open(file_path, "w") as fp:
                    pass

            # 6 Else if the file path ends with "Imagenes",
            # create three subfolders and move them inside
            elif file_path.endswith("Imágenes"):
                os.mkdir(file_path)

                for subfolder in subfolders_list:
                    os.mkdir(subfolder)
                    shutil.move(subfolder, file_path)

            # 7 Else create a folder
            else:
                os.mkdir(file_path)

        # 8 Else if the file exist, check the next one
        else:
            pass


while True:
    try:
        folder_path = input("Dirección de la carpeta: ")
        create_files(folder_path)
        print("\nCarpetas creadas con exito!\n")

        break
    except FileNotFoundError:
        print("\nLa dirección es incorrecta o no existe.\n")
        answer = input("\nQuieres crearla?[si/no]: \n").lower()
        if answer == "si":
            os.mkdir(folder_path)
            create_files(folder_path)
            print("\ncarpeta creadas con exito!\n")
            break
        else:
            print("\nLa carpeta no sera creada.\n")
            break
