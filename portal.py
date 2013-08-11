from flask import Flask
import locale
locale.setlocale( locale.LC_ALL, '' )
app = Flask(__name__, static_folder='static', static_url_path='')
event = {}

@app.route('/')
def index():
	f = open('index.html')
	page = f.read()
	f.close()

	portalStatus = ''
	color = ''
	name = ''
	accountDollars = 0.00
	eventName = ''
	dueTime = ''
	foodEta = ''
	orderStatus = ''
	orderStatusButtons = ''
	paidStatus = ''
	items = ''

	if len(event.keys()) == 0:
		portalStatus = 'Closed'
		color = 'Red'
		name = 'Test Name'
		accountDollars = 12.34
		page = page.replace('PORTALSTATUS', portalStatus)
		page = page.replace('COLOR', color)
		page = page.replace('EVENT', 'Nothing happening right now...')
		page = page.replace('NAME', name)
		page = page.replace('ACCOUNTDOLLARS', locale.currency(accountDollars))
		page = page.replace('PAGESTUFF', '')
		return page
	
	pageStuff = open('openportal.html')
	page = page.replace('PAGESTUFF', pageStuff.read())
	pageStuff.close()
	
	portalStatus = 'Open'
	color = 'Green'
	name = 'Test Name'
	accountDollars = 12.34
	eventName = event['name']
	dueTime = event['dueTime']
	foodEta = event['foodEta']
	orderStatus = 'Placed'
	if orderStatus == 'Placed':
		buttonsHtmlFile = open('orderbuttons.html')
		orderButtons = buttonsHtmlFile.read()
		buttonsHtmlFile.close()
	paidStatus = 'Yes'
	for section in event['items'].keys():
		items += '<h3 class="col-lg-12 text-center">'
		items += section
		items += '</h3>'
		counter = 0
		column1 = '<div class="col-lg-3">'
		column2 = '<div class="col-lg-3">'
		column3 = '<div class="col-lg-3">'
		column4 = '<div class="col-lg-3">'
		for item in event['items'][section].keys():
			itemHtml = '<input type="checkbox" name="items"><span id="check">'
			itemHtml += ' ' + item + ' ' + locale.currency(event['items'][section][item])
			itemHtml += '</span></input>'

			if counter <= len(event['items'][section].keys()) * 1.0 / 4:
				column1 += itemHtml
			elif counter <= len(event['items'][section].keys()) * 2.0 / 4:
				column2 += itemHtml
			elif counter <= len(event['items'][section].keys()) * 3.0 / 4:
				column3 += itemHtml
			else:
				column4 += itemHtml

			counter += 1
		column1 += '</div>'
		column2 += '</div>'
		column3 += '</div>'
		column4 += '</div>'
		items += column1 + column2 + column3 + column4

	page = page.replace('PORTALSTATUS', portalStatus)
	page = page.replace('COLOR', color)
	page = page.replace('NAME', name)
	page = page.replace('ACCOUNTDOLLARS', locale.currency(accountDollars))
	page = page.replace('EVENT', eventName)
	page = page.replace('DUETIME', dueTime)
	page = page.replace('FOODETA', foodEta)
	page = page.replace('ORDERSTATUS', orderStatus)
	page = page.replace('ORDERBUTTONS', orderButtons)
	page = page.replace('PAIDSTATUS', paidStatus)
	page = page.replace('ITEMS', items)
	return page

if __name__ == '__main__':
	#going to be loaded from a mongodb thingy
	event = {'name':'Chinese Food', 'dueTime':'7:00', 'foodEta':'7:30', 'items':{'entrees':{'chicken':6.25, 'pork':4.50, 'chickenandpork':12.76}, 'sides':{'rice':2.00, 'soup':1.75}}}
	app.run(host='0.0.0.0', debug=True)
