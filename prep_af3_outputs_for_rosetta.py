#!/usr/bin/python

#alter af3 cif files, filter by RMSD
from pyrosetta import *
init()
import sys
import re

def get_chains_A_B(pose)
  dc=pyrosetta.rosetta.protocols.simple_moves.DeleteChainMover()
  dc.chain_num(3) #guideRNA chain
  dc.apply(pose)

def get_rmsd(pose, refpose,name)
  superimp=pyrosetta.rosetta.protocols.stepwise.modeler.align.superimpose_with_stepwise_aligner()
  superimp(pose,refpose)
  rmsd=pyrosetta.rosetta.protocols.stepwise.modeler.align.get_rmsd(refpose, pose)
  if rmsd < 2.0:
      pose.dump_pdb(f"{name}.pdb")
  return rmsd
def main()
  input_file=sys.argv[1]
  term=re.search("(\d+)_model, input_file)
  if term:
      path = glob.glob(f'/wynton/scratch/rdalal/colabfold_w_templates/cif_desns/*{term.group(1)}*.cif')
      if path:
          ref_file = path[0]
      else:
          print("No matching .cif file found.")
  else:
      print("Regex did not match.")
  pose=pose_from_file(input_file)
  refpose=pose_from_pdb(ref_file)
  get_chains_A_B(pose,name)
  rmsd=get_rmsd(pose,refpose)
  
  
