# import uuid
# import datetime
#
# # Input strings
# string1 = "user1234"
# string2 = str(datetime.datetime.now().strftime("%H:%M:%S"))
# print(string2)
# # Create a unique ID
# unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, string1 + string2))
#
# # Output the unique ID
# print(unique_id)
# # f9fc09e1-6058-5717-bb90-d5859c54242a

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
# chrome_options.add_argument('--headless=old')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
download_dir = "E:\\takshil\\quantum_pdf\\"
# download_dir = "/var/www/novyy-dev/novyyloans/storage/app/public/qmlApplications/"
# download_dir = "/var/www/novyy-dev/Novyy/storage/app/public/qmlApplications/"
# download_dir = "/home/ubuntu/storage/loan-applications/"

# download_dir = "D:\\khushali\\pdf\\"
driver.execute_cdp_cmd("Page.setDownloadBehavior", {
    "behavior": "allow",
    "downloadPath": download_dir
})

print('************** started ****************')
# url = "https://novyyloans.ntlstaging.co.uk/api/applications"
# response = requests.request("GET", url)
with open('jsn.json', 'r') as json_file:
    jss = json.load(json_file)

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
        try:
            error_log = driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
            print(error_log)
        except:
            error_log = ''
            pass
        if error_log:
            print('field missing or error : ' + error_log)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break

        purchace_new = js['purchace_new']
        # if purchace_new == 'Yes':
        if 'Yes' in purchace_new:
            purchace_new = driver.find_element(By.XPATH, '//*[contains(text(),"PURCHASE a new property")]/..').click()
        else:
            purchace_new = driver.find_element(By.XPATH, '//*[contains(text(),"REMORTGAGE an existing property")]/..').click()
        try:
            error_log = driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
            print(error_log)
        except:
            error_log = ''
            pass
        if error_log:
            print('field missing or error : ' + error_log)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break

        first_time = js['first_time']
        # if first_time == 'Yes':
        if 'Yes' in first_time:
            first_time = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
        else:
            first_time = driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()
        try:
            error_log = driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
            print(error_log)
        except:
            error_log = ''
            pass
        if error_log:
            print('field missing or error : ' + error_log)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break

        plan_occupy = js['plan_occupy']
        # if  plan_occupy == "yes":
        if  'Yes' in plan_occupy:
            plan_occupy = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
        else:
            plan_occupy = driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()
        try:
            error_log = driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
            print(error_log)
        except:
            error_log = ''
            pass
        if error_log:
            print('field missing or error : ' + error_log)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break

        try:
            # btl_properties = js['btl_property']
            # if 'Yes' in btl_properties:
            btl_properties = driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
        except:
            pass


        service = js['service']
        # if  service == "Advised":
        if "Advised" in service:
            service = driver.find_element(By.XPATH, '//*[contains(text(),"Advised")]/..').click()#Advised
        else:
            service = driver.find_element(By.XPATH, '//*[contains(text(),"Information Only")]/..').click()
        try:
            error_log = driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
            print(error_log)
        except:
            error_log = ''
            pass
        if error_log:
            print('field missing or error : ' + error_log)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break

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
            sic_code = driver.find_element(By.XPATH, '//*[@id="Company_SICCode"]')
            sic_code_js = js['sic_code']
            sic_code.send_keys(sic_code_js)
            # deopdown = driver.find_element(By.XPATH, f'//*[contains(text(),"{sic_code_js}")]').click()
            # print(deopdown)
            # a = f'//*[contains(text(),"{sic_code_js}")]'
            # print(a)
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
            city = driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_AddressCity"]')
            city.send_keys(js['city'])
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
            security_city = driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressCity"]')
            security_city.send_keys(js['security_city'])
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
            security_purchace_date = driver.find_element(By.XPATH, '//*[@name="Mortgage.PurchaseDate_Date"]')
            security_purchace_date.send_keys(js['purchace_date'])
        except:
            pass

        try:
            security_estimated_value_of_property = driver.find_element(By.XPATH, '//*[@name="Mortgage.EstimatedValue"]')
            security_estimated_value_of_property.send_keys(js['security_purchase_price'])
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
            previous_city = driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressCity"]')
            previous_city.send_keys(js['previous_city'])
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

        try:
            error_log_page1 = driver.find_element(By.XPATH, '//*[@class="help-block"]/../label[1]').text
            print(error_log_page1)
        except:
            error_log_page1 = ''
            pass
        if error_log_page1:
            print('field missing or error : ' + error_log_page1)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_page1}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break

        print('****** first page done *******')
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

        try:
            satisfied_default = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Satisfied Defaults")]/../..//*[contains(text(),"No defaults within last 24 months")]/../input').click()

            satisfied_ccjs = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Satisfied CCJs")]/../..//*[contains(text(),"No CCJs")]/../input').click()

            unsatisfied_ccjs = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Unsatisfied CCJ/Defaults")]/../..//*[contains(text(),"None")]/../input').click()

            mortgage_arrears = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Mortgage Arrears")]/../..//*[contains(text(),"No missed mortgage")]/../input').click()

            payment_arrears = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payment Arrears")]/../..//*[contains(text(),"No missed payments")]/../input').click()

            payment_holidays = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payment Holidays")]/../..//*[contains(text(),"No")]/../input').click()

            payday_loans = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payday Loans")]/../..//*[contains(text(),"None")]/../input').click()

            bankruptcy = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Bankruptcy")]/../..//*[contains(text(),"No")]/../input').click()

            iva = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"IVA - Individual and Company")]/../..//*[contains(text(),"No")]/../input').click()

            administration_order = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Administration Orders")]/../..//*[contains(text(),"No")]/../input').click()

            payment_arrangements = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payment Arrangements")]/../..//*[contains(text(),"No")]/../input').click()

            repossessions = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Repossessions")]/../..//*[contains(text(),"No")]/../input').click()

            debt_relief_orders = driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Debt Relief Orders")]/../..//*[contains(text(),"No")]/../input').click()
        except:
            pass

        select_product = driver.find_element(By.XPATH, '//*[contains(text(),"Select product ")]').click()
        time.sleep(5)

        print('****** second page done *******')
        # '//*[@class="well no-padding "]//*[contains(text(),"Satisfied Defaults")]/../..//*[contains(text(),"No defaults within last 24 months")]/../input'
        #*******************************************************************************************************#

        #********************************************* (page 3) ********************************************#
        try:
            number_of_loan = driver.find_element(By.XPATH,'//*[@id="Product_NumberOfYearsToRepay"]')
            number_of_loan.clear()
            time.sleep(6)
            number_of_loan.send_keys(js['numner_of_year_to_repay'])
        except:
            pass
        time.sleep(3)
        # driver.refresh()

        try:
            fees = driver.find_element(By.XPATH, '//*[@id="Product_ProductFeePaymentType"]')
            fees.send_keys(js['fees'])
        except:
            pass
        time.sleep(6)

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

        # driver.refresh()

        try:
            error_log_page3 = driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
            print(error_log_page3)
        except:
            error_log_page3 = ''
            pass
        if error_log_page3:
            print('field missing or error : ' + error_log_page3)
            url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_page3}"
            payload = {}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
            break
        print('****** third page done *******')
        #************************************************************************************************************#

        continue_application = driver.find_element(By.XPATH, '//*[contains(text(),"Continue application")]').click()
        time.sleep(3)
        print('continue')

        next = driver.find_element(By.XPATH, '//*[contains(text(),"Next")]').click()
        time.sleep(3)
        print('next')

        main_url = driver.current_url
        #-------------------- other income -----------------#
        try:
            driver.find_element(By.XPATH, '//*[contains(text(),"Other Income")]/../..').click()
            time.sleep(3)

            try:
                other_inc_details1 = driver.find_element(By.XPATH, '//*[@class="form-control otherIncome1"]')
                other_inc_details1.send_keys(js['details'])
            except:
                pass
            try:
                other_inc_amount1 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount1"]')
                other_inc_amount1.send_keys(js['amount'])
            except:
                pass
            try:
                other_inc_frequency1 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency1"]')
                other_inc_frequency1.send_keys(js['frequency'])
            except:
                pass
            try:
                other_inc_guarantee1 = js['guaranteed']
                if other_inc_guarantee1 == 'Yes':
                    other_inc_guarantee1 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed1"]/../span[3]').click()
                else:
                    pass
            except:
                pass

            try:
                other_inc_details2 = driver.find_element(By.XPATH, '//*[@class="form-control otherIncome2"]')
                other_inc_details2.send_keys(js['details1'])
            except:
                pass
            try:
                other_inc_amount2 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount2"]')
                other_inc_amount2.send_keys(js['amount1'])
            except:
                pass
            try:
                other_inc_frequency2 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency2"]')
                other_inc_frequency2.send_keys(js['frequency1'])
            except:
                pass
            try:
                other_inc_guarantee2 = js['guaranteed1']
                if other_inc_guarantee2 == 'Yes':
                    other_inc_guarantee2 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed2"]/../span[3]').click()
                else:
                    pass
            except:
                pass

            try:
                other_inc_details3 = driver.find_element(By.XPATH, '//*[@class="form-control otherIncome3"]')
                other_inc_details3.send_keys(js['details2'])
            except:
                pass
            try:
                other_inc_amount3 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount3"]')
                other_inc_amount3.send_keys(js['amount2'])
            except:
                pass
            try:
                other_inc_frequency3 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency3"]')
                other_inc_frequency3.send_keys(js['frequency2'])
            except:
                pass
            try:
                other_inc_guarantee3 = js['guaranteed2']
                if other_inc_guarantee3 == 'Yes':
                    other_inc_guarantee3 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed3"]/../span[3]').click()
                else:
                    pass
            except:
                pass

            try:
                other_inc_details4 = driver.find_element(By.XPATH, '//*[@class="form-control otherIncome4"]')
                other_inc_details4.send_keys(js['details3'])
            except:
                pass
            try:
                other_inc_amount4 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount4"]')
                other_inc_amount4.send_keys(js['amount3'])
            except:
                pass
            try:
                other_inc_frequency4 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency4"]')
                other_inc_frequency4.send_keys(js['frequency3'])
            except:
                pass
            try:
                other_inc_guarantee4 = js['guaranteed3']
                if other_inc_guarantee4 == 'Yes':
                    other_inc_guarantee4 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed4"]/../span[3]').click()
                else:
                    pass
            except:
                pass

            try:
                other_inc_details5 = driver.find_element(By.XPATH, '//*[@class="form-control otherIncome5"]')
                other_inc_details5.send_keys(js['details4'])
            except:
                pass
            try:
                other_inc_amount5 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount5"]')
                other_inc_amount5.send_keys(js['amount4'])
            except:
                pass
            try:
                other_inc_frequency5 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency5"]')
                other_inc_frequency5.send_keys(js['frequency4'])
            except:
                pass
            try:
                other_inc_guarantee5 = js['guaranteed4']
                if other_inc_guarantee5 == 'Yes':
                    other_inc_guarantee5 = driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed5"]/../span[3]').click()
                else:
                    pass
            except:
                pass


            other_inc_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(3)

            try:
                error_log_otherinc = driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]')
                error_log_other_inc = error_log_otherinc.get_attribute('for')
                print(error_log_other_inc)
            except:
                error_log_other_inc = ''
                pass
            if error_log_other_inc:
                print('field missing or error : ' + error_log_other_inc)
                url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_other_inc}"
                payload = {}
                headers = {}
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                break

            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('OTHER INCOME not found or error')
            pass
        #---------------------------------------------------#

        #----------------- asset -----------------------#
        try:
            driver.find_element(By.XPATH, '//span[contains(text(),"Assets")]/../..').click()
            time.sleep(3)
            asset_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(3)
            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('assets not found or error')
            pass
        #-----------------------------------------------#

        #------------------ commitments -----------------#
        try:
            driver.find_element(By.XPATH, '//*[contains(text(),"Commitments")]/../..').click()
            time.sleep(3)
            commitment_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(3)
            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('commitments not found or error')
            pass
        #------------------------------------------------#

        #------------------- property -------------------#
        try:
            driver.find_element(By.XPATH, '//*[contains(text(),"Properties ")]/../..').click()
            time.sleep(3)

            driver.find_element(By.XPATH, '//*[@id="Property_HaveAnyBuyToLetProperties"]/../span[3]').click()

            try:
                number_of_own_blt_properties = driver.find_element(By.XPATH, '//*[@id="Property_NoOfBuyToLetProperties"]')
                number_of_own_blt_properties.clear()
                number_of_own_blt_properties.send_keys(js['number_of_own_blt_properties'])
            except:
                pass

            try:
                total_value_of_portfolio = driver.find_element(By.XPATH, '//*[@id="Property_TotalValueOfPortfolio"]')
                total_value_of_portfolio.send_keys(js['total_value_of_portfolio'])
            except:
                pass

            try:
                total_monthly_rent = driver.find_element(By.XPATH, '//*[@id="Property_TotalMonthlyRent"]')
                total_monthly_rent.send_keys(js['total_monthly_rent'])
            except:
                pass

            try:
                total_mortgage_balances_outstanding_portfolio = driver.find_element(By.XPATH, '//*[@id="Property_TotalMortgageBalance"]')
                total_mortgage_balances_outstanding_portfolio.send_keys(js['total_mortgage_balances_outstanding_portfolio'])
            except:
                pass

            portfolio_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(3)

            try:
                error_log_property = driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                print(error_log_property)
            except:
                error_log_property = ''
                pass
            if error_log_property:
                print('field missing or error : ' + error_log_property)
                url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_property}"
                payload = {}
                headers = {}
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                break

            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('property not found or error')
            pass
        #----------------------------------------------#

        #-------------------- product ------------------#
        try:
            driver.find_element(By.XPATH, '//span[contains(text(),"Product")]/../..').click()
            time.sleep(3)
            product_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(3)
            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('product not found or errror')
            pass
        #------------------------------------------------#

        # -------------------- personal_details ------------------#
        try:
            driver.find_element(By.XPATH, '//span[contains(text(),"Personal Details ")]/../..').click()
            time.sleep(3)

            try:
                retire_age = driver.find_element(By.XPATH, '//*[@name="Applicant.RetirementAge"]')
                retire_age.send_keys(js['retirement_age'])
            except:
                pass

            try:
                merital_status = driver.find_element(By.XPATH, '//*[@name="Applicant.MaritalStatus"]')
                merital_status.send_keys(js['marital_status'])
            except:
                pass

            personal_details_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(4)

            try:
                error_log_personal_details = driver.find_element(By.XPATH, '//*[@class="help-block"]/../label[1]').text
                print(error_log_personal_details)
            except:
                error_log_personal_details = ''
                pass
            if error_log_personal_details:
                print('field missing or error : ' + error_log_personal_details)
                url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_personal_details}"
                payload = {}
                headers = {}
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                break

            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('personal details not found or error')
        # ------------------------------------------------#

        # -------------------- property type ------------------#
        try:
            driver.find_element(By.XPATH, '//span[contains(text(),"Property type ")]/../..').click()
            time.sleep(3)

            try:
                epc_rating = driver.find_element(By.XPATH, '//*[@id="Security_EnergyPerformanceCertificate"]')
                epc_rating.send_keys(js['epc_rating'])
            except:
                pass

            # provide_details = driver.find_element(By.XPATH, '//*[@id="Security_FullVacantPossessionDetails"]')
            # # provide_details.send_keys('abc')
            # provide_details.send_keys(js['share_of_freehold_details'])

            try:
                lift = js['is_there_lift']
                if lift == 'Yes':
                    istherelift = driver.find_element(By.XPATH, '//*[contains(text(),"Is there a lift?")]/../div/div/div/span[2]').click()
                else:
                    pass
            except:
                pass

            try:
                garage = js['is_there_garage']
                if garage == 'Yes':
                    istheregarage= driver.find_element(By.XPATH, '//*[contains(text(),"Is there a Garage?")]/../div/div/div/span[2]').click()
                else:
                    pass
            except:
                pass

            try:
                balcony = js['is_flat_accessed_via_balcony']
                if balcony == 'Yes':
                    istherebalcony = driver.find_element(By.XPATH, '//*[contains(text(),"Is the Flat accessed via a balcony or deck?")]/../div/div/div/span[2]').click()
                else:
                    pass
            except:
                pass

            try:
                property_licence = js['local_authority_private_rented_property_licence']
                if property_licence == 'Yes':
                    isproperty_licence = driver.find_element(By.XPATH, "//*[contains(text(),'Local Authority Private Rented Property Licence')]/../div/div/div/span[2]").click()
                    licence_type = driver.find_element(By.XPATH, '//*[@id="Security_PropertyLicence"]')
                    licence_type.send_keys('property_licence')
                else:
                    pass
            except:
                pass

            try:
                commercial_premises = js['is_adjacent_to_commercial_premises']
                if commercial_premises == 'Yes':
                    commercial_premises = driver.find_element(By.XPATH, "//*[contains(text(),'Is the flat above or adjacent to commercial premises')]/../div/div/div/span[2]").click()
                    commercial_premises_details = driver.find_element(By.XPATH, '//*[@id="Security_FlatAboveCommercialPremisesDetails"]')
                    commercial_premises_details.send_keys('commercial_premises_details')
                else:
                    pass
            except:
                pass

            try:
                property_new = js['is_property_new']
                if property_new == 'Yes':
                    isproperty_new = driver.find_element(By.XPATH, '//*[contains(text(),"Is the Property a new Build/new Conversion?")]/../div/div/div/span[2]').click()
                    time.sleep(1)
                    course_construction = js['is_property_in_course_of_construction']
                    if course_construction == 'Yes':
                        iscourse_construction = driver.find_element(By.XPATH, '//*[contains(text(),"Is the property in the course of construction?")]/../div/div/div/span[2]').click()
                    else:
                        pass
                else:
                    pass
            except:
                pass

            try:
                standerd_construction = js['is_property_of_standard_construction']
                if standerd_construction == 'No':
                    isstanderd_construction = driver.find_element(By.XPATH, '//*[contains(text(),"Is the Property of Standard Construction?")]/../div/div/div/span[2]').click()
                    construction_details = driver.find_element(By.XPATH, '//*[@name="Security.ConstructionDetails"]')
                    construction_details.send_keys(js['construction_details'])
                else:
                    pass
            except:
                pass

            try:
                if js['security_property_tenure'] == 'Leasehold':
                    service_charge = driver.find_element(By.XPATH, '//*[@name="Security.ServiceCharge"]')
                    service_charge.send_keys(js['service_charge'])

                    ground_rent = driver.find_element(By.XPATH, '//*[@name="Security.GroundRent"]')
                    ground_rent.send_keys(js['ground_rent'])

                    remaining_lease_year = driver.find_element(By.XPATH, '//*[@name="Security.UnexpiredRemainingLease"]')
                    remaining_lease_year.send_keys(js['remaining_lease_year'])

                    is_lease_extended = js['is_lease_extended']
                    if is_lease_extended == 'Yes':
                        is_lease_extended = driver.find_element(By.XPATH, '//*[@id="Security_IsExtendedLease"]/../span[3]').click()
                        lease_term = driver.find_element(By.XPATH, '//*[@name="Security.ExtendedLease"]')
                        lease_term.send_keys(js['current_lease_years'])
                    else:
                        pass

                    purchasing_share_of_freehold = js['purchasing_share_of_freehold']
                    if purchasing_share_of_freehold == 'Yes':
                        purchasing_share_of_freehold = driver.find_element(By.XPATH, '//*[@id="Security_PurchaseShareOfFreehold"]/../span[3]').click()
                        share_of_freehold_details = driver.find_element(By.XPATH, '//*[@name="Security.PurchaseShareOfFreeholdDetails"]')
                        share_of_freehold_details.send_keys(js['share_of_freehold_details'])
                    else:
                        pass
            except:
                pass

            try:
                is_used_for_business_purposes = js['is_used_for_business_purposes']
                if is_used_for_business_purposes == 'Yes':
                    is_used_for_business_purposes = driver.find_element(By.XPATH, '//*[@id="Security_BusinessPurpose"]/../span[3]').click()
                    business_purposes_details = driver.find_element(By.XPATH, '//*[@name="Security.BusinessPurposeDetails"]')
                    business_purposes_details.send_keys(js['business_purposes_details'])
                else:
                    pass
            except:
                pass

            try:
                is_there_occupancy_restriction = js['is_there_occupancy_restriction']
                if is_there_occupancy_restriction == 'Yes':
                    is_there_occupancy_restriction = driver.find_element(By.XPATH, '//*[@id="Security_OccupancyRestrictions"]/../span[3]').click()
                    occupancy_restriction_details = driver.find_element(By.XPATH, '//*[@name="Security.OccupancyRestrictionDetails"]')
                    occupancy_restriction_details.send_keys(js['occupancy_restriction_details'])
                else:
                    pass
            except:
                pass

            try:
                is_full_vacant_possession = js['is_full_vacant_possession']
                if is_full_vacant_possession == 'Yes':
                    is_full_vacant_possession = driver.find_element(By.XPATH, '//*[@id="Security_FullVacantPossession"]/../span[3]').click()
                else:
                    pass
                try:
                    full_vacant_possession_details = driver.find_element(By.XPATH, '//*[@name="Security.FullVacantPossessionDetails"]')
                    full_vacant_possession_details.send_keys(js['full_vacant_possession_details'])
                except:
                    pass
            except:
                pass

            try:
                is_used_other_than_btl_details = js['is_used_other_than_btl_details']
                if is_used_other_than_btl_details == 'Yes':
                    is_used_other_than_btl_details = driver.find_element(By.XPATH, '//*[@id="Security_OtherThanBTL"]/../span[3]').click()
                    other_than_btl_details = driver.find_element(By.XPATH, '//*[@name="Security.OtherThanBTLDetails"]')
                    other_than_btl_details.send_keys(js['other_than_btl_details'])
                else:
                    pass
            except:
                pass

            try:
                buying_under_purchase_scheme = js['buying_under_purchase_scheme']
                if buying_under_purchase_scheme == 'yes':
                    buying_under_purchase_scheme = driver.find_element(By.XPATH, '//*[@id="Security_BuyingUnderPurchaseScheme"]/../span[3]').click()
                    under_purchase_scheme_details = driver.find_element(By.XPATH, '//*[@name="Security.BuyingUnderPurchaseSchemeDetails"]')
                    under_purchase_scheme_details.send_keys(js['under_purchase_scheme_details'])
                else:
                    pass
            except:
                pass

            try:
                is_receipt_discount_details = js['is_receipt_discount_details']
                if is_receipt_discount_details == "Yes":
                    is_receipt_discount_details = driver.find_element(By.XPATH, '//*[@id="Security_ReceiptOfAnyDiscount"]/../span[3]').click()
                    receipt_discount_details = driver.find_element(By.XPATH, '//*[@name="Security.ReceiptOfDiscountDetails"]')
                    receipt_discount_details.send_keys(js['receipt_discount_details'])
                else:
                    pass
            except:
                pass

            try:
                is_let_family_member = js['is_let_family_member']
                if is_let_family_member == 'Yes':
                    is_let_family_member = driver.find_element(By.XPATH, '//*[@id="Security_LetToFamilyMember"]/../span[3]').click()
                    let_family_member_details = driver.find_element(By.XPATH, '//*[@name="Security.LetToFamilyMemberDetails"]')
                    let_family_member_details.send_keys(js['let_family_member_details'])
                else:
                    pass
            except:
                pass

            try:
                is_property_tenanted = js['is_property_tenanted']
                if is_property_tenanted == "Yes":
                    is_property_tenanted = driver.find_element(By.XPATH, '//*[@id="Security_IsPropertyTenanted"]/../span[3]').click()
                else:
                    pass
            except:
                pass

            try:
                notes = driver.find_element(By.XPATH, '//*[@id="Security_SecurityNotes"]')
                notes.send_keys(js['notes'])
            except:
                pass

            try:
                number_of_floors = driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfFloors"]')
                number_of_floors.clear()
                number_of_floors.send_keys(js['number_of_floors'])
            except:
                pass

            try:
                number_of_bedrooms = driver.find_element(By.XPATH, '//*[@id="Security_FlatNumberOfBedrooms"]')
                number_of_bedrooms.clear()
                number_of_bedrooms.send_keys(js['number_of_bedrooms'])
            except:
                pass

            try:
                number_of_livingrooms = driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfLivingRooms"]')
                number_of_livingrooms.clear()
                number_of_livingrooms.send_keys(js['number_of_living_rooms'])
            except:
                pass

            try:
                number_of_kitchens = driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfKitchens"]')
                number_of_kitchens.clear()
                number_of_kitchens.send_keys(js['number_of_kitchens'])
            except:
                pass

            try:
                number_of_bathrooms = driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfBathrooms"]')
                number_of_bathrooms.clear()
                number_of_bathrooms.send_keys(js['number_of_bathrooms'])
            except:
                pass

            try:
                number_of_tenants = driver.find_element(By.XPATH, '//*[@id="Security_TenantsOnTenancyAgreement"]')
                number_of_tenants.clear()
                number_of_tenants.send_keys(js['number_of_tenants'])
            except:
                pass

            try:
                number_of_tenancy_agreements = driver.find_element(By.XPATH, '//*[@id="Security_TenancyAgreementsGranted"]')
                number_of_tenancy_agreements.clear()
                number_of_tenancy_agreements.send_keys(js['number_of_tenancy_agreements'])
            except:
                pass

            try:
                number_of_floors_in_block = driver.find_element(By.XPATH, '//*[@id="Security_FlatNumberOfFloors"]')
                number_of_floors_in_block.clear()
                number_of_floors_in_block.send_keys(js['number_of_floors_in_block'])
            except:
                pass

            try:
                floor_number = driver.find_element(By.XPATH, '//*[@id="Security_FloorFlatSituated"]')
                floor_number.clear()
                floor_number.send_keys(js['floor_number'])
            except:
                pass

            property_type_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(2)

            try:
                error_log_property_type = driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                print(error_log_property_type)
            except:
                error_log_property_type = ''
                pass
            if error_log_property_type:
                print('field missing or error : ' + error_log_property_type)
                url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_property_type}"
                payload = {}
                headers = {}
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                break

            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except Exception as e:
            print(e)
            print('property type not found or error')
            pass
        # ------------------------------------------------#

        #-------------------- loan -----------------------#
        try:
            driver.find_element(By.XPATH, '//span[@class="title"][contains(text(),"Loan ")]/../..').click()
            time.sleep(3)

            try:
                deposit_come_from = driver.find_element(By.XPATH, '//*[@id="Mortgage_DepositComeFrom"]')
                deposit_come_from.send_keys(js['deposit_come_from'])
            except:
                pass

            try:
                exit_strategy = driver.find_element(By.XPATH, '//*[@id="Mortgage_ExitStrategy"]')
                exit_strategy.send_keys(js['exit_strategy'])
            except:
                pass

            try:
                valuation_contact_person = driver.find_element(By.XPATH, '//*[@id="Mortgage_ValuationContact"]')
                valuation_contact_person.send_keys(js['valuation_contact_person'])
            except:
                pass

            try:
                valuation_contact_person_number = driver.find_element(By.XPATH, '//*[@id="Mortgage_TelephoneNumber"]')
                valuation_contact_person_number.send_keys(js['valuation_contact_person_number'])
            except:
                pass

            try:
                valuation_contact_name = driver.find_element(By.XPATH, '//*[@id="Mortgage_ContactName"]')
                valuation_contact_name.send_keys(js['valuation_contact_name'])
            except:
                pass

            try:
                is_private_sale = js['is_private_sale']
                if is_private_sale == "Yes":
                    is_private_sale = driver.find_element(By.XPATH, '//*[@id="Mortgage_PrivateSale"]/../span[3]').click()
                    private_sale_details = driver.find_element(By.XPATH, '//*[@id="Mortgage_PrivateSaleDetails"]')
                    private_sale_details.send_keys(js['private_sale_details'])
                else:
                    pass
            except:
                pass

            try:
                proposed_tenants = driver.find_element(By.XPATH, '//*[@id="Mortgage_ProposedTenants"]')
                proposed_tenants.send_keys(js['proposed_tenants'])
            except:
                pass

            try:
                lease_type = driver.find_element(By.XPATH, '//*[@id="Mortgage_LeaseType"]')
                lease_type.send_keys(js['lease_type'])
            except:
                pass

            try:
                tenancy_agreement_months = driver.find_element(By.XPATH, '//*[@id="Mortgage_AnticipatedTenancyAgreement"]')
                tenancy_agreement_months.clear()
                tenancy_agreement_months.send_keys(js['tenancy_agreement_months'])
            except:
                pass

            try:
                is_distressed_sale = js['is_distressed_sale']
                if is_distressed_sale == 'Yes':
                    is_distressed_sale = driver.find_element(By.XPATH, '//*[@id="Mortgage_IsDistressedSale"]/../span[3]').click()
                    distressed_sale_details = driver.find_element(By.XPATH, '//*[@id="Mortgage_IsDistressedSaleDetails"]')
                    distressed_sale_details.send_keys(js['distressed_sale_details'])
                else:
                    pass
            except:
                pass

            try:
                is_purchased_below_market_value = js['is_purchased_below_market_value']
                if is_purchased_below_market_value == "Yes":
                    is_purchased_below_market_value = driver.find_element(By.XPATH, '//*[@id="Mortgage_IsPurchasedBelowMarketValue"]/../span[3]').click()
                    purchased_below_market_value_details = driver.find_element(By.XPATH, '//*[@id="Mortgage_IsPurchasedBelowMarketDetails"]')
                    purchased_below_market_value_details.send_keys(js['purchased_below_market_value_details'])
                else:
                    pass
            except:
                pass

            try:
                is_government_initiative_purchased = js['is_government_initiative_purchased']
                if is_government_initiative_purchased == 'Yes':
                    is_government_initiative_purchased = driver.find_element(By.XPATH, '//*[@id="Mortgage_IsGovermentInitiative"]/../span[3]').click()
                    government_initiative_purchased_details = driver.find_element(By.XPATH, '//*[@id="Mortgage_GovernmentInitiativeDetails"]')
                    government_initiative_purchased_details.send_keys(js['government_initiative_purchased_details'])
                else:
                    pass
            except:
                pass

            try:
                is_ready_to_let_out = js['is_ready_to_let_out']
                if is_ready_to_let_out == 'No':
                    is_ready_to_let_out = driver.find_element(By.XPATH, '//*[@id="Mortgage_IsReadyToSell"]/../span[3]').click()
                    ready_to_let_out_details = driver.find_element(By.XPATH, '//*[@name="Mortgage.IsReadyToSellDetails"]')
                    ready_to_let_out_details.send_keys(js['ready_to_let_out_details'])
                else:
                    pass
            except:
                pass

            try:
                vendor_name = driver.find_element(By.XPATH, '//*[@id="Mortgage_VendorsName"]')
                vendor_name.send_keys(js['vendor_name'])
            except:
                pass

            loan_next = driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
            time.sleep(3)

            try:
                error_log_loan = driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                print(error_log_loan)
            except:
                error_log_loan = ''
                pass
            if error_log_loan:
                print('field missing or error : ' + error_log_loan)
                url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={'field missing or error : ' + error_log_loan}"
                payload = {}
                headers = {}
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                break

            driver.get(main_url)
            driver.refresh()
            time.sleep(2)
        except:
            print('loan not found or error')
        #-------------------------------------------------#

        driver.get(main_url)
        driver.refresh()
        time.sleep(3)

        unique_id_file_name = str(uuid.uuid5(uuid.NAMESPACE_DNS, js['email'] + str(datetime.datetime.now().strftime("%H:%M:%S"))))
        print(unique_id_file_name)

        download = driver.find_element(By.XPATH, '//*[contains(text(),"Reissue DIP")]')
        before_download = set(os.listdir(download_dir))

        # Click the download button to start downloading
        download.click()
        time.sleep(8)
        print('download done')

        # Wait for a new file to appear in the download directory
        new_file_name = None
        while not new_file_name:
            time.sleep(1)  # Check every second for a new file
            after_download = set(os.listdir(download_dir))
            new_files = after_download - before_download  # Get the new file(s)
            print(new_files)
            # If there's a new file, get its name
            if new_files:
                print('get new file')
                new_file_name = new_files.pop()
            else:
                break

        # Wait until the file is fully downloaded (Chrome adds .crdownload until the download is complete)
        new_file_path = os.path.join(download_dir, new_file_name)
        while new_file_name.endswith(".crdownload") or not os.path.exists(new_file_path):
            time.sleep(1)

        # Define the new file name
        updated_file_name = unique_id_file_name+'.pdf'  # Replace with your desired file name
        updated_file_path = os.path.join(download_dir, updated_file_name)
        print(updated_file_path)
        print('file update done')

        # Rename the file
        os.rename(new_file_path, updated_file_path)
        print('****** download done *******')
        id = js["id"]
        url = f"https://novyyloans.ntlstaging.co.uk/api/applications?id={id}&filename={updated_file_name}"

        response = requests.request("POST", url)

        print(response.status_code)
        print('****** final update done *******')
        print('**********')
    except Exception as e:
        print(e)
        url = f"https://novyyloans.ntlstaging.co.uk/api/applications/logs?id={js['id']}&email={js['email']}&message={e}"
        payload = {}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        pass


driver.quit()