#! /bin/bash

# Armand Abrahamian
# COMP 490/L: Prof. Fitzgerald
# 9/12/16

# This is a little CGI program

###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The MIME type of associated with the option body of the HTTP request.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOST:         The name of the vhost of the server.  
# HTTP_USER_AGENT:   Information about the browser/client that made requested.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. The most common methods are GET and POST.
# REQUEST_URI:       The URI of the request
# SERVER_PROTOCOL:   Currently HTTP/1.1
# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address
# SERVER_PORT:       The port of the server

#      Added a content type and a blank line
echo "Content-type: text/html"
echo ""

# 		Link CSS style sheet.
echo '<link rel="stylesheet" href="http://www.csun.edu/~aya42388/cgi-bin/style.css" type="text/css">'
echo "<a href="http://www.csun.edu/~aya42388/cgi-bin/style.css">Press here for link to CSS sheet.</a><br /><br />"

# 		Start HTML Content
echo "<head><title>Welcome to Armand's CGI Interface!</title></head>"
echo "<tt><strong>Time: </strong>"
echo "<tt style=\"text-align:center; color:green\">"
date
echo "</tt></tt><br />"

#echo '<body>'
#echo 'Environment Variables:'
#echo '<pre>'
#/usr/bin/env
#echo '</pre>'
#echo '</body>'

#echo $SCRIPT_NAME
#echo $SERVER_NAME
#echo $SERVER_PORT
echo "<p>" 
echo "URI: "
echo $REQUEST_URI
echo "</p>"

echo "$REQUEST_METHOD:"
echo "   $QUERY_STRING"
#echo "Everything after the first ='s:"
#output=$(echo $QUERY_STRING | cut -d'=' -f2)
#echo $output
echo "<br /><br />"

echo "Extracting information from <a href="http://www.csun.edu/engineering-computer-science">http://www.csun.edu/engineering-computer-science</a>:"
echo "<br /><br />"

/usr/bin/curl -o /tmp/csun-aya42388   http://www.csun.edu/engineering-computer-science
cat /tmp/csun-aya42388

if [ -n "${QUERY_STRING}" ] ; then 
   cat  ./${QUERY_STRING}
fi

# Read the body -- if it is a post
while read _post_line ; do
  echo ${_post_line} ";loop"
done 
echo $_post_line

exit 0
