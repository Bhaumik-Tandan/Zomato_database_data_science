from pickle import load
import os

def load_cuisines():
    parent_dir=os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    with open(os.path.join(parent_dir,"cuisines"+'.txt'),'rb') as f:
        cuisines=load(f)

    return cuisines