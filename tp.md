1 
mkdir tpLinux

2
tree 

3
cd ./tpLinux
 touch fic1.txt 
 touch fic2.txt 
 touch fichier.md 
 touch image.jpg 
 touch exos.md 
 touch exoos.txt

4
mkdir dosA
mkdir dosD
cd ./dosA
mkdir dosB
mkdir dosC

5
cd ../
mv ./fi* ./dosA/dosB

6
cd ./dosA/dosB
cp fic1.txt ../
cp fic2.txt ./
cp ./fichier.md ../.././dosD

7
cd ../../
echo "bonjour tout le monde" >> fic1.txt

8
$ find ./ -name '*.???'

9
mv ./exoos.txt ./exos.txt

10

