from pyrosetta import *
init()
chBresis=[]
chAresis=[]
for i in range(1,len(pose.sequence())+1):
    for j in hbond_set.residue_hbonds(i):
        accres=pose.pdb_info().pose2pdb(j.acc_res())
        donres=pose.pdb_info().pose2pdb(j.don_res())
        if (accres[-2] != donres[-2]) or (donres[-2] != accres[-2]):
            if 'A' in accres and accres not in chAresis:
                chAresis.append(accres)
            elif 'A' in donres and donres not in chAresis:
                chAresis.append(donres)            
            if 'B' in accres and accres not in chBresis:
                chBresis.append(accres)
            elif 'B' in donres and donres not in chBresis:
                chBresis.append(donres) 
