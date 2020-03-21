for i in `grep '^\w' $1.yaml | sed 's/://'`
do
    inkscape ../public/cards/$1/$1.svg
    inkscape ../public/cards/$1/$1-back.svg
done
