# -*- coding: utf-8 -*-
from lettuce import *
from lettuce_webdriver.util import AssertContextManager

from selenium import webdriver


@before.all
def setup_browser():
    world.browser = webdriver.Firefox()


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


@step(u'Then I should see "([^"]*)" within "([^"]*)" seconds')
def then_i_should_see(step, value, seconds):
    return True
