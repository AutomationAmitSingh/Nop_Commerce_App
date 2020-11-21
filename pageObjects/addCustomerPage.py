import time
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menu_item_xpath = "//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAdd_new_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txt_customerRoles_xpath = "//div[@class='form-group'][10]//div[@class='k-multiselect-wrap k-floatwrap']"
    lst_itemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lst_itemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lst_itemGuests_xpath = "//li[contains(text(),'Guests')]"
    lst_itemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drp_mgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_customers_menu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def click_on_customers_menu_item(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_item_xpath).click()

    def click_on_add_new(self):
        self.driver.find_element_by_xpath(self.btnAdd_new_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def set_customer_roles(self, role):
        self.driver.find_element_by_xpath(self.txt_customerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lst_itemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def set_manager_of_vendor(self, value):
        drp=Select(self.driver.find_element_by_xpath(self.drp_mgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def set_first_name(self, f_name):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(l_name)

    def set_dob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def set_company_name(self, com_name):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(com_name)

    def set_admin_content(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def click_on_save(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()
