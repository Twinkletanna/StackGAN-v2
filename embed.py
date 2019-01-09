import torch
import pickle
GLOVE_PATH = '../dataset/GloVe/glove.840B.300d.txt'
infersent = torch.load('infersent.allnli.pickle')
infersent.set_glove_path(GLOVE_PATH)

with open('../sentences.pkl','rb') as f:
        sentences=pickle.load(f)

embed={}
i=0
for k in sentences.keys():
        infersent.build_vocab(sentences[k], tokenize=True)
        embeddings = infersent.encode(sentences[k], tokenize=True)
        #print ('Encoded : {0}'.format(len(embeddings)))
        i+=1
        print (i)
        if k not in embed:
                embed[k]=embeddings

with open('embeddings2.pkl','wb') as f:
        pickle.dump(embed,f)
