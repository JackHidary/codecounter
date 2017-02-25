

import urllib.request
import json

def get_users() :


	users = urllib.request.urlretrieve ("https://api.github.com/users?since=111", "testusers.txt")
	print(users)
	usersList = list(users)
	print(usersList)
	for item in usersList:
		pass
		#print(item)


	return users


"""
def get_repos (users) :
USER='AUSER'
API_TOKEN='ATOKEN'
GIT_API_URL='https://api.github.com'
def get_api(url):
    try:
        request = urllib2.Request(GIT_API_URL + url)
        base64string = base64.encodestring('%s/token:%s' % (USER, API_TOKEN)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)
        result.close()
    except:
        print 'Failed to get api request from %s' % url
    return (repos)
def get_lines (repos) :
git ls-files | [cat all these files] | wc -l
    return (lines)
"""
def main() :

	userslist1 = get_users()
	#print(type(userslist1))

	#for item in userslist1:
		#pass
		#print(item)



main ()
