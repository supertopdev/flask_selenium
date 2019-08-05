from flask import Flask, jsonify, make_response
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import random
import time
import sys

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
exe_path = "/home/ubuntu/flask_selenium/geckodriver"
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path=exe_path)
driver_1 = webdriver.Firefox(capabilities=cap, executable_path=exe_path)
driver_2 = webdriver.Firefox(capabilities=cap, executable_path=exe_path)


@app.route('/companyinfo/<company_name>/')
def home(company_name):
    response = get_company_info(company_name)
    if response:
        api_response = make_response(jsonify(response), 200)
    else:
        response = {'message': 'No such company with the specified name'}
        api_response = make_response(jsonify(response), 404)
    api_response.headers['Content-Type'] = 'application/json'
    return api_response


def login(user_id, password_id, driver):
    sign_in_page = 'https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin'
    driver.get(sign_in_page)
    username = driver.find_element_by_id("username")
    username.click()
    username.clear()
    username.click()
    username.send_keys("{}".format(user_id))
    password = driver.find_element_by_id("password")
    password.click()
    password.clear()
    password.click()
    password.send_keys("{}".format(password_id))
    driver.find_element_by_class_name(
        "login__form_action_container ").click()


def link(name):
    name = name.lower()
    name = name.replace(" ", "-")
    linkedin_url = "https://www.linkedin.com/company/" + \
        str(name)+str('/about/')
    crunchbase_url = "https://www.crunchbase.com/organization/" + \
        str(name)+str("#section-overview")
    driver.get(linkedin_url)
    driver_1.get(crunchbase_url)
    # return linkedin_employee_data


def emp(name):
    name = name.lower()
    name = name.replace(" ", "-")
    linkedin_employee_data = "https://www.linkedin.com/company/" + \
        str(name)+str('/people/')
    driver.get(linkedin_employee_data)


def info_scraping(company):
    # about
    try:
        about = driver.find_element_by_class_name(
            "org-grid__core-rail--no-margin-left")
        new_about = about.find_element_by_tag_name('p')
        about = new_about.text
        print('ABOUT THE COMPANY: {}'.format(about))
        # print("\n")
        # time.sleep(1)
    except:
        try:
            new_about = driver_1.find_element_by_css_selector(
                "span.component--field-formatter.field-type-text_long.ng-star-inserted")
            about = new_about.text
            print('ABOUT THE COMPANY: {}'.format(about))
            # print("\n")
            # time.sleep(1)Latitude@6440
        except:
            about = "null"
            print("ABOUT THE COMPANY: {}".format(about))
            # print("\n")
            # time.sleep(1)
    # url
    try:
        website_url = driver.find_element_by_css_selector(
            'span.link-without-visited-state')
        url = website_url.text
        print('WEBSITE URL LINK: {}' .format(url))
        # print("\n")
        # time.sleep(1)
    except:
        try:
            website_url = driver_1.find_element_by_css_selector(
                "link-formatter.ng-star-inserted")
            url = website_url.text
            print('WEBSITE URL LINK: {}' .format(url))
            # print("\n")
            # time.sleep(1)
        except:
            url = "null"
            print('WEBSITE URL LINK: {}' .format(url))
            # print("\n")
            # time.sleep(1)
    # founded year
    try:
        founded_year = driver.find_element_by_css_selector(
            'dl.overflow-hidden')
        founded_year = founded_year.text.splitlines()
        f = founded_year.index('Founded')
        year = founded_year[f+1]
        print('FOUNDED YEAR IS : {}'.format(year))
        # print("\n")
        # time.sleep(1)
    except:
        try:
            crunch_founded_year = driver_1.find_element_by_css_selector(
                "span.component--field-formatter.field-type-date_precision.ng-star-inserted")
            year = crunch_founded_year.text
            print('FOUNDED YEAR IS : {}'.format(year))
            # print("\n")
            # time.sleep(1)
        except:
            year = "null"
            print('FOUNDED YEAR IS : {}'.format(year))
            # print("\n")
            # time.sleep(1)

    # Address
    try:
        address = driver.find_element_by_css_selector('dl.overflow-hidden')
        address = address.text.splitlines()
        a = address.index('Headquarters')
        Address = address[a+1]
        print('ADDRESS : {}'.format(Address))
        # print("\n")
        # time.sleep(1)
    except:
        try:
            crunch_address = driver_1.find_element_by_css_selector(
                "identifier-multi-formatter.ng-star-inserted")
            Address = crunch_address.text
            print('FOUNDED YEAR IS : {}'.format(Address))
            # print("\n")
            # time.sleep(1)
        except:
            Address = "null"
            print('ADDRESS:  {}'.format(Address))
            # print("\n")
            # time.sleep(1)

    # email
    try:
        contact_email = driver_1.find_elements_by_css_selector(
            "span.wrappable-label-with-info.ng-star-inserted")
        z = []
        for i in contact_email:
            z.append(i.text)
        email = driver_1.find_elements_by_css_selector(
            "span.field-value.flex-100.flex-gt-sm-75.ng-star-inserted")
        x = []
        for i in email:
            x.append(i.text)
        for j in range(0, len(x), 1):
            if("@" in x[j]) == True:
                email_id = x[j]
                print("email_id: {}".format(email_id))
                # print("\n")
                break
        else:
            email_id = "null"
            print("email_id: {}".format(email_id))
            # print("\n")
            # time.sleep(1)
        # time.sleep(1)
    except:
        email_id = "null"
        print("email_id: {}".format(email_id))
        # print("\n")
        # time.sleep(1)

    # phone_number
    try:
        contact_num = driver_1.find_elements_by_css_selector(
            "span.wrappable-label-with-info.ng-star-inserted")
        z = []
        for i in contact_num:
            z.append(i.text)
        contact = driver_1.find_elements_by_css_selector(
            "span.field-value.flex-100.flex-gt-sm-75.ng-star-inserted")
        x = []
        for i in contact:
            x.append(i.text)
        # print(x[2][0])
        for j in range(0, len(x), 1):
            if(x[j][0]) == "+":
                phone_number = x[j]
                print("phone_number: {}".format(phone_number))
                # print("\n")
                break
        else:
            phone_number = "null"
            print("phone_number: {}".format(phone_number))
            # print("\n")
            # time.sleep(1)
    except:
        phone_number = "null"
        print("phone_number: {}".format(phone_number))
        # print("\n")
        # time.sleep(1)

    # image_url
    try:
        img = driver_1.find_element_by_css_selector(
            "div.text-card-image.flex-none.cb-margin-gt-sm-large-right.cb-margin-large-bottom.cb-margin-gt-sm-none-bottom.cb-image-with-placeholder.organization")
        img = img.find_element_by_tag_name("img").get_attribute('src')
        Company_logo = img
        print("COMPANY LOGO: {}".format(Company_logo))
        # print("\n")
        # time.sleep(1)
    except:
        Company_logo = 'null'
        print("Company_logo:  {}".format(Company_logo))
        # print("\n")
        # time.sleep(1)

    return about, url, year, Address, email_id, phone_number, Company_logo


