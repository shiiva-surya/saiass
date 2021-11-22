from tree_sitter import Language, Parser

import pep8ext_naming
def find_ident(node, lis_ident):
    if(node.type == "identifier"):
        return [node.start_point, node.end_point]
    elif(len(node.children) != 0):
        count = 0
        while(count != len(node.children)):
            l = find_ident(node.children[count], lis_ident)
            count += 1
            if l=="0" or l==lis_ident:
                continue
            if(len(l) != 0):
                lis_ident.append(l)
        return lis_ident
    return "0"


fin = open("C:\\Users\\shiva\\Downloads\\sai_new\\NAME.py", 'r')
a = fin.read()

Language.build_library(
    # Store the library in the `build` directory
    'build/my-languages.so',

    # Include one or more languages
  [
      'vendor/tree-sitter-python'
  ]
)

PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

tree = parser.parse(bytes(a, "utf8"))


root_node = tree.root_node
i = len(root_node.children)
count = 0
l=[]
while(i != count):
    n = root_node.children[count]  # n- expression statement
    l1=find_ident(n.children[0], [])
    count += 1
    if(len(l1) == 0):
        continue 
    l.append(l1)
a=a.split('\n')
sl=[]
check=[]
for i in l:
    for j in i:
        s=a[j[0][0]][j[0][1]:j[1][1]]
        if s in check:
            continue
        sl.append([s,j[0][0],j[0][1],j[1][1]])
        check.append(s)
out1=open("output1.txt","w")
print(1)
for i in sl:
     out1.write(i[0]+"  Location: ["+str(i[1])+","+str(i[2])+"] - ["+str(i[1])+","+str(i[3])+"]\n")
out1.close()
    
"""first part of output is done----need to include filepath"""

