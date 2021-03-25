########################################################################################################

#mstar, SG
#capturedata_1e1_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e1_45_mstar_SG.txt")
capturedata_1e2_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e2_45_mstar_SG.txt")
capturedata_1e3_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e3_45_mstar_SG.txt")
capturedata_1e4_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e4_45_mstar_SG.txt")
#capturedata_1e5_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e5_45_mstar_SG.txt")
#capturedata_1e6_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e6_45_mstar_SG.txt")
#capturedata_1e7_45_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e7_45_mstar_SG.txt")

capturedata_1e4_5_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e4_5_mstar_SG.txt")
capturedata_1e4_15_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e4_15_mstar_SG.txt")
capturedata_1e4_30_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e4_30_mstar_SG.txt")
capturedata_1e4_60_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e4_60_mstar_SG.txt")
capturedata_1e4_80_mstar_SG=loadtxt("capturedata/capturedataSG/mstar/capturedata_1e4_80_mstar_SG.txt")

####################################################

capturedata_a_mstar_SG=[[],[],[]]

#capturedata_a_mstar_SG[0].append(capturedata_1e1_45_mstar_SG[0][0]/Rg)
#capturedata_a_mstar_SG[1].append(capturedata_1e1_45_mstar_SG[0][len(capturedata_1e1_45_mstar_SG[0])-1]/Rg)
#capturedata_a_mstar_SG[2].append(capturedata_1e1_45_mstar_SG[3][len(capturedata_1e1_45_mstar_SG[3])-1])

capturedata_a_mstar_SG[0].append(capturedata_1e2_45_mstar_SG[0][0]/Rg)
capturedata_a_mstar_SG[1].append(capturedata_1e2_45_mstar_SG[0][len(capturedata_1e2_45_mstar_SG[0])-1]/Rg)
capturedata_a_mstar_SG[2].append(capturedata_1e2_45_mstar_SG[3][len(capturedata_1e2_45_mstar_SG[3])-1])

capturedata_a_mstar_SG[0].append(capturedata_1e3_45_mstar_SG[0][0]/Rg)
capturedata_a_mstar_SG[1].append(capturedata_1e3_45_mstar_SG[0][len(capturedata_1e3_45_mstar_SG[0])-1]/Rg)
capturedata_a_mstar_SG[2].append(capturedata_1e3_45_mstar_SG[3][len(capturedata_1e3_45_mstar_SG[3])-1])

capturedata_a_mstar_SG[0].append(capturedata_1e4_45_mstar_SG[0][0]/Rg)
capturedata_a_mstar_SG[1].append(capturedata_1e4_45_mstar_SG[0][len(capturedata_1e4_45_mstar_SG[0])-1]/Rg)
capturedata_a_mstar_SG[2].append(capturedata_1e4_45_mstar_SG[3][len(capturedata_1e4_45_mstar_SG[3])-1])

#capturedata_a_mstar_SG[0].append(capturedata_1e5_45_mstar_SG[0][0]/Rg)
#capturedata_a_mstar_SG[1].append(capturedata_1e5_45_mstar_SG[0][len(capturedata_1e5_45_mstar_SG[0])-1]/Rg)
#capturedata_a_mstar_SG[2].append(capturedata_1e5_45_mstar_SG[3][len(capturedata_1e5_45_mstar_SG[3])-1])

#capturedata_a_mstar_SG[0].append(capturedata_1e6_45_mstar_SG[0][0]/Rg)
#capturedata_a_mstar_SG[1].append(capturedata_1e6_45_mstar_SG[0][len(capturedata_1e6_45_mstar_SG[0])-1]/Rg)
#capturedata_a_mstar_SG[2].append(capturedata_1e6_45_mstar_SG[3][len(capturedata_1e6_45_mstar_SG[3])-1])

#capturedata_a_mstar_SG[0].append(capturedata_1e7_45_mstar_SG[0][0]/Rg)
#capturedata_a_mstar_SG[1].append(capturedata_1e7_45_mstar_SG[0][len(capturedata_1e7_45_mstar_SG[0])-1]/Rg)
#capturedata_a_mstar_SG[2].append(capturedata_1e7_45_mstar_SG[3][len(capturedata_1e7_45_mstar_SG[3])-1])

####################################################

capturedata_i_mstar_SG=[[],[]]

capturedata_i_mstar_SG[0].append(capturedata_1e4_5_mstar_SG[1][0])
capturedata_i_mstar_SG[1].append(capturedata_1e4_5_mstar_SG[3][len(capturedata_1e4_5_mstar_SG[3])-1])

capturedata_i_mstar_SG[0].append(capturedata_1e4_15_mstar_SG[1][0])
capturedata_i_mstar_SG[1].append(capturedata_1e4_15_mstar_SG[3][len(capturedata_1e4_15_mstar_SG[3])-1])

capturedata_i_mstar_SG[0].append(capturedata_1e4_30_mstar_SG[1][0])
capturedata_i_mstar_SG[1].append(capturedata_1e4_30_mstar_SG[3][len(capturedata_1e4_30_mstar_SG[3])-1])

capturedata_i_mstar_SG[0].append(capturedata_1e4_45_mstar_SG[1][0])
capturedata_i_mstar_SG[1].append(capturedata_1e4_45_mstar_SG[3][len(capturedata_1e4_45_mstar_SG[3])-1])

