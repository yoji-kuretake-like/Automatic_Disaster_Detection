#This is the function to convert one hot expression into index values

def onehot2index(pred):
  img_h = pred.shape[0]
  img_w = pred.shape[1]
  img_index = np.zeros((img_h, img_w, 1), dtype = np.float32)
  for h in range(img_h):
    for w in range(img_w):
      index_max = np.argmax(pred[h, w, :])
      img_index[h, w, :] = index_max
  return img_index
