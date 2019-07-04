# creating employee based on basic details


# import the required Library

from bs4 import BeautifulSoup

# create employee html Document

employee_html_doc="""<employees>
            <employee class="accountant">
            <firstname>John</firstname> <lastname>Doe</lastname>
            </employee>


            <employee class="manager">
            <firstname>Anna </firstname> <lastname>Smith</lastname>
            </employee>

            <employee class="developer">
            <firstname>Lohit  </firstname> <lastname>Badiger</lastname>
            </employee>


</employees>"""
# create soup objects

soup_emp=BeautifulSoup(employee_html_doc, 'html.parser')

print(soup_emp)

print('___________________________________tag_______________________________________')
# access and view the tag
tag=soup_emp.employee
print(tag)
print('_________________________________manager_________________________________________')

# modify the tag im adding new tag


tag['class']='manager'
print(tag)

print('__________________________________________________________________________')

# to change one more 

tag['class']='developer'
print(tag)

print('__________________________________________________________________________')

print(soup_emp)


print('________________________________NewTag__________________________________________')

print('\n')
# add a tag
tag=soup_emp.new_tag('NewTag')
tag.string='Lohith Learning Process'
print(tag)

# modify using insert_aftr method
print('________________________________insert_after__________________________________________')

soup_emp.employees.employee.insert_after(tag)
print(soup_emp)
print('__________________________________________________________________________')

print('______________________________clear____________________________________________')
# clear all tge modified tag
# it will delete the last generated output from the tag i.e 'Lohith Learning Process'
tag.clear()
# it will 
print(soup_emp)


print('__________________________________________________________________________')
print('____________________________________create______________________________________')

# create a tag object and view it
tag=soup_emp.employees.employee
print(tag)



print('__________________________________________________________________________')
print('__________________________________________________________________________')

# extract the info using extract method
print(tag.firstname.string.extract())

print('__________________________________________________________________________')
print('__________________________________________________________________________')

# modify the tag name
print(tag.firstname.replace_with('first name gfdsggfd'))

print('__________________________________________________________________________')
print('__________________________________________________________________________')
print(soup_emp.employees)




print('_________________________dfssfd_________________________________________________')
print('__________________________________________________________________________')
ook=soup_emp.employees.employee
print(ook)
print(tag.lastname.replace_with('first name gfdsggfd'))
print(soup_emp.employees)