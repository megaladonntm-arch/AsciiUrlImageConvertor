import numpy as np
import sys, os, math, random
from PIL import Image

first_scale = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. "
second_scale = "@%#*+=-:. "

def getAverageLuminance(image):
    im = np.array(image)
    width, height = im.shape
    return np.average(im.reshape(width * height))

def convertImageToASCII(fileName, cols, scale, moreLevels):
    image = Image.open(fileName).convert('L')
    width, height = image.size
    
    w = width / cols
    h = w / scale
    rows = int(height / h)
    
    if cols > width or rows > height:
        print("Image too small for specified cols!")
        exit(0)
    aimg = []
    
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        if j == rows - 1:
            y2 = height 
        aimg.append("")
        for i in range(cols):
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            if i == cols - 1:
                x2 = width
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageLuminance(img))
            if moreLevels:
                gsval = first_scale[int((avg * 69) / 255)]
            else:
                gsval = second_scale[int((avg * 9) / 255)]
            aimg[j] += gsval
    
    return aimg

def main():
    print("ASCII Art Generator")
    print("=" * 30)
    imgFile=input("FilePath: ").strip()
    if not os.path.exists(imgFile):
        print("Error: File not found!")
        return
    
    scale_choice=input("enter sscale factor (default 0.43): ").strip()
    scale=0.43 if scale_choice == "" else float(scale_choice)
    
    cols_choice=input("Enter number of columns (default 80): ").strip()
    cols = 80 if cols_choice == "" else int(cols_choice)
    
    levels_choice = input("Use more character levels? (y/n, default y): ").strip().lower()
    moreLevels = True if levels_choice == "" or levels_choice == "y" else False
    
    outFile = input("Enter output file name (default 'out.txt'): ").strip()
    outFile = "out.txt" if outFile == "" else outFile
    
    print('Generating ASCII art...')
    
    try:
        aimg = convertImageToASCII(imgFile, cols, scale, moreLevels)
        
        with open(outFile, 'w') as f:
            for row in aimg:
                f.write(row + '\n')
        
        print(f"ASCII art successfully written to {outFile}")
        
        preview = input("Preview first 10 lines? (y/n): ").strip().lower()
        if preview == "y":
            print("\nPreview:")
            for i in range(min(10, len(aimg))):
                print(aimg[i])
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()