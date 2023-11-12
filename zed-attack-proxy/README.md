# Usage
1. Download the ZAP application.
2. ``docker-compose up``
    * Starts an image of a vulnerable web application. 
3. Visit http://localhost:81 
    * Login without credentials to config the website.
    * Click the **Create/Reset Database** button, this will initialize the User table for you.
    * Login using - username:admin password: password.

# Zed Attack Proxy
OWASP Zed Attack Proxy (ZAP) is the world’s most widely used web application security testing
tool which is free and open source.
* Download link: https://www.zaproxy.org/download/

# DVWA Image
Damn Vulnerable Web Application (DVWA), vulnerable web application to test ZED on.
* https://hub.docker.com/r/vulnerables/web-dvwa
* 
