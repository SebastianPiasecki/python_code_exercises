import os
from unittest.mock import patch
path = r'C:\Users\AMD\Desktop\Udemy\Python\mydata.txt'

# os.remove(path)


# if os.path.isfile(path):
#     print('File %s exists' % path)
# else:
#     print('Creating a file %s' % path)
#     open(path, 'x').close()


# result = os.path.isfile(path) or open(path, 'x').close()

# print(result)

# quote = 'Ciemność za oknem bo noc i tylko lampy drogowe'



# with open(path, 'w', encoding='utf-8') as f:
#     f.write(quote)
#     f.close()
#     result = os.path.isfile(path)
   

# print(result)

def countsWords(path):
    with open(path, 'r', encoding='utf-8') as f:    
        content = f.read()
        word_count = len(content.split())
    return word_count




if os.path.isfile(path):
    print("There are {} words in the file {}".format(countsWords(path),path))



#     f.write(quote)

