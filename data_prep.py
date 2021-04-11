import numpy as np
import pandas as pd
from glob import iglob
import gzip
import os
import shutil
import json

PATH_WITH_GZ = "archiv/"
NEW_PATH = "dataset/"


def unzip():
    for file in iglob(PATH_WITH_GZ + "/*.gz"):
        with gzip.open(file, 'rb') as f_in:
            with open(os.path.join(NEW_PATH, os.path.basename(file)[:-3]), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

def read_data():
    result = dict()
    i = 0
    for file in iglob(NEW_PATH + "/*"):
        print(i)
        i += 1
        with open(file, 'rb') as f:
            content = f.read()
            for paper in content.decode('utf-8', 'ignore').split('\n'):
                if paper:
                    paper = json.loads(paper)
                    id = paper.pop('id')
                    result[id] = paper
    return result

if __name__ == "__main__":
    data = read_data()
    with open("data.pickle", "wb") as f:
        pickle.dump(data, f)
