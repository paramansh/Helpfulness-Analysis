if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    echo "Enter data file"
    exit 1
fi

sz=$(wc -l < $1)
echo "Number of reviews: " $sz

if [ -f fingerprints.txt ]
then
    rm fingerprints.txt
fi
touch fingerprints.txt

counter=1
batch_size=100000
num_batches=50
#while [ $counter -le $(( $batch_size * $num_batches )) ]
while [ $counter -le $sz ]
do
    echo "Reading Review: " $counter
    counter2=$(( counter +  $batch_size - 1))
    sed -n -e "$counter, $counter2 p;$counter2 q" $1 > temp.json
    python generate_fingerprints.py
    (( counter += $batch_size))
done

#rename file
filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"
#echo $filename.pkl
if [ ! -d fingerprints ]
then
    mkdir fingerprints
fi
echo "Renaming file.."
#overrides existing file
if [ -f data_frames/$filename.pkl ]
then
    echo "File name already exists"
    echo "Overriding.."
fi
mv fingerprints.txt fingerprints/$filename.txt
echo "Saved as: "fingerprints/$filename.txt
