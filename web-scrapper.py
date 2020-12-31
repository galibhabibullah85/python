import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

#---Step 01: Get the HTML
r = requests.get(url)
# htmlContent = r.content---->recommended
htmlContent = r.text
# print(htmlContent)

#----Step 02: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.find('img').get('src')[1:])

#---Step 03: HTML Tree
# title = soup.title #will return the html <title> tag
# print(title)
# print(title.string)
#--------->.stripped_strings returns all the strings formetedly(keeps the closer one closer) for a single element

"""
----------------------
Commonly used objects types:
1. print(type(title))===>Tag
2. print(type(title.string))===>NavigatableString #.string/.strings returns the innertext of a single element
3. print(type(soup))===>BeautifulSoup
4. Comment
5. generator===>this objects always needs to be iterated by loops. can't be printed
--------------------------
"""
"""
-----------------------------
Comment object--->
markup = "<tag_name><!-- any_comment --></tag_name>"
soupComnt = BeautifulSoup(markup)
print(soupComnt)
print(soupComnt.tag_name) #output: <!-- any_comment -->
print(soupComnt.tag_name.string) #output: any_comment
print(type(soupComnt.tag_name.string)) #output: bs4.element.comment
-----------------------------
"""
# ptag = soup.find_all('p') #returns all the <p> tags and its children also
# print(ptag)


# anchors = soup.find_all('a') #returns all the <a> tags and its children also
# print(anchors)
# anchorHref = soup.find('a').get('href') #get() can return any attr's value of a single element/tag
# print(anchorHref)

"""
--------------------------------
For getting all the attr values, we need loop.
# anchors = soup.find_all('a')
# for link in anchors:
# 	print(link.get('href'))
--------------------------------
"""



"""
--------------------------------------------------
For getting all the links nicely and without #
# all_links = set()
# anchors = soup.find_all('a')
# for link in anchors:
# 	if((link.get('href')!='#') and (link.get('href')!='/')):
# 		all_links.add(f'https://codewithharry.com{link.get("href")}')

# for i in all_links:
# 	print(i)
-------------------------------------------------
"""

# firstPtag = soup.find('p') #returns only the first html element
# print(firstPtag)


# firstPtagCls = soup.find('p')['class'] #returns the classes of the first element
# firstPtagCls = soup.find_all(class_='lead') #returns the tags containing the specified class
# print(firstPtagCls)


# elmntsWithCls = soup.find_all('p',class_='lead') #returns all the tags with the specified class name
# print(elmntsWithCls)

# elmntWithAttr = soup.find_all(attrs={'shortable-date':'1607957288000000'}) #attrs={'attr_name':'attr_value'}
# print(elmntWithAttr)

# elmntsWithId = soup.find(id='navbarSupportedContent') #returns the tag along with its children having the id
# print(elmntsWithId)
# print(elmntsWithId.children)
# print(elmntsWithId.contents)
# print(elmntsWithId.string) #have to use .string only for a single tag that doesn't have any children
# print(elmntsWithId.strings) #this is a generator. so, it cann't be printed. always need to be itareted by loops
# for item in elmntsWithId.stripped_strings: #.stripped_strings is also a generator that returns all the strings formetedly(keeps the closer one closer) for a single element
# 	print(item)
#__________________________________
#for item in soup.find_all(): #.find_all() will not work in this case.have to use .find() or that returns a single element
	#print(item.stripped_strings)
	#.stripped_strings can not be executed like this.this will only print <generator ....>.so this will need to be executed like the above
#___________________________________
#-----------------------------------------------
# print(elmntsWithId.parent)
# print(elmntsWithId.parents) #.parents is a generator
# for parent in elmntsWithId.parents:
# 	print(parent)
# 	print(parent.name) #returns only the name of the parent tags
#-------------------------------------------------
# sibling = elmntsWithId.next_sibling
# nextSibling = elmntsWithId.next_sibling.next_sibling
# siblingprev = elmntsWithId.previous_sibling
# prevSibling = elmntsWithId.previous_sibling.previous_sibling
# print(sibling)
# print(nextSibling)
# print(siblingprev)
# print(prevSibling)
"""
------------------------
line breaks and spaces are also counted as an element in these sibling properties
------------------------
"""
#-------------------------------------------------------


"""
-------------------------
Difference between:
.contents===> returns a tag's childdren as a list and uses memory for which its slower.
.children===> returns a tag's childdren like a constant and is faster
--------------------------
"""


# textAll = soup.get_text() #returns all the texts inside html tags
# print(textAll)


#----Returns texts inside of some specified tags
#_______not applicable for soup.find_all().get_text()
# text = soup.find('p').get_text()
# print(text)


#----------------------------------------------
"""
----------------------------
Select elements with css-selector like Jquery{$('tag_name / .class_name / #id_name')}
----------------------------
"""
# jquerySelector = soup.select('#loginModal')
# jquerySelector = soup.select('.modal-footer')
# print(jquerySelector)
#------------------------------------------------