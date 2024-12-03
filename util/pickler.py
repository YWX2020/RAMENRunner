import pickle

def pickle_object(to_pickle, filename):
    pickle_file = open( filename, "ab" )
    pickle.dump( to_pickle, pickle_file )
    pickle_file.close()

def load_pickle(filename):
    pickle_file = open(filename, "rb")
    obj = pickle.load(pickle_file)
    pickle_file.close()
    return obj
