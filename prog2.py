import os
import re 
import sys 

# python prog2.py out1.txt out2.txt 

#Steps
#Call script with input/output
#program parses through file and does transpose of date with aggregate values
#print output to output_file
	
	
def main():

	in_arg=sys.argv[1]
	out_arg=sys.argv[2]

	out_file = open( os.path.join(os.getcwd() ,out_arg ), "w")
	in_file = open( os.path.join(os.getcwd() ,in_arg ), "r") 
	AllItems=[]
	for line in in_file:
		TempItem=line.replace('\t', ' ')
		TempItem=TempItem.replace('\n', '')
		TempItem=TempItem.replace(' ', '~')
		TempArray = list(TempItem.split("~")) 

		remList=list(set(TempArray) - set(list(TempArray[0].split(' '))))
		print(remList)
		AllItems=AllItems+remList
		

	FinalListUniq=[]
	for x in AllItems: 
			if x not in FinalListUniq: 
				FinalListUniq.append(x) 
	MainString=""
	FinalListUniq.sort(reverse=True)
	for item in FinalListUniq:
		MainString=MainString+item+"\t"
		in_file = open( os.path.join(os.getcwd() ,in_arg ), "r") 
		for line1 in in_file:
			TempItem=line1.replace('\t', ' ')
			TempItem=TempItem.replace('\n', '')
			TempArray = list(TempItem.split(" ")) 
			if item in TempArray:
				MainString=MainString+TempArray[0]+"\t"
		MainString=MainString+"\n"
	MainString=MainString.replace(',', '')
	out_file.write(MainString)

	out_file.close()
	in_file.close()
	
	
main()