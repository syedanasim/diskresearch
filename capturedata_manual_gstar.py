########################################################################################################

#gstar, SG
#capturedata_1e1_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e1_45_gstar_SG.txt")
capturedata_1e2_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e2_45_gstar_SG.txt")
capturedata_1e3_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e3_45_gstar_SG.txt")
capturedata_1e4_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e4_45_gstar_SG.txt")
#capturedata_1e5_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e5_45_gstar_SG.txt")
#capturedata_1e6_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e6_45_gstar_SG.txt")
#capturedata_1e7_45_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e7_45_gstar_SG.txt")

capturedata_1e4_5_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e4_5_gstar_SG.txt")
capturedata_1e4_15_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e4_15_gstar_SG.txt")
capturedata_1e4_30_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e4_30_gstar_SG.txt")
capturedata_1e4_60_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e4_60_gstar_SG.txt")
capturedata_1e4_80_gstar_SG=loadtxt("capturedata/capturedataSG/gstar/capturedata_1e4_80_gstar_SG.txt")

####################################################

capturedata_a_gstar_SG=[[],[],[]]

#capturedata_a_gstar_SG[0].append(capturedata_1e1_45_gstar_SG[0][0]/Rg)
#capturedata_a_gstar_SG[1].append(capturedata_1e1_45_gstar_SG[0][len(capturedata_1e1_45_gstar_SG[0])-1]/Rg)
#capturedata_a_gstar_SG[2].append(capturedata_1e1_45_gstar_SG[3][len(capturedata_1e1_45_gstar_SG[3])-1])

capturedata_a_gstar_SG[0].append(capturedata_1e2_45_gstar_SG[0][0]/Rg)
capturedata_a_gstar_SG[1].append(capturedata_1e2_45_gstar_SG[0][len(capturedata_1e2_45_gstar_SG[0])-1]/Rg)
capturedata_a_gstar_SG[2].append(capturedata_1e2_45_gstar_SG[3][len(capturedata_1e2_45_gstar_SG[3])-1])

capturedata_a_gstar_SG[0].append(capturedata_1e3_45_gstar_SG[0][0]/Rg)
capturedata_a_gstar_SG[1].append(capturedata_1e3_45_gstar_SG[0][len(capturedata_1e3_45_gstar_SG[0])-1]/Rg)
capturedata_a_gstar_SG[2].append(capturedata_1e3_45_gstar_SG[3][len(capturedata_1e3_45_gstar_SG[3])-1])

capturedata_a_gstar_SG[0].append(capturedata_1e4_45_gstar_SG[0][0]/Rg)
capturedata_a_gstar_SG[1].append(capturedata_1e4_45_gstar_SG[0][len(capturedata_1e4_45_gstar_SG[0])-1]/Rg)
capturedata_a_gstar_SG[2].append(capturedata_1e4_45_gstar_SG[3][len(capturedata_1e4_45_gstar_SG[3])-1])

#capturedata_a_gstar_SG[0].append(capturedata_1e5_45_gstar_SG[0][0]/Rg)
#capturedata_a_gstar_SG[1].append(capturedata_1e5_45_gstar_SG[0][len(capturedata_1e5_45_gstar_SG[0])-1]/Rg)
#capturedata_a_gstar_SG[2].append(capturedata_1e5_45_gstar_SG[3][len(capturedata_1e5_45_gstar_SG[3])-1])

#capturedata_a_gstar_SG[0].append(capturedata_1e6_45_gstar_SG[0][0]/Rg)
#capturedata_a_gstar_SG[1].append(capturedata_1e6_45_gstar_SG[0][len(capturedata_1e6_45_gstar_SG[0])-1]/Rg)
#capturedata_a_gstar_SG[2].append(capturedata_1e6_45_gstar_SG[3][len(capturedata_1e6_45_gstar_SG[3])-1])

#capturedata_a_gstar_SG[0].append(capturedata_1e7_45_gstar_SG[0][0]/Rg)
#capturedata_a_gstar_SG[1].append(capturedata_1e7_45_gstar_SG[0][len(capturedata_1e7_45_gstar_SG[0])-1]/Rg)
#capturedata_a_gstar_SG[2].append(capturedata_1e7_45_gstar_SG[3][len(capturedata_1e7_45_gstar_SG[3])-1])

####################################################

capturedata_i_gstar_SG=[[],[]]

capturedata_i_gstar_SG[0].append(capturedata_1e4_5_gstar_SG[1][0])
capturedata_i_gstar_SG[1].append(capturedata_1e4_5_gstar_SG[3][len(capturedata_1e4_5_gstar_SG[3])-1])

capturedata_i_gstar_SG[0].append(capturedata_1e4_15_gstar_SG[1][0])
capturedata_i_gstar_SG[1].append(capturedata_1e4_15_gstar_SG[3][len(capturedata_1e4_15_gstar_SG[3])-1])

capturedata_i_gstar_SG[0].append(capturedata_1e4_30_gstar_SG[1][0])
capturedata_i_gstar_SG[1].append(capturedata_1e4_30_gstar_SG[3][len(capturedata_1e4_30_gstar_SG[3])-1])

capturedata_i_gstar_SG[0].append(capturedata_1e4_45_gstar_SG[1][0])
capturedata_i_gstar_SG[1].append(capturedata_1e4_45_gstar_SG[3][len(capturedata_1e4_45_gstar_SG[3])-1])

capturedata_i_gstar_SG[0].append(capturedata_1e4_60_gstar_SG[1][0])
capturedata_i_gstar_SG[1].append(capturedata_1e4_60_gstar_SG[3][len(capturedata_1e4_60_gstar_SG[3])-1])

