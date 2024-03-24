"""Barcode Generator Class"""
import tempfile
import os
import barcode


class BarcodeGenerator:
    def __init__(self):
        self.temp_folder = tempfile.gettempdir()

    def generate(self, data):
        """Generate barcode image"""
        self.barcode_path = os.path.join(self.temp_folder, "barcode.png")
        with open(self.barcode_path, "wb") as f:
            barcode128 = barcode.get_barcode_class("code128")
            barcode_image = barcode128(
                data, writer=barcode.writer.ImageWriter())
            barcode_image.write(f)

        return self.barcode_path

    def __del__(self):
        print(self.barcode_path)
        if os.path.exists(self.barcode_path):
            print("Deleting barcode image")
            # os.remove(self.barcode_path)
        else:
            print("The file does not exist")


if __name__ == "__main__":
    barcode_gen = BarcodeGenerator()
    barcode_path = barcode_gen.generate("1234567890")
    print(f"Barcode path: {barcode_path}")

    # show image usig PIL 
    from PIL import Image
    image = Image.open(barcode_path)
    image.show()
