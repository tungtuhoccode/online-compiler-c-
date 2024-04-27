# cd into app folder in the container image
cd "/app" 
# echo "Compiling main.cc"
# echo "g++ -o main main.cc"

g++ -o main main.cc

# echo "running main"

./main