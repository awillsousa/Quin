#path_app = '/home/willian/desenv/master/Quin/'
import sys
sys.path.append('.')
sys.path.append('..')

import pickle
from quin import Quin

# Carrega os documentos serializados
documentos = None
with open('data/docs.pickle', 'rb') as f_docs:
    documentos = pickle.load(f_docs)

# Indexa em um indice Faiss
q = Quin(mode='index', index_path='index')
q.index_documents(documents=documentos)


