import pandas as pd
import numpy as np

def map(ds):
    mapped_op = {}
    for i in range(len(ds)):
        sample = ds[i]
        if (sample[0] not in mapped_op):
            mapped_op[sample[0]] = []
        mapped_op[sample[0]].append(sample[2])
    return mapped_op

def emit(dict,str):
    i = 1
    for m_id,list_rating in dict.items():
        print("\nindex: ",i," movie id: ",m_id,"\n",str)
        print(list_rating)
        i += 1
        if( i == 6):
            break

def reduce(mapped_op):
    reduced_op = {}
    for m_id,list_rating in mapped_op.items():
        reduced_op[m_id] = np.mean(list_rating)
    return reduced_op

def main():
    df = pd.read_csv("/home/chaitrali/Desktop/python/dataset/movie.csv",sep = "\t",names = ["m_id","u_id","rating","timestamp"])
    ds = df.values.tolist()
    mapped_op = map(ds)
    print("\nThere are ",len(mapped_op)," unique films in dataset of ",len(ds)," samples.")
    print("\nFirst five emitted values of mapped output: ")
    emit(mapped_op,"list of ratings: ")
    reduced_op = reduce(mapped_op)
    print("\nFirst five emitted values of reduced output: ")
    emit(reduced_op,"averaged rating: ")

main()
