import os
import json
import time
import datetime
import uuid

from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
load_dotenv()

class ApplicationProcessor:
    def __init__(self, download_dir, chrome_options=None):
        self.download_dir = download_dir
        self.driver = self.init_driver(chrome_options)
        # self.api_url = "https://novyyloans.ntlstaging.co.uk/api/applications"
        print(os.getenv('json_url'))
        self.api_url = os.getenv('json_url')

    def init_driver(self, chrome_options=None):
        if chrome_options is None:
            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-software-rasterizer")
            chrome_options.add_argument("--disable-setuid-sandbox")
        # custom_cache_path = '/home/ubuntu/quantum/quantum/'
        # os.environ['WDM_LOCAL'] = custom_cache_path
        #
        # # Ensure the directory exists
        # if not os.path.exists(custom_cache_path):
        #     os.makedirs(custom_cache_path)
        #
        # print(f"WebDriverManager cache directory: {custom_cache_path}")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.maximize_window()
        driver.execute_cdp_cmd("Page.setDownloadBehavior", {
            "behavior": "allow",
            "downloadPath": self.download_dir
        })
        return driver

    def fetch_applications(self):
        response = requests.get(self.api_url)
        print('response: '+response.text)
        return json.loads(response.text)
        # with open('jsn.json', 'r') as json_file:
        #     print(json_file)
        #     return json.load(json_file)

    def login(self, username, password, url):
        self.driver.get(url)
        time.sleep(3)
        try:
            self.driver.find_element(By.ID, 'Email').send_keys(username)
            self.driver.find_element(By.ID, 'Password').send_keys(password)
            self.driver.find_element(By.XPATH, '//*[@type="submit"]').click()
            time.sleep(2)
        except Exception as e:
            print(f"Login Error: {e}")

    def process_application(self,application):
        try:
            self.select_applicant_type(application)
            # self.fill_form(application)
            value1 = self.fill_form(application)
            self.download_and_upload(application, value1)
        except Exception as e:
            self.log_error(application, str(e), '', '')

    def select_applicant_type(self, application):
        try:
            agree = self.driver.find_element(By.XPATH, '//*[@for="Application_TermsAndCondition"]/../div/div/div//*[contains(text(),"No")]').click()
        except:
            pass
        try:
            time.sleep(2)
            next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default  btnNavRight blueBtn"]').click()
        except:
            pass
        time.sleep(5)
        try:
            lending_type = application['lending_type']
            if lending_type == 'Buy to let mortgage':
                lending_type = self.driver.find_element(By.XPATH, '//*[contains(text(),"Buy to let mortgage")]/..').click()
            else:
                lending_type = self.driver.find_element(By.XPATH, '//*[contains(text(),"Buy to let mortgage")]/..').click()
        except Exception as e:
            print(f"Is the application for a Error: {e}")

        try:
            if application.get('name_of_company'):
                self.driver.find_element(By.XPATH, '//*[contains(text(),"UK Limited Company")]/..').click()
            else:
                self.driver.find_element(By.XPATH, '//*[contains(text(),"Private individual")]/..').click()
        except Exception as e:
            print(f"Applicant Type Selection Error: {e}")

    def fill_form(self, application):
        try:

            # Example filling in a field, repeat for other fields
            number_of_applicants = self.driver.find_element(By.XPATH, '//*[@id="Application_NumberOfApplicants"]')
            number_of_applicants.clear()
            number_of_applicants.send_keys(application['number_of_applicants'])

            next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default  btnNavRight blueBtn"]').click()
            next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default  btnNavRight blueBtn"]').click()

            located_england = application['located_england']
            # if located_england == 'Yes':
            if 'Yes' in located_england:
                located_england = self.driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
            else:
                located_england = self.driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()
            try:
                error_log = self.driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, error_log, '', '')
                sys.exit()

            purchace_new = application['purchace_new']
            # if purchace_new == 'Yes':
            if 'Yes' in purchace_new:
                purchace_new = self.driver.find_element(By.XPATH, '//*[contains(text(),"PURCHASE a new property")]/..').click()
            else:
                purchace_new = self.driver.find_element(By.XPATH, '//*[contains(text(),"REMORTGAGE an existing property")]/..').click()
            try:
                error_log = self.driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, error_log, '', '')
                sys.exit()

            first_time = application['first_time']
            # if first_time == 'Yes':
            if 'Yes' in first_time:
                first_time = self.driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
            else:
                first_time = self.driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()
            try:
                error_log = self.driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, error_log, '', '')
                sys.exit()

            plan_occupy = application['plan_occupy']
            # if  plan_occupy == "yes":
            if 'Yes' in plan_occupy:
                plan_occupy = self.driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
            else:
                plan_occupy = self.driver.find_element(By.XPATH, '//*[contains(text(),"No")]/..').click()
            try:
                error_log = self.driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, error_log, '', '')
                sys.exit()

            try:
                btl_properties = self.driver.find_element(By.XPATH, '//*[contains(text(),"Yes")]/..').click()
            except:
                pass

            service = application['service']
            # if  service == "Advised":
            if "Advised" in service:
                service = self.driver.find_element(By.XPATH, '//*[contains(text(),"Advised")]/..').click()  # Advised
            else:
                service = self.driver.find_element(By.XPATH, '//*[contains(text(),"Information Only")]/..').click()
            try:
                error_log = self.driver.find_element(By.XPATH, '//div[@class="col-xs-12 "]//*[contains(text(), "Sorry...")]/../p[2]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, error_log, '', '')
                sys.exit()

            # *************************** form start(page 1) ******************************** #

            time.sleep(3)
            self.driver.refresh()
            time.sleep(3)

            try:
                company_name = self.driver.find_element(By.XPATH, '//*[@name="Company.RegisteredName"]')
                company_name.send_keys(application['name_of_company'])
            except:
                pass


            reg_no = application['company_registration_number']
            if reg_no:
                try:
                    reg_yes = self.driver.find_element(By.XPATH, '//*[@for="Company_DoYouKnowRegisteredNumber"]/../div/div/div/span[2]').click()
                except:
                    print('form Error : ' + 'is register number not found in form')
                    self.log_error(application, 'is register number not found in form', '', '')
                    sys.exit()
                time.sleep(2)
                comp_no = self.driver.find_element(By.XPATH, '//*[@name="Company.RegisteredNumber"]')
                comp_no.send_keys(application['company_registration_number'])
            else:
                pass

            try:
                sic_code = self.driver.find_element(By.XPATH, '//*[@id="Company_SICCode"]')
                sic_code_js = application['sic_code']
                sic_code.send_keys(sic_code_js)
            except:
                pass

            try:
                comp_postalcode = self.driver.find_element(By.XPATH, '//*[@id="Company_AddressPostCode"]')
                comp_postalcode.send_keys(application['company_postlecode'])
            except:
                pass

            try:
                comp_add = self.driver.find_element(By.XPATH, '//*[@id="Company_AddressLine1"]')
                comp_add.send_keys(application['company_address_line_1'])
            except:
                pass

            try:
                comp_city = self.driver.find_element(By.XPATH, '//*[@name="Company.AddressCity"]')
                comp_city.send_keys(application['company_city'])
            except:
                pass

            try:
                comp_country = self.driver.find_element(By.XPATH, '//*[@id="Company_AddressCountry"]')
                comp_country.send_keys(application['company_country'])
            except:
                pass

            try:
                title = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Title"]')
                title.send_keys(application['title'])
            except:
                pass

            try:
                postlecode = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_AddressPostCode"]')
                postlecode.send_keys(application['postlecode'])
            except:
                pass

            try:
                first_name = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.FirstName"]')
                first_name.send_keys(application['first_name'])
            except:
                pass

            try:
                address_line_1 = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.AddressLine1"]')
                address_line_1.send_keys(application['address_line_1'])
            except:
                pass

            try:
                last_name = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.LastName"]')
                last_name.send_keys(application['last_name'])
            except:
                pass

            try:
                dob = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.DateOfBirth_Date"]')
                dob.send_keys(application['dob'])
            except:
                pass

            try:
                city = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_AddressCity"]')
                city.send_keys(application['city'])
            except:
                pass

            try:
                nationality = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Nationality"]')
                nationality.send_keys(application['nationality'])
            except:
                nationality = ''

            try:
                country = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_AddressCountry"]')
                country.send_keys(application['country'])
            except:
                country = ''

            try:
                employment_status = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_EmploymentClass"]')
                employment_status.send_keys(application['employment_status'])
            except:
                pass

            try:
                residential_status = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_ResidentialStatus"]')
                residential_status.send_keys(application['residential_status'])
            except:
                pass

            try:
                anual_income = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Employment.BasicGrossIncome"]')
                anual_income.send_keys(application['anual_income'])
            except:
                pass

            try:
                date_moved_to_address = self.driver.find_element(By.XPATH,
                                                            '//*[@name="Applicant[0].Applicant.AddressMovedDate_Date"]')
                date_moved_to_address.send_keys(application['date_moved_to_address'])
            except:
                pass

            try:
                marginal_tax_band = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.TaxPayer"]')
                marginal_tax_band.send_keys(application['marginal_tax_band'])
            except:
                pass

            try:
                existing_borrower = application['existing_borrower']
                if existing_borrower == 'Yes':
                    existing_borrower = self.driver.find_element(By.XPATH, '//*[@for="Applicant[0]_Applicant_ExistingLenderRelationship"]/../div/div/div//*[contains(text(),"No")]').click()
                else:
                    pass
            except:
                pass

            try:
                email = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Email"]')
                email.send_keys(application['email'])
            except:
                pass

            try:
                phone_number = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.MobileNumber_Phone"]')
                phone_number.send_keys(application['phone_number'])
            except:
                pass

            try:
                security_property_type = self.driver.find_element(By.XPATH, '//*[@id="Security_PropertyType"]')
                security_property_type.send_keys(application['security_property_type'])
            except:
                pass

            time.sleep(2)
            try:
                popup_button = self.driver.find_element(By.XPATH, '//button[contains(text(),"Ok")]').click()
            except:
                pass

            try:
                security_no_of_unit = self.driver.find_element(By.XPATH, '//*[@id="Security_NumberOfUnits"]')
                security_no_of_unit.clear()
                security_no_of_unit.send_keys(application['security_no_of_unit'])
            except:
                pass

            try:
                number_of_floors_in_block = self.driver.find_element(By.XPATH, '//*[@id="Security_FlatNumberOfFloors"]')
                number_of_floors_in_block.clear()
                number_of_floors_in_block.send_keys(application['number_of_floors_in_block'])
            except:
                pass

            try:
                number_of_letting_rooms = self.driver.find_element(By.XPATH, '//*[@id="Security_NumberOfLettingRooms"]')
                number_of_letting_rooms.clear()
                number_of_letting_rooms.send_keys(application['number_of_letting_rooms'])
            except:
                pass

            try:
                is_adjacent_to_commercial_premises = application['is_adjacent_to_commercial_premises']
                if is_adjacent_to_commercial_premises == 'Yes':
                    is_adjacent_to_commercial_premises = self.driver.find_element(By.XPATH, '//*[@for="Security_FlatAboveCommercial"]/../div/div/div//*[contains(text(),"No")]').click()
                else:
                    pass
            except:
                pass

            try:
                hmo_planning_permission = application['hmo_planning_permission']
                if hmo_planning_permission == 'Yes':
                    hmo_planning_permission = self.driver.find_element(By.XPATH, '//*[@for="Security_HousePlanningPermission"]/../div/div/div//*[contains(text(),"No")]').click()
                else:
                    pass
            except:
                pass

            try:
                commercial_property_detail = self.driver.find_element(By.XPATH, '//*[@id="Security_AdditionalTextCommercialProperty"]')
                commercial_property_detail.send_keys(application['commercial_property_detail'])
            except:
                pass

            try:
                square_meters = self.driver.find_element(By.XPATH, '//*[@id="Security_FlatSquareMetres"]')
                square_meters.send_keys(application['square_meters'])
            except:
                pass

            try:
                security_postalcode = self.driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressPostCode"]')
                security_postalcode.send_keys(application['security_postalcode'])
            except:
                pass

            try:
                security_address = self.driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressLine1"]')
                security_address.send_keys(application['security_address'])
            except:
                pass

            try:
                security_city = self.driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressCity"]')
                security_city.send_keys(application['security_city'])
            except:
                pass

            try:
                security_property_tenure = self.driver.find_element(By.XPATH, '//*[@name="Security.PropertyTenure"]')
                security_property_tenure.send_keys(application['security_property_tenure'])
            except:
                pass

            try:
                remaining_lease_year = self.driver.find_element(By.XPATH, '//*[@name="Security.UnexpiredRemainingLease"]')
                remaining_lease_year.send_keys(application['remaining_lease_year'])
            except:
                pass

            try:
                security_purchase_price = self.driver.find_element(By.XPATH, '//*[@name="Mortgage.PurchasePrice"]')
                security_purchase_price.send_keys(application['security_purchase_price'])
            except:
                pass

            try:
                security_loan_amount = self.driver.find_element(By.XPATH, '//*[@name="Mortgage.LoanRequired"]')
                security_loan_amount.send_keys(application['security_loan_amount'])
            except:
                pass

            try:
                security_rental_income = self.driver.find_element(By.XPATH, '//*[@name="Mortgage.MonthlyRentalIncome"]')
                security_rental_income.send_keys(application['security_rental_income'])
            except:
                pass

            try:
                security_purchace_date = self.driver.find_element(By.XPATH, '//*[@name="Mortgage.PurchaseDate_Date"]')
                security_purchace_date.send_keys(application['purchace_date'])
            except:
                pass

            try:
                security_estimated_value_of_property = self.driver.find_element(By.XPATH, '//*[@name="Mortgage.EstimatedValue"]')
                security_estimated_value_of_property.send_keys(application['security_purchase_price'])
            except:
                pass

            try:
                security_sector_experience = self.driver.find_element(By.XPATH, '//*[@name="Security.SectorExperience"]')
                security_sector_experience.send_keys(application['security_sector_experience'])
            except:
                pass

            try:
                security_built_year = self.driver.find_element(By.XPATH, '//*[@name="Security.PropertyYearBuilt"]')
                security_built_year.send_keys(application['security_built_year'])
            except:
                pass

            # try:
            #     if application['have_valid_warranty'] == 'Yes':
            #         have_valid_warrenty = self.driver.find_element(By.XPATH,'//*[@for="Security_ValidWarranty"]/../div/div/div//*[contains(text(),"No")]').click()
            #     else:
            #         pass
            # except:
            #     pass
            #
            # try:
            #     warranty_scheme = self.driver.find_element(By.XPATH,'//*[@id="Security_WarrantyScheme"]')
            #     warranty_scheme.send_keys(application['warranty_scheme'])
            # except:
            #     pass

            try:
                security_no_of_unit = self.driver.find_element(By.XPATH, '//*[@name="Security.NumberOfUnits"]')
                security_no_of_unit.send_keys(application['security_no_of_unit'])
            except:
                pass

            try:
                security_country = self.driver.find_element(By.XPATH, '//*[@name="Security.PropertyAddressCountry"]')
                security_country.send_keys(application['security_country'])
            except:
                pass

            try:
                if application['have_valid_warranty'] == 'Yes':
                        have_valid_warrenty = self.driver.find_element(By.XPATH,'//*[@for="Security_ValidWarranty"]/../div/div/div//*[contains(text(),"No")]').click()
                else:
                    pass
            except:
                pass

            try:
                warranty_scheme = self.driver.find_element(By.XPATH,'//*[@id="Security_WarrantyScheme"]')
                warranty_scheme.send_keys(application['warranty_scheme'])
            except:
                pass

            try:
                other_warranty_scheme = self.driver.find_element(By.XPATH, '//*[@id="Security_OtherWarrantyScheme"]')
                other_warranty_scheme.send_keys(application['other_warranty_scheme'])
            except:
                pass

            try:
                previous_postalcode = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressPostCode"]')
                previous_postalcode.send_keys(application['previous_postalcode'])
            except:
                pass

            try:
                previous_address = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressLine1"]')
                previous_address.send_keys(application['previous_address'])
            except:
                pass

            try:
                previous_city = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressCity"]')
                previous_city.send_keys(application['previous_city'])
            except:
                pass

            try:
                previous_country = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Previous1AddressCountry"]')
                previous_country.send_keys(application['previous_country'])
            except:
                pass

            try:
                previous_date_moved_to_address = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous1AddressMovedDate_Date"]')
                previous_date_moved_to_address.send_keys(application['previous_date_moved_to_address'])
            except:
                pass

            try:
                contin_btn = self.driver.find_element(By.XPATH, '//*[@id="requestCreditReport"]').click()
            except:
                pass

            try:
                previous2_postalcode = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous2AddressPostCode"]')
                previous2_postalcode.send_keys(application['previous2_postalcode'])
            except:
                pass

            try:
                previous2_address = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous2AddressLine1"]')
                previous2_address.send_keys(application['previous2_address'])
            except:
                pass

            try:
                previous2_country = self.driver.find_element(By.XPATH, '//*[@id="Applicant[0]_Applicant_Previous2AddressCountry"]')
                previous2_country.send_keys(application['previous2_country'])
            except:
                pass

            try:
                previous2_date_moved_to_address = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Applicant.Previous2AddressMovedDate_Date"]')
                previous2_date_moved_to_address.send_keys(application['previous2_date_moved_to_address'])
            except:
                pass

            try:
                contin_btn = self.driver.find_element(By.XPATH, '//*[@id="requestCreditReport"]').click()
            except:
                pass
            try:
                contin_btn = self.driver.find_element(By.XPATH, '//*[@id="requestCreditReport"]').click()
            except:
                pass

            try:
                error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"]/../label[1]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, 'field missing or error : '+error_log, '', '')
                sys.exit()

            print('****** first page done *******')
            # ****************************************************************************************************#


            # ********************************** (page 2) *****************************************#

            time.sleep(5)
            self.driver.refresh()
            time.sleep(5)

            satisfied_default = self.driver.find_element(By.XPATH, '//*[contains(text(),"Satisfied Defaults")]/../..//*[contains(text(),"No defaults within last 24 months")]/../input').click()

            satisfied_ccjs = self.driver.find_element(By.XPATH, '//*[contains(text(),"Satisfied CCJs")]/../..//*[contains(text(),"No CCJs")]/../input').click()

            unsatisfied_ccjs = self.driver.find_element(By.XPATH, '//*[contains(text(),"Unsatisfied CCJ’s/Defaults")]/../..//*[contains(text(),"None")]/../input').click()

            mortgage_arrears = self.driver.find_element(By.XPATH, '//*[contains(text(),"Mortgage Arrears")]/../..//*[contains(text(),"No missed mortgage")]/../input').click()

            payment_arrears = self.driver.find_element(By.XPATH, '//*[contains(text(),"Payment Arrears")]/../..//*[contains(text(),"No missed payments")]/../input').click()

            payment_holidays = self.driver.find_element(By.XPATH, '//*[contains(text(),"Payment Holidays")]/../..//*[contains(text(),"No")]/../input').click()

            payday_loans = self.driver.find_element(By.XPATH, '//*[contains(text(),"Payday Loans")]/../..//*[contains(text(),"None")]/../input').click()

            bankruptcy = self.driver.find_element(By.XPATH, '//*[contains(text(),"Bankruptcy")]/../..//*[contains(text(),"No")]/../input').click()

            iva = self.driver.find_element(By.XPATH, '//*[contains(text(),"IVA - Individual and Company")]/../..//*[contains(text(),"No")]/../input').click()

            administration_order = self.driver.find_element(By.XPATH, '//*[contains(text(),"Administration Orders")]/../..//*[contains(text(),"No")]/../input').click()

            payment_arrangements = self.driver.find_element(By.XPATH, '//*[contains(text(),"Payment Arrangements")]/../..//*[contains(text(),"No")]/../input').click()

            repossessions = self.driver.find_element(By.XPATH, '//*[contains(text(),"Repossessions")]/../..//*[contains(text(),"No")]/../input').click()

            debt_relief_orders = self.driver.find_element(By.XPATH, '//*[contains(text(),"Debt Relief Orders")]/../..//*[contains(text(),"No")]/../input').click()

            try:
                satisfied_default = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Satisfied Defaults")]/../..//*[contains(text(),"No defaults within last 24 months")]/../input').click()

                satisfied_ccjs = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Satisfied CCJs")]/../..//*[contains(text(),"No CCJs")]/../input').click()

                unsatisfied_ccjs = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Unsatisfied CCJ/Defaults")]/../..//*[contains(text(),"None")]/../input').click()

                mortgage_arrears = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Mortgage Arrears")]/../..//*[contains(text(),"No missed mortgage")]/../input').click()

                payment_arrears = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payment Arrears")]/../..//*[contains(text(),"No missed payments")]/../input').click()

                payment_holidays = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payment Holidays")]/../..//*[contains(text(),"No")]/../input').click()

                payday_loans = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payday Loans")]/../..//*[contains(text(),"None")]/../input').click()

                bankruptcy = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Bankruptcy")]/../..//*[contains(text(),"No")]/../input').click()

                iva = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"IVA - Individual and Company")]/../..//*[contains(text(),"No")]/../input').click()

                administration_order = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Administration Orders")]/../..//*[contains(text(),"No")]/../input').click()

                payment_arrangements = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Payment Arrangements")]/../..//*[contains(text(),"No")]/../input').click()

                repossessions = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Repossessions")]/../..//*[contains(text(),"No")]/../input').click()

                debt_relief_orders = self.driver.find_element(By.XPATH, '//*[@class="well no-padding "]//*[contains(text(),"Debt Relief Orders")]/../..//*[contains(text(),"No")]/../input').click()
            except:
                pass

            select_product = self.driver.find_element(By.XPATH, '//*[contains(text(),"Select product ")]').click()
            time.sleep(5)

            print('****** second page done *******')
            # *******************************************************************************************************#

            # ********************************************* (page 3) ********************************************#
            time.sleep(3)
            self.driver.refresh()
            time.sleep(5)

            try:
                number_of_loan = self.driver.find_element(By.XPATH, '//*[@id="Product_NumberOfYearsToRepay"]')
                number_of_loan.clear()
                time.sleep(6)
                number_of_loan.send_keys(application['numner_of_year_to_repay'])
            except:
                pass
            time.sleep(3)

            try:
                fees = self.driver.find_element(By.XPATH, '//*[@id="Product_ProductFeePaymentType"]')
                fees.send_keys(application['fees'])
            except:
                pass
            time.sleep(6)

            try:
                repayment_type = self.driver.find_element(By.XPATH, '//*[@id="Product_LoanRepaymentType"]')
                repayment_type.send_keys(application['repayment_type'])
                time.sleep(6)
            except:
                pass
            time.sleep(3)

            try:
                reason = self.driver.find_element(By.XPATH, '//*[@class="FailedReasons"]/li').text
            except:
                reason = ''
            if reason:
                print('field missing or error : No product found')
                initial_rate = self.driver.find_element(By.XPATH, '//*[@class="productSelection"]/table/tbody/tr//td[@class="td-initialrate"]/span').text
                monthly_payment = self.driver.find_element(By.XPATH, '//*[@class="productSelection"]/table/tbody/tr//td[6]').text
                self.log_error(application, reason, initial_rate, monthly_payment)
                sys.exit()
            else:
                pass

            try:
                product = application['product']
                sel_product = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[@class="selectproduct"]/input').click()
                sel_prod = True
            except:
                try:
                    sel_product = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[@class="selectproduct"]/input').click()
                    sel_prod = False
                except:
                    print('field missing or error : No product found')
                    initial_rate = self.driver.find_element(By.XPATH, '//*[@class="productSelection"]/table/tbody/tr//td[@class="td-initialrate"]/span').text
                    monthly_payment = self.driver.find_element(By.XPATH, '//*[@class="productSelection"]/table/tbody/tr//td[6]').text
                    self.log_error(application, 'field missing or error : No product found', initial_rate, monthly_payment)
                    sys.exit()

            try:
                fix_amount = self.driver.find_element(By.XPATH, '//*[@name="Broker.FixedAmount"]')
                fix_amount.send_keys(application['fix_amount'])
            except:
                pass

            try:
                general_illustration = self.driver.find_element(By.XPATH, '//*[contains(text(),"Generate Illustration")]').click()
                time.sleep(6)
            except:
                pass

            if sel_prod == False:
                name = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[1]').text
                try:
                    erc = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[2]').text
                except:
                    erc = ''
                initial_rate = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[@id="RateText"]/span').text
                reversion_rate = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[4]').text
                apr = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[5]').text
                monthly_payment = self.driver.find_element(By.XPATH, '//*[@id="tableproducts"]/tbody/tr[1]/td[6]').text
            else:
                name = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[1]').text
                try:
                    erc = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[2]').text
                except:
                    erc = ''
                initial_rate = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[@id="RateText"]/span').text
                reversion_rate = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[4]').text
                apr = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[5]').text
                monthly_payment = self.driver.find_element(By.XPATH, f'//*[contains(text(),"{product}")]/../td[6]').text

            ltv = self.driver.find_element(By.XPATH, '//*[@data-field="LTV"]').text
            rental_coverage = self.driver.find_element(By.XPATH, '//*[@data-field="RentalCoverage"]').text

            product_fee = self.driver.find_element(By.XPATH, '//*[@class="ProductFeeText"]').text
            redemption_admin_fee = self.driver.find_element(By.XPATH, '//*[@class="RedemptionAdminFeeText"]').text
            estimated_solicitor_fee = self.driver.find_element(By.XPATH, '//*[@class="SolicitorFeeText"]').text
            broker_fee_payable_by_borrower = self.driver.find_element(By.XPATH, '//*[@class="brokrageByBorrower"]').text
            valuation_fee = self.driver.find_element(By.XPATH, '//*[@id="ValuationFeeText"]').text
            funds_release_fee = self.driver.find_element(By.XPATH, '//*[@class="FundReleaseFeeText"]').text
            building_insurance_admin_fee = self.driver.find_element(By.XPATH, '//*[@class="BuildingsInsuranceAdminFeeText"]').text
            application_fee = self.driver.find_element(By.XPATH, '//*[@class="ApplicationFeeText"]').text

            try:
                general_illustration = self.driver.find_element(By.XPATH, '//*[contains(text(),"Generate Illustration")]').click()
            except:
                pass
            time.sleep(5)

            try:
                error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                print(error_log)
            except:
                error_log = ''
                pass
            if error_log:
                print('field missing or error : ' + error_log)
                self.log_error(application, error_log, '', '')
                sys.exit()

            print('****** third page done *******')
            # ************************************************************************************************************#
            continue_application = self.driver.find_element(By.XPATH, '//*[contains(text(),"Continue application")]').click()
            time.sleep(3)
            print('continue')

            next = self.driver.find_element(By.XPATH, '//*[contains(text(),"Next")]').click()
            time.sleep(3)
            print('next')

            try:
                refrence_number1 = self.driver.find_element(By.XPATH, '//strong[contains(text(),"Ref: ")]/..').text
                refrence_number = ''.join(refrence_number1.replace('Ref: ',''))
            except:
                refrence_number = ''

            main_url = self.driver.current_url
            # -------------------- Company ------------------#
            try:
                self.driver.find_element(By.XPATH, '//span[contains(text(),"company ")]/../..').click()
                time.sleep(3)

                try:
                    company_telephone = self.driver.find_element(By.XPATH, '//*[@id="Company_Telephone"]')
                    company_telephone.send_keys(application['company_telephone'])
                except:
                    pass

                try:
                    company_type = self.driver.find_element(By.XPATH, '//*[@id="Company_Type"]')
                    company_type.send_keys(application['company_type'])
                except:
                    pass

                try:
                    trading_postcode = self.driver.find_element(By.XPATH, '//*[@id="Company_TradingPostcode"]')
                    trading_postcode.send_keys(application['trading_postcode'])
                except:
                    pass

                try:
                    trading_address_line1 = self.driver.find_element(By.XPATH, '//*[@id="Company_TradingAddressLine1"]')
                    trading_address_line1.send_keys(application['trading_address_line1'])
                except:
                    pass

                try:
                    trading_address_line2 = self.driver.find_element(By.XPATH, '//*[@id="Company_TradingAddressLine2"]')
                    trading_address_line2.send_keys(application['trading_address_line2'])
                except:
                    pass

                try:
                    trading_city = self.driver.find_element(By.XPATH, '//*[@id="Company_TradingAddressCity"]')
                    trading_city.send_keys(application['trading_city'])
                except:
                    pass

                try:
                    trading_country = self.driver.find_element(By.XPATH, '//*[@id="Company_TradingAddressCountry"]')
                    trading_country.send_keys(application['trading_country'])
                except:
                    pass

                try:
                    state_your_position = self.driver.find_element(By.XPATH,
                                                              '//*[@id="Applicant[0]_Company_DirectorShareholder"]')
                    state_your_position.send_keys(application['state_your_position'])
                except:
                    pass

                try:
                    shareholding = self.driver.find_element(By.XPATH, '//*[@name="Applicant[0].Company.Shareholding"]')
                    shareholding.send_keys(application['shareholding'])
                except:
                    pass

                company_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)
                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)

                try:
                    error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                    print(error_log)
                except:
                    error_log = ''
                    pass
                if error_log:
                    print('field missing or error : ' + error_log)
                    self.log_error(application, error_log, '', '')
                    sys.exit()
            except:
                print('Individual Data')
                pass
            # ------------------------------------------------#
            # -------------------- other income -----------------#
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(),"Other Income")]/../..').click()
                time.sleep(3)

                try:
                    other_inc_details1 = self.driver.find_element(By.XPATH, '//*[@class="form-control otherIncome1"]')
                    other_inc_details1.send_keys(application['details'])
                except:
                    pass
                try:
                    other_inc_amount1 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount1"]')
                    other_inc_amount1.send_keys(application['amount'])
                except:
                    pass
                try:
                    other_inc_frequency1 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency1"]')
                    other_inc_frequency1.send_keys(application['frequency'])
                except:
                    pass
                try:
                    other_inc_guarantee1 = application['guaranteed']
                    if other_inc_guarantee1 == 'Yes':
                        other_inc_guarantee1 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed1"]/../span[3]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    other_inc_details2 = self.driver.find_element(By.XPATH, '//*[@class="form-control otherIncome2"]')
                    other_inc_details2.send_keys(application['details2'])
                except:
                    pass
                try:
                    other_inc_amount2 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount2"]')
                    other_inc_amount2.send_keys(application['amount2'])
                except:
                    pass
                try:
                    other_inc_frequency2 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency2"]')
                    other_inc_frequency2.send_keys(application['frequency2'])
                except:
                    pass
                try:
                    other_inc_guarantee2 = application['guaranteed2']
                    if other_inc_guarantee2 == 'Yes':
                        other_inc_guarantee2 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed2"]/../span[3]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    other_inc_details3 = self.driver.find_element(By.XPATH, '//*[@class="form-control otherIncome3"]')
                    other_inc_details3.send_keys(application['details3'])
                except:
                    pass
                try:
                    other_inc_amount3 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount3"]')
                    other_inc_amount3.send_keys(application['amount3'])
                except:
                    pass
                try:
                    other_inc_frequency3 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency3"]')
                    other_inc_frequency3.send_keys(application['frequency3'])
                except:
                    pass
                try:
                    other_inc_guarantee3 = application['guaranteed3']
                    if other_inc_guarantee3 == 'Yes':
                        other_inc_guarantee3 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed3"]/../span[3]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    other_inc_details4 = self.driver.find_element(By.XPATH, '//*[@class="form-control otherIncome4"]')
                    other_inc_details4.send_keys(application['details4'])
                except:
                    pass
                try:
                    other_inc_amount4 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount4"]')
                    other_inc_amount4.send_keys(application['amount4'])
                except:
                    pass
                try:
                    other_inc_frequency4 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency4"]')
                    other_inc_frequency4.send_keys(application['frequency4'])
                except:
                    pass
                try:
                    other_inc_guarantee4 = application['guaranteed4']
                    if other_inc_guarantee4 == 'Yes':
                        other_inc_guarantee4 = self.driver.find_element(By.XPATH,
                                                                   '//*[@id="OtherIncome_Guaranteed4"]/../span[3]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    other_inc_details5 = self.driver.find_element(By.XPATH, '//*[@class="form-control otherIncome5"]')
                    other_inc_details5.send_keys(application['details5'])
                except:
                    pass
                try:
                    other_inc_amount5 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Amount5"]')
                    other_inc_amount5.send_keys(application['amount5'])
                except:
                    pass
                try:
                    other_inc_frequency5 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_PayFrequency5"]')
                    other_inc_frequency5.send_keys(application['frequency5'])
                except:
                    pass
                try:
                    other_inc_guarantee5 = application['guaranteed5']
                    if other_inc_guarantee5 == 'Yes':
                        other_inc_guarantee5 = self.driver.find_element(By.XPATH, '//*[@id="OtherIncome_Guaranteed5"]/../span[3]').click()
                    else:
                        pass
                except:
                    pass

                other_inc_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)

                try:
                    error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]')
                    error_log = error_log.get_attribute('for')
                    print(error_log)
                except:
                    error_log_other_inc = ''
                    pass
                if error_log:
                    print('field missing or error : ' + error_log)
                    self.log_error(application, 'field missing or error'+error_log, '', '')
                    sys.exit()

                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except:
                print('OTHER INCOME not found or error')
                pass
            # ---------------------------------------------------#
            # ----------------- asset -----------------------#
            try:
                self.driver.find_element(By.XPATH, '//span[contains(text(),"Assets")]/../..').click()
                time.sleep(3)
                asset_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)
                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except:
                print('assets not found or error')
                pass
            # -----------------------------------------------#
            # ------------------ commitments -----------------#
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(),"Commitments")]/../..').click()
                time.sleep(3)
                commitment_next = self.driver.find_element(By.XPATH,
                                                      '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)
                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except:
                print('commitments not found or error')
                pass
            # ------------------------------------------------#
            # ------------------- property -------------------#
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(),"Properties ")]/../..').click()
                time.sleep(3)

                self.driver.find_element(By.XPATH, '//*[@id="Property_HaveAnyBuyToLetProperties"]/../span[3]').click()

                try:
                    number_of_own_blt_properties = self.driver.find_element(By.XPATH, '//*[@id="Property_NoOfBuyToLetProperties"]')
                    number_of_own_blt_properties.clear()
                    number_of_own_blt_properties.send_keys(application['number_of_own_blt_properties'])
                except:
                    pass

                try:
                    total_value_of_portfolio = self.driver.find_element(By.XPATH, '//*[@id="Property_TotalValueOfPortfolio"]')
                    total_value_of_portfolio.send_keys(application['total_value_of_portfolio'])
                except:
                    pass

                try:
                    total_monthly_rent = self.driver.find_element(By.XPATH, '//*[@id="Property_TotalMonthlyRent"]')
                    total_monthly_rent.send_keys(application['total_monthly_rent'])
                except:
                    pass

                try:
                    total_mortgage_balances_outstanding_portfolio = self.driver.find_element(By.XPATH, '//*[@id="Property_TotalMortgageBalance"]')
                    total_mortgage_balances_outstanding_portfolio.send_keys(application['total_mortgage_balances_outstanding_portfolio'])
                except:
                    pass

                portfolio_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)

                try:
                    error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                    print(error_log)
                except:
                    error_log = ''
                    pass
                if error_log:
                    print('field missing or error : ' + error_log)
                    self.log_error(application, 'field missing or error' + error_log, '', '')
                    sys.exit()

                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except:
                print('property not found or error')
                pass
            # ----------------------------------------------#
            # -------------------- product ------------------#
            try:
                self.driver.find_element(By.XPATH, '//span[contains(text(),"Product")]/../..').click()
                time.sleep(3)

                try:
                    procuration_fee = self.driver.find_element(By.XPATH, '//label[contains(text(),"Procuration Fee")]/../../div[2]/div').text
                except:
                    procuration_fee = 0

                product_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)
                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except:
                print('product not found or errror')
                pass
            # ------------------------------------------------#
            # -------------------- personal_details ------------------#
            try:
                self.driver.find_element(By.XPATH, '//span[contains(text(),"Personal Details ")]/../..').click()
                time.sleep(3)

                try:
                    retire_age = self.driver.find_element(By.XPATH, '//*[@name="Applicant.RetirementAge"]')
                    retire_age.send_keys(application['retirement_age'])
                except:
                    pass

                try:
                    merital_status = self.driver.find_element(By.XPATH, '//*[@name="Applicant.MaritalStatus"]')
                    merital_status.send_keys(application['marital_status'])
                except:
                    pass

                personal_details_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(4)

                try:
                    error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"]/../label[1]').text
                    print(error_log)
                except:
                    error_log = ''
                    pass
                if error_log:
                    print('field missing or error : ' + error_log)
                    self.log_error(application, 'field missing or error' + error_log, '', '')
                    sys.exit()

                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except:
                print('personal details not found or error')
            # ------------------------------------------------#
            # -------------------- property type ------------------#
            try:
                self.driver.find_element(By.XPATH, '//span[contains(text(),"Property type ")]/../..').click()
                time.sleep(3)

                try:
                    year_of_conversion = self.driver.find_element(By.XPATH, '//*[@id="Security_YearConversion"]')
                    year_of_conversion.send_keys(application['year_of_conversion'])
                except:
                    pass

                try:
                    epc_rating = self.driver.find_element(By.XPATH, '//*[@id="Security_EnergyPerformanceCertificate"]')
                    epc_rating.send_keys(application['epc_rating'])
                except:
                    pass

                # provide_details = driver.find_element(By.XPATH, '//*[@id="Security_FullVacantPossessionDetails"]')
                # # provide_details.send_keys('abc')
                # provide_details.send_keys(js['share_of_freehold_details'])

                try:
                    lift = application['is_there_lift']
                    if lift == 'Yes':
                        istherelift = self.driver.find_element(By.XPATH, '//*[contains(text(),"Is there a lift?")]/../div/div/div/span[2]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    garage = application['is_there_garage']
                    if garage == 'Yes':
                        istheregarage = self.driver.find_element(By.XPATH, '//*[contains(text(),"Is there a Garage?")]/../div/div/div/span[2]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    balcony = application['is_flat_accessed_via_balcony']
                    if balcony == 'Yes':
                        istherebalcony = self.driver.find_element(By.XPATH, '//*[contains(text(),"Is the Flat accessed via a balcony or deck?")]/../div/div/div/span[2]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    property_licence = application['local_authority_private_rented_property_licence']
                    if property_licence == 'Yes':
                        isproperty_licence = self.driver.find_element(By.XPATH, "//*[contains(text(),'Local Authority Private Rented Property Licence')]/../div/div/div/span[2]").click()
                        licence_type = self.driver.find_element(By.XPATH, '//*[@id="Security_PropertyLicence"]')
                        licence_type.send_keys(application['property_licence'])
                    else:
                        pass
                except:
                    pass

                try:
                    commercial_premises = application['is_adjacent_to_commercial_premises']
                    if commercial_premises == 'Yes':
                        commercial_premises = self.driver.find_element(By.XPATH, "//*[contains(text(),'Is the flat above or adjacent to commercial premises')]/../div/div/div/span[2]").click()
                        commercial_premises_details = self.driver.find_element(By.XPATH, '//*[@id="Security_FlatAboveCommercialPremisesDetails"]')
                        commercial_premises_details.send_keys(application['commercial_premises_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    property_new = application['is_property_new']
                    if property_new == 'Yes':
                        isproperty_new = self.driver.find_element(By.XPATH, '//*[contains(text(),"Is the Property a new Build/new Conversion?")]/../div/div/div/span[2]').click()
                        time.sleep(1)
                        course_construction = application['is_property_in_course_of_construction']
                        if course_construction == 'Yes':
                            iscourse_construction = self.driver.find_element(By.XPATH, '//*[contains(text(),"Is the property in the course of construction?")]/../div/div/div/span[2]').click()
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

                try:
                    standerd_construction = application['is_property_of_standard_construction']
                    if standerd_construction == 'No':
                        isstanderd_construction = self.driver.find_element(By.XPATH, '//*[contains(text(),"Is the Property of Standard Construction?")]/../div/div/div/span[2]').click()
                        construction_details = self.driver.find_element(By.XPATH, '//*[@name="Security.ConstructionDetails"]')
                        construction_details.send_keys(application['construction_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    if application['security_property_tenure'] == 'Leasehold':
                        try:
                            service_charge = self.driver.find_element(By.XPATH, '//*[@name="Security.ServiceCharge"]')
                            service_charge.send_keys(application['service_charge'])
                        except:
                            pass

                        try:
                            ground_rent = self.driver.find_element(By.XPATH, '//*[@name="Security.GroundRent"]')
                            ground_rent.send_keys(application['ground_rent'])
                        except:
                            pass

                        try:
                            is_lease_extended = application['is_lease_extended']
                            if is_lease_extended == 'Yes':
                                is_lease_extended = self.driver.find_element(By.XPATH, '//*[@id="Security_IsExtendedLease"]/../span[3]').click()
                                lease_term = self.driver.find_element(By.XPATH, '//*[@name="Security.ExtendedLease"]')
                                lease_term.send_keys(application['current_lease_years'])
                            else:
                                pass
                        except:
                            pass

                        try:
                            purchasing_share_of_freehold = application['purchasing_share_of_freehold']
                            if purchasing_share_of_freehold == 'Yes':
                                purchasing_share_of_freehold = self.driver.find_element(By.XPATH, '//*[@id="Security_PurchaseShareOfFreehold"]/../span[3]').click()
                                share_of_freehold_details = self.driver.find_element(By.XPATH, '//*[@name="Security.PurchaseShareOfFreeholdDetails"]')
                                share_of_freehold_details.send_keys(application['share_of_freehold_details'])
                            else:
                                pass
                        except:
                            pass
                except:
                    pass

                try:
                    is_used_for_business_purposes = application['is_used_for_business_purposes']
                    if is_used_for_business_purposes == 'Yes':
                        is_used_for_business_purposes = self.driver.find_element(By.XPATH, '//*[@id="Security_BusinessPurpose"]/../span[3]').click()
                        business_purposes_details = self.driver.find_element(By.XPATH, '//*[@name="Security.BusinessPurposeDetails"]')
                        business_purposes_details.send_keys(application['business_purposes_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_there_occupancy_restriction = application['is_there_occupancy_restriction']
                    if is_there_occupancy_restriction == 'Yes':
                        is_there_occupancy_restriction = self.driver.find_element(By.XPATH, '//*[@id="Security_OccupancyRestrictions"]/../span[3]').click()
                        occupancy_restriction_details = self.driver.find_element(By.XPATH, '//*[@name="Security.OccupancyRestrictionDetails"]')
                        occupancy_restriction_details.send_keys(application['occupancy_restriction_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_full_vacant_possession = application['is_full_vacant_possession']
                    if is_full_vacant_possession == 'Yes':
                        is_full_vacant_possession = self.driver.find_element(By.XPATH, '//*[@id="Security_FullVacantPossession"]/../span[3]').click()
                    else:
                        pass
                    try:
                        full_vacant_possession_details = self.driver.find_element(By.XPATH, '//*[@name="Security.FullVacantPossessionDetails"]')
                        full_vacant_possession_details.send_keys(application['full_vacant_possession_details'])
                    except:
                        pass
                except:
                    pass

                try:
                    is_used_other_than_btl_details = application['is_used_other_than_btl_details']
                    if is_used_other_than_btl_details == 'Yes':
                        is_used_other_than_btl_details = self.driver.find_element(By.XPATH, '//*[@id="Security_OtherThanBTL"]/../span[3]').click()
                        other_than_btl_details = self.driver.find_element(By.XPATH, '//*[@name="Security.OtherThanBTLDetails"]')
                        other_than_btl_details.send_keys(application['other_than_btl_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    buying_under_purchase_scheme = application['buying_under_purchase_scheme']
                    if buying_under_purchase_scheme == 'yes':
                        buying_under_purchase_scheme = self.driver.find_element(By.XPATH, '//*[@id="Security_BuyingUnderPurchaseScheme"]/../span[3]').click()
                        under_purchase_scheme_details = self.driver.find_element(By.XPATH, '//*[@name="Security.BuyingUnderPurchaseSchemeDetails"]')
                        under_purchase_scheme_details.send_keys(application['under_purchase_scheme_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_receipt_discount_details = application['is_receipt_discount_details']
                    if is_receipt_discount_details == "Yes":
                        is_receipt_discount_details = self.driver.find_element(By.XPATH, '//*[@id="Security_ReceiptOfAnyDiscount"]/../span[3]').click()
                        receipt_discount_details = self.driver.find_element(By.XPATH, '//*[@name="Security.ReceiptOfDiscountDetails"]')
                        receipt_discount_details.send_keys(application['receipt_discount_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_let_family_member = application['is_let_family_member']
                    if is_let_family_member == 'Yes':
                        is_let_family_member = self.driver.find_element(By.XPATH, '//*[@id="Security_LetToFamilyMember"]/../span[3]').click()
                        let_family_member_details = self.driver.find_element(By.XPATH, '//*[@name="Security.LetToFamilyMemberDetails"]')
                        let_family_member_details.send_keys(application['let_family_member_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_property_tenanted = application['is_property_tenanted']
                    if is_property_tenanted == "Yes":
                        is_property_tenanted = self.driver.find_element(By.XPATH, '//*[@id="Security_IsPropertyTenanted"]/../span[3]').click()
                    else:
                        pass
                except:
                    pass

                try:
                    notes = self.driver.find_element(By.XPATH, '//*[@id="Security_SecurityNotes"]')
                    notes.send_keys(application['notes'])
                except:
                    pass

                try:
                    number_of_floors = self.driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfFloors"]')
                    number_of_floors.clear()
                    number_of_floors.send_keys(application['number_of_floors'])
                except:
                    pass

                try:
                    number_of_bedrooms = self.driver.find_element(By.XPATH, '//*[@id="Security_FlatNumberOfBedrooms"]')
                    number_of_bedrooms.clear()
                    number_of_bedrooms.send_keys(application['number_of_bedrooms'])
                except:
                    pass

                try:
                    number_of_livingrooms = self.driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfLivingRooms"]')
                    number_of_livingrooms.clear()
                    number_of_livingrooms.send_keys(application['number_of_living_rooms'])
                except:
                    pass

                try:
                    number_of_kitchens = self.driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfKitchens"]')
                    number_of_kitchens.clear()
                    number_of_kitchens.send_keys(application['number_of_kitchens'])
                except:
                    pass

                try:
                    number_of_bathrooms = self.driver.find_element(By.XPATH, '//*[@id="Security_HouseNumberOfBathrooms"]')
                    number_of_bathrooms.clear()
                    number_of_bathrooms.send_keys(application['number_of_bathrooms'])
                except:
                    pass

                try:
                    number_of_tenants = self.driver.find_element(By.XPATH, '//*[@id="Security_TenantsOnTenancyAgreement"]')
                    number_of_tenants.clear()
                    number_of_tenants.send_keys(application['number_of_tenants'])
                except:
                    pass

                try:
                    number_of_tenancy_agreements = self.driver.find_element(By.XPATH, '//*[@id="Security_TenancyAgreementsGranted"]')
                    number_of_tenancy_agreements.clear()
                    number_of_tenancy_agreements.send_keys(application['number_of_tenancy_agreements'])
                except:
                    pass

                try:
                    number_of_floors_in_block = self.driver.find_element(By.XPATH, '//*[@id="Security_FlatNumberOfFloors"]')
                    number_of_floors_in_block.clear()
                    number_of_floors_in_block.send_keys(application['number_of_floors_in_block'])
                except:
                    pass

                try:
                    floor_number = self.driver.find_element(By.XPATH, '//*[@id="Security_FloorFlatSituated"]')
                    floor_number.clear()
                    floor_number.send_keys(application['floor_number'])
                except:
                    pass

                property_type_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(2)

                try:
                    error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                    print(error_log)
                except:
                    error_log = ''
                    pass
                if error_log:
                    print('field missing or error : ' + error_log)
                    self.log_error(application, 'field missing or error' + error_log, '', '')
                    sys.exit()

                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
            except Exception as e:
                print(e)
                print('property type not found or error')
                pass
            # ------------------------------------------------#
            # -------------------- loan -----------------------#
            try:
                self.driver.find_element(By.XPATH, '//span[@class="title"][contains(text(),"Loan ")]/../..').click()
                time.sleep(3)

                try:
                    deposit_come_from = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_DepositComeFrom"]')
                    deposit_come_from.send_keys(application['deposit_come_from'])
                except:
                    pass

                try:
                    exit_strategy = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_ExitStrategy"]')
                    exit_strategy.send_keys(application['exit_strategy'])
                except:
                    pass

                try:
                    valuation_contact_person = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_ValuationContact"]')
                    valuation_contact_person.send_keys(application['valuation_contact_person'])
                except:
                    pass

                try:
                    valuation_contact_person_number = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_TelephoneNumber"]')
                    valuation_contact_person_number.send_keys(application['valuation_contact_person_number'])
                except:
                    pass

                try:
                    valuation_contact_name = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_ContactName"]')
                    valuation_contact_name.send_keys(application['valuation_contact_name'])
                except:
                    pass

                try:
                    is_private_sale = application['is_private_sale']
                    if is_private_sale == "Yes":
                        is_private_sale = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_PrivateSale"]/../span[3]').click()
                        private_sale_details = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_PrivateSaleDetails"]')
                        private_sale_details.send_keys(application['private_sale_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    proposed_tenants = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_ProposedTenants"]')
                    proposed_tenants.send_keys(application['proposed_tenants'])
                except:
                    pass

                try:
                    lease_type = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_LeaseType"]')
                    lease_type.send_keys(application['lease_type'])
                except:
                    pass

                try:
                    tenancy_agreement_months = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_AnticipatedTenancyAgreement"]')
                    tenancy_agreement_months.clear()
                    tenancy_agreement_months.send_keys(application['tenancy_agreement_months'])
                except:
                    pass

                try:
                    is_distressed_sale = application['is_distressed_sale']
                    if is_distressed_sale == 'Yes':
                        is_distressed_sale = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_IsDistressedSale"]/../span[3]').click()
                        distressed_sale_details = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_IsDistressedSaleDetails"]')
                        distressed_sale_details.send_keys(application['distressed_sale_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_purchased_below_market_value = application['is_purchased_below_market_value']
                    if is_purchased_below_market_value == "Yes":
                        is_purchased_below_market_value = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_IsPurchasedBelowMarketValue"]/../span[3]').click()
                        purchased_below_market_value_details = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_IsPurchasedBelowMarketDetails"]')
                        purchased_below_market_value_details.send_keys(application['purchased_below_market_value_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_government_initiative_purchased = application['is_government_initiative_purchased']
                    if is_government_initiative_purchased == 'Yes':
                        is_government_initiative_purchased = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_IsGovermentInitiative"]/../span[3]').click()
                        government_initiative_purchased_details = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_GovernmentInitiativeDetails"]')
                        government_initiative_purchased_details.send_keys(
                            application['government_initiative_purchased_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    is_ready_to_let_out = application['is_ready_to_let_out']
                    if is_ready_to_let_out == 'No':
                        is_ready_to_let_out = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_IsReadyToSell"]/../span[3]').click()
                        ready_to_let_out_details = self.driver.find_element(By.XPATH, '//*[@name="Mortgage.IsReadyToSellDetails"]')
                        ready_to_let_out_details.send_keys(application['ready_to_let_out_details'])
                    else:
                        pass
                except:
                    pass

                try:
                    vendor_name = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_VendorsName"]')
                    vendor_name.send_keys(application['vendor_name'])
                except:
                    pass

                try:
                    purpose_of_remortgage = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_PurposeOfMortgage"]')
                    purpose_of_remortgage.send_keys(application['purpose_of_remortgage'])
                except:
                    pass

                try:
                    full_breakdown_details = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_RemortagePortfolioDetails"]')
                    full_breakdown_details.send_keys(application['full_breakdown_details'])
                except:
                    full_breakdown_details = ''

                try:
                    is_property_currently_mortgaged = application['is_property_currently_mortgaged']
                    if is_property_currently_mortgaged == 'Yes':
                        is_property_currently_mortgaged = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_CurrentlyMortgaged"]/../span[3]').click()
                        outstanding_balance = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_OutstandingBalance"]')
                        outstanding_balance.send_keys(application['outstanding_balance'])

                        existing_mortgage_lender = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_ExistingMortgageLender"]')
                        existing_mortgage_lender.send_keys(application['existing_mortgage_lender'])

                        borrow_to_purchase_property = self.driver.find_element(By.XPATH, '//*[@id="Mortgage_OriginalAmountBorrowed"]')
                        borrow_to_purchase_property.send_keys(application['borrow_to_purchase_property'])
                except:
                    pass

                loan_next = self.driver.find_element(By.XPATH, '//*[@class="btn btn-default nav-button pull-right blueBtn "]').click()
                time.sleep(3)

                try:
                    error_log = self.driver.find_element(By.XPATH, '//*[@class="help-block"][contains(text(), "This field is required.")]/../label[1]').text
                    print(error_log)
                except:
                    error_log = ''
                    pass
                if error_log:
                    print('field missing or error : ' + error_log)
                    self.log_error(application, 'field missing or error' + error_log, '', '')
                    sys.exit()

                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(2)
                self.driver.get(main_url)
                self.driver.refresh()
                time.sleep(3)
                print('loan done')

                # my_dict = {"key1": "value1", "key2": "value2"}

                # value1 = {'erc': erc, 'initial_rate': initial_rate}
                value1 = {}
                value1["name"] = name
                value1["erc"] = erc
                value1["initial_rate"] = initial_rate
                value1["reversion_rate"] = reversion_rate
                value1["apr"] = apr
                value1["monthly_payment"] = monthly_payment
                value1["ltv"] = ltv
                value1["rental_coverage"] = rental_coverage
                value1["product_fee"] = product_fee
                value1["redemption_admin_fee"] = redemption_admin_fee
                value1["estimated_solicitor_fee"] = estimated_solicitor_fee
                value1["broker_fee_payable_by_borrower"] = broker_fee_payable_by_borrower
                value1["valuation_fee"] = valuation_fee
                value1["funds_release_fee"] = funds_release_fee
                value1["building_insurance_admin_fee"] = building_insurance_admin_fee
                value1["application_fee"] = application_fee
                value1["refrence_number"] = refrence_number
                value1["procuration_fee"] = procuration_fee
                return value1


            except:
                print('loan not found or error')
            # -------------------------------------------------#

            # Add logic to fill out other fields as per your existing code
            # Each section can be broken into smaller functions like fill_personal_details, fill_property_details
        except Exception as e:
            print(f"Form Filling Error: {e}")
            raise

    def download_and_upload(self, application, value1):
        try:
            print(value1)
            # print(value1["initial_rate"])
            download_button = self.driver.find_element(By.XPATH, '//*[contains(text(),"Reissue DIP")]')
            before_download = set(os.listdir(self.download_dir))
            download_button.click()
            time.sleep(8)
            print(str(datetime.datetime.now())+'download')

            new_file_name = self.wait_for_download(before_download)
            if new_file_name:
                updated_file_name = self.rename_downloaded_file(new_file_name)
                self.upload_file(application['id'], updated_file_name, value1)
            else:
                raise Exception("File download failed.")
        except Exception as e:
            print(f"Download/Upload Error: {e}")
            raise

    def wait_for_download(self, before_download):
        while True:
            after_download = set(os.listdir(self.download_dir))
            new_files = after_download - before_download
            if new_files:
                new_file_name = new_files.pop()
                if not new_file_name.endswith(".crdownload"):
                    return new_file_name
            time.sleep(1)

    def rename_downloaded_file(self, new_file_name):
        unique_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, str(datetime.datetime.now().strftime("%H:%M:%S"))))
        updated_file_name = f"{unique_id}.pdf"
        os.rename(
            os.path.join(self.download_dir, new_file_name),
            os.path.join(self.download_dir, updated_file_name)
        )
        return updated_file_name

    def upload_file(self, application_id, file_name, value1):
        print(value1)
        url = f"{self.api_url}?id={application_id}&filename={file_name}"
        response = requests.post(url)
        print(f"Upload Response: {response.status_code}")

        name = value1["name"]
        erc = value1["erc"].replace('£ ','')
        initial_rate = value1["initial_rate"].replace('£ ','').replace('%','')
        procuration_fee = value1["procuration_fee"].replace('£ ','').replace('%','')
        reversion_rate = value1["reversion_rate"].replace('£ ','')
        apr = value1["apr"].replace('£ ','').replace('%','')
        monthly_payment = value1["monthly_payment"].replace('£ ','')
        ltv = value1["ltv"].replace('£ ','').replace('%','')
        rental_coverage = value1["rental_coverage"].replace('£ ','').replace('%','')
        product_fee = value1["product_fee"].replace('£ ','')
        redemption_admin_fee = value1["redemption_admin_fee"].replace('£ ','')
        estimated_solicitor_fee = value1["estimated_solicitor_fee"].replace('£ ','')
        broker_fee_payable_by_borrower = value1["broker_fee_payable_by_borrower"].replace('£ ','')
        valuation_fee = value1["valuation_fee"].replace('£ ','')
        funds_release_fee = value1["funds_release_fee"].replace('£ ','')
        building_insurance_admin_fee = value1["building_insurance_admin_fee"].replace('£ ','')
        application_fee = value1["application_fee"].replace('£ ','')
        refrence_number = value1["refrence_number"].replace('£ ','')

        url1 = f"{self.api_url}/product?id={application_id}&name={name}&erc={erc}&initial_rate={initial_rate}&reversion_rate={reversion_rate}&monthly_payment={monthly_payment}&ltv={ltv}&procuration_fee={procuration_fee}&product_fee={product_fee}&reference_number={refrence_number}&token=YRcwnMgyrR&rental_coverage={rental_coverage}&redemption_admin_fee={redemption_admin_fee}&estimated_solicitor_fee={estimated_solicitor_fee}&broker_fee_payable_by_borrower={broker_fee_payable_by_borrower}&valuation_fee={valuation_fee}&funds_release_fee={funds_release_fee}&buildings_insurance_admin_fee={building_insurance_admin_fee}&application_fee={application_fee}&apr={apr}"
        print(url1)
        response1 = requests.post(url1)
        print(f"Upload Response: {response1.status_code}")

        print(str(datetime.datetime.now())+'finish')

    def log_error(self, application, message, initial_rate, monthly_payment):
        print(initial_rate)
        print(monthly_payment)
        url = f"{self.api_url}/logs?id={application['id']}&email={application['email']}&message={message}&initial_rate={initial_rate}&monthly_payment={monthly_payment}"
        print(url)
        requests.post(url)
        print(f"Logged Error for {application['id']}")
        print(str(datetime.datetime.now()))
        self.driver.quit()
        sys.exit()

    def close(self):
        self.driver.quit()
        sys.exit()


if __name__ == "__main__":
    print('*******************************************  STARTED ***********************************************')
    print(str(datetime.datetime.now()))
    # download_dir = "E:\\takshil\\quantum_pdf\\"
    print('done')
    download_dir = "/home/ubuntu/storage/loan-applications/"
    print('a')
    print(download_dir)
    # download_dir = "/var/www/novyy-dev/Novyy/storage/app/public/qmlApplications/"
    # download_dir = "/var/www/novyy-dev/novyyloans/storage/app/public/qmlApplications/"

    processor = ApplicationProcessor(download_dir)
    applications = processor.fetch_applications()

    print(os.getenv('uname'))
    print(os.getenv('pword'))
    processor.login(os.getenv('uname'), os.getenv('pword'),
                    'https://www.qmlsystem.co.uk/Portal/Application/DisplayForm?formName=Apply%20-%20Terms%20And%20Conditions')
                    # 'https://www.qmlsystem.co.uk/Portal/Application/DisplayForm?formName=Apply%20-%20Who%20is%20applying&items=2TnhPEhIjm8pGUhSWoIm%2B5jvt6o6pgltxGSdMUZKE2ky8vF7wyt5DSNT395nKyC%2B')

    for app in applications:
        processor.process_application(app)

    processor.close()




#/home/ubuntu/quantum/quantum/myenv/bin/python3 -u /home/ubuntu/quantum/quantum/qml_integration.py >> /home/ubuntu/quantum/quantum/logfile.log