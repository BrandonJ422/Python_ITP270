#!/bin/bash


echo "Please enter your name:"

read name



echo "Please enter your age:"

read age



echo "Please enter your degree program:"

read degree


remaining_age=$(expr $age \* 3 / 2)



echo "Hello, my name is $name. My remaining age is $remaining_age and I am currently studying $degree."

