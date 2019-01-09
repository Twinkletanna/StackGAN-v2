import os
import pickle
import torch
folder=('sent_data/text_c10')
cwd=os.getcwd()
Path=os.path.join(cwd,folder)
sentences={}
for folders in os.listdir(Path):
        if not os.path.isfile(os.path.join(Path,folders)):
                Path2=os.path.join(Path,folders)
                for filename in os.listdir(Path2):
                        if ".txt" in filename:
                                file=filename.split('.')[0]
                                with open(os.path.join(Path2,filename),'r') as f:
                                        sent=[]
                                        for line in f:
                                                sent.append(line)
                                        if file not in sentences:
                                                sentences[file]=sent
                        print(filename)
print(len(sentences))
with open('sentences.pkl','wb')as f:
        pickle.dump(sentences,f)
