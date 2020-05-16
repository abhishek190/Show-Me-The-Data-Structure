import sys
import heapq
class Huff_Node:
    def __init__(self,value, wt):
        """Create node for given symbol and weight."""
        self.left = None
        self.right = None
        self.value = value
        self.wt = wt        
    def __lt__(self, other):
        return self.wt < other.wt
    def __str__(self):
        return str(self.value)+" "+str(self.wt)
    

def get_frequecies(data):
  freq = {}
  for item in data:
    if item not in freq:
      freq[item] = 1
    else:
      freq[item] +=1
  freq_sorted = sorted(zip(freq.values(), freq.keys()))
  for i in range(len(freq_sorted)):
     value = freq_sorted[i][1] 
     freq = freq_sorted[i][0] 
     freq_sorted[i] = Huff_Node(value, freq)
  return freq_sorted  
def huffman_tree(data):
    heap = get_frequecies(data)
    heapq.heapify(heap)
    while len(heap) != 1:
        Z = Huff_Node(None,None)
        lft = heapq.heappop(heap)
        Z.left  = lft
        rgt = heapq.heappop(heap)
        Z.right  = rgt
        Z.wt = lft.wt + rgt.wt
        heapq.heappush(heap, Z)
    return heap 
def create_Huffcode_table(root):
    code = {}
    def getCode(hNode, currentCode=""):
        if (hNode == None): 
            return
        if (hNode.left == None and hNode.right == None):
            code[hNode.value] = currentCode
        getCode(hNode.left, currentCode + "0")
        getCode(hNode.right, currentCode + "1")
    getCode(root[0])
    return code

def huff_encode(data):
   
    if(len(get_frequecies(data))) == 1:
      return "0"*len(data)
    huff_code = "" 
    root = huffman_tree(data)
    table = create_Huffcode_table(root)
    for item in data:
       huff_code += table[item]
    return huff_code
def huffman_decode(bit_string,root):
    if(len(get_frequecies(bit_string))) == 1:
      return len(bit_string)*str(root.value)
    decode = ""
    n = len(bit_string)
    count = 0
    while count < n:
        current = root[0]
        while current.left != None and current.right != None:
            if bit_string[count] == "0":
                current = current.left
            else:
                current = current.right
            count+=1
        decode+=current.value
    return decode
def huffman_encoding(data):
  return huff_encode(data), huffman_tree(data)
def huffman_decoding(data,tree):
  return huffman_decode(data,tree)
def test_Huffman(data):
  if data == None:
    print(None)
  elif data == "":
    print("Empty String")
  elif len(get_frequecies(data)) == 1:
    code = "0"*len(data)
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(code, base=2))))
    print ("The content of the encoded data is: {}\n".format(code))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(data)))
  else:
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    encoded_data, tree = huffman_encoding(data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


test_Huffman(None)
test_Huffman("")
test_Huffman("The bird is the word")
test_Huffman("h")
