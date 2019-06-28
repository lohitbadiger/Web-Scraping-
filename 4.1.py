from  bs4 import BeautifulSoup as Bs

school="""
<address>

<head>
    <title> this is spiceup academy</title>


</head>
<body>
    
<schools>

    <p class="title">
         <b> This is located in the heart of Banglore city Koramangala</b>

    </p>

    <classrooms>
        <classroom id="555F">
        
            <teacher>Lohith</teacher>
            <subject> Python And Machine Learing</subject>
            <dob>30/10/1994</dob>
            <date>30-10-2019</date>
            <review>Amazing to study with you</review>

        </classroom>

        <good id="666F">
        
                <teacher>Sususmu</teacher>
                <subject> Php And Machine Learing</subject>
                <dob>02/10/1990</dob>
                <date>04-10-2019</date>
                <review> banhlore study with you</review>
                
            </good>


            <bad id="777F">
        
                    <teacher>KOyta</teacher>
                    <subject> Ruby And Machine Learing</subject>
                    <dob>20/10/1980</dob>
                    <date>08-10-2018</date>
                    <review>Good to meet you and  to study with you</review>
                    
                </bad>
    </classrooms>
</schools>


 <ok>
     <p>hejsdkd</p>
     <h1>hsdnjsdfnjksdf</h1>
     <p>bsajdb</p>
 </ok>

</body>
</address>"""


ss=Bs(school, 'html.parser')
print(ss)

print('---------------------------------------------')
print('-------------------contents--------------------------')


# if i want to make content in the list format

print(ss.contents)

print('---------------------------------------------')
print('------------------address---------------------------')

print(ss.address)

print('---------------------------------------------')
print('--------------------head-------------------------')
print(ss.head)

print('---------------------------------------------')
print('-------------------title_tag--------------------------')

title_tag=ss.title

print(title_tag)


print('---------------------------------------------')
print('---------------------------------------------')


# navigate down  and gives results for the next tag

for me in ss.head.descendants:
    print(me)


print('---------------------------------------------')
print('---------------------------------------------')
#  this will go to the next tag .. 
# here there is no tag in after the <teacher> Tag so this will giv me string

for me in ss.teacher.descendants:
    print(me)


print('---------------------------------------------')
print('--------------------stripped_strings-------------------------')
# navigate down using the strippeed string method

#  now we wil get all string value present inside the html documents

for  string in ss.stripped_strings:
    print(repr(string))


print('---------------------------------------------')
print('------------------parent---------------------------')


# navigate up using the parent method


print(title_tag.parent)

print('---------------------------------------------')
print('--------------------navigate_up-------------------------')

# taking one  parent

navigate_up=ss.subject
print(navigate_up)

print('---------------------------------------------')
print('-------------------stripped_strings--------------------------')

for me in navigate_up.stripped_strings:
    print(repr(me))

    

print('---------------------------------------------')
print('--------------------descendants-------------------------')
# this will give with quotes ' '
# bcz of repr

for me in ss.stripped_strings:

    print(repr(me))
print('---------------------------------------------')

print('---------------------------------------------')

# this will not give quote  ' '
for me in ss.stripped_strings:
    
    print(me)

# navigating element object to navigate back and forth
print('---------------------------------------------')
print('---------------------------------------------')


back_and_forth=ss.address.bad
print(back_and_forth)

print('---------------------------------------------')
print('---------------------------------------------')
ok=next_element=back_and_forth.next_element.next_element
print(ok)


okk=ok.next_element.next_element

print(okk)



print('---------------------------------------------')
print('---------------------------------------------')

select_ok_tag=ss.ok
print(select_ok_tag)


print('---------------------------------------------')
print('---------------------------------------------')

ok_tag_saving_here=select_ok_tag.next_element.next_element
print(ok_tag_saving_here)

print('---------------------------------------------')
print('---------------------------------------------')



next=ss.ok.p
print(next)

nex=next.next_element.next_elements
print(nex)