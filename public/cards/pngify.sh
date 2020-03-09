for i in "$@"
do
if [[ $i == *"back"* ]]; then
    convert -background none -density 400 $i \
        -channel rgba -alpha set \
        -fill '#d9a36e' -opaque none \
        -define png:exclude-chunk=time,date \
        -alpha off -negate ${i/.svg/.png}
else
    convert -background white -density 400 $i \
        -define png:exclude-chunk=time,date \
        ${i/.svg/.png}
fi
    echo $i '=>' ${i/.svg/.png}
done

