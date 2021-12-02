from pickle import load
import os


def load_models(already_loaded,algo):
    if algo not in already_loaded:
        parent_dir=os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        with open(os.path.join(parent_dir,algo+'.sav'),'rb') as f:
            already_loaded[algo]=load(f)

    return already_loaded[algo]

