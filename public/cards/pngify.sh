rm -rf */*.png
for i in "$@"
do
    inkscape \
        --export-png=${i/.svg/.png} --export-dpi=200 \
        --export-background-opacity=0 --without-gui $i
    echo $i '=>' ${i/.svg/.png}
done

