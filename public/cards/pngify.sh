rm -rf png/
mkdir png
for i in *.svg
do
    inkscape \
        --export-png=png/`basename $i .svg`.png --export-dpi=200 \
        --export-background-opacity=0 --without-gui $i
    echo $i
done

