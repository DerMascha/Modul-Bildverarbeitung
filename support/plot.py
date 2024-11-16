import numpy as np
from IPython.display import display, Math, Latex
import matplotlib.pyplot as plt

def draw_matrix(mat: np.ndarray) -> str:
    if mat.size == 1:
        return str(mat)
    s = r"\begin{bmatrix}"
    if mat.ndim == 1:
        s += " & ".join([draw_matrix(r) for r in mat]) + r'\\'
    else:
        for row in mat:
            s += " & ".join([draw_matrix(r) for r in row]) + r'\\'
    return s + r"\end{bmatrix}"

def plot_tensor(tensor: np.ndarray):
    display(Math(draw_matrix(tensor)))

def show_images(imgs, names = None):
    fig, axes = plt.subplots(1, len(imgs))
    fig.set_size_inches(len(imgs) * 5, 5)
    if not names:
        names = [''] * len(imgs)
    for img, ax, name in zip(imgs, axes, names):
        ax.imshow(img, cmap='grey')
        ax.title.set_text(name)
    plt.show()

def main():
    print(draw_matrix(np.ones([3,4,2])))

if __name__=="__main__":
    main()


                         