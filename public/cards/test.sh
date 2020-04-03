for i in kill ctrlc stop-kill pipe-read use-sockets unix-differences read-file inherit threads-share proc same-address allocate-more use-more-memory shared-library-memory mmap
do
    echo "$i:"
    echo "    question:"
    echo "        big: |"
    grep 'id="tspan..">' linux/$i.svg |  sed 's:</tspan></text>::g' | sed 's:id="tspan..">:   :g'| sed 's:</tspan><tspan::g'
    echo "    answer:"
    echo "        big: |"
    echo "        small: |"
    grep 'id="tspan..">' linux/$i-back.svg |  sed 's:</tspan></text>::g' | sed 's:id="tspan..">:   :g' | sed 's:</tspan><tspan::g'
done
