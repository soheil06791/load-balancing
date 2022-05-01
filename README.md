# load-balancing


### this is test for distribute request between multi server by haproxy also can request to each server to direct base server port.
### use framework : sanic python
### count servers : 4
### load servers : by docker-compose
### how create : docker-compose up <you can use -d for run in background> --build
### how use: for use, in your terminal you write :
	
<b>curl -H "CLIENT-KEY: <e.g. one>" $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' haproxy); echo </b>
