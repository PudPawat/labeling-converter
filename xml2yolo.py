# -*- coding: utf-8 -*-

from xml.dom import minidom
import os
import glob

lut={}
# lut["ppoint"] = 0
# lut["ppointwwww"] = 0
# lut["burr"]       = 1
# lut["scratch"]    = 2
# lut["crack"]      =3
# lut["foreign"]    =4
# lut["dust"]    =4
# lut["dot"]    =4
# lut["defect"]    =4
# lut["defectww"]    =4
# lut["printed"]     =5
# lut["print"]     =5
# lut["bubble"]     =6
# lut[""]     =6
# lut["distort"]     =7
# lut["cloudy"]     =8
# lut["blur"]     =8

### only mirror
lut["a"] =0
lut["b"]       =1
lut["scratch"]    =2
lut["d"]       =3
lut["dust"]     =4
lut["defect"]     =4
lut["defectww"]     =4
lut["dot"]     =5
lut["6"]     =6
lut["W1"]     =7
lut["blur"]     =8
lut["cloudy"]     =8
# lut["white_nv"]     =9
# lut["purple_box"]     =10



def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    # print(x,w,h,y)
    return (x,y,w,h)


def convert_xml2yolo( lut ,path = ""):

    for fname in glob.glob(path+"*.xml"):
        
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    label_str = "-1"
                    print ("warning: label '%s' not in look-up table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                # print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s " % fname_out)



def main():
    convert_xml2yolo(lut ,"F:\Ph.D\mirror\data\\20220628\img_RGB\XML\\")


if __name__ == '__main__':
    main()