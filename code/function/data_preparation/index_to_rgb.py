#This is the function to turn the index pixel values into the RGB values

def opp_comp(val, palette):
  for idx, clr in enumerate(palette):
    judje = val == idx
    if all(judje) == True:
      return clr

def index2rgb(img, palette):
  img_h = img.shape[0]
  img_w = img.shape[1]
  rgb_colar = np.zeros((img_h, img_w, 3), dtype = np.float32)
  for h in range(img_h):
    for w in range(img_w):
      rgb_pix = opp_comp(img[h, w], palette)
      rgb_colar[h, w, :] = rgb_pix
  return rgb_colar
