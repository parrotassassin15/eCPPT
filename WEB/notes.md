# Web Security Notes Udemy ( Parrotassassin15 )


## Sections: 

* WebMap ( Docker Container )
* Nmap Automater ( Shell Script )
* 

## Important Notes: 

* 

<br>
<br>

### WebMap 

<br>

Installation and Usage: 

1.  ` sudo docker run -d --name webmap -h webmap -p 8000:8000 -v /opt/scan-results/:/opt/xml reborntc/webmap `

2. start the container: ` docker start webmap `

3. output nmap xml scans to /opt/xml directory 

4. generate the token ` docker exec -ti webmap /root/token `

5. login with that token and view your resuts 



<br>

### NmapAutomator

<br>

Installation and Usage: 

1. ` git clone https://github.com/21y4d/nmapAutomator.git `

2. `./nmapAutomator.sh -H <ip or url> -t <scan type>`

