# NEET UG Marks PDF to Graph Plotter

This project is a PDF to graph plotter for NTA NEET 2024 Supreme Court requested data. It extracts marks from multiple PDF files, processes the data, and visualizes the distribution of marks using histograms.

## Features

- Extracts marks data from PDF files
- Processes marks data and aggregates it
- Plots histograms for negative marks, high marks (>600), and other marks (0 to 600)
- Displays the total number of students scanned

## Requirements

- Python 3.x
- `pymupdf`
- `pandas`
- `matplotlib`
- `tkinter`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RealRuthvik//NEET-UG-Marks-PDF-to-Graph-Plotter.git
    cd NEET-UG-Marks-PDF-to-Graph-Plotter
    ```

2. Install the required Python packages:

    ```bash
    pip install pymupdf pandas matplotlib tk
    ```

## Usage

1. Run the script:

    ```bash
    python plot_neet_marks.py
    ```

2. A file dialog will appear. Select the folder containing the NEET PDF files.

3. The script will process the PDF files, extract the marks data, and display a histogram plot of the marks distribution.

## Script Details

The script performs the following steps:

1. **ExtractedpdfMarks(pdfPath)**: Extracts marks from a single PDF file using regex to find matches for serial numbers and marks.
2. **ProcessFolder(folder)**: Processes all PDF files in the selected folder and aggregates the marks data.
3. **Visualization**: Uses `matplotlib` to plot histograms for different ranges of marks (negative, high marks, and others).

## Example Output

The script generates a histogram plot with three different colored bars representing:
- Negative marks (red)
- Marks greater than 600 (yellow)
- Marks between 0 and 600 (blue)

Additionally, the total number of students scanned is displayed on the plot.
