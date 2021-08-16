import os
import numpy as np
import h5py
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--path', type=str, default = './capture/')
parser.add_argument('--name', type=str, default='training.h5')
args = parser.parse_args()

# get all data from dir
files = os.listdir(args.path)
length = len(files)
label = []

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
    if 'data' in locals():
        data = np.vstack((data,raw))
    else:
        data = raw

print(data.shape)
data = data.reshape(length,2000,56)
label = np.array(label)

print(data.dtype,data.shape)

f = h5py.File(args.name,'w')
#g = f.create_group("gourp")
f.create_dataset('data' , data = data)
f.create_dataset('label' , data = label)
f.close()
