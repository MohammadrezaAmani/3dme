# 3DME - Simple 3D Point Cloud Viewer  

**3DME** is a lightweight and interactive tool to visualize images as 3D point clouds. It provides a simple interface for transforming images into stunning 3D visualizations either using a web-based viewer or a Python script.  

---

## Features  

- Convert images into 3D point clouds interactively in a browser or using Python.  
- Export 3D models in `.ply` format for further use in 3D modeling software.  
- Adjust point size, rotation speed, and background color in the web viewer.  

---

## How to Use the Web Viewer  

1. **Open the Project**  
   Download the project and open the `index.html` file in your browser.  

2. **Upload an Image**  
   Use the "Upload Image" button to select and load your image.  

3. **Interact with the Scene**  
   Use the on-screen controls to customize the visualization (e.g., point size, rotation).  

---

## How to Use the Python Script  

### Requirements  

- **Python 3.7+**  
- Required Libraries:  
  - `numpy`  
  - `Pillow`  

Install dependencies using:  

```bash
pip install numpy pillow
```

### Instructions  

1. **Prepare an Image**  
   Ensure your image is saved as `.png`, `.jpg`, or any supported format.  

2. **Run the Script**  
   Save the Python code into a file (e.g., `generate_3d.py`).  
   Run the script using:  

   ```bash
   python generate_3d.py
   ```

3. **Check Output**  
   The script will create a 3D model in `.ply` format with the same resolution as the image.  

### Example Code Usage  

```python
from generate_3d import generate_3d_from_image

# Convert an image to 3D point cloud
image_path = "example_image.png"
generate_3d_from_image(image_path, file_name="output.ply")
print("3D model generated successfully!")
```  

---

## Credits  

Developed with ❤️ by [Mohammadreza Amani](https://github.com/MohammadrezaAmani).  
