import os
import json
import time
import datetime
import uuid
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
# import test
# import subprocess
# subprocess.run(["python3", "test.py"])

# test()
chrome_options = Options()
chrome_options.add_argument('--headless=old')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
# download_dir = "E:\\takshil\\quantum_pdf\\"
download_dir = "/var/www/novyy-dev/novyyloans/storage/app/public/qmlApplications/"
# download_dir = "/home/ubuntu/storage/loan-applications/"

# download_dir = "D:\\khushali\\pdf\\"
driver.execute_cdp_cmd("Page.setDownloadBehavior", {
    "behavior": "allow",
    "downloadPath": download_dir
})

url = "https://novyyloans.ntlstaging.co.uk/api/applications"
response = requests.request("GET", url)
jss = json.loads(response.text)
for js in jss:
    print('Time:'+str(datetime.datetime.now().strftime("%H:%M:%S")))
    print(js)

    driver.get('https://www.qmlsystem.co.uk/Portal/Application/DisplayForm?formName=Apply%20-%20Who%20is%20applying&items=2TnhPEhIjm8pGUhSWoIm%2B5jvt6o6pgltxGSdMUZKE2ky8vF7wyt5DSNT395nKyC%2B')
    time.sleep(3)
    try:
        username = driver.find_element(By.ID ,'Email')
        username.send_keys('asaraff@arethacapital.com')
        time.sleep(1)

        password = driver.find_element(By.ID ,'Password')
        password.send_keys('X5VA5uX!tLLj4Yg')
        time.sleep(1)

        login = driver.find_element(By.XPATH, '//*[@type="submit"]').click()
        time.sleep(2)
    except:
        pass


    company = js['name_of_company']
    if company:
        comp = driver.find_element(By.XPATH, '//*[contains(text(),"UK Limited Company, UK SPV or UK LLP")]/..').click()
        print('company')
    else:
        private = driver.find_element(By.XPATH, '//*[contains(text(),"Private individual")]/..').click()
        print('no')

    try:
        number_of_applicants = driver.find_element(By.XPATH, '//*[@id="Application_NumberOfApplicants"]')
        number_of_applicants.clear()
        number_of_applicants.send_keys(js['number_of_applicants'])

        next = driver.find_element(By.XPATH, '//*[@class="btn btn-default  btnNavRight blueBtn"]').click()
        next = driver.find_element(By.XPATH, '//*[@class="btn btn-default  btnNavRight blueBtn"]').click()

        located_england = js['located_england']
        # if located_england == 'Yes':
        if 'Yes' in located_england:
            located_england = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
        else:
            located_england = driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()

        purchace_new = js['purchace_new']
        # if purchace_new == 'Yes':
        if 'Yes' in purchace_new:
            purchace_new = driver.find_element(By.XPATH, '//*[contains(text(),"PURCHASE a new property")]/..').click()
        else:
            purchace_new = driver.find_element(By.XPATH, '//*[contains(text(),"REMORTGAGE an existing property")]/..').click()

        first_time = js['first_time']
        # if first_time == 'Yes':
        if 'Yes' in first_time:
            first_time = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
        else:
            first_time = driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()

        plan_occupy = js['plan_occupy']
        # if  plan_occupy == "yes":
        if  'Yes' in plan_occupy:
            plan_occupy = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
        else:
            plan_occupy = driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()

        try:
            btl_properties = js['btl_property']
            if 'Yes' in btl_properties:
                btl_properties = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
            else:
                btl_properties = driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()
        except:
            pass


        service = js['service']
        # if  service == "Advised":
        if "Advised" in service:
            service = driver.find_element(By.XPATH, '//*[contains(text(),"Advised")]/..').click()#Advised
        else:
            service = driver.find_element(By.XPATH, '//*[contains(text(),"Information Only")]/..').click()

        # *************************** form start(page 1) ******************************** #
        try:
            company_name = driver.find_element(By.XPATH, '//*[@name="Company.RegisteredName"]')
            company_name.send_keys(js['name_of_company'])
        except:
            pass

        reg_no = js['company_registration_number']
        if reg_no:
            reg_yes = driver.find_element(By.XPATH, '//*[@for="Company_DoYouKnowRegisteredNumber"]/../div/div/div/span[2]').click()
            time.sleep(2)
            comp_no = driver.find_element(By.XPATH, '//*[@name="Company.RegisteredNumber"]')
            comp_no.send_keys(js['company_registration_number'])
        else:
            pass

        try:
            sic_code = driver.find_element(By.XPATH, '//*[@name="Company.SICCode"]')
            sic_code.send_keys(js['sic_code'])
        except:
            pass

        try:
            comp_postalcode = driver.find_element(By.XPATH, '//*[@id="Company_AddressPostCode"]')
            comp_postalcode.send_keys(js['company_postlecode'])
        except:
            pass

        try:
            comp_add = driver.find_element(By.XPATH, '//*[@id="Company_AddressLine1"]')
            comp_add.send_keys(js['company_address_line_1'])
        except:
            pass

        try:
            comp_city = driver.find_element(By.XPATH, '//*[@name="Company.AddressCity"]')
            comp_city.send_keys(js['company_city'])
        except:
            pass

        try:
            comp_country = driver.find_element(By.XPATH, '//*[@id="Company_AddressCountry"]')
            comp_country.send_keys(js['company_country'])
        except:
            pass

        try:
            title = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Title"]')
            title.send_keys(js['title'])
        except:
            pass

        try:
            postlecode = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_AddressPostCode"]')
            postlecode.send_keys(js['postlecode'])
        except:
            pass

        try:
            first_name = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.FirstName"]')
            first_name.send_keys(js['first_name'])
        except:
            pass

        try:
            address_line_1 = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.AddressLine1"]')
            address_line_1.send_keys(js['address_line_1'])
        except:
            pass

        try:
            last_name = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.LastName"]')
            last_name.send_keys(js['last_name'])
        except:
            pass

        try:
            dob = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.DateOfBirth_Date"]')
            dob.send_keys(js['dob'])
        except:
            pass

        try:
            nationality = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Nationality"]')
            nationality.send_keys(js['nationality'])
        except:
            nationality = ''

        try:
            country = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_AddressCountry"]')
            country.send_keys(js['country'])
        except:
            country = ''

        try:
            employment_status = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_EmploymentClass"]')
            employment_status.send_keys(js['employment_status'])
        except:
            pass

        try:
            residential_status = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_ResidentialStatus"]')
            residential_status.send_keys(js['residential_status'])
        except:
            pass

        try:
            anual_income = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Employment.BasicGrossIncome"]')
            anual_income.send_keys(js['anual_income'])
        except:
            pass

        try:
            date_moved_to_address = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.AddressMovedDate_Date"]')
            date_moved_to_address.send_keys(js['date_moved_to_address'])
        except:
            pass

        try:
            marginal_tax_band = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.TaxPayer"]')
            marginal_tax_band.send_keys(js['marginal_tax_band'])
        except:
            pass

        try:
            existing_borrower = js['existing_borrower']
            if existing_borrower == 'Yes':
                existing_borrower = driver.find_element(By.XPATH, '//*[@for="Applicant[0]_Applicant_ExistingLenderRelationship"]/../div/div/div//*[contains(text(),"No")]').click()
            else:
                pass
        except:
            pass

        try:
            email = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Email"]')
            email.send_keys(js['email'])
        except:
            pass

        try:
            phone_number = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.MobileNumber_Phone"]')
            phone_number.send_keys(js['phone_number'])
        except:
            pass


        try:
            security_property_type = driver.find_element(By.XPATH, '//*[@id="Security_PropertyType"]')
            security_property_type.send_keys(js['security_property_type'])
        except:
            pass

        time.sleep(2)
        try:
            popup_button = driver.find_element(By.XPATH, '//button[contains(text(),"Ok")]').click()
        except:
            pass

        try:
            security_postalcode = driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressPostCode"]')
            security_postalcode.send_keys(js['security_postalcode'])
        except:
            pass

        try:
            security_address = driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressLine1"]')
            security_address.send_keys(js['security_address'])
        except:
            pass

        try:
            security_property_tenure = driver.find_element(By.XPATH, '//*[@name="Security.PropertyTenure"]')
            security_property_tenure.send_keys(js['security_property_tenure'])
        except:
            pass

        try:
            security_purchase_price = driver.find_element(By.XPATH, '//*[@name="Mortgage.PurchasePrice"]')
            security_purchase_price.send_keys(js['security_purchase_price'])
        except:
            pass

        try:
            security_loan_amount = driver.find_element(By.XPATH, '//*[@name="Mortgage.LoanRequired"]')
            security_loan_amount.send_keys(js['security_loan_amount'])
        except:
            pass

        try:
            security_rental_income = driver.find_element(By.XPATH, '//*[@name="Mortgage.MonthlyRentalIncome"]')
            security_rental_income.send_keys(js['security_rental_income'])
        except:
            pass

        try:
            security_sector_experience = driver.find_element(By.XPATH, '//*[@name="Security.SectorExperience"]')
            security_sector_experience.send_keys(js['security_sector_experience'])
        except:
            pass

        try:
            security_built_year = driver.find_element(By.XPATH, '//*[@name="Security.PropertyYearBuilt"]')
            security_built_year.send_keys(js['security_built_year'])
        except:
            pass

        try:
            security_no_of_unit = driver.find_element(By.XPATH, '//*[@name="Security.NumberOfUnits"]')
            security_no_of_unit.send_keys(js['security_no_of_unit'])
        except:
            pass

        try:
            security_country = driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressCountry"]')
            security_country.send_keys(js['security_country'])
        except:
            pass

        try:
            previous_postalcode = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressPostCode"]')
            previous_postalcode.send_keys(js['previous_postalcode'])
        except:
            pass

        try:
            previous_address = driver.find_element(By.XPATH ,'//*[@name="Applicant[0].Applicant.Previous1AddressLine1"]')
            previous_address.send_keys(js['previous_address'])
        except:
            pass

        try:
            previous_country = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Previous1AddressCountry"]')
            previous_country.send_keys(js['previous_country'])
        except:
            pass

        try:
            previous_date_moved_to_address = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressMovedDate_Date"]')
            previous_date_moved_to_address.send_keys(js['previous_date_moved_to_address'])
        except:
            pass

        try:
            contin_btn = driver.find_element(By.XPATH, '//*[@id="requestCreditReport"]').click()
        except:
            pass

        try:
            previous2_postalcode = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous2AddressPostCode"]')
            previous2_postalcode.send_keys(js['previous2_postalcode'])
        except:
            pass

        try:
            previous2_address = driver.find_element(By.XPATH ,'//*[@name="Applicant[0].Applicant.Previous2AddressLine1"]')
            previous2_address.send_keys(js['previous2_address'])
        except:
            pass

        try:
            previous2_country = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Previous2AddressCountry"]')
            previous2_country.send_keys(js['previous2_country'])
        except:
            pass

        try:
            previous2_date_moved_to_address = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous2AddressMovedDate_Date"]')
            previous2_date_moved_to_address.send_keys(js['previous2_date_moved_to_address'])
        except:
            pass

        try:
            contin_btn = driver.find_element(By.XPATH, '//*[@id="requestCreditReport"]').click()
        except:
            pass
        try:
            contin_btn = driver.find_element(By.XPATH, '//*[@id="requestCreditReport"]').click()
        except:
            pass

        #****************************************************************************************************#

        #********************************** (page 2) *****************************************#

        time.sleep(3)
        satisfied_default = driver.find_element(By.XPATH, '//*[contains(text(),"Satisfied Defaults")]/../..//*[contains(text(),"No defaults within last 24 months")]/../input').click()

        satisfied_ccjs = driver.find_element(By.XPATH, '//*[contains(text(),"Satisfied CCJs")]/../..//*[contains(text(),"No CCJs")]/../input').click()

        unsatisfied_ccjs = driver.find_element(By.XPATH, '//*[contains(text(),"Unsatisfied CCJ’s/Defaults")]/../..//*[contains(text(),"None")]/../input').click()

        mortgage_arrears = driver.find_element(By.XPATH, '//*[contains(text(),"Mortgage Arrears")]/../..//*[contains(text(),"No missed mortgage")]/../input').click()

        payment_arrears = driver.find_element(By.XPATH, '//*[contains(text(),"Payment Arrears")]/../..//*[contains(text(),"No missed payments")]/../input').click()

        payment_holidays = driver.find_element(By.XPATH, '//*[contains(text(),"Payment Holidays")]/../..//*[contains(text(),"No")]/../input').click()

        payday_loans = driver.find_element(By.XPATH, '//*[contains(text(),"Payday Loans")]/../..//*[contains(text(),"None")]/../input').click()

        bankruptcy = driver.find_element(By.XPATH, '//*[contains(text(),"Bankruptcy")]/../..//*[contains(text(),"No")]/../input').click()

        iva = driver.find_element(By.XPATH, '//*[contains(text(),"IVA - Individual and Company")]/../..//*[contains(text(),"No")]/../input').click()

        administration_order = driver.find_element(By.XPATH, '//*[contains(text(),"Administration Orders")]/../..//*[contains(text(),"No")]/../input').click()

        payment_arrangements = driver.find_element(By.XPATH, '//*[contains(text(),"Payment Arrangements")]/../..//*[contains(text(),"No")]/../input').click()

        repossessions = driver.find_element(By.XPATH, '//*[contains(text(),"Repossessions")]/../..//*[contains(text(),"No")]/../input').click()

        debt_relief_orders = driver.find_element(By.XPATH, '//*[contains(text(),"Debt Relief Orders")]/../..//*[contains(text(),"No")]/../input').click()

        select_product = driver.find_element(By.XPATH, '//*[contains(text(),"Select product ")]').click()
        time.sleep(5)
        #*******************************************************************************************************#

        #********************************************* (page 3) ********************************************#
        try:
            fees = driver.find_element(By.XPATH, '//*[@id="Product_ProductFeePaymentType"]')
            fees.send_keys(js['fees'])
        except:
            pass
        time.sleep(6)

        try:
            number_of_loan = driver.find_element(By.XPATH,'//*[@id="Product_NumberOfYearsToRepay"]')
            number_of_loan.clear()
            time.sleep(6)
            number_of_loan.send_keys(js['numner_of_year_to_repay'])
        except:
            pass
        time.sleep(3)

        try:
            repayment_type = driver.find_element(By.XPATH, '//*[@id="Product_LoanRepaymentType"]')
            # time.sleep(6)
            repayment_type.send_keys(js['repayment_type'])
            time.sleep(6)
        except:
            pass
        time.sleep(3)

        try:
            product = js['product']
            sel_product = driver.find_element(By.XPATH,f'//*[contains(text(),"{product}")]/../td[@class="selectproduct"]/input').click()
        except:
            try:
                sel_product =driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[@class="selectproduct"]/input').click()
            except:
                pass

        try:
            fix_amount = driver.find_element(By.XPATH, '//*[@name="Broker.FixedAmount"]')
            fix_amount.send_keys(js['fix_amount'])
        except:
            pass

        try:
            general_illustration =  driver.find_element(By.XPATH, '//*[contains(text(),"Generate Illustration")]').click()
            time.sleep(6)
        except:
            pass
        try:
            general_illustration =  driver.find_element(By.XPATH, '//*[contains(text(),"Generate Illustration")]').click()
        except:
            pass
        time.sleep(5)
        #************************************************************************************************************#
        continue_application = driver.find_element(By.XPATH, '//*[contains(text(),"Continue application")]').click()
        time.sleep(3)

        next = driver.find_element(By.XPATH, '//*[contains(text(),"Next")]').click()
        time.sleep(3)


        unique_id_file_name = str(uuid.uuid5(uuid.NAMESPACE_DNS, js['email'] + str(datetime.datetime.now().strftime("%H:%M:%S"))))

        download = driver.find_element(By.XPATH, '//*[contains(text(),"Reissue DIP")]')

        before_download = set(os.listdir(download_dir))

        # Click the download button to start downloading
        download.click()
        time.sleep(8)

        # Wait for a new file to appear in the download directory
        new_file_name = None
        while not new_file_name:
            time.sleep(1)  # Check every second for a new file
            after_download = set(os.listdir(download_dir))
            new_files = after_download - before_download  # Get the new file(s)

            # If there's a new file, get its name
            if new_files:
                new_file_name = new_files.pop()

        # Wait until the file is fully downloaded (Chrome adds .crdownload until the download is complete)
        new_file_path = os.path.join(download_dir, new_file_name)
        while new_file_name.endswith(".crdownload") or not os.path.exists(new_file_path):
            time.sleep(1)

        # Define the new file name
        updated_file_name = unique_id_file_name+'.pdf'  # Replace with your desired file name
        updated_file_path = os.path.join(download_dir, updated_file_name)

        # Rename the file
        os.rename(new_file_path, updated_file_path)
        id = js["id"]
        url = f"https://novyyloans.ntlstaging.co.uk/api/applications?id={id}&filename={updated_file_name}"

        response = requests.request("POST", url)

        print(response.status_code)
        print('**********')
    except Exception as e:
        print(e)
        url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={e}"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        pass
