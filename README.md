# Synthetic jet simulation with SU2  
This project is set to solve the problem of the absence of changing boundary conditions(BCs) with time in Stanford University Unstructured(SU2). It is mainly based on Python Scripts. If any criticism or correction, please contact me via mengqinghe0909@126.com  
## The basic structure of the codes  
The *python codes* are managed with the basic structure to monitor the working directory with new temporal result files. If new file detected, the *python codes* will change the *configuration file* to change the BCs and start SU2 with new *configuration file*. SU2 will output a new temporal result file and new cycle starts.  
## The preparation for the simulation
### The code is based on python files. Before the work, you should prepare the following files:  
1. SU2 configuration file(*.cfg)  
2. *.bat file to start SU2  
3. mesh file(*.cgns or *.SU2)
4. necessary result files and necessary restart files
### Environment preparation  
1. [environment for SU2](https://su2code.github.io/docs_v7/Installation/)  
