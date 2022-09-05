#这个模块负责进行图像的切割

import PIL

def main(Path, Scale = 64):
    ''' Path: 图片的路径
        Scale: 每个小图片的尺寸，默认为 16*16
    '''
    img = PIL.Image.open(Path)
    w, h = img.size
    for i in range(0, w, Scale):
        for j in range(0, h, Scale):
            box = (i, j, i+Scale, j+Scale)
            img.crop(box).save(f'./output/%d_%d.png' % (i, j))
    print('Done!')

if __name__ == '__main__':
    main()