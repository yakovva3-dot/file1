
import os

# def folder_path():
#     return os.getcwd()
# print(folder_path())


# def folders_list():
#     return os.listdir()
# print(folders_list())


# def switching_between_folders():
#     this_folder = os.getcwd()
#     other_folder = os.chdir('../')
#     return os.listdir(other_folder),this_folder
# print(switching_between_folders())


# def print_file():
#     file_list = os.listdir()
#     for file in file_list:
#         if os.path.isfile(file):
#             print(file)
# print_file()


# def print_file_py():
#     file_list = os.listdir()
#     for file in file_list:
#         if file.endswith(".py"):
#             print(file)
#
# print_file_py()

# def num_of_type_file():
#     file_list = os.listdir()
#     dict_file = {}
#     for file in file_list:
#         ext = os.path.splitext(file)[1]
#         if ext not in dict_file:
#             dict_file[ext]=1
#         elif ext in dict_file:
#             dict_file[ext]+=1
#     print(dict_file)
# num_of_type_file()






# def find_large_files(path, min_size):
#     large_files = []
#     for filename in os.listdir(path):
#         full_path = os.path.join(path, filename)
#         if os.path.isfile(full_path) and os.path.getsize(full_path) > min_size:
#             large_files.append(full_path)
#     return large_files

# print(find_large_files('.', 1000))



def find_duplicate_files(path):
    files_map = {}
    duplicates = {}

    for root, dirs, files in os.walk(path):
        for filename in files:
            full_path = os.path.join(root, filename)
            if filename in files_map:
                files_map[filename].append(full_path)
            else:
                files_map[filename] = [full_path]

    for filename, paths in files_map.items():
        if len(paths) > 1:
            duplicates[filename] = paths

    return duplicates

print(find_duplicate_files('.'))


        
        
        


