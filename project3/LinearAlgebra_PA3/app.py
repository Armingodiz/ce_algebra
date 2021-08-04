from matplotlib import pyplot 
import numpy as np
from numpy import linalg
k = 250
imageName = "1.bmp"
image = pyplot.imread(imageName, format=None)
r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]

uR,sR,vhR = linalg.svd(r)
uG,sG,vhG = linalg.svd(g)
uB,sB,vhB = linalg.svd(b)

muR = uR[:,:k]
msR = np.diag(sR[:k])
mvhR = vhR[:k, :]

muG = uG[:,:k]
msG = np.diag(sG[:k])
mvhG = vhG[:k, :]

muB = uB[:,:k]
msB = np.diag(sB[:k])
mvhB = vhB[:k, :]

newR = muR.dot(msR).dot(mvhR)
newG = muG.dot(msG).dot(mvhG)
newB = muB.dot(msB).dot(mvhB)
decomposed = np.dstack((newR, newG, newB)).astype(np.uint8)
pyplot.imshow(decomposed)
pyplot.imsave(f"decomposedWith_k{k}.png", decomposed)

