#!/bin/bash

    # Following by the #hash symbol are comments

ps | grep $$

    # This response shows that the shell you are
    # using is of type 'bash'.

echo "Hello world"

    # This response print the message in shell

mygreeting=5

    # Variable is case sensitive, supports for underscore,
    # even space counts
    # To access the variable use $ sign

a='jidhu     vijay'
echo $a "$a"
    #There is difference of using it inside quotes
echo "Before after space avoided by ooooo${a}ooooo"

\

    # Backslash is a escape statement in shell