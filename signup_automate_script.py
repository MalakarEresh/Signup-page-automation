from selenium import webdriver
from selenium.webdriver.common.by import By
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
from dotenv import load_dotenv

import os
import time
import unittest
import re

load_dotenv()

api_key = os.getenv("MAILOSAUR_API_KEY")
server_id = os.getenv("MAILOSAUR_SERVER_ID")
server_domain = os.getenv("MAILOSAUR_SERVER_DOMAIN")



# Setup Your Accout Credetials
first_name = "Test"
last_name = "Test"
email = "test02@" + server_domain
phone_no = "9849623468"
password = "Goldberg7879@"
confirm_password = "Goldberg7879@"

# Agency Detail Credentials
agency_name = "Test"
agency_role = "Test"
agency_email = email
agency_website = "example.com"
agency_address = "Test"

# Professional Experience
years_of_experience = "6 years"
number_of_student_recruited = 100
focus_area = "test"
success_metrics = 50
##checkbox
career_counseling = True
admission_applications = False
visa_processing = True
test_preparation = True

## verification
business_registration_number = 123456789
universities = True
colleges = True
vocational_school = True
other = True
certification_details = "test"

options_to_select = ["Australia", "Canada"]

FILE = "D:\\Selenium automation\\Vritech task\\test.pdf"




class mysignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_sign_up(self):
        driver = self.driver
        try:
            driver.get("https://authorized-partner.vercel.app/")
        except Exception as ex:
            print(ex)
        else:

            #Setup Your Account
            driver.find_element(By.XPATH,"//a[@href='/register']//button").click()
            time.sleep(5)
            agreement = driver.find_element(By.ID, "remember")
            agreement.click()
            time.sleep(5)

            driver.find_element(By.XPATH,"//a[@href='register?step=setup']//button").click()
            time.sleep(5)

            

            fname = driver.find_element(By.NAME, "firstName")
            fname.clear()
            time.sleep(5)
            fname.send_keys(first_name)

            lname = driver.find_element(By.NAME, "lastName")
            lname.clear()
            time.sleep(5)
            lname.send_keys(last_name)

            form_email = driver.find_element(By.NAME, "email")
            form_email.clear()
            time.sleep(5)
            form_email.send_keys(email)

            form_phone = driver.find_element(By.NAME, "phoneNumber")
            form_phone.clear()
            time.sleep(5)
            form_phone.send_keys(phone_no)

            form_password = driver.find_element(By.NAME, "password")
            form_password.clear()
            time.sleep(5)
            form_password.send_keys(password)

            form_confirm_password = driver.find_element(By.NAME, "confirmPassword")
            form_confirm_password.clear()
            time.sleep(5)
            form_confirm_password.send_keys(confirm_password)
            time.sleep(10)

            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(10)

            
            
            # OTP 
            mailosaur = MailosaurClient(api_key)
            criteria = SearchCriteria()
            criteria.sent_to = email
            message = mailosaur.messages.get(server_id, criteria)
            match = re.search("([0-9]{6})", message.text.body)
            otp = match.group()


            form_otp = driver.find_element(By.XPATH, "//input[@autocomplete='one-time-code']")
            form_otp.clear()
            form_otp.send_keys(otp)
            time.sleep(20)

            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            

            # Agency Detail
            form_agency_name = driver.find_element(By.NAME, "agency_name")
            form_agency_name.clear()
            form_agency_name.send_keys(agency_name)
            time.sleep(5)

            form_agency_role = driver.find_element(By.NAME, "role_in_agency")
            form_agency_role.clear()
            form_agency_role.send_keys(agency_role)
            time.sleep(5)

            form_agency_email = driver.find_element(By.NAME, "agency_email")
            form_agency_email.clear()
            form_agency_email.send_keys(agency_email)
            time.sleep(5)

            form_agency_website = driver.find_element(By.NAME, "agency_website")
            form_agency_website.clear()
            form_agency_website.send_keys(agency_website)
            time.sleep(5)

            form_agency_address = driver.find_element(By.NAME, "agency_address")
            form_agency_address.clear()
            form_agency_address.send_keys(agency_address)
            time.sleep(5)

            driver.find_element(By.XPATH,"//button[@role='combobox']").click()

            

            for option in options_to_select:
                driver.find_element(
                    By.XPATH,
                    f"//div[contains(@class,'cursor-pointer')]//span[normalize-space()='{option}']"
                ).click()
                time.sleep(10)

            driver.find_element(By.XPATH,"//button[@role='combobox']").click()
            time.sleep(5)

            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            

            # Professional Experience
            
            driver.find_element(By.XPATH, "//label[contains(text(), 'Years of Experience')]/following-sibling::button").click()
            time.sleep(5)

            option = driver.find_element(By.XPATH, f"//div[@role='option' and normalize-space(.)='{years_of_experience}']")
            option.click()
            time.sleep(5)

            form_number_of_student_recruited = driver.find_element(By.NAME, "number_of_students_recruited_annually")
            form_number_of_student_recruited.send_keys(number_of_student_recruited)
            time.sleep(5)

            form_focus_area = driver.find_element(By.NAME, "focus_area")
            
            form_focus_area.send_keys(focus_area)
            time.sleep(5)

            form_success_metrics = driver.find_element(By.NAME, "success_metrics")
          
            form_success_metrics.send_keys(success_metrics)
            time.sleep(5)

            ## Checkboxes

            service_provided = driver.find_elements(By.XPATH, "//button[@role='checkbox']")

            if career_counseling:
                service_provided[0].click()
                time.sleep(5)
            if admission_applications:
                service_provided[1].click()
                time.sleep(5)
            if visa_processing:
                service_provided[2].click()
                time.sleep(5)
            if test_preparation:
                service_provided[3].click()
                time.sleep(5)
            


            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

            


            # Verification and preferences

            form_business_registration_number = driver.find_element(By.NAME, "business_registration_number")
            form_business_registration_number.send_keys(business_registration_number)
            time.sleep(5)

            driver.find_element(By.XPATH, "//button[@role='combobox']").click()

            for option in options_to_select:
                driver.find_element(
                    By.XPATH,
                    f"//div[contains(@class,'cursor-pointer')]//span[normalize-space()='{option}']"
                ).click()
                time.sleep(10)
            
            institution_type = driver.find_elements(By.XPATH,"//button[@role='checkbox']")
            if universities:
                institution_type[0].click() 
                time.sleep(5)
            if colleges:
                institution_type[1].click() 
                time.sleep(5)
            if vocational_school:
                institution_type[2].click() 
                time.sleep(5)
            if other:
                institution_type[3].click() 
                time.sleep(5)

            if certification_details:
                form_certification_details = driver.find_element(By.NAME, "certification_details")
                form_certification_details.send_keys(certification_details)
                time.sleep(5)

            form_file_input = driver.find_elements(By.XPATH, "//input[@type='file']")

            form_file_input[0].send_keys(FILE)
            time.sleep(6)

            form_file_input[1].send_keys(FILE)
            time.sleep(5)


            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(5)

           


            print("Signup Test Complete")
            time.sleep(10)

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
