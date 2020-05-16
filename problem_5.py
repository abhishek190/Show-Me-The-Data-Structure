import hashlib
import datetime 
utc = datetime.datetime.utcnow()
def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()
class Block:

    def __init__(self, data, previous_hash):
      utc = datetime.datetime.utcnow()
      self.timestamp = utc
      self.data = data
      self.previous_hash = previous_hash
      self.previous_block = None
      self.hash = calc_hash(str(data))
    def __str__(self):
        return str(self.timestamp)+" "+str(self.data)+" "+str( self.previous_hash)+" "+str( self.hash)
class BlockChain:

    def __init__(self):
        self.head = None
    def append(self, data,previous_hash):
        if self.head is None:
          self.head = Block(data,0)
          return
        new_head = Block(data,self.head.hash)
        new_head.previous_block = self.head
        self.head = new_head
    def size(self):
      size = 0
      block = self.head
      while block:
          size += 1
          block = block.previous_block
      return size
    def to_list(self):
      out = []
      block = self.head
      while block:
        out.append(block)
        block = block.previous_block
      return out
print("Test Case 1 Empty BlockChain")
A = BlockChain()
print("size",A.size())
print(A.head)
print()
print("Test Case 2 One item BlockChain")
B = BlockChain()
B.append("Genesis",0)
print("size",B.size())
for item in B.to_list():
    print(item)
print()
print("Test Case 3 Two item BlockChain")
C = BlockChain()
C.append("Genesis",0)
C.append("Udacity",calc_hash("Genesis"))


print("size",C.size())
for item in C.to_list():
    print(item)

print()
