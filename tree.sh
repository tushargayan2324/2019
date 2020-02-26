#!/bin/bash
FILES=/home/tsg19ms153/Documents/bio_prac/Rajib_tree_data_1/*
for f in  $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  #convert $f -threshold 50% -define histogram:unique-colors=true -format %c histogram:info:- | awk '{print substr($1,1,length($1)-1)}' | cat  >> pixel.dat
  convert $f -threshold 50% -define histogram:unique-colors=true -format %c histogram:info:- | awk  '{ printf( "%s ", substr($1,1,length($1)-1) ); } END { printf( "\n" ); }'|awk '{print $1,$2,$1/$2}'| cat  >> pixel_rajib_1.dat
  
  #cat $f
done

#awk 'BEGIN{getline to_add < "f3"}{print $0,to_add}'
