#!/usr/bin/env bash

# validate format of provided
validate_modulename() {
    case $1 in
    .* ) 
        echo "module name should not start with period"
        exit 1 
        ;;    
    *. ) 
        echo "module name should not end with period"
        exit 1 
        ;;   
    *[^a-zA-Z.]* ) 
        echo "module name should include only alpha characters"
        exit 1
        ;;
    *..* )
        echo "module name contains duplicated periods"
        exit 1    
    esac
    echo "$1"
}

# capitalize first letter of each word in string
title_case() { 
    echo "$1" | gsed -E "s/[[:alnum:]_'-]+/\u&/g"
}

# convert module name to class name
classify() {
    local titlecased
    titlecased=$(title_case "$1")
    echo "${titlecased//.}"
}
