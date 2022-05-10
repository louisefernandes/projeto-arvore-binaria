'''
Classe para instanciação de nós que vão ficar na memória
'''

class Node:
    def __init__(self,data:object):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    @property
    def data(self)->object:
        return self.__data

    @data.setter
    def data(self, newData:object):
        self.__data = newData

    @property
    def leftChild(self)->'Node':
        return self.__leftChild

    @leftChild.setter
    def leftChild(self, newLeftChild:object):
        self.__leftChild = newLeftChild

    @property
    def rightChild(self)->'Node':
        return self.__rightChild

    @rightChild.setter
    def rightChild(self, newRightChild:'Node'):
        self.__rightChild = newRightChild

    def insertLeft(self, data:object):
        if self.__leftChild == None:
            self.__leftChild = Node(data)	

    def insertRight(self,data:object):
        if self.__rightChild == None:
            self.__rightChild = Node(data)

    def __str__(self):
        return str(self.__data)

    def hasLeftChild(self)->bool:
        return self.__leftChild != None

    def hasRightChild(self)->bool:
        return self.__rightChild != None
        
	    
'''
Esta classe é um exemplo de um da estrutura de Arvore Binária implementada
como uma classe.
'''
class BinaryTree:
    # constructor initializes an empty Tree of integers
    def __init__(self, data_root:object):
        self.root = Node(data_root)
        self.cursor = self.root

    def getRoot(self)->'Node':
        return self.root

    def downLeft(self)->'Node':
        if(self.cursor.hasLeftChild()): 
            self.cursor = self.cursor.leftChild
            return self.cursor
        else:
            return None
            
    def downRight(self)->'Node':
        if(self.cursor.hasRightChild()): 
            self.cursor = self.cursor.rightChild
            return self.cursor
        else:
            return None

    def addLeftChild(self, dado:object):
        if(not self.cursor.hasLeftChild()):
            self.cursor.leftChild = Node(dado)

    def addRightChild(self, dado:object):
        if(not self.cursor.hasRightChild()):
            self.cursor.rightChild = Node(dado)

    def resetCursor(self):
        self.cursor = self.root

    def getCursor(self)->'Node':
        return self.cursor

    def search(self, chave:object )->'Node':
        return self.__searchData(chave, self.root)
    
    def __searchData(self, chave, node):
        if (node == None):
            return False # Nao encontrou a chave
        if ( chave == node.data):
            return True
        elif ( self.__searchData( chave, node.leftChild)):
            return True
        else:
            return self.__searchData( chave, node.rightChild)

    def preorderTraversal(self):
        self.__preorder(self.root)

    def inorderTraversal(self):
        self.__inorder(self.root)

    def postorderTraversal(self):
        self.__postorder(self.root)
        
    def __preorder(self, node):
        if( node == None):
            return
        print(f'{node.data} ',end='')
        self.__preorder(node.leftChild)
        self.__preorder(node.rightChild)

    def __inorder(self, node):
        if( node == None):
            return
        self.__inorder(node.leftChild)
        print(f'{node.data} ',end='')
        self.__inorder(node.rightChild)

    def __postorder(self, node):
        if( node == None):
            return
        self.__postorder(node.leftChild)
        self.__postorder(node.rightChild)
        print(f'{node.data} ',end='')

    def deleteTree(self):
        # garbage collector fará o trabalho de eliminação dos nós
        # abandonados 
        self.root = None

    # o cursor tem que estar posicionado no nó pai
    # do nó que vai ser removido
    def deleteNode(self, key:object):
        self.__deleteNode(self.cursor, key)


    def __deleteNode(self,root, key):

        if root is None: 
            return
        elif root.leftChild == None and root.rightChild == None:
            return
        
        if root.leftChild == None:
            if root.rightChild.data == key:
                root.rightChild = None
        elif root.rightChild == None:
            if root.leftChild.data == key:
                root.leftChild = None


if __name__ == '__main__':  
    tree = BinaryTree(30)
    tree.addLeftChild(15)
    tree.addRightChild(17)
    print(tree.downLeft())
    tree.addLeftChild(70)
    tree.resetCursor()
    print(tree.downRight())
    tree.addLeftChild(5)
    tree.addRightChild(52)
    print(tree.downLeft())
    tree.addRightChild(77)

    print('Root:',tree.getRoot())
    print('Cursor:',tree.getCursor())

    tree.preorderTraversal()
    print()
    tree.inorderTraversal()
    print()
    tree.postorderTraversal()
    chave = 150
    if( tree.search( chave )):
        print('\nChave',chave,'está na árvore')
    else:
        print('\nChave',chave,'NÃO está na árvore')


    print('Cursor:',tree.getCursor())
    chave = 77
    tree.preorderTraversal()
    tree.deleteNode(chave)
    tree.preorderTraversal()
    print()
    print()
    chave = 70
    tree.preorderTraversal()
    print()
    tree.deleteNode(chave)
    tree.preorderTraversal()
