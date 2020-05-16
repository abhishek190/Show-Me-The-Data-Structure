import os
def find_files(suffix, path):
    # create a list of file and sub directories 
    # names in the given directory 
    if path == None:
        return None
    file_list = []
    dir_list= os.listdir(path)  
    # Iterate over all the entries
    for item in dir_list:
        #build path
        temp_path = os.path.join(path, item)
        #recursion base case
        if os.path.isfile(temp_path) and temp_path.endswith(suffix):
            file_list.append(temp_path)
        #if directory, then concatenate current list with all 
        #to be qualified files then recurse 
        elif os.path.isdir(temp_path):
            file_list+=find_files(suffix,temp_path)
                
    return file_list 

print("****Empty test directory****")        
print(find_files(".c", 'C:\\Users\\rawab\\Python 3.8\\testdir'))
print("****No files ending in .c test no_c_dir****")        
print(find_files(".c", 'C:\\Users\\rawab\\Python 3.8\\testdir'))
print("****Single file ending in .c test c_dir****")        
print(find_files(".c", 'C:\\Users\\rawab\\Python 3.8\\testdir'))
print()
