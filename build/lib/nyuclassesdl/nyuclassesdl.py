# coding: utf-8

#############################################
# File Name: nyuclassesdl.py
# Author: Zhiao Zhou
# Mail: zz1749@nyu.edu
# Created Time:  2018/4/16 22:40 EST
#############################################

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import os
import urllib
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

try:
    from urllib import unquote
except ImportError:
    from urllib.parse import unquote

def run(netid,password,MFA,DIR=None):

    driver = webdriver.Firefox()
    timeout = 5

    driver.get("http://newclasses.nyu.edu/")
    driver.maximize_window()

    assert "NYU Login" in driver.title

    elem1 = driver.find_element_by_id('netid')
    elem2 = driver.find_element_by_id('password')

    elem1.clear()
    elem1.send_keys(netid)
    elem2.clear()
    elem2.send_keys(password)

    elem2.send_keys(Keys.RETURN)

    if 'NYU Login' in driver.title:
        print("You have to pass the MFA using the way you've chosen")
        time.sleep(7)
        driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="duo_iframe"]'))
        if MFA == 'duo':
            time.sleep(7)
            duo = driver.find_element_by_xpath("/html/body/div/div[1]/div/form/fieldset[2]/div[1]/button")
            duo.click()
            print('Please accept the push notification on your personal device')
        driver.switch_to_default_content()

    x = raw_input('Input [Y] if you have already approved for the MFA: ')

    assert "NYU Classes : My Workspace" in driver.title

    pattern_name = """title=.*?role"""
    list_name = re.findall(pattern_name,str(driver.page_source))[2:-1]

    pattern_id = """data-site-id=.*?role"""
    list_id = re.findall(pattern_id,str(driver.page_source))

    list_id = [x[14:50] for x in list_id]
    list_name = [x[7:x.find('role')-2] for x in list_name]
    classes = dict(zip(list_id,list_name))

    def find_file_url():
        file_list = driver.find_elements_by_class_name('org_sakaiproject_content_types_fileUpload')
        if file_list == []:
            return None
        else:
            return [x.get_attribute("href") for x in file_list]

    def find_folder():
        pattern = pattern = """folder.*?class"""
        folder_list = re.findall(pattern,str(driver.page_source))
        if folder_list == []:
            return None
        else:
            return [x.split('"')[2] for x in folder_list]

    def download(id):
        driver.get("https://newclasses.nyu.edu/access/content/group/"+id+'/')
        driver.maximize_window()
        assert classes[id] in driver.title
        # In the first level directory
        if find_file_url(): #check if there's file in the first level dir
            for url in find_file_url():
                filename = unquote(url.split('/')[-1])
                if filename not in os.listdir(directory+'/'):
                    print('downloading {}'.format(filename))
                    urllib.urlretrieve(url,directory+'/'+filename)
                    print('success')
                else:
                    print('file already existed')
        if find_folder(): # check if there's second level folders
            for folder2 in find_folder():
                folder_dir = directory+'/'+unquote(folder2)
                if not os.path.exists(folder_dir):
                    os.makedirs(folder_dir)
                driver.get("https://newclasses.nyu.edu/access/content/group/"+id+'/'+folder2) # get in the second level folder
                driver.maximize_window()

                if find_file_url(): #check if there's file in the second level dir
                    for url in find_file_url():
                        filename = unquote(url.split('/')[-1])
                        if filename not in os.listdir(directory+'/' + unquote(folder2) +'/'):
                            print('downloading {}'.format(filename))
                            urllib.urlretrieve(url,directory+'/' + unquote(folder2) +'/'+filename)
                            print('success')
                        else:
                            print('file already existed')

                if find_folder(): # check if there's third level folders
                    for folder3 in find_folder():
                        folder_dir = directory+'/'+unquote(folder2)+'/'+unquote(folder3)
                        if not os.path.exists(folder_dir):
                            os.makedirs(folder_dir)
                        driver.get("https://newclasses.nyu.edu/access/content/group/"+id+'/'+folder2+'/'+folder3) # get in the third level folder
                        driver.maximize_window()

                        if find_file_url(): #check if there's file in the second level dir
                            for url in find_file_url():
                                filename = unquote(url.split('/')[-1])
                                if filename not in os.listdir(directory+'/' + unquote(folder2) +'/'+unquote(folder3)+'/'):
                                    print('downloading {}'.format(filename))
                                    urllib.urlretrieve(url,directory+'/' + unquote(folder2) +'/'+unquote(folder3)+'/'+filename)
                                    print('success')
                                else:
                                    print('file already existed')                   
    for id in classes.keys():
        print('For class: {}'.format(classes[id]))
        if DIR:
            directory = DIR + '/' + classes[id]
        else:
            directory = './'+classes[id]
        if not os.path.exists(directory):
            os.makedirs(directory)
        download(id)

    print('All downloads were successful!')
    driver.quit()


