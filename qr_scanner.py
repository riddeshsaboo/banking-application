import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from pyzbar.pyzbar import decode

def scan_qr_code_from_file():
    try:
        file_path = filedialog.askopenfilename(
            title="Select QR Code Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp"), ("All Files", "*.*")]
        )

        if not file_path:
            messagebox.showinfo("No File Selected", "Please select a valid QR code image.")
            return None

        image = cv2.imread(file_path)

        if image is None:
            messagebox.showerror("Error", "Failed to read the file. Please check the file path.")
            return None

        qr_codes = decode(image)

        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')  # Extract the QR code data
            messagebox.showinfo("QR Code Scanned", f"Scanned QR Data: {qr_data}")
            return qr_data  # Return the scanned QR data (assumed PRN)

        messagebox.showwarning("No QR Code Found", "No QR code detected in the selected image.")
        return None

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None


