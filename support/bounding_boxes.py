import numpy as np
import matplotlib.pyplot as plt
from support.iou import iou

def create_bounding_boxes(labels):
    '''Create bounding boxes from a labeled image.
    Args:
        labels: a 2D numpy array with labels.
        Returns:
        A list of tuples (x, y, w, h) where x, y are the coordinates of the top-left corner of the bounding box
        and w, h are the width and height of the bounding box.'''
    results = []
    for i in np.unique(labels):
        index_y, index_x = np.where(labels == i)
        lmin = np.min(index_x)
        lmax = np.max(index_x)
        rmin = np.min(index_y)
        rmax = np.max(index_y)
        results.append((lmin, rmin, lmax-lmin, rmax-rmin))
    return results

def draw_bounding_boxes(rectangles : list[(int, int, int, int)]):
    '''Draw bounding boxes on the current plot.
    Args:
        rectangles: a list of tuples (x, y, w, h) where x, y are the coordinates of the top-left corner of the bounding box
        and w, h are the width and height of the bounding box.'''
    for rect in rectangles:
        x, y, w, h = rect
        box = plt.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=2)
        plt.gca().add_patch(box)

def non_maximum_suppression(rects_with_score: dict[(int,int,int,int), float], overlap_threshold: float) -> list:
    '''Apply non-maximum suppression to a list of rectangles.
    Args:
        rects_with_score: a dictionary with keys being tuples (x, y, w, h) and values being the score of the rectangle.
        overlap_threshold: the threshold for the intersection over union (IoU) between two rectangles.
        Returns:
        A list of rectangles that are not suppressed.'''
    # sort by score
    sorted_rects = sorted(rects_with_score.keys(), key=rects_with_score.get, reverse=True)
    result = []
    while len(sorted_rects) > 0:
        rect = sorted_rects.pop()
        # remove all rectangles that overlap with current rectangle
        sorted_rects = {r for r in sorted_rects if iou(r, rect) < overlap_threshold}
        result.append(rect)
    return result