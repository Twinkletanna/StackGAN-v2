import numpy as np
import pickle
data_dir = '/mnt/nfs/work1/696ds-s18/srideepikaja/data/birds/train/'
embedding_filename = 'embeddings.pkl'

with open(data_dir + embedding_filename, 'rb') as f:
            embeddings = pickle.load(f)
            #embeddings = np.array(embeddings)
            # embedding_shape = [embeddings.shape[-1]]
            embeddings = np.array([embeddings[key] for key in embeddings.keys()])
            print('embeddings: ',embeddings.shape)
#            print('embeddings: ',np.array( embeddings[embeddings.keys()[0]]).shape)


