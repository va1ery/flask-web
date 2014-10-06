# -*- coding: utf-8 -*-
from lettuce import *
from lettuce_webdriver.util import AssertContextManager
from datetime import datetime

from selenium import webdriver


@before.all
def setup_browser():
    world.browser = webdriver.Firefox()


def find_field_by_class(browser, attribute):
    xpath = "//input[@class='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False


@step(u'Given I go to "([^"]*)"')
def given_i_go_to_url(step, url):
    world.response = world.browser.get(url)


@step(u'When I fill in field with id "([^"]*)" with "([^"]*)"')
def when_i_fill_in_field_with_id_group1_with_group2(step, field_id, value):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(value)


@step(u'And I fill in field with id "([^"]*)" with "([^"]*)"')
def and_i_fill_in_field_with_id_group1_with_group2(step, field_id, value):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(value)


@step(u'And save the appointment in the bottom "([^"]*)"')
def and_save_the_appointment_in_the_bottom_group1(step, field_id):
    with AssertContextManager(step):
        submit_button = world.browser.find_element_by_id(field_id)
        submit_button.click()


# General
@step('Then The element with class of "(.*?)" contains "(.*?)"')
def element_contains(step, element_class, value):
    with AssertContextManager(step):
        element = world.browser.find_element_by_class_name(element_class)
        assert value in element.text, "Got %s " % element.text


@step(u'Then I see that the title of the page contains "([^"]*)"')
def then_i_see_the_title(step, title):
    with AssertContextManager(step):
        element = world.browser.find_element_by_tag_name('h1')
        assert title == element.text, "Got %s " % element.text


@step(u'When I update the field with id "([^"]*)" with "([^"]*)"')
def when_i_update(step, field_id, value):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(value)

fechaActual = datetime.now().strftime("%Y-%m-%d %l:%M:%S")
fechaActualComparacion = datetime.now().strftime("%Y-%m-%d")


@step(u'When I update the field with id "([^"]*)" with actual date')
def when_i_update_with_actual_date(step, field_id):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(fechaActual)


@step(u'Then The element with class of "([^"]*)" contains the actual date')
def then_the_element_with_actual_date(step, element_class):
    with AssertContextManager(step):
        element = world.browser.find_element_by_class_name(element_class)
        assert fechaActualComparacion in element.text, "Got %s " % element.text
