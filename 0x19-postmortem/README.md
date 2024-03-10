# 0x19-postmortem: Nginx Not Listening on Port 80 Issue

Issue Summary:
- Duration:  
  Start Time: January 29, 2024, 06:00 AM 
  End Time: February 2, 2024, 06:00AM 
- Impact:  
  The Nginx installation in the Ubuntu container was not listening on port 80 on all active IPv4 IPs, causing the web server to be inaccessible for incoming web traffic.
 
- On the above stated date I was assigned a debugging task to help develop my debugging skills. I was to find out what’s keeping my Ubuntu container’s Nginx installation from listening on port 80.
![DEBUGGING!](assigned.jpg)

- Somehow, I wondered where I could start from. Slowly I began investigating the Nginx configuration, service status, and port binding to identify the root cause of the port 80 listening failure.
![FOUND IT!](found.jpg)
- Oops! I discovered that the Nginx configuration file was missing the explicit listen 80; directive, which prevented Nginx from binding to port 80 on all active IPv4 IPs.

  So I attempted to manually add the listen 80; directive to the configuration, but little did I know that I also needed to check the firewall rules to ensure port 80 traffic was not blocked and the ufw rules allows incoming traffic on port 80.

  Shortly after doing this, the Nginx service was restarted, resolving the issue, and the web server started listening on port 80 of all active IPv4 IPs.
![FIXED AT LAST!](fixed.jpg)
# Root Cause and Resolution:
- Root Cause:  
  The root cause of the issue was the absence of the listen 80; directive in the Nginx configuration file, preventing Nginx from binding to port 80 and serving web traffic.
- Resolution:  
  The issue was resolved by updating the Nginx configuration to include the necessary listen 80; directive, adjusting firewall rules to allow traffic on port 80, and restarting the Nginx service to ensure it listened on port 80 on all active IPv4 IPs.

# Corrective and Preventative Measures:
- Corrective Actions:
  - Regularly review and update Nginx configuration files to ensure critical directives are present and correctly set.
  - Implement automated monitoring/alerting for critical service ports to detect future port listening failures promptly.
- Preventative Measures:
  - Perform periodic health checks on Nginx services to proactively identify and address potential configuration issues.
  - Establish a structured process for updating firewall rules to prevent unintended blockage of essential service ports.