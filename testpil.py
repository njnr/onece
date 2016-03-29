from PIL import Image, ImageEnhance





def resizeImg(im, dst_w=0, dst_h=0, qua=85):

    ori_w, ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1

    if (ori_w and ori_w > dst_w) or (ori_h and ori_h  > dst_h):
        if dst_w and ori_w > dst_w:
            widthRatio = float(dst_w) / ori_w                        
        if dst_h and ori_h > dst_h:
            heightRatio = float(dst_h) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio

        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    
    #im.resize((newWidth,newHeight),Image.ANTIALIAS).save("test5.png",
    #                                                     "PNG", quality=qua)
    return im.resize((newWidth,newHeight),Image.ANTIALIAS)

def set_opacity(im, opacity):
  
    assert opacity >=0 and opacity < 1
    if im.mode != "RGBA":
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def logo_watermark(img, base_path):
  
    logoim = img
    baseim = Image.open(base_path)
    bw, bh = baseim.size
    lw, lh = logoim.size

    
    
    baseim.paste(logoim, (bw-lw, bh-lh))
    baseim.save('test3.jpg', 'JPEG')

    
cc = Image.open('code.png')
pic = resizeImg(cc, 100,100)
logo_watermark(pic,'1.jpg')


