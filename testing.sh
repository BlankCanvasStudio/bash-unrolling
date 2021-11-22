yep() {
echo global vars: $i $j
echo functional vars: $1
}
for i in 1 2; do
    for j in a b; do
        echo $i $j foo
        yep "$i .. $j"
    done
done