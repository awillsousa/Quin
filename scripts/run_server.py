path_app = '/home/willian/desenv/master/Quin/'
import os
os.chdir(path_app)
from quin import Quin

# Serve o indice por meio de API Flask
q = Quin(mode='serve', index_path='index')
q.serve()


