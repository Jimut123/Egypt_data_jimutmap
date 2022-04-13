# run inside Delhi folder
i=0; 
for f in *; 
do 
    d=Delhi_$(printf %03d $((i/25000+1))); # 20480 = file count; 
    mkdir -p $d; 
    mv "$f" $d; 
    let i++; 
done



