#!/bin/bash

outdir=$1
executable=$2

build () {
    local commit=$1
    local outfile=$outdir/$commit
    [ -e $outfile ] && return
    echo $outfile
    git checkout --quiet $commit
    cargo build --release 2>&1 > /dev/null && \
        mv target/release/$executable $outfile || \
        echo build failed: $commit 1>&2
    git reset --hard HEAD
}

original_head=$(git rev-parse --abbrev-ref HEAD)
mkdir -p $outdir
git rev-list HEAD | while read commit; do build $commit; done
git checkout $original_head
