rm -rf ../preview/*
mkdir -p ../preview
#for i in linux tls dns network-packets advanced-containers reverse-proxies network-packets
for i in sql-basics
do
    ./generate.py $i
done

cd ..

python3 -m http.server 8000 --bind 0.0.0.0
