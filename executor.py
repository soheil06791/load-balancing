import subprocess
import os
import random



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def execute():
    os.chdir(os.path.split(os.path.abspath(__file__))[0])
    check_version = subprocess.check_output(["bash","check.sh"]).decode().split(" ")
    if check_version[1] < "20.10.0":
        print(f"{bcolors.WARNING}docker version is lower of 20.10.0{bcolors.ENDC}")
        return
    os.system("docker-compose rm -fs")
    os.system("docker build -t api:v1.0.0 ./api")
    os.system("docker-compose  up -d ")
    ip_haproxy =subprocess.check_output(["docker", "inspect", "-f", "'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", "haproxy"])
    
    check_nginx =os.system(' '.join(["service","--status-all", "|", "grep", "nginx"]))
    
    if check_nginx == 256:
        print(f"{bcolors.WARNING}please install nginx on operation system{bcolors.ENDC}")
        return
    
    nginx = """events {}
                        http{
                        server {

                            listen 80;
                            server_name localhost;
                            access_log /var/log/nginx/access.log;
                            location / {
                            proxy_pass http://$Haproxy;
                            }
                        }
                        }"""
        
    nginx = nginx.replace("$Haproxy", ip_haproxy.decode().replace('\n', '')).replace("'","")
    with open('nginx.conf', mode='w') as f:
        f.write(nginx)
    try:
        subprocess.check_output(["cp", "/etc/nginx/nginx.conf", "/etc/nginx/nginx.confold"])
        subprocess.check_output(["cp", "nginx.conf", "/etc/nginx/"])
        subprocess.check_output(['systemctl', 'restart', 'nginx'])
    except:
        print(f"{bcolors.WARNING}pleas run python file with root or sudo python3 executor.py{bcolors.ENDC}")
        return

    key = ['one', 'two', 'three', 'four']
    for i in range(100):
        os.system(f"""curl -H "CLIENT-KEY: {random.choice(key)}" localhost;echo""")
    print(f"""{bcolors.OKBLUE}for new key write curl -H "CLIENT-KEY: five" localhost;echo{bcolors.ENDC}""")
    print(f"{bcolors.OKBLUE}for see all key on each server type  ===>{bcolors.BOLD}curl localhost;echo<==={bcolors.ENDC}")

if __name__ == "__main__":
    execute()