def employees_info(company):
    #  Scrolling function 1
    emp(company)
    SCROLL_PAUSE_TIME = 4
    last_height = driver.execute_script("return document.body.scrollHeight")
    employees = []
    while True:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(4)
    # Scrolling function 2
    try:
        # 2. Getting employee class # name and designation
        employee_info = driver.find_elements_by_class_name(
            "artdeco-entity-lockup__content.ember-view")
        for i in employee_info:
            employee = {}
            new_emp = i.find_element_by_class_name(
                "artdeco-entity-lockup__title.ember-view")
            role_name = i.find_element_by_class_name(
                "artdeco-entity-lockup__subtitle.ember-view")
            employee['Name'] = new_emp.text
            employee['Role'] = role_name.text
            print("Name:{}".format(employee['Name']))
            print("Role:{}".format(employee['Role']))
            try:
                # employee email and url
                Employee_linkedin_url = new_emp.find_element_by_tag_name(
                    "a").get_attribute("href")
                print("Employee_linkedin_url:{}".format(Employee_linkedin_url))
                url = Employee_linkedin_url+str('detail/contact-info/')
                employee['url'] = url
                driver_2.get(url)
                # time.sleep(1)
                try:
                    email = driver_2.find_element_by_class_name(
                        "pv-contact-info__contact-type.ci-email")
                    email = email.find_element_by_tag_name("div")
                    employee['email'] = email.text
                    print("email:{}".format(email.text))
                    # print("\n")
                except:
                    print("email: null")
                    # print("\n")
            except:
                pass
            employees.append(employee)
    except Exception as e:
        print("No", e)
    time.sleep(random.randrange(1, 10, 1))
    return employees


def get_company_info(company_name):
    login('poojadoll29@gmail.com', 'juttu@143#', driver)
    login('poojadoll29@gmail.com', 'juttu@143#', driver_2)
    link(company_name)
    try:
        link_data = driver.find_element_by_css_selector('h1.error-headline')
        crunch_data = driver_1.find_element_by_class_name(
            "cb-margin-large-vertical.cb-font-size-xlarge.cb-font-weight-xbold")
        if link_data.text == "Oops!" and crunch_data.text == "Oops.":
            company_name = company_name.replace(".", "-")
            link(company_name)
            try:
                modified_data = driver.find_element_by_css_selector(
                    'h1.error-headline')
                modified_cruch_data = driver_1.find_element_by_class_name(
                    "cb-margin-large-vertical.cb-font-size-xlarge.cb-font-weight-xbold")
                if modified_data.text == "Oops!" and modified_cruch_data.text == "Oops.":
                    print("please enter the company name correctly")
                    # print("\n")
                else:
                    pass
            except:
                about, url, year, Address, email_id, phone_number, Company_logo = info_scraping(company_name)
                employees = employees_info(company_name)
        else:
            pass
    except:
        about, url, year, Address, email_id, phone_number, Company_logo = info_scraping(company_name)
        employees = employees_info(company_name)

    company_details = {'company_name': company_name, 'About': about, 'URL': url, 'YEAR': year, 'ADDRESS': Address, 'EMAIL': email_id, 'PHONE_NUMBER': phone_number, 'LOGO': Company_logo, 'Employees': employees }
    print(company_details)
    print("\n")
    return company_details
