# Download sonar-scanner and unzip it
wget "https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip" -O "/tmp/sonar-scanner.zip"
unzip /tmp/sonar-scanner.zip -d /tmp && mv /tmp/sonar-scanner-3.2.0.1227-linux /tmp/sonar-scanner
rm /tmp/sonar-scanner.zip
# Set extracted sonar-scanner location to $PATH so we can use commands
export SONAR_SCANNER_HOME="/tmp/sonar-scanner"
export PATH="$SONAR_SCANNER_HOME/bin:$PATH"