from behave import given
from behave import when
from behave import then
import time
from pageobjects.contact_page import ContactPage

@given(u'que estoy en la pagina de contacto')
@given(u'I am on the contact page')
def step_impl(context):
    context.contact_page = ContactPage(context.driver)
    context.contact_page.open()
    time.sleep(8)
    context.contact_page.contact()
    time.sleep(8)

@when(u'lleno el campo de nombre con "{name}"')
def step_impl(context, name):
    context.contact_page.set_name(name)
    time.sleep(8)

@when(u'lleno el campo de correo electronico con "{email}"')
def step_impl(context, email):
    context.contact_page.set_email(email)
    time.sleep(8)

@then(u'lleno el campo de mensaje con "{message}"')
def step_impl(context, message):
    context.contact_page.set_message(message)
    time.sleep(8)

@given(u'que estoy en la pagina de trabaja con nosotros')
def step_impl(context):
    context.contact_page = ContactPage(context.driver)
    context.contact_page.open()
    time.sleep(8)
    context.contact_page.trabaja()
    time.sleep(5)

@when(u'lleno el campo de nombre de trabajo con "{name}"')
def step_impl(context, name):
    context.contact_page.set_namet(name)
    time.sleep(8)

@then(u'lleno el campo de mensaje')
def step_impl(context, message):
    context.contact_page.set_message(message)
    time.sleep(8)

@given(u'que estoy en la pagina de modalidad')
def step_impl(context):
    context.contact_page = ContactPage(context.driver)
    context.contact_page.open()
    time.sleep(8)
    context.contact_page.servicio()
    time.sleep(5)

@when(u'se recorra la pagina')
def step_impl(context):
    context.contact_page.recorrido()
    time.sleep(2)

@then(u'vuelve al inicio')
def step_impl(context):
    context.contact_page.iniciosof()
    time.sleep(2)

@given(u'que estoy en la pagina de softesting')
def step_impl(context):
    context.contact_page = ContactPage(context.driver)
    context.contact_page.open()
    time.sleep(8)

@when(u'ingreso icono de chat')
def step_impl(context):
    context.contact_page.chat()
    time.sleep(2)

@then(u'lleno el chat mensaje')
def step_impl(context):
    context.contact_page.mensajechat()
    time.sleep(2)

@given(u'que estoy en la pagina de componentes de servicio')
def step_impl(context):
    context.contact_page = ContactPage(context.driver)
    context.contact_page.open()
    time.sleep(8)
    context.contact_page.componentesservicio()
    time.sleep(5)

@when(u'se recorre la pagina de componentes')
def step_impl(context):
    context.contact_page.componentes()
    time.sleep(2)