#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# #### Load the example dataset

# In[2]:

class FOFCPlugin:
 def input(self, inputfile):
  data_dir = inputfile
  self.df = pd.read_table(data_dir, sep="\t")

 def run(self):
  pass

 def output(self, outputfile):
  # #### Start Java VM

  # In[3]:


  from pycausal.pycausal import pycausal as pc
  pc = pc()
  pc.start_vm()


  # #### Load causal algorithms from the py-causal library and Run FOFC Continuous

  # In[4]:


  from pycausal import search as s
  tetrad = s.tetradrunner()
  tetrad.getAlgorithmParameters(algoId = 'fofc')


  # In[5]:


  tetrad.run(algoId = 'fofc', dfs = self.df, alpha = 0.01, useWishart = False, useGap = False, 
           include_structure_model = False, verbose = True)


  # #### FOFC Continuous' Result's Nodes

  # In[6]:


  tetrad.getNodes()


  # #### FOFC Continuous' Result's Edges

  # In[7]:


  tetrad.getEdges()


  # #### Plot The Result's Graph

  # In[8]:


  import pydot
  #from IPython.display import SVG
  dot_str = pc.tetradGraphToDot(tetrad.getTetradGraph())
  outf = open(outputfile+".txt", 'w')
  outf.write(dot_str)
  graphs = pydot.graph_from_dot_data(dot_str)
  graphs[0].write_png(outputfile)
  #svg_str = graphs[0].create_svg()
  #SVG(svg_str)


  # #### Stop Java VM

  # In[9]:


  pc.stop_vm()


  # In[ ]:




