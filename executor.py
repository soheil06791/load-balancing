import subprocess
import os
import random

def execute():
    os.chdir(os.getcwd())
    os.system("docker-compose rm -fs")
    os.system("docker-compose  up -d --build")
    ip_haproxy =subprocess.check_output(["docker", "inspect", "-f", "'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", "haproxy"])
    
    check_nginx =os.system(' '.join(["service","--status-all", "|", "grep", "nginx"]))
    
    if check_nginx == 256:
        print("please install nginx on operation system")
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
        print("pleas run python file with root or sudo python3 executor.py")
        return

    key = ['one', 'two', 'three', 'four']
    for i in range(100):
        os.system(f"""curl -H "CLIENT-KEY: {random.choice(key)}" localhost;echo""")
    print("""for new key cammand  [curl -H "CLIENT-KEY: five" localhost;echo]""")
    print("for see all key on each server type  ===>curl localhost<===")

if __name__ == "__main__":
    execute()