capturedata_i_mstar_SG[0].append(capturedata_1e4_60_mstar_SG[1][0])
capturedata_i_mstar_SG[1].append(capturedata_1e4_60_mstar_SG[3][len(capturedata_1e4_60_mstar_SG[3])-1])

capturedata_i_mstar_SG[0].append(capturedata_1e4_80_mstar_SG[1][0])
capturedata_i_mstar_SG[1].append(capturedata_1e4_80_mstar_SG[3][len(capturedata_1e4_80_mstar_SG[3])-1])

########################################################################################################

########################################################################################################

#mstar, TQM
#capturedata_1e2_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e2_45_mstar_TQM.txt")
capturedata_1e3_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e3_45_mstar_TQM.txt")
capturedata_1e4_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_45_mstar_TQM.txt")
capturedata_1e5_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e5_45_mstar_TQM.txt")
#capturedata_1e6_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e6_45_mstar_TQM.txt")
#capturedata_1e7_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e7_45_mstar_TQM.txt")

#capturedata_1e4_5_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_5_mstar_TQM.txt")
#capturedata_1e4_15_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_15_mstar_TQM.txt")
capturedata_1e4_30_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_30_mstar_TQM.txt")
capturedata_1e4_60_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_60_mstar_TQM.txt")
#capturedata_1e4_80_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_80_mstar_TQM.txt")

####################################################

capturedata_a_mstar_TQM=[[],[],[]]

#capturedata_a_mstar_TQM[0].append(capturedata_1e2_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e2_45_mstar_TQM[0][len(capturedata_1e2_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e2_45_mstar_TQM[3][len(capturedata_1e2_45_mstar_TQM[3])-1])

capturedata_a_mstar_TQM[0].append(capturedata_1e3_45_mstar_TQM[0][0]/Rg)
capturedata_a_mstar_TQM[1].append(capturedata_1e3_45_mstar_TQM[0][len(capturedata_1e3_45_mstar_TQM[0])-1]/Rg)
capturedata_a_mstar_TQM[2].append(capturedata_1e3_45_mstar_TQM[3][len(capturedata_1e3_45_mstar_TQM[3])-1])

capturedata_a_mstar_TQM[0].append(capturedata_1e4_45_mstar_TQM[0][0]/Rg)
capturedata_a_mstar_TQM[1].append(capturedata_1e4_45_mstar_TQM[0][len(capturedata_1e4_45_mstar_TQM[0])-1]/Rg)
capturedata_a_mstar_TQM[2].append(capturedata_1e4_45_mstar_TQM[3][len(capturedata_1e4_45_mstar_TQM[3])-1])

capturedata_a_mstar_TQM[0].append(capturedata_1e5_45_mstar_TQM[0][0]/Rg)
capturedata_a_mstar_TQM[1].append(capturedata_1e5_45_mstar_TQM[0][len(capturedata_1e5_45_mstar_TQM[0])-1]/Rg)
capturedata_a_mstar_TQM[2].append(capturedata_1e5_45_mstar_TQM[3][len(capturedata_1e5_45_mstar_TQM[3])-1])

#capturedata_a_mstar_TQM[0].append(capturedata_1e6_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e6_45_mstar_TQM[0][len(capturedata_1e6_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e6_45_mstar_TQM[3][len(capturedata_1e6_45_mstar_TQM[3])-1])

#capturedata_a_mstar_TQM[0].append(capturedata_1e7_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e7_45_mstar_TQM[0][len(capturedata_1e7_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e7_45_mstar_TQM[3][len(capturedata_1e7_45_mstar_TQM[3])-1])

####################################################

capturedata_i_mstar_TQM=[[],[]]

#capturedata_i_mstar_TQM[0].append(capturedata_1e4_5_mstar_TQM[1][0])
#capturedata_i_mstar_TQM[1].append(capturedata_1e4_5_mstar_TQM[3][len(capturedata_1e4_5_mstar_TQM[3])-1])

#capturedata_i_mstar_TQM[0].append(capturedata_1e4_15_mstar_TQM[1][0])
#capturedata_i_mstar_TQM[1].append(capturedata_1e4_15_mstar_TQM[3][len(capturedata_1e4_15_mstar_TQM[3])-1])

capturedata_i_mstar_TQM[0].append(capturedata_1e4_30_mstar_TQM[1][0])
capturedata_i_mstar_TQM[1].append(capturedata_1e4_30_mstar_TQM[3][len(capturedata_1e4_30_mstar_TQM[3])-1])

capturedata_i_mstar_TQM[0].append(capturedata_1e4_45_mstar_TQM[1][0])
capturedata_i_mstar_TQM[1].append(capturedata_1e4_45_mstar_TQM[3][len(capturedata_1e4_45_mstar_TQM[3])-1])

capturedata_i_mstar_TQM[0].append(capturedata_1e4_60_mstar_TQM[1][0])
capturedata_i_mstar_TQM[1].append(capturedata_1e4_60_mstar_TQM[3][len(capturedata_1e4_60_mstar_TQM[3])-1])

#capturedata_i_mstar_TQM[0].append(capturedata_1e4_80_mstar_TQM[1][0])
#capturedata_i_mstar_TQM[1].append(capturedata_1e4_80_mstar_TQM[3][len(capturedata_1e4_80_mstar_TQM[3])-1])

########################################################################################################