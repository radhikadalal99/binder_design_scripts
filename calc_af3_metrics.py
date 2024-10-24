#!/usr/bin/python
import sys
import json

import json_stream
#data = json_stream.load(f)

def calc_pae_interface(jsonfilepath, pdbpath)
    pose=pose_from_file(pdbpath)
    interface_resis=pyrosetta.rosetta.protocols.interface.select_interface_residues(pose, 'A_B', 7) #reminder to use the pose that matches the chain order from af3 input but doesn't have chain C (gRNA)
    interface_resis=list(interface_resis)

    with open(f, 'r') as file:
      data = json_stream.load(jsonfilepath)
      results=(data["pae"])
      idex=0
      ipae=[]
      for i in list(results[0])[:1455]: 
          if int(list(x)[idex])!= 0:
              ipae.append(i)
          idex+=1
    return np.average(ipae)      
def plddt_monomer_binder(jsonfilepath)
  with open(f, 'r') as file:
      data = json_stream.load(file)
      results=data["atom_plddts"]
      plddts=[]
      for i in list(results)[1369:1455]: plddts.append(i)
  return np.average(plddts)
def plddt_complex(jsonfilepath)
  with open(f, 'r') as file:
    data = json_stream.load(file)
    results=data["atom_plddts"]
    plddts=[]
    for i in list(results)[1:1455]: plddts.append(i)
    return np.average(plddts)
def main()
  jsonfilepath=sys.argv[1]
  pdbpath=sys.argv[2]
  interface_PAE=calc_pae_interface(jsonfilepath, pdbpath)
  monomer_pLDDT=plddt_monomer_binder(jsonfilepath)
  plddt_complex=plddt_complex(jsonfilepath)
  with open("alphafold_scores.sc",'w+') as f:
    f.write(f"{pdbpath}\t{interface_PAE}\t{monomer_pLDDT}\t{plddt_complex}")
  
  
