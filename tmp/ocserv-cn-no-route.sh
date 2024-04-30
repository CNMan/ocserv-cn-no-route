cd /root/githubrepo/ocserv-cn-no-route/tmp
wget -N https://gitlab.com/ocserv/ocserv/raw/master/doc/sample.config

python3 ocserv-cn-no-route.py

cd /root/githubrepo/ocserv-cn-no-route
rm -rf .git/
git init
git remote add origin git@github.com:CNMan/ocserv-cn-no-route.git
git add .
git commit -m "`date`"
git push -f origin master
