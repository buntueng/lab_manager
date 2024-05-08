""" Main Controller class"""
# import QMessageBox from PySide6.QtWidgets
from typing import Any
import time
from PySide6.QtWidgets import QMessageBox
from models.barcode_generator import BarcodeGenerator
from models.order_detail_pdf import create_parasite_biology, create_bacteriology, create_molecular_biology
import tempfile
import os


class Main_Controller:
    """Main Controller class"""

    def __init__(self, main_model, main_view):
        self.model = main_model
        self.view = main_view

        self.user_login_info = []

        self.event_bindings()

        self.all_customer_names = []
        self.all_employee_names = []

    def event_bindings(self):
        """Event bindings for the main view"""
        self.view.login_pushButton.clicked.connect(self.user_sign_in)
        # bind enter key in login page
        self.view.password_lineEdit.returnPressed.connect(self.user_sign_in)
        self.view.sign_out_pushButton.clicked.connect(self.user_sign_out)

        self.view.customer_reg_pushButton.clicked.connect(
            self.view.show_customer_register_page)
        self.view.case_register_pushButton.clicked.connect(
            self.view.show_job_register_page)
        self.view.check_job_pushButton.clicked.connect(
            self.view.show_check_job_progress_page)
        self.view.barcode_pushButton.clicked.connect(
            self.barcode_pushButton_clicked)
        self.view.lab_order_pushButton.clicked.connect(
            self.view.show_lab_order_report_page)
        self.view.bill_pushButton.clicked.connect(self.view.show_bill_page)
        self.view.check_report_pushButton.clicked.connect(
            self.view.show_check_report_page)

        self.view.employee_pushButton.clicked.connect(
            self.view.show_employee_page)
        self.view.personal_info_pushButton.clicked.connect(
            self.view.show_personal_information_page)

        self.view.update_prog_pushButton.clicked.connect(
            self.view.show_update_page)

        self.view.sign_out_pushButton.clicked.connect(
            self.view.show_login_page)

        self.view.received_order_pushButton.clicked.connect(
            self.show_received_order_page)

        self.bind_event_in_new_customer_page()
        self.bind_event_in_case_register_page()
        self.bind_event_in_specimen_page()
        self.bind_event_in_molecular_biology_page()
        self.bind_event_in_parasitology_page()
        self.bind_event_in_microbiology_page()
        self.bind_event_in_barcode_page()
        self.bind_event_in_lab_received_sample_page()
        self.bind_event_in_check_job_progress_page()

    def bind_event_in_check_job_progress_page(self):
        """Bind event in check job progress page"""
        self.view.check_job_page_search_pushButton.clicked.connect(
            self.search_job_in_check_job_progress_page)
        self.view.check_job_page_show_detail_pushButton.clicked.connect(
            self.show_detail_job_progress_page)

    def show_detail_job_progress_page(self):
        """Show detail job progress page"""
        selected_item = self.view.check_job_page_running_job_treeWidget.selectedItems()
        if selected_item == [] or len(selected_item) > 1:
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาเลือกงานเพื่อดูรายละเอียด")
        else:
            for row in selected_item:
                job_id = int(row.text(1))
                job_detail = self.model.get_job_detail_in_check_job_progress_page_by_id(
                    job_id)
                self.view.show_job_detail_in_progress_page(job_detail)

    def search_job_in_check_job_progress_page(self):
        """Search job in check job progress page"""
        job_detail = self.model.get_job_detail_in_check_job_progress_page()
        self.view.check_job_page_running_job_treeWidget.clear()
        if job_detail == [] or job_detail == None:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่พบข้อมูลงานในระบบ")
        else:
            self.view.add_job_detail_to_check_job_progress_page(job_detail)

    def bind_event_in_lab_received_sample_page(self):
        """Bind event in lab received sample page"""
        self.view.lab_received_sample_search_employee_lineEdit.textChanged.connect(
            self.search_employee_in_lab_received_sample_page)
        self.view.lab_received_sample_select_pushButton.clicked.connect(
            self.select_employee_in_lab_received_sample_page)
        self.view.lab_received_sample_save_pushButton.clicked.connect(
            self.save_lab_received_sample_information)

    def save_lab_received_sample_information(self):
        if self.view.lab_received_sample_barcode_lineEdit.text() == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณากรอกหมายเลข Barcode")
        elif self.view.lab_received_sample_employee_lineEdit.text() == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาเลือกพนักงานที่รับตัวอย่าง")
        else:
            barcode_id = self.view.lab_received_sample_barcode_lineEdit.text()
            if barcode_id.isdigit():
                barcode_id = int(barcode_id)
                employee_id = int(
                    self.view.lab_received_sample_personal_code_lineEdit.text())
                if self.model.save_tracking_information(barcode_id, employee_id, self.user_login_info[0][1], "ห้องปฏิบัติการรับตัวอย่างสิ่งส่งตรวจแล้ว"):
                    QMessageBox.information(self.view, "Success",
                                            "บันทึกข้อมูลเรียบร้อย")
                    self.view.lab_received_sample_barcode_lineEdit.clear()
                    self.view.lab_received_sample_employee_lineEdit.clear()
                    self.view.lab_received_sample_personal_code_lineEdit.clear()
                    self.view.lab_received_sample_treeWidget.clear()
                    self.view.lab_received_sample_search_employee_lineEdit.clear()

                else:
                    QMessageBox.critical(self.view, "Error",
                                         "ไม่สามารถบันทึกข้อมูลได้")
            else:
                QMessageBox.critical(self.view, "Error",
                                     "กรุณาใส่หมายเลข Barcode เป็นตัวเลข")

    def select_employee_in_lab_received_sample_page(self):
        """ select employee from treeview"""
        selected_item = self.view.lab_received_sample_treeWidget.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to add employee information")
        else:
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to add employee information")
            else:
                for row in selected_item:
                    self.view.lab_received_sample_employee_lineEdit.setText(
                        row.text(0) + " " + row.text(1))
                    self.view.lab_received_sample_personal_code_lineEdit.setText(
                        row.text(2))

    def search_employee_in_lab_received_sample_page(self):
        """search employee in lab received sample page by name"""
        input_text = self.view.lab_received_sample_search_employee_lineEdit.text()
        if input_text == "":
            self.view.lab_received_sample_treeWidget.clear()
        else:
            employee_info = []
            for employee_detail in self.all_employee_names:
                if input_text in employee_detail[0] or input_text in employee_detail[1]:
                    employee_info.append(
                        [employee_detail[0], employee_detail[1], str(employee_detail[2]).zfill(5)])

            if len(employee_info) > 0:
                # insert data to Qtreeview
                self.view.add_employee_info_to_lab_received_sample_page(
                    employee_info)

    def show_received_order_page(self):
        """Show received order page"""
        self.all_employee_names = self.model.get_all_employee_detail()
        self.view.clear_received_order_page()
        self.view.show_received_order_page()

    def barcode_pushButton_clicked(self):
        """Barcode push button clicked"""
        self.view.reset_print_barcode_page()
        self.view.show_print_barcode_page()

    def bind_event_in_barcode_page(self):
        """"Bind event in barcode page"""
        self.view.sticker_search_lineEdit.textChanged.connect(
            self.search_customer_in_barcode_page)
        self.view.print_barcode_pushButton.clicked.connect(
            self.print_barcode)
        self.view.sticker_search_pushButton.clicked.connect(
            self.search_sticker)
        self.view.today_sticker_search_pushButton.clicked.connect(
            self.search_today_sticker)

    def search_customer_in_barcode_page(self):
        """Search customer in barcode page"""
        input_text = self.view.sticker_search_lineEdit.text()
        if input_text == "":
            self.view.barcode_page_customertreeWidget.clear()
        else:
            customer_detial = []
            for cs_detail in self.all_customer_names:
                if input_text in cs_detail[0] or input_text in cs_detail[1]:
                    customer_detial.append(cs_detail)

            if len(customer_detial) > 0:
                # insert data to Qtreeview
                self.view.add_customer_info_to_barcode_page(customer_detial)

    def bind_event_in_new_customer_page(self):
        """Bind event in new customer page"""
        self.view.save_new_customer_button.clicked.connect(
            self.save_new_customer)
        self.view.anonymous_tax_checkbox.stateChanged.connect(
            self.disable_tax_entry)
        self.view.new_customer_addres_for_bill_checkbox.stateChanged.connect(
            self.copy_address_to_bill_address)

    def bind_event_in_case_register_page(self):
        """Bind event in case register page"""
        self.view.new_case_select_sender_button.clicked.connect(
            self.new_case_add_sender_info)
        self.view.new_case_select_owner_button.clicked.connect(
            self.new_case_add_owner_info)
        self.view.new_case_anonymous_owner_button.clicked.connect(
            self.clear_new_case_owner_info)
        self.view.new_case_save_button.clicked.connect(
            self.register_new_case)

        self.view.new_case_add_data_specimen_button.clicked.connect(
            self.view.show_specimen_page)

        self.view.new_case_search_name_entry.textChanged.connect(
            self.new_case_search_user_change)
        self.view.new_case_print_sticker_button.clicked.connect(
            self.print_barcode_in_new_case_page)

        self.view.new_case_print_lab_report_button.clicked.connect(
            self.print_lab_order_detail_in_new_case_page)

        self.view.new_case_delete_data_specimen_button.clicked.connect(
            self.delete_specimen_in_new_case_page)

    def print_lab_order_detail_in_new_case_page(self):
        """Print lab order detail in new case page"""
        selected_item = self.view.new_case_detail_case_tree_view.selectedItems()
        if selected_item == [] or len(selected_item) > 1:
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาเลือกรายการเพื่อพิมพ์ใบส่งงาน")
        else:
            for row in selected_item:
                case_id = int(row.text(1))
                # get sample information
                sample_info = self.model.get_sample_information_by_id(case_id)
                # tempolary folder
                temp_folder = tempfile.mkdtemp()
                temp_pdf_file = os.path.join(temp_folder, "lab_order.pdf")
                test_info = []
                case_lab = row.text(3)
                if case_lab == 'E304(Parasite)':
                    # create parasite biology pdf
                    test_info = self.model.get_parasite_test_information_by_id(
                        case_id)
                    # create parasite lab order in tempolary folder
                    create_parasite_biology(
                        sample_info, test_info, temp_pdf_file)
                    # open pdf file using default pdf viewer
                    os.system(f"start {temp_pdf_file}")

                elif case_lab == 'D403(Fungal)':
                    # create bacteriology pdf
                    test_info = self.model.get_bacteriology_test_information_by_id(
                        case_id)
                    # create_bacteriology(case_detail)
                    create_bacteriology(
                        sample_info, test_info, temp_pdf_file)
                    # open pdf file using default pdf viewer
                    os.system(f"start {temp_pdf_file}")

                elif case_lab == 'E410(PCR)':
                    test_info = self.model.get_molecular_test_information_by_id(
                        case_id)
                    # create_molecular_biology(case_detail)
                    create_molecular_biology(
                        sample_info, test_info, temp_pdf_file)
                    # open pdf file using default pdf viewer
                    os.system(f"start {temp_pdf_file}")
                else:
                    QMessageBox.critical(self.view, "Error",
                                         "ไม่สามารถพิมพ์ใบส่งงานได้")

    def delete_specimen_in_new_case_page(self):
        """Delete specimen in new case
        """
        selected_item = self.view.new_case_detail_case_tree_view.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to delete")
        else:
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to delete")
            else:
                case_id = int(selected_item[0].text(1))
                if self.model.delete_specimen_in_new_case_page(case_id):
                    QMessageBox.information(self.view, "Success",
                                            "ลบข้อมูลเรียบร้อย")
                    self.reload_new_job_page()

    def print_barcode_in_new_case_page(self):
        """Print barcode in new case page"""

        selected_item = self.view.new_case_detail_case_tree_view.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to print barcode")
        else:
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to print barcode")
            else:
                barcode_obj = BarcodeGenerator()
                row_list = []
                for row in selected_item:
                    column_list = []
                    for col in range(self.view.new_case_detail_case_tree_view.columnCount()):
                        column_list.append(row.text(col))
                    row_list.append(column_list)
                barcode_obj.generate(row_list)
                barcode_obj.print_barcode()

    def new_case_search_user_change(self):
        """"Auto complete search name in the new case register page"""
        search_word = self.view.new_case_search_name_entry.text()
        show_customer_names = []
        if search_word != "":
            for current_customer_info in self.all_customer_names:
                if search_word in current_customer_info[0] or search_word in current_customer_info[1] or search_word in current_customer_info[2]:
                    show_customer_names.append(current_customer_info)

        self.view.new_case_search_tree_view.clear()
        if len(show_customer_names) > 0:
            self.view.add_customer_info_new_case(show_customer_names)

    def bind_event_in_specimen_page(self):
        """Bind event in specimen page"""
        self.view.specimen_page_save_pushButton.clicked.connect(
            self.save_specimen_information)
        self.view.specimen_page_back_pushButton.clicked.connect(
            self.view.backto_job_register_page)

        self.view.specimen_page_molecular_pushButton.clicked.connect(
            self.show_molecular_biology_page)

        self.view.specimen_page_Parasitology_pushButton.clicked.connect(
            self.view.show_Parasitology_page)

        self.view.specimen_page_Microbiology_pushButton.clicked.connect(
            self.load_microbiology_page)

    def load_microbiology_page(self):
        """Load microbiology page"""
        self.view.clear_microbiology_page()
        self.view.show_Microbiology_page()

    def show_molecular_biology_page(self):
        """" Clear and show molecular biology page"""
        self.view.clear_molecular_biology_page()
        self.view.show_molecular_biology_page()

    def bind_event_in_parasitology_page(self):
        """Bind event in parasitology page"""
        self.view.parasite_summary_pushButton.clicked.connect(
            self.compute_parasite_test_summary)
        self.view.parasite_save_data_pushButton.clicked.connect(
            self.save_parasite_information)
        self.view.parasite_cancel_pushButton.clicked.connect(
            self.view.back_to_specimen_page)
        self.view.back_to_home_pushButton.clicked.connect(
            self.view.back_to_specimen_page)

    def save_parasite_information(self):
        """Save parasite information"""
        # get data from the view
        data_list, checkbox_state = self.view.get_parasite_data()
        # save data to the database
        sample_id = self.view.specimen_page_label.text().split(":")[1]
        if self.model.save_parasite_information(int(sample_id), data_list, checkbox_state, self.user_login_info[0][1]):
            lab_id = "5"            # 5 is the lab id for parasite lab
            self.model.save_lab_order(
                sample_id, lab_id, "", self.user_login_info[0][1])  # save lab order
            QMessageBox.information(self.view, "Success",
                                    "บันทึกข้อมูลเรียบร้อย")
            self.model.save_tracking_information(
                sample_id, self.user_login_info[0][1], self.user_login_info[0][1], "รับงานเข้าระบบ")
            self.reload_new_job_page()
        else:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่สามารถบันทึกข้อมูลได้")

    def compute_parasite_test_summary(self):
        """Compute parasite test summary"""
        # get data from the view
        data_list, checkbox_state = self.view.get_parasite_data()
        self.view.parasite_amount_lineEdit.setText(str(sum(checkbox_state)))
        total_cost = 0
        for i, cb_state in enumerate(checkbox_state):
            if cb_state == 1:
                total_cost += int(data_list[2*i+1])
        self.view.parasite_cost_lineEdit.setText(str(total_cost))

    def bind_event_in_microbiology_page(self):
        """Bind event in microbiology page"""
        self.view.bacteria_lab_summary_Button.clicked.connect(
            self.compute_bacteria_lab_summary)
        self.view.bacteria_page_save_data_pushButton.clicked.connect(
            self.save_bacteria_lab_information)
        self.view.bacteria_page_cancel_pushButton.clicked.connect(
            self.view.back_to_specimen_page)

    def save_bacteria_lab_information(self):
        """Save bacteria lab information"""
        sample_preparation, preparation_name, preparation_amount, drug_sensitivity_status, drug_sensitivity_name, bacteria_identification_name, bacteria_identification_status, lab_request_name, lab_request_status, lab_request_price, remark = self.view.get_bacteria_lab_data()

        preparation_data = []
        for i, p_name in enumerate(preparation_name):
            preparation_data.append(p_name)
            preparation_data.append(sample_preparation[i])
            preparation_data.append(preparation_amount[i])

        drug_sensitivity_data = []
        for i, ds_name in enumerate(drug_sensitivity_name):
            drug_sensitivity_data.append(ds_name)
            drug_sensitivity_data.append(drug_sensitivity_status[i])

        bacteria_identification_data = []
        for i, bi_name in enumerate(bacteria_identification_name):
            bacteria_identification_data.append(
                bi_name)
            bacteria_identification_data.append(
                bacteria_identification_status[i])

        lab_request_data = []
        for i, lr_name in enumerate(lab_request_name):
            lab_request_data.append(lr_name)
            lab_request_data.append(lab_request_status[i])
            lab_request_data.append(lab_request_price[i])

        data = preparation_data + drug_sensitivity_data + \
            bacteria_identification_data + lab_request_data + [remark]

        sample_id = self.view.specimen_page_label.text().split(":")[1]
        if self.model.save_bacteria_lab_information(sample_id, data, self.user_login_info[0][1]):
            lab_id = "2"            # 2 is the lab id for bacteria lab
            self.model.save_lab_order(
                sample_id, lab_id, "", self.user_login_info[0][1])
            QMessageBox.information(self.view, "Success",
                                    "บันทึกข้อมูลเรียบร้อย")
            self.model.save_tracking_information(
                sample_id, self.user_login_info[0][1], self.user_login_info[0][1], "รับงานเข้าระบบ")
            self.reload_new_job_page()
        else:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่สามารถบันทึกข้อมูลได้")

    def compute_bacteria_lab_summary(self):
        """Compute bacteria lab summary"""
        # get data from the view
        sample_preparation, preparation_name, preparation_amount, drug_sensitivity_status, drug_sensitivity_name, bacteria_identification_name, bacteria_identification_status, lab_request_name, lab_request_status, lab_request_price, remark = self.view.get_bacteria_lab_data()

        count = sum(sample_preparation) + sum(drug_sensitivity_status) + \
            sum(bacteria_identification_status) + sum(lab_request_status)
        total_cost = 0
        for index, lab_request in enumerate(lab_request_status):
            if lab_request == 1:
                total_cost += lab_request_price[index]

        self.view.bacteria_page_amount_lineEdit.setText(str(count))
        self.view.bacteria_page_cost_lineEdit.setText(str(total_cost))

    def bind_event_in_molecular_biology_page(self):
        """Bind event in molecular biology page"""
        self.view.molecular_biology_summary_pushButton.clicked.connect(
            self.compute_molecular_biology_summary)

        # self.view.molecular_biology_back_pushButton.clicked.connect(
        # self.view.backto_specimen_page)

        self.view.molecular_biology_save_data_pushButton.clicked.connect(
            self.save_molecular_biology_information)

    def save_molecular_biology_information(self):
        """Save molecular biology information"""
        # get data from the view
        data, error_message, checkbox_state = self.view.get_molecular_biology_data()
        # save data to the database
        sample_id = self.view.specimen_page_label.text().split(":")[1]
        if self.model.save_molecular_biology_information(sample_id, data, self.user_login_info[0][1]):
            lab_id = "8"            # 8 is the lab id for molecular biology
            self.model.save_lab_order(
                sample_id, lab_id, "", self.user_login_info[0][1])
            QMessageBox.information(self.view, "Success",
                                    "บันทึกข้อมูลเรียบร้อย")
            self.model.save_tracking_information(
                sample_id, self.user_login_info[0][1], self.user_login_info[0][1], "รับงานเข้าระบบ")
            self.reload_new_job_page()
            # ==================== enable lab buttons ====================
        else:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่สามารถบันทึกข้อมูลได้")

    def compute_molecular_biology_summary(self):
        """Compute molecular biology summary"""
        # get data from the view
        data = self.view.get_molecular_biology_data()

    def save_specimen_information(self):
        """Save specimen information
        """
        # get data from the view
        specimen_data = []
        specimen_data.append(int(self.view.new_case_number_job_entry.text()))
        specimen_data.append(
            self.view.specimen_page_name_animal_entry.text())
        specimen_data.append(
            self.view.specimen_page_number_id_opd_entry.text())
        specimen_data.append(
            self.view.specimen_page_sex_animal_comboBox.currentText())
        specimen_data.append(self.view.specimen_page_year_animal_entry.text())
        specimen_data.append(self.view.specimen_page_month_animal_entry.text())
        specimen_data.append(self.view.specimen_page_day_animal_entry.text())
        specimen_data.append(
            self.view.specimen_page_cause_of_death_comboBox.currentText())
        species = ""
        if self.view.swine_radioButton.isChecked():
            species = self.view.swine_radioButton.text()
        elif self.view.avian_radioButton.isChecked():
            species = self.view.avian_radioButton.text()
        elif self.view.bovine_radioButton.isChecked():
            species = self.view.bovine_radioButton.text()
        elif self.view.equine_radioButton.isChecked():
            species = self.view.equine_radioButton.text()
        elif self.view.canine_radioButton.isChecked():
            species = self.view.canine_radioButton.text()
        elif self.view.feline_radioButton.isChecked():
            species = self.view.feline_radioButton.text()
        elif self.view.elephant_radioButton.isChecked():
            species = self.view.elephant_radioButton.text()
        elif self.view.another_radioButton.isChecked():
            species = self.view.another_type_animal_entry.text()
        elif self.view.unknow_radioButton.isChecked():
            species = self.view.unknow_radioButton.text()
        else:
            species = "Unknow"
        specimen_data.append(species)
        specimen_data.append(self.view.specimen_page_breed_entry.text())

        sample_type = ""
        if self.view.specimen_page_most_argent_radioButton.isChecked():
            sample_type = self.view.specimen_page_most_argent_radioButton.text()
        elif self.view.specimen_page_normal_radioButton.isChecked():
            sample_type = self.view.specimen_page_normal_radioButton.text()
        specimen_data.append(sample_type)

        specimen_data.append(
            self.view.specimen_page_weight_animal_entry.text())
        specimen_data.append(
            self.view.specimen_page_day_of_death_dateTime.text())
        specimen_data.append(
            self.view.specimen_page_day_keep_sample_dateTime.text())

        keep_method = ""
        if self.view.specimen_page_chill_specimen_radioButton.isChecked():
            keep_method = self.view.specimen_page_chill_specimen_radioButton.text()
        elif self.view.specimen_page_freeze_specimen_radioButton.isChecked():
            keep_method = self.view.specimen_page_freeze_specimen_radioButton.text()
        elif self.view.specimen_page_room_temp_specimen_radioButton.isChecked():
            keep_method = self.view.specimen_page_room_temp_specimen_radioButton.text()
        else:
            keep_method = "Unknow"
        specimen_data.append(keep_method)

        sample_test_speed = ""
        if self.view.specimen_page_normal_radioButton.isChecked():
            sample_test_speed = self.view.specimen_page_normal_radioButton.text()
        elif self.view.specimen_page_most_argent_radioButton.isChecked():
            sample_test_speed = self.view.specimen_page_most_argent_radioButton.text()
        else:
            sample_test_speed = "Unknow"
        specimen_data.append(sample_test_speed)

        specimen_data.append(
            self.view.specimen_page_record_heal_textEdit.toPlainText())

        specimen_data.append(int(self.user_login_info[0][1]))
        current_id = self.model.save_specimen_information(specimen_data)
        if current_id > 0:
            QMessageBox.information(self.view, "Success",
                                    "บันทึกข้อมูลตัวอย่างเรียบร้อย")
            # disable widgets
            self.view.disable_widgets_in_specimen_page()

            # clear all entry
            self.view.clear_specimen_information()
            self.view.enable_lab_buttons()
            # set specimen page label
            specimen_page_label = "Specimen:" + str(current_id)
            self.view.specimen_page_label.setText(specimen_page_label)
            # ==================== enable lab buttons ====================
        else:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่สามารถบันทึกข้อมูลตัวอย่างได้")

    def register_new_case(self):
        """register new case to the database"""
        skip = False

        if self.view.new_case_name_sender_entry.text() == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาเลือกผู้ส่งตัวอย่าง")
        else:
            if self.view.new_case_name_project_entry.text() == "":
                reply = QMessageBox.warning(self.view, "Warning",
                                            "ต้องการดำเนินการต่อโดยไม่บันทึกชื่อโครงการหรือไม่?",
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.No:
                    self.view.new_case_name_project_entry.setFocus()
                    skip = True
            if not skip:
                # disable all add button
                self.view.new_case_select_sender_button.setEnabled(False)
                self.view.new_case_select_owner_button.setEnabled(False)
                self.view.new_case_anonymous_owner_button.setEnabled(False)
                self.view.new_case_save_button.setEnabled(False)

                # get data from the view
                case_data = []
                case_data.append(self.view.new_case_name_sender_entry.text())
                case_data.append(
                    self.view.new_case_surename_sender_entry.text())
                case_data.append(self.view.new_case_tax_sender_entry.text())
                case_data.append(self.view.new_case_name_owner_entry.text())
                case_data.append(
                    self.view.new_case_surename_owner_entry.text())
                case_data.append(self.view.new_case_tax_owner_entry.text())
                case_data.append(self.view.new_case_name_project_entry.text())
                case_id = self.model.save_new_case_register(
                    case_data, self.user_login_info[0][1])
                if case_id > 0:
                    self.view.new_case_number_job_entry.setText(str(case_id))
                    QMessageBox.information(self.view, "Success",
                                            "บันทึกข้อมูลเรียบร้อย")
                    # clear data in search tree view
                    self.view.new_case_search_tree_view.clear()
                    self.view.new_case_search_name_entry.setText("")

                    # disable entry name and tree view
                    self.view.new_case_search_name_entry.setEnabled(False)
                    self.view.new_case_search_tree_view.setEnabled(False)

                    # disable sender and owner information
                    self.view.new_case_name_sender_entry.setEnabled(False)
                    self.view.new_case_surename_sender_entry.setEnabled(False)
                    self.view.new_case_tax_sender_entry.setEnabled(False)
                    self.view.new_case_name_owner_entry.setEnabled(False)
                    self.view.new_case_surename_owner_entry.setEnabled(False)
                    self.view.new_case_tax_owner_entry.setEnabled(False)
                    self.view.new_case_name_project_entry.setEnabled(False)

                    # enable add lab button
                    self.view.new_case_add_data_specimen_button.setEnabled(
                        True)
                    self.view.new_case_delete_data_specimen_button.setEnabled(
                        True)
                    self.view.new_case_print_sticker_button.setEnabled(True)
                    self.view.new_case_print_lab_report_button.setEnabled(True)

    def clear_new_case_owner_info(self) -> None:
        """Clear owner information in the case register page"""
        self.view.new_case_name_owner_entry.setText("")
        self.view.new_case_surename_owner_entry.setText("")
        self.view.new_case_tax_owner_entry.setText("")

    def new_case_add_owner_info(self):
        """Add owner information to the case register"""
        if self.view.new_case_search_tree_view.selectedItems() == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to add owner information")
        else:
            selected_item = self.view.new_case_search_tree_view.selectedItems()
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to add owner information")
            else:
                for row in selected_item:
                    self.view.new_case_name_owner_entry.setText(row.text(0))
                    self.view.new_case_surename_owner_entry.setText(
                        row.text(1))
                    self.view.new_case_tax_owner_entry.setText(row.text(2))

    def new_case_add_sender_info(self):
        """Add sender information to the case register"""
        # # if case number is empty, read the last case number from the database
        # if self.view.new_case_number_job_entry.text() == "":
        #     last_case_number = self.model.get_last_case_number()
        #     last_case_number = int(last_case_number) + 1
        #     self.view.new_case_number_job_entry.setText(str(last_case_number))

        if self.view.new_case_search_tree_view.selectedItems() == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to add sender information")
        else:
            selected_item = self.view.new_case_search_tree_view.selectedItems()
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to add sender information")
            else:
                for row in selected_item:
                    self.view.new_case_name_sender_entry.setText(row.text(0))
                    self.view.new_case_surename_sender_entry.setText(
                        row.text(1))
                    self.view.new_case_tax_sender_entry.setText(row.text(2))

    def new_case_search_user(self):
        """Search case register"""
        keyword_search = self.view.new_case_search_name_entry.text()
        if keyword_search == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาป้อนชื่อหรือนามสกุลของลูกค้า")
        else:
            customer_information = self.model.new_case_search_customer(
                keyword_search)
            if customer_information == []:
                QMessageBox.critical(self.view, "Error",
                                     "ไม่พบข้อมูลลูกค้า")
            else:
                self.view.add_customer_info_new_case(customer_information)

    def disable_tax_entry(self, state: int) -> None:
        """Disable tax entry if the checkbox is checked"""
        if state == 2:
            self.view.new_customer_tax_entry.setEnabled(False)
            self.view.new_customer_tax_entry.clear()
        else:
            self.view.new_customer_tax_entry.setEnabled(True)

    def copy_address_to_bill_address(self, state: int) -> None:
        """Copy address to bill address"""
        if state == 2:
            self.view.new_customer_address_for_bill_entry.setPlainText(
                self.view.new_customer_address_entry.toPlainText())
        else:
            self.view.new_customer_address_for_bill_entry.clear()

    def save_new_customer(self) -> None:
        """Save new customer to the database"""
        # check all fields are filled
        if self.view.new_customer_title_entry.text() == "" or self.view.new_customer_name_entry.text() == "" or self.view.new_customer_surname_entry.text() == "" or self.view.new_customer_phone_entry.text() == "" or self.view.new_customer_email_entry.text() == "":
            message = "กรุณากรอกข้อมูล \n คำนำหน้าชื่อ \n ชื่อ \n สกุล \n เบอร์โทร \n และ email ให้ครบถ้วน"
            QMessageBox.critical(self.view, "Error", message)
        else:
            # get all data from the view
            group_id = 0
            if self.view.new_customer_private_radioBT.isChecked():
                group_id = 1
            elif self.view.new_customer_public_radioBT.isChecked():
                group_id = 2
            elif self.view.new_customer_internal_radioBT.isChecked():
                group_id = 3
            elif self.view.new_customer_professor_radioBT.isChecked():
                group_id = 4
            elif self.view.new_customer_student_radioBT.isChecked():
                group_id = 5

            title = self.view.new_customer_title_entry.text()
            name = self.view.new_customer_name_entry.text()
            surname = self.view.new_customer_surname_entry.text()
            tax_id = self.view.new_customer_tax_entry.text()
            email = self.view.new_customer_email_entry.text()
            line_id = self.view.new_customer_line_entry.text()
            phone = self.view.new_customer_phone_entry.text()
            # get data from qtexedit
            contact_address = self.view.new_customer_address_entry.toPlainText()
            bill_address = self.view.new_customer_address_for_bill_entry.toPlainText()
            # get updater id from the user_login_info
            updater = self.user_login_info[0][1]
            # save data to the database
            if self.model.save_new_customer(group_id, title, name, surname, tax_id,
                                            email, line_id, phone, contact_address, bill_address, updater):
                QMessageBox.information(self.view, "Success",
                                        "บันทึกข้อมูลลูกค้าเรียบร้อย")
                self.view.clear_new_customer_information()
                # reload all customer names
                self.all_customer_names = self.model.get_all_customer_names()
            else:
                QMessageBox.critical(self.view, "Error",
                                     "ไม่สามารถบันทึกข้อมูลลูกค้าได้")

    def search_today_sticker(self):
        """ serach all case that registered today. Sorting the result by date and time"""
        data = self.model.get_today_case_detail()
        self.view.sticker_search_treeWidget.clear()

        data_list = []
        for item in data:
            data_item = []
            data_item.append(item[0].strftime("%d-%m-%Y %H:%M:%S"))
            data_item.append(str(item[1]).zfill(10))
            data_item.append(item[2])
            lab_name = item[3] + "(" + item[4] + ")"
            data_item.append(lab_name)
            data_item.append(item[5])
            data_item.append(item[6])
            data_item.append("")
            data_list.append(data_item)
        self.add_customer_case_to_view(data_list)

    def search_sticker(self):
        """ serach customer name to get a sticker information"""
        # keyword_search = self.view.sticker_search_lineEdit.text()
        # get name from selected first column in QTreeWidget
        selected_item = self.view.barcode_page_customertreeWidget.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาเลือกข้อมูลของลูกค้า")
        else:
            selected_name = selected_item[0].text(0)
            selected_surname = selected_item[0].text(1)
            data = self.model.get_case_detail_by_customer_name(
                selected_name, selected_surname)
            self.view.sticker_search_treeWidget.clear()

            data_list = []
            for item in data:
                data_item = []
                data_item.append(item[0].strftime("%d-%m-%Y %H:%M:%S"))
                data_item.append(str(item[1]).zfill(10))
                data_item.append(item[2])
                lab_name = item[3] + "(" + item[4] + ")"
                data_item.append(lab_name)
                data_item.append(item[5])
                data_item.append(item[6])
                data_item.append("")
                data_list.append(data_item)
            self.add_customer_case_to_view(data_list)

    def add_customer_case_to_view(self, data):
        """Add customer case to the view"""
        if data == None or data == []:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่พบข้อมูลลูกค้า")
            self.view.sticker_search_lineEdit.clear()
        else:
            self.view.add_data_to_listview_printerpage(data)

    def print_barcode(self):
        """Print a selected information to barcode """
        # get selected item from the QTreeWidget
        selected_item = self.view.sticker_search_treeWidget.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to print barcode")
        else:
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to print barcode")
            else:
                barcode_obj = BarcodeGenerator()
                row_list = []
                for row in selected_item:
                    column_list = []
                    for col in range(self.view.sticker_search_treeWidget.columnCount()):
                        column_list.append(row.text(col))
                    row_list.append(column_list)
                barcode_obj.generate(row_list)
                barcode_obj.print_barcode()

        # generate barcode

    def user_sign_in(self):
        """User sign in method"""
        # get username and password from the view
        username = self.view.username_lineEdit.text()
        password = self.view.password_lineEdit.text()

        # if username and password are not empty
        if username != "" and password != "":
            self.view.clear_user_and_password()
            login_info = self.model.user_sign_in(username, password)
            if login_info:
                self.user_login_info = login_info
                current_name = login_info[0][3] + " " + \
                    login_info[0][4] + " " + login_info[0][5]
                self.view.show_current_user_information(current_name)
                self.view.enable_all_buttons()
                # self.view.show_molecular_biology_page()
                self.all_customer_names = self.model.get_all_customer_names()
                self.view.show_job_register_page()

        elif username == "" and password != "":
            self.view.username_lineEdit.setFocus()
            QMessageBox.critical(self.view, "Error",
                                 "Username cannot be empty")
            # show message
        elif username != "" and password == "":
            self.view.password_lineEdit.setFocus()
            # show message
            QMessageBox.critical(self.view, "Error",
                                 "Password cannot be empty")
        else:
            self.view.username_lineEdit.setFocus()
            # show message
            QMessageBox.critical(self.view, "Error",
                                 "Username and Password cannot be empty")

    def user_sign_out(self):
        """User sign out method"""
        self.view.clear_user_and_password()
        self.view.clear_information()
        self.user_login_info = []
        # disable all buttons
        self.view.disable_all_buttons()
        self.view.show_login_page()
        # clear user information on top right corner
        self.view.clear_current_user_information()

    def reload_new_job_page(self):
        """Reload specimen page"""
        # clear list views and load all labs to the tree view
        self.view.new_case_detail_case_tree_view.clear()
        # read all lab_order from the current case
        case_id = self.view.new_case_number_job_entry.text()
        lab_order_details = self.model.get_lab_order_details(case_id)
        lab_info = []
        for lab_order_detail in lab_order_details:
            info = []
            # convert timestamp to string
            info.append(str(lab_order_detail[0]))
            # if lab order is intger less than 10, add 0 in front of the number
            info.append(str(lab_order_detail[1]).zfill(12))
            info.append(lab_order_detail[2])
            room_code = lab_order_detail[3] + "(" + lab_order_detail[4] + ")"
            info.append(room_code)
            info.append(lab_order_detail[5])
            info.append(lab_order_detail[6])
            lab_info.append(info)
        self.view.reload_lab_order_detail_to_tree_view(lab_info)
        self.view.reload_new_job_page()
