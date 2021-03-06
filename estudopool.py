from pprint import pprint
import socket
import sys
import json

txt = """1.site.com.br
2.site.com.br/teste123
a.outrosite.com.br
b.outrosite.com.br
c.site.com.br
site.com.br/
3.outrosite.com.br"""

pool_domain = {}


def host2ip(domain):
	try:
		return socket.gethostbyname(domain)
	except Exception as e:
		return 'failed'

def makeArrayKeyIpValueHosts(txt):
	for line in txt.splitlines():
	  if "/" in line:
	  	print(line)
	  	domain = line.split('/')[0]
	  else:
	  	print(line)
	  	domain = line
	  ipDomain = host2ip(domain)

	  if ipDomain not in pool_domain:
	    pool_domain[ipDomain] = [line]
	    #pool_domain[ipDomain]['lastActivity'] = 'None'
	  else:
	    pool_domain[ipDomain].append(line)
	
	print(json.dumps(pool_domain, indent = 3, sort_keys=True))

if __name__ == "__main__":
	if not sys.stdin.isatty():
		txt = sys.stdin.read()

	makeArrayKeyIpValueHosts(txt)
