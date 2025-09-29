#composite Pattern
from abc import ABC,abstractmethod
class FileSystemComposite(ABC):
    
    @abstractmethod
    def show(self, indent:int):
        pass

class File(FileSystemComposite):
    
    def __init__(self, fname, size="12kb"):
        self.filename=fname
        self.file_size=size
    def show(self, indent):
        print(' '*indent+f"The file name is {self.filename}")
        
    def get_size(self):
        return self.file_size

class Folders(FileSystemComposite):
    
    def __init__(self, fname, size="50kb"):
        self.children=[]
        self.foldername=fname
        self.folder_size=size
    
    def addchild(self,child:FileSystemComposite):
        self.children.append(child)
    def show(self, indent):
        print(' '*indent+f"The folder name is {self.foldername}")

        for child in self.children:
            child.show(indent+4)

    def get_size(self):
        return sum(child.get_size() for child in self.children)
root=Folders("root")
folder1=Folders("Folder 1")
folder2=Folders("Folder 2")
file1=File("File 1")
file2=File("File 2")

root.addchild(folder1)
root.addchild(folder2)
folder1.addchild(file1)

root.show(0)

""" 

Composite Pattern Concept : Composite Pattern allows you to represent tree-like structures.




Problem: We want to treat individual objects (Files) and groups of objects (Folders) uniformly.


Key idea:

Component (common interface)

Leaf (File, no children)

Composite (Folder, can contain children)


Interview Explanation

If asked:

“Explain Composite Pattern in this file system example.”

You can say:

“Composite Pattern lets us treat individual files and folders uniformly because both implement the same interface FileSystemComponent. A File is a leaf node, while a Folder is a composite that can contain other components. This way, we can call show() on both a file or a folder, and folders recursively call show() on their children. This is especially useful for representing hierarchical structures like file systems, UI elements, or organizational charts.”
"""
