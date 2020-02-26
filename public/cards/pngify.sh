for i in *.svg
do
    convert $i png/`basename $i .svg`.png
done

