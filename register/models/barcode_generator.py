"""Barcode Generator Class"""
import tempfile
import os
from PIL.ImageQt import ImageQt
from PIL import Image, ImageDraw, ImageFont

import barcode
from barcode.writer import ImageWriter


from PySide6.QtGui import QPageSize
from PySide6.QtCore import QSizeF
from PySide6 import QtWidgets, QtPrintSupport, QtCore, QtGui
from PySide6.QtPrintSupport import QPrintPreviewDialog


class BarcodeGenerator:
    def __init__(self):
        self.temp_folder = tempfile.gettempdir()
        self.barcode_file_path = os.path.join(self.temp_folder, "barcode.png")

    def generate(self, data):
        """Generate barcode image"""
        # [sample_code, species, date, lab_name, speed, collect, comments] = data[0]
        [date, sample_code, species, lab_name, collect, speed, comments] = data[0]
        label2 = self.generate_sticker_label(
            sample_code=sample_code, species=species, date=date, lab_name=lab_name, speed=speed, collect=collect)
        label2.save(self.barcode_file_path, 'PNG')

    def generate_sticker_label(self, sample_code=" ", species=" ", date=" ", lab_name=" ", speed="ด่วนที่สุด", collect="ไม่แช่เย็น (Chill)"):
        """Generate barcode image with sample code, species, date, lab name, speed, collect"""
        try:
            text_font = ImageFont.truetype(r'TH Niramit AS Bold.ttf', 120)
            text_font_big = ImageFont.truetype(r'TH Niramit AS Bold.ttf', 135)
        except:
            text_font = ImageFont.truetype(r'D:/project/lab_manager/register/models/TH Niramit AS Bold.ttf', 120)
            text_font_big = ImageFont.truetype(r'D:/project/lab_manager/register/models/TH Niramit AS Bold.ttf', 135)
        background_layer = Image.new('RGB', (2000, 2000), "white")
        # ================ barcode layer ============================================
        barcode.base.Barcode.default_writer_options['write_text'] = False
        barcode_code128 = barcode.get(
            'code128', str(sample_code), writer=ImageWriter())
        barcode_image = barcode_code128.render({"mode": "RGBA"})
        # barcode_image.convert('RGBA')
        barcode_image = barcode_image.resize(
            (1650, 1500), Image.Resampling.LANCZOS)
        # ============ sample code layer ==============================================
        sample_code_layer = Image.new('RGBA', (2000, 2000))
        sample_code_layer_text = ImageDraw.Draw(sample_code_layer)
        sample_code_layer_text.text(xy=(
            80, 90), text="LAB NO.:  "+str(sample_code), font=text_font, anchor='lt', fill="#000000")
        # ============ species layer ==============================================
        species_layer = Image.new('RGBA', (2000, 2000))
        species_layer_text = ImageDraw.Draw(species_layer)
        species_layer_text.text(xy=(80, 240), text="SPECIES: " +
                                str(species), font=text_font, anchor='lt', fill="#000000")
        # ============ lab_name layer ==============================================
        lab_name_layer = Image.new('RGBA', (2000, 2000))
        lab_name_layer_text = ImageDraw.Draw(lab_name_layer)
        lab_name_layer_text.text(xy=(
            80, 370), text="ROOM: "+str(lab_name), font=text_font, anchor='lt', fill="#000000")
        # ================= datetime layer ========================================
        datetime_layer = Image.new('RGBA', (2000, 2000))
        datetime_layer_text = ImageDraw.Draw(datetime_layer)
        datetime_layer_text.text(xy=(
            80, 500), text="DATE:  "+str(date), font=text_font, anchor='lt', fill="#000000")
        # ================= order_speed layer ========================================
        speed_layer = Image.new('RGBA', (2000, 2000))
        speed_layer_text = ImageDraw.Draw(speed_layer)
        speed_layer_text.text(xy=(1100, 200), text=str(
            speed), font=text_font_big, anchor='lt', fill="#000000")

        # ================= collect layer ========================================
        collect_layer = Image.new('RGBA', (2000, 2000))
        collect_layer_text = ImageDraw.Draw(collect_layer)
        collect_layer_text.text(xy=(1100, 70), text=str(
            collect), font=text_font, anchor='lt', fill="#000000")

        intermediate_layer = Image.alpha_composite(
            sample_code_layer, species_layer)
        intermediate_layer = Image.alpha_composite(
            lab_name_layer, intermediate_layer)
        intermediate_layer = Image.alpha_composite(
            datetime_layer, intermediate_layer)
        intermediate_layer = Image.alpha_composite(
            speed_layer, intermediate_layer)
        intermediate_layer = Image.alpha_composite(
            collect_layer, intermediate_layer)
        Image.Image.paste(background_layer, barcode_image, (10, 550))

        background_layer.paste(intermediate_layer, (0, 0), intermediate_layer)

        final_layer = background_layer.crop((0, 0, 2000, 1000))
        return final_layer

    def print_barcode(self):
        """ Print barcode image on the printer using Qtprinter"""
        im = Image.open(self.barcode_file_path)
        printer = QtPrintSupport.QPrinter()
        pageSize = QPageSize(QSizeF(50, 30), QPageSize.Millimeter)
        printer.setPageSize(pageSize)

        # # Create print preview dialog
        preview = QPrintPreviewDialog(printer)
        preview.paintRequested.connect(
            lambda p: self.handle_paint_request(p, im))
        preview.exec()

        # dialog = QtPrintSupport.QPrintDialog(printer)
        # if dialog.exec() == QtWidgets.QDialog.Accepted:
        #     self.handle_paint_request(printer, im)

    def handle_paint_request(self, printer, im):
        """Handle paint request"""
        # printer.setPaperSize(QtCore.QSizeF(50, 30), QtPrintSupport.QPrinter.Millimeter)
        printer.setResolution(1200)
        printer.setPageMargins(QtCore.QMargins(
            0, 0, 0, 0), QtGui.QPageLayout.Millimeter)
        im = ImageQt(im).copy()
        painter = QtGui.QPainter(printer)
        image = QtGui.QPixmap.fromImage(im).scaled(
            2500, 1400, QtCore.Qt.KeepAspectRatio)
        # Draw the pixmap onto the printer
        painter.drawPixmap(0, 0, image)

        painter.end()

    def __del__(self):
        # print(self.barcode_file_path)
        try:
            if os.path.exists(self.barcode_file_path):
                # print("Deleting barcode image")
                os.remove(self.barcode_file_path)
            else:
                print("The file does not exist")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # create simple QT application
    app = QtWidgets.QApplication([])

    barcode_gen = BarcodeGenerator()
    barcode_gen.generate(["660000990001", "Avine", "22-02-2022  12:00:00",
                         "D304(BAC)", "สบาย สบาย", "ไม่แช่เย็น (Chill)"])
    print(f"Barcode path: {barcode_gen.barcode_file_path}")

    # open image
    # image = Image.open(barcode_path)
    # image = Image.open("C:/Users/ASUS/Desktop/kn.png").convert("1")
    barcode_gen.print_barcode()

    # # show image usig PIL
    # from PIL import Image
    # image = Image.open(barcode_path)
    # image.show()

    app.exec()
