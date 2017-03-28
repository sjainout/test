#
# https://pypi.python.org/pypi/yahoo-finance
#

from yahoo_finance import Share

yahoo = Share("YHOO")
print "Yahoo Open Price = " + yahoo.get_open()
