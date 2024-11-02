def iou(rect1, rect2):
    '''Calculates the Intersection over Union (IoU) of two rectangles.
    Rectangles are specified by x,y,width,height'''
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    # Calculate the intersection area
    xA = max(x1, x2)
    yA = max(y1, y2)
    xB = min(x1 + w1, x2 + w2)
    yB = min(y1 + h1, y2 + h2)
    interArea = max(0, xB - xA) * max(0, yB - yA)
    # Calculate the area of both rectangles
    boxAArea = w1 * h1
    boxBArea = w2 * h2
    # Calculate the IoU
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou