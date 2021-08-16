import os
import numpy as np
import h5py
import argparse
from sklearn.decomposition import PCA

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--path', type=str, default = './capture/')
parser.add_argument('--name', type=str, default='training.h5')
parser.add_argument('--nameinfo', type=bool, default=False)
args = parser.parse_args()

# get all data from dir
files = os.listdir(args.path)
length = len(files)
files.sort()
label = []
nameinfo = []
for f in range(len(files)):
    fname = files[f]
    action, num, m = fname.split('-')
    if action == 'walk':
        label.append(0)
    elif action == 'fall':
        label.append(1)
    elif action == 'sit':
        label.append(2)
    elif action == 'stand':
        label.append(3)
    else:
        label.append(4)
    
    raw = np.genfromtxt(args.path+fname, delimiter=',')
    if len(raw) != 2000:
        print(fname)
    Pca = PCA(n_components=5)
    Pca.fit(raw)
    pca_data = Pca.transform(raw)
    if 'data' in locals():
        data = np.vstack((data,pca_data))
    else:
        data = pca_data
    nameinfo.append(fname.encode("utf-8"))

print(data.shape)
data = data.reshape(length,2000,5)
label = np.array(label)

print(data.dtype,data.shape)

f = h5py.File(args.name,'w')
#g = f.create_group("gourp")
f.create_dataset('data' , data = data)
f.create_dataset('label' , data = label)
if args.nameinfo == True:
    print('filename included\n')
    #nameinfo = np.array(nameinfo,dtype=utf8_type)
    #f.attrs('filename', data = nameinfo)
    f.attrs['filename'] = np.chararray.encode(np.array(nameinfo, dtype='U'), encoding='utf8')
f.close()
