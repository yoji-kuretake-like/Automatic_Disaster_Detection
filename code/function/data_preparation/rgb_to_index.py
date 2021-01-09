# This is the function to turn the pixel values into index values


palette_list = [(255, 255, 255), # Impervious surfaces (white) : 0
                (0, 0, 255),  # Buildings (blue) : 1
                (0, 255, 255), # Low vegetation (cyan) : 2
                (0, 255, 0), # Trees (green) : 3
                (255, 255, 0), # Cars (yellow) : 4
                (255, 0, 0)] # Clutter (red) : 5

def comp_pixel(val, palette):
  for idx, clr in enumerate(palette):
    judje = val == clr
    if all(judje) == True:
      return idx



def rgb2index(img, palette):
  img_h, img_w = img.shape[0], img.shape[1]
  index_colar = np.zeros((img_h, img_w, 1), dtype = np.float32)
  for h in range(img_h):
    for w in range(img_w):
      index_pix = comp_pixel(img[h, w, :], palette)
      index_colar[h, w] = index_pix
  return index_colar
