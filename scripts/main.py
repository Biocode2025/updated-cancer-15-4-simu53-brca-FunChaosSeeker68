import random



def gaford():
    alter_metirial=open('data/human_p53_coding.txt','r')
    alter_metirial2=''
    alter_metirial2 = ""
    DNA_codon_table = dict () 
    def Read_dict():
      file1 = open('data/codon_to_amino','r')
      for line in file1:
        part=line.split("\t")
        part1=part[0].rstrip("\n\r")
        part2 = part[1].rstrip("\n\r")
        DNA_codon_table[part1]=part2
      file1.close()
      return DNA_codon_table#מחזיר את שולחן הקודונים

    DNA_codon_table = Read_dict()


    for line in alter_metirial:
        if line[0] != ">":
            line=line.rstrip()
            alter_metirial2 = alter_metirial2 + line
    i=0
    amino_seq=""
    curr_codon=""
    while i<= len(alter_metirial2)-3:
        curr_codon=alter_metirial2[i]+alter_metirial2[i+1]+alter_metirial2[i+2]
        amino_seq = amino_seq + DNA_codon_table[curr_codon]
        i=i+3

    alterd_metirial=alter_metirial2
    alter_metirial.close()


    time=0
    genretion=0
    Q=0
    while Q <1000:#מריץ 1000
        k=0
        Q=Q+1
        amino_seq2=""
        alterd_metirial = alter_metirial2
        amino_seq2 = amino_seq
        mute_yes_no=0
        while amino_seq==amino_seq2:
            time=time+1
            mute_yes_no=random.randrange(1,10001)
            if mute_yes_no==1:
                argent=random.randrange(1,4)
                base_list = ['A','T','G','C']
                randy=random.randrange(1,101)
                if randy <= 98:
                    base_list = ['A','T','G','C']
                    randy=random.randrange(0,len(alterd_metirial))
                    base_list.remove(alterd_metirial[randy])
                    loock=random.randrange(0,3)
                    new_base=base_list[loock]
                    alterd_metirial=alterd_metirial[:randy]+new_base+alterd_metirial[randy+1:]
                elif randy == 100:
                    base_list= ['A','T','G','C']
                    randy=random.randrange(0,len(alterd_metirial))
                    loock=random.randrange(0,4)
                    new_base=base_list[loock]
                    alterd_metirial=alterd_metirial[:randy]+new_base+alterd_metirial[randy:] 
                elif randy == 99:
                    randy=random.randrange(0,len(alterd_metirial))
                    alterd_metirial=alterd_metirial[:randy]+alterd_metirial[randy+1:]
                    k=0
                    amino_seq2=""
                while k<= len(alterd_metirial)-3:
                    curr_codon=alterd_metirial[k]+alterd_metirial[k+1]+alterd_metirial[k+2]
                    amino_seq2 = amino_seq2 + DNA_codon_table[curr_codon]
                    k=k+3
    return time

Yes_or_No = (input("Does the Female has a BRCA1,2 mutation? (Y=Yes, N=No) "))
avregetime=0
Yes_or_No=Yes_or_No.upper()
print (Yes_or_No)
if Yes_or_No == "Y":
    avregetime=gaford()/1000
elif Yes_or_No == "N":
    avregetime=(gaford()+gaford())/1000
else: 
    print ("system error")
avregetime=avregetime/365
print(int(avregetime))
