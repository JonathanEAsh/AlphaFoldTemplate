import os
import subprocess
import os.path
import time
ctr=0
for files in os.listdir('protease_out/'):
	if os.path.isfile('protease_out/'+files+'/seq_0_model_1.pdb')==False:
		process1=subprocess.Popen(['squeue','-u','ja961'], stdout=subprocess.PIPE)
		process2=subprocess.check_output(['wc','-l'], stdin=process1.stdout)
		while int(process2)>=500:
			time.sleep(300)
			process1=subprocess.Popen(['squeue','-u','ja961'], stdout=subprocess.PIPE)
			process2=subprocess.check_output(['wc','-l'], stdin=process1.stdout)
		#command="sbatch python relax_run.py --og_seq="+og_seq+" --design_seq="+design_seq+" --design_num="+str(design_ctr)
		
		print(files)
		#subprocess.run(['sbatch', '--time=10:00:00','--mem=64G','--output=/dev/null','--error=/dev/null','./submit_af2.sh', str(files)])
		#subprocess.run(['sbatch', '--time=10:00:00','--mem=64G','--partition=gpu','--gres=gpu:1','./submit_af2.sh', str(files)])
		subprocess.run(['sbatch', '--time=10:00:00','--mem=64G','--nodes=2','./submit_af2.sh', str(files)])
		# ctr+=1
		# if ctr == 5:
		# 	break