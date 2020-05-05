
import os

files = ["Instances_genome/Inst_0000010_7.adn","Instances_genome/Inst_0000010_8.adn","Instances_genome/Inst_0000010_44.adn","Instances_genome/Inst_0000012_32.adn","Instances_genome/Inst_0000012_56.adn"]


for i in range(len(files)-1,len(files)):

    print("fichier :",files[i])
    os.system("python adn.py "+files[i]+" -distnaif -t")
	
