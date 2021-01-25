import os
import sys
import time

xdoc = '''<!DOCTYPE html>
<html>
<head>
<HTA:APPLICATION
APPLICATIONNAME="Hello World"
BORDER="none"
BORDERSTYLE="none"
CAPTION="no"
ICON="img/favicon.ico"
MAXIMIZEBUTTON="no"
MINIMIZEBUTTON="no"
SHOWINTASKBAR="yes"
WINDOWSTATE="normal"
INNERBORDER="no"
NAVIGABLE="yes"
SCROLL="no"
SCROLLFLAT="no"
SYSMENU="no"
SINGLEINSTANCE="yes"
CONTEXTMENU="yes"
SELECTION="yes"
VERSION="1.0" />
</head>
<body bgcolor="#050505">

<script type="text/javascript">

	window.resizeTo(700,500);
	window.moveTo(250,50);
	window.focus();

	function exitAPP() {

		window.close();
	}

</script>

<style type="text/css">

body, html {

	background:#050505;
	background-size:cover;
	width:100%;
	height:100%;
	overflow:hidden;
}

#closeBTN {

	position:absolute;
	top:5px;
	right:13px;
	font-family:Consolas;
	font-size:16px;
	font-weight:bold;
	color:#8a8a8a;
	cursor:pointer;
}

#closeBTN:hover {

	position:absolute;
	top:5px;
	right:13px;
	font-family:Consolas;
	font-size:16px;
	font-weight:bold;
	color:#ffffff;
	cursor:pointer;
}

</style>

<font id="closeBTN" onclick="exitAPP();">close</font>

</body>
</html>
'''

class wapp:

	def create(xvar):

		xpath = str(xvar.replace(" ","-").lower())
		ximgs = str(xpath+'//img')
		xtico = str('favicon.ico')
		xicon = str(ximgs+'//'+xtico)
		os.mkdir(xpath)
		os.mkdir(ximgs)
		mvicon = str('copy "'+xtico+'" "'+xicon+'"')
		os.system(mvicon)
		xapp = str(xpath+'//index.hta')
		xfile = open(xapp, 'w')
		xfile.write(xdoc)
		xfile.close()
		os.system('START '+xapp)
