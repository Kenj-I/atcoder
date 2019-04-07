# $1 category
# $2 number

if [[ ! $1 =~ abc|arc|agc ]]; then
  echo 'Not correct category. Category is abc, arc, agc'
  exit
fi

if [[ ! $2 =~ [0-9]{1,3} ]]; then
  echo 'Not correct number format'
  exit
fi

category=`echo $1 | tr '[a-z]' '[A-Z]'`
number=`printf %03d $2`


if [ ! -e $category ]; then mkdir $category; fi
  target=$category/$number
if [ ! -e $target ]; then
  mkdir $target
  touch $target/input.txt
  echo "Create ${target}/input.txt"
  if [ $1 = 'abc' ]; then
    files=(A B C D)
  elif [ $1 = 'agc' ]; then
    files=(A B C D)
  elif [ $1 = 'arc' ]; then
    if [ $2 -gt 57 ]; then
      files=(C D E F)
    else
      files=(A B C D)
    fi
  fi

  for var in ${files[@]}
  do
    touch $target/$var.py
    echo "Create ${target}/${var}.py"
  done
else
  echo 'Not crate'
fi