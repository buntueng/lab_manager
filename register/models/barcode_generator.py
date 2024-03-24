"""Barcode Generator Class"""
import tempfile
import os
import barcode
from PySide6 import QtWidgets, QtPrintSupport
from PIL.ImageQt import ImageQt
from PIL import Image
from PySide6 import QtGui
from PySide6 import QtCore
from PySide6.QtGui import QPageSize
from PySide6.QtCore import QSizeF


class BarcodeGenerator:
    def __init__(self):
        self.temp_folder = tempfile.gettempdir()

    def generate(self, data):
        """Generate barcode image set the image size to 50x30 millimeters and save it to a temporary folder"""
        self.barcode_path = os.path.join(self.temp_folder, "barcode.png")
        # set image size to 50x30 millimeters
        with open(self.barcode_path, "wb") as f:
            barcode128 = barcode.get_barcode_class("code128")
            barcode_image = barcode128(
                data, writer=barcode.writer.ImageWriter())
            barcode_image.write(f)
        return self.barcode_path

    def print_barcode(self, im):
        """ Print barcode image on the printer using Qtprinter"""
        printer = QtPrintSupport.QPrinter()
        pageSize = QPageSize(QSizeF(50, 30), QPageSize.Millimeter)
        printer.setPageSize(pageSize)
        dialog = QtPrintSupport.QPrintDialog(printer)
        if dialog.exec() == QtWidgets.QDialog.Accepted:
            self.handle_paint_request(printer, im)

    def handle_paint_request(self, printer, im):
        """Handle paint request"""
        # printer.setPaperSize(QtCore.QSizeF(50, 30), QtPrintSupport.QPrinter.Millimeter)
        printer.setResolution(100)
        printer.setPageMargins(QtCore.QMargins(1, 6, 1, 1), QtGui.QPageLayout.Millimeter)
        im = ImageQt(im).copy()
        painter = QtGui.QPainter(printer)
        # Get the page size in pixels
        pageRect = printer.pageRect(QtPrintSupport.QPrinter.DevicePixel)
        # Convert the image to a QPixmap and scale it to the page size
        image = QtGui.QPixmap.fromImage(im).scaled(pageRect.width(), pageRect.height(), QtCore.Qt.KeepAspectRatio)
        # Draw the pixmap onto the printer
        painter.drawPixmap(0, 0, image)

        painter.end()

    def __del__(self):
        print(self.barcode_path)
        if os.path.exists(self.barcode_path):
            print("Deleting barcode image")
            # os.remove(self.barcode_path)
        else:
            print("The file does not exist")


if __name__ == "__main__":
    # create simple QT application
    app = QtWidgets.QApplication([])

    barcode_gen = BarcodeGenerator()
    barcode_path = barcode_gen.generate("1234567890")
    print(f"Barcode path: {barcode_path}")

    # open image
    image = Image.open(barcode_path)
    barcode_gen.print_barcode(image)

    # # show image usig PIL
    # from PIL import Image
    # image = Image.open(barcode_path)
    # image.show()

    app.exec()
