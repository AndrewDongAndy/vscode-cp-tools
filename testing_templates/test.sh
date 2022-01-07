FILENAME="sol.cpp"
CASES=500

rm a
rm slow

g++ $FILENAME -std=c++17 -D_DEBUG -D_GLIBCXX_DEBUG -Wall -Wextra -Wfatal-errors -Wpedantic -Wshadow -Wno-unused-parameter -O2 -o a
g++ slow.cpp -std=c++17 -D_DEBUG -D_GLIBCXX_DEBUG -Wall -Wextra -Wfatal-errors -Wpedantic -Wshadow -Wno-unused-parameter -O2 -o slow

for (( i = 0; i < $CASES; i++ ))
do
  python3.9 gen.py > "in"
  ./a < "in" > "out"
  ./slow < "in" > "ok"
  lines=$( diff out ok | wc -l )
  if (( $lines > 0 ))
  then
    echo "failed test case #$i:"
    echo $( diff out ok )
    exit 0
  fi
  echo "passed test case #$i"
done

echo "passed $CASES test cases"
