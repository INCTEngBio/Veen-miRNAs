## Tool: Veen-miRNAs (Visualizing miRNA Family Distribution)
Authors: ELÍBIO LEOPOLDO RECH FILHO, DEBORAH BAMBIL, RAYANE NUNES LIMA, MARCO ANTÔNIO DE OLIVEIRA, PATRÍCIA VERDUGO PASCOAL, LUISA MAYUMI ARAKE DE TACCA

This tool generates high-quality **Venn Diagrams** to visualize the intersection and uniqueness of miRNA families across different biological groups or biomes. It includes automated data cleaning and legend formatting for publication-ready figures.

### Data Input Format:
The script expects a **.txt (tab-separated)** file named `familias_mirna.txt`.
* **Columns:** Each column represents a group (e.g., a specific Biome).
* **Values:** Each row contains the names of miRNA families identified in that group. 
* **Handling:** The script automatically removes empty values (NaN), trims whitespace, and considers only unique occurrences within each column.

### Key Features:
* **Automated Data Cleaning:** Built-in dictionary mapping that filters and de-duplicates entries from the input file.
* **Smart Visualization:** * Automatically hides "0" values in non-intersecting areas for a cleaner plot.
    * Customizable font sizes for both labels and intersection counts.
* **Enhanced Legend Control:** Fixes common legend positioning issues in the `venn` library, ensuring biomes are clearly labeled and do not overlap with the diagram.
* **Publication Ready:** Exports high-resolution (300 DPI) PNG files with tight bounding boxes to prevent clipping.

### Tech Stack:
* **Python** (`Pandas`, `Matplotlib`, `Venn`).
* **Install**
pip install: pandas numpy matplotlib seaborn scikit-learn venn
