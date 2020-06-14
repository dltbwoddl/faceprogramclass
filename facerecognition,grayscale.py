import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

imagelist=[]
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        imagelist.append(os.path.join(dirname, filename))
import face_recognition
import numpy as np
from PIL import Image
i=10000100
for imagefile in imagelist:
    img = face_recognition.load_image_file(imagefile)
    face_locations = face_recognition.face_locations(img)
    if len(face_locations)==1:
        a=face_locations[0][0]
        b=face_locations[0][2]
        c=face_locations[0][3]
        d=face_locations[0][1]
        img=Image.open(imagefile)
        img=np.array(img)
        img=Image.fromarray(img[a:b,c:d])
        img.save(str(i)+'.jpg')
        img=Image.open(str(i)+'.jpg').convert("LA")
        img.save(str(i)+'.png')
    i+=1
