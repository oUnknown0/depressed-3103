# Docker Containers
The [docker-compose.yml](docker-compose.yml) will create 4 containers - Nginx, Jenkins, SonarQube and PostgresSQL DB.
* Jenkins is built using a custom Dockerfile that installs docker, docker-compose, docker cli and 3 jenkins plugins - BlueOcean, OWASP Dependency Checks and SonarQube Scanner.

## Setting Jenkins with OWASP Dependency Checks and SonarQube
1. Dockerfile will build a Jenkins image with the following plugins:
    * BlueOcean Plugin
    * OWASP Dependency Check
    * SonarQube Scanner
2. To configure OWASP Dependency Check:
    *  Manage Jenkins > Tool Configuration > Add Dependency Check > Install Automatically > Add installer automatically and select the git version.
3. Setting up SonarQube:
    * Follow X09 SonarQube Lab.
    * Login using admin/admin.
    * Create project manually > name your project **OWASP** with Project Key **OWASP** > Use Global Settings > Locally > Generate a Token for the OWASP project.
    * SonarQube is now configured. You can integrate SonarQube with Jenkins using the SonarQube Scanner.
4. Integrating SonarQube with SonarQube Scanner.
    * Manage Jenkins > System Configuration > Add SonarQube > Add authentication token as secret text (the token u generated for OWASP project). 
    * Tool Configuration > SonarQube Scanner > Add SonarQube Scanner and name it **SonarQube** > Install automatically (from Maven Central).