import os
import fitz
import re
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def ExtractedpdfMarks(pdfPath):
    document = fitz.open(pdfPath)
    marksData = []
    pattern = re.compile(r'(\d+)\s+(-?\d+)')

    for pageNum in range(document.page_count):
        page = document.load_page(pageNum)
        text = page.get_text("text")
        matches = pattern.findall(text)
        for match in matches:
            serialNumber, marks = match
            marksData.append((int(serialNumber), int(marks)))

    return marksData

def ProcessFolder(folder):
    allMarks = []
    TotalStudents = 0
    for fileName in os.listdir(folder):
        if fileName.endswith('.pdf'):
            pdfPath = os.path.join(folder, fileName)
            marksData = ExtractedpdfMarks(pdfPath)
            allMarks.extend(marksData)
            if marksData:
                TotalStudents += marksData[-1][0]
    return allMarks, TotalStudents

root = Tk()
root.withdraw()

folder = filedialog.askdirectory(title="Select Folder Containing PDF Files")

if folder:
    marksList, TotalStudents = ProcessFolder(folder)
    df = pd.DataFrame(marksList, columns=['Serial Number', 'Marks'])

    plt.figure(figsize=(10, 6))

    negativeMarks = df[df['Marks'] < 0]
    plt.hist(negativeMarks['Marks'], bins=range(-180, 0, 10), edgecolor='black', color='red', label='Negative Marks')

    highMarks = df[df['Marks'] > 600]
    plt.hist(highMarks['Marks'], bins=range(600, 721, 10), edgecolor='black', color='yellow', label='Marks > 600')

    otherMarks = df[(df['Marks'] >= 0) & (df['Marks'] <= 600)]
    plt.hist(otherMarks['Marks'], bins=range(0, 601, 10), edgecolor='black', color='blue', label='0 <= Marks <= 600')

    plt.title('Distribution of NEET UG Marks')
    plt.xlabel('Marks')
    plt.ylabel('Number of Students')
    plt.grid(True)
    plt.legend()

    plt.xticks(range(-180, 721, 36))  # Adjust x-axis intervals to 10

    plt.text(0.95, 0.95, f'Total Students: {TotalStudents}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

    plt.show()
else:
    print("No folder selected.")
