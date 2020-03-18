import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0.0, 12*np.pi, 0.01)
x = np.sin(t)*(np.e**np.cos(t) - 2*np.cos(4*t)-np.sin(t/12)**5)
y = np.cos(t)*(np.e**np.cos(t) - 2*np.cos(4*t)-np.sin(t/12)**5)
plt.figure(figsize=(8,6))
plt.axis('off')
plt.plot(x,y,color='blue',linewidth = '2')
#plt.show()
plt.savefig("butter.jpg",dpi=400)

from PIL import Image
im = Image.open("butter.jpg")
favicon = im.resize((50,50))
favicon.save("favicon.ico")
