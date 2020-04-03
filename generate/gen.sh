rm -rf ../preview/*
mkdir -p ../preview
for i in linux tls dns network-packets advanced-containers reverse-proxies network-packets
do
    mkdir -p ../public/cards/$i
    ./generate.py $i
done

cd ..

python3 -m http.server 8000 --bind 0.0.0.0
