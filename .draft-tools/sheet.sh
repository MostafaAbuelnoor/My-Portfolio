#!/bin/bash
# usage: sheet.sh <start> <outprefix>  (10 drafts from start)
cd /tmp/claude-0/-home-user-My-Portfolio/c6a29b36-bb3e-51ea-a835-e1ca413da967/scratchpad/pfout
mk(){ ins=""; f=""; i=0; H=$(( $3*$4/$2 + 4 )); for k in 0 1 2 3 4 5 6 7 8 9; do n=$(printf %d $(( $START + k ))); ins="$ins -i $n-$1.png"; f="$f[$i]crop=$2:'min(ih,$3)':0:0,scale=$4:-2,pad=$4:$H:0:0:gray,pad=iw+12:ih+12:6:6:white[v$i];"; i=$((i+1)); done
 ffmpeg -loglevel error -y $ins -filter_complex "$f[v0][v1][v2][v3][v4]hstack=5[a];[v5][v6][v7][v8][v9]hstack=5[b];[a][b]vstack" $5; }
START=$1
mk d 1440 1500 560 $2-d.png; mk m 390 1500 300 $2-m.png
