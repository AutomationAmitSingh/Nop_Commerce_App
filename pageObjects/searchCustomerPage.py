class SearchCustomer:
    # Add customer Page
    txtEmail_id = "SearchEmail"
    txtEmail_xpath = "//input[@id='SearchEmail']"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        print(email)
        self.driver.find_element_by_xpath(self.txtEmail_xpath).click()
        print("Before Clear")
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        print("After Clear")
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)
        print("Email printed in input text")

    def set_first_name(self, f_name):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(l_name)

    def click_search(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def get_no_of_rows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def get_no_of_columns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_no_of_rows()+1):
          table = self.driver.find_element_by_xpath(self.table_xpath)
          email_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
          print(email_id)
          if email_id == email:
              flag = True
              break
        return flag

    def search_customer_by_name(self, Name):
        flag = False
        for r in range(1,self.get_no_of_rows()+1):
          table = self.driver.find_element_by_xpath(self.table_xpath)
          name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
          if name == Name:
              flag = True
              break
        return flag
