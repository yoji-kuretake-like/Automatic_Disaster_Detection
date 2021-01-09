#This is the function to split the images into the designated size

def slice_image(path, size):
  files = glob.glob(os.path.join(path, '*.tif'))
  names = os.listdir(path)
  files.sort()
  names.sort()
  for name, file in zip(names, files):
    out_img = []
    name = name[:-4] #name except the extension
    srcImg = Image.open(file)
    imgArray = np.asarray(srcImg)
    v_size, h_size = imgArray.shape[0] // size * size, imgArray.shape[1] // size * size
    img = imgArray[:v_size, :h_size]
    v_split, h_split = img.shape[0] // size, img.shape[1] // size
    [out_img.extend(np.hsplit(h_img, h_split)) for h_img in np.vsplit(img, v_split)]
    count = 1
    for piece_img in out_img:
      print('now is {0} of {1}'.format(name, count))
      pil_img = Image.fromarray(piece_img)
      pil_img.save('/content/drive/My Drive/Potsdom/train/cut_gt_image/{0}/{1}_{2}.png'.format(name, name, count))
      count += 1
  return