capturedata_i_gstar_SG[0].append(capturedata_1e4_80_gstar_SG[1][0])
capturedata_i_gstar_SG[1].append(capturedata_1e4_80_gstar_SG[3][len(capturedata_1e4_80_gstar_SG[3])-1])

########################################################################################################

########################################################################################################

#gstar, TQM
#capturedata_1e2_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e2_45_gstar_TQM.txt")
capturedata_1e3_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e3_45_gstar_TQM.txt")
capturedata_1e4_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_45_gstar_TQM.txt")
capturedata_1e5_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e5_45_gstar_TQM.txt")
#capturedata_1e6_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e6_45_gstar_TQM.txt")
#capturedata_1e7_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e7_45_gstar_TQM.txt")

#capturedata_1e4_5_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_5_gstar_TQM.txt")
#capturedata_1e4_15_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_15_gstar_TQM.txt")
capturedata_1e4_30_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_30_gstar_TQM.txt")
capturedata_1e4_60_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_60_gstar_TQM.txt")
#capturedata_1e4_80_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_80_gstar_TQM.txt")

####################################################

capturedata_a_gstar_TQM=[[],[],[]]

#capturedata_a_gstar_TQM[0].append(capturedata_1e2_45_gstar_TQM[0][0]/Rg)
#capturedata_a_gstar_TQM[1].append(capturedata_1e2_45_gstar_TQM[0][len(capturedata_1e2_45_gstar_TQM[0])-1]/Rg)
#capturedata_a_gstar_TQM[2].append(capturedata_1e2_45_gstar_TQM[3][len(capturedata_1e2_45_gstar_TQM[3])-1])

capturedata_a_gstar_TQM[0].append(capturedata_1e3_45_gstar_TQM[0][0]/Rg)
capturedata_a_gstar_TQM[1].append(capturedata_1e3_45_gstar_TQM[0][len(capturedata_1e3_45_gstar_TQM[0])-1]/Rg)
capturedata_a_gstar_TQM[2].append(capturedata_1e3_45_gstar_TQM[3][len(capturedata_1e3_45_gstar_TQM[3])-1])

capturedata_a_gstar_TQM[0].append(capturedata_1e4_45_gstar_TQM[0][0]/Rg)
capturedata_a_gstar_TQM[1].append(capturedata_1e4_45_gstar_TQM[0][len(capturedata_1e4_45_gstar_TQM[0])-1]/Rg)
capturedata_a_gstar_TQM[2].append(capturedata_1e4_45_gstar_TQM[3][len(capturedata_1e4_45_gstar_TQM[3])-1])

capturedata_a_gstar_TQM[0].append(capturedata_1e5_45_gstar_TQM[0][0]/Rg)
capturedata_a_gstar_TQM[1].append(capturedata_1e5_45_gstar_TQM[0][len(capturedata_1e5_45_gstar_TQM[0])-1]/Rg)
capturedata_a_gstar_TQM[2].append(capturedata_1e5_45_gstar_TQM[3][len(capturedata_1e5_45_gstar_TQM[3])-1])

#capturedata_a_gstar_TQM[0].append(capturedata_1e6_45_gstar_TQM[0][0]/Rg)
#capturedata_a_gstar_TQM[1].append(capturedata_1e6_45_gstar_TQM[0][len(capturedata_1e6_45_gstar_TQM[0])-1]/Rg)
#capturedata_a_gstar_TQM[2].append(capturedata_1e6_45_gstar_TQM[3][len(capturedata_1e6_45_gstar_TQM[3])-1])

#capturedata_a_gstar_TQM[0].append(capturedata_1e7_45_gstar_TQM[0][0]/Rg)
#capturedata_a_gstar_TQM[1].append(capturedata_1e7_45_gstar_TQM[0][len(capturedata_1e7_45_gstar_TQM[0])-1]/Rg)
#capturedata_a_gstar_TQM[2].append(capturedata_1e7_45_gstar_TQM[3][len(capturedata_1e7_45_gstar_TQM[3])-1])

####################################################

capturedata_i_gstar_TQM=[[],[]]

#capturedata_i_gstar_TQM[0].append(capturedata_1e4_5_gstar_TQM[1][0])
#capturedata_i_gstar_TQM[1].append(capturedata_1e4_5_gstar_TQM[3][len(capturedata_1e4_5_gstar_TQM[3])-1])

#capturedata_i_gstar_TQM[0].append(capturedata_1e4_15_gstar_TQM[1][0])
#capturedata_i_gstar_TQM[1].append(capturedata_1e4_15_gstar_TQM[3][len(capturedata_1e4_15_gstar_TQM[3])-1])

capturedata_i_gstar_TQM[0].append(capturedata_1e4_30_gstar_TQM[1][0])
capturedata_i_gstar_TQM[1].append(capturedata_1e4_30_gstar_TQM[3][len(capturedata_1e4_30_gstar_TQM[3])-1])

capturedata_i_gstar_TQM[0].append(capturedata_1e4_45_gstar_TQM[1][0])
capturedata_i_gstar_TQM[1].append(capturedata_1e4_45_gstar_TQM[3][len(capturedata_1e4_45_gstar_TQM[3])-1])

capturedata_i_gstar_TQM[0].append(capturedata_1e4_60_gstar_TQM[1][0])
capturedata_i_gstar_TQM[1].append(capturedata_1e4_60_gstar_TQM[3][len(capturedata_1e4_60_gstar_TQM[3])-1])

#capturedata_i_gstar_TQM[0].append(capturedata_1e4_80_gstar_TQM[1][0])
#capturedata_i_gstar_TQM[1].append(capturedata_1e4_80_gstar_TQM[3][len(capturedata_1e4_80_gstar_TQM[3])-1])

########################################################################################################