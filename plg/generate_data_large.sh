if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    echo "Enter data file"
    exit 1
fi

sz=$(wc -l < $1)
echo "Number of reviews: " $sz
# delete .pkl file if it alrady exists so that we can starto oveu
if [ -e 'data.pkl' ]
then
    echo "Pickle file already exists"
    echo "deleting"
    rm data.pkl
fi

counter=1
batch_size=100000
num_batches=50
#while [ $counter -le $(( $batch_size * $num_batches )) ]
while [ $counter -le $sz ]
do
    echo "Reading Review: " $counter
    counter2=$(( counter +  $batch_size - 1))
    sed -n -e "$counter, $counter2 p;$counter2 q" $1 > temp.json
    python generate_data_large.py
    (( counter += $batch_size))
done

#rename file
filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"
#echo $filename.pkl
if [ ! -d data_frames_fp ]
then
    mkdir data_frames_fp
fi
echo "Renaming file.."
#overrides existing file
if [ -f data_frames_fp/$filename.pkl ]
then
    echo "File name already exists"
    echo "Overriding.."
fi
mv data.pkl data_frames_fp/$filename.pkl
echo "Saved as: "data_frames_fp/$filename.pkl
