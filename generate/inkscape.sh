for i in `grep '^\w' $1.yaml | sed 's/://'`
do
    inkscape ../public/cards/$1/$i.svg
    inkscape ../public/cards/$1/$i-back.svg
done
