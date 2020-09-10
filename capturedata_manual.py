i_0=pi/4
irange=[pi/36,pi/12,pi/6,pi/4,pi/3,4*pi/9]
ideg=[pi/36*degrees,pi/12*degrees,pi/6*degrees,pi/4*degrees,pi/3*degrees,4*pi/9*degrees]
am_0=1e4*Rg
amrange=[1e2*Rg,1e3*Rg,1e4*Rg,1e5*Rg,1e6*Rg,1e7*Rg]
amrange_SG=surfacedensityam_SG
amrange_TQM=surfacedensityam_TQM

irange2_SG=ivals(amrange[0],hint_SG)
irange3_SG=ivals(amrange[1],hint_SG)
irange4_SG=ivals(amrange[2],hint_SG)
irange5_SG=ivals(amrange[3],hint_SG)
irange6_SG=ivals(amrange[4],hint_SG)
irange7_SG=ivals(amrange[5],hint_SG)
ideg2_SG=ivals(amrange[0],hint_SG)*(180/pi)
ideg3_SG=ivals(amrange[1],hint_SG)*(180/pi)
ideg4_SG=ivals(amrange[2],hint_SG)*(180/pi)
ideg5_SG=ivals(amrange[3],hint_SG)*(180/pi)
ideg6_SG=ivals(amrange[4],hint_SG)*(180/pi)
ideg7_SG=ivals(amrange[5],hint_SG)*(180/pi)
irange2_TQM=ivals(amrange[0],hint_TQM)
irange3_TQM=ivals(amrange[1],hint_TQM)
irange4_TQM=ivals(amrange[2],hint_TQM)
irange5_TQM=ivals(amrange[3],hint_TQM)
irange6_TQM=ivals(amrange[4],hint_TQM)
irange7_TQM=ivals(amrange[5],hint_TQM)
ideg2_TQM=ivals(amrange[0],hint_TQM)*(180/pi)
ideg3_TQM=ivals(amrange[1],hint_TQM)*(180/pi)
ideg4_TQM=ivals(amrange[2],hint_TQM)*(180/pi)
ideg5_TQM=ivals(amrange[3],hint_TQM)*(180/pi)
ideg6_TQM=ivals(amrange[4],hint_TQM)*(180/pi)
ideg7_TQM=ivals(amrange[5],hint_TQM)*(180/pi)

Tcaprgianta_SG=[]
Tcapostara_SG=[]
Tcapgstara_SG=[]
Tcapmstara_SG=[]
Tcaprgianta_TQM=[]
Tcapostara_TQM=[]
Tcapgstara_TQM=[]
Tcapmstara_TQM=[]
for j in range(len(amrange_SG)):
        Tcaprgianta_SG.append(Tcap_estim_STO(i_0,amrange_SG[j],rrgiant,densityrgiant,hint_SG,density_SG))
        Tcapostara_SG.append(Tcap_estim_STO(i_0,amrange_SG[j],rostar,densityostar,hint_SG,density_SG))
        Tcapgstara_SG.append(Tcap_estim_STO(i_0,amrange_SG[j],rsun,densitysun,hint_SG,density_SG))
        Tcapmstara_SG.append(Tcap_estim_STO(i_0,amrange_SG[j],rmstar,densitymstar,hint_SG,density_SG))       
for j in range(len(amrange_TQM)):
        Tcaprgianta_TQM.append(Tcap_estim_STO(i,amrange_TQM[j],rrgiant,densityrgiant,hint_TQM,density_TQM))
        Tcapostara_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rostar,densityostar,hint_TQM,density_TQM))
        Tcapgstara_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rsun,densitysun,hint_TQM,density_TQM))
        Tcapmstara_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rmstar,densitymstar,hint_TQM,density_TQM))

Tcaprgianti_SG=[]
Tcapostari_SG=[]
Tcapgstari_SG=[]
Tcapmstari_SG=[]
Tcaprgianti_TQM=[]
Tcapostari_TQM=[]
Tcapgstari_TQM=[]
Tcapmstari_TQM=[]
for j in range(len(irange4_SG)):
        Tcaprgianti_SG.append(Tcap_estim_STO(irange4_SG[j],am_0,rrgiant,densityrgiant,hint_SG,density_SG))
        Tcapostari_SG.append(Tcap_estim_STO(irange4_SG[j],am_0,rostar,densityostar,hint_SG,density_SG))
        Tcapgstari_SG.append(Tcap_estim_STO(irange4_SG[j],am_0,rsun,densitysun,hint_SG,density_SG))
        Tcapmstari_SG.append(Tcap_estim_STO(irange4_SG[j],am_0,rmstar,densitymstar,hint_SG,density_SG))
for j in range(len(irange4_TQM)):
        Tcaprgianti_TQM.append(Tcap_estim_STO(irange4_TQM[j],am_0,rrgiant,densityrgiant,hint_TQM,density_TQM))
        Tcapostari_TQM.append(Tcap_estim_STO(irange4_TQM[j],am_0,rostar,densityostar,hint_TQM,density_TQM))
        Tcapgstari_TQM.append(Tcap_estim_STO(irange4_TQM[j],am_0,rsun,densitysun,hint_TQM,density_TQM))
        Tcapmstari_TQM.append(Tcap_estim_STO(irange4_TQM[j],am_0,rmstar,densitymstar,hint_TQM,density_TQM))

Tcap80deg_SG=[]
Tcap60deg_SG=[]
Tcap45deg_SG=[]
Tcap30deg_SG=[]
Tcap15deg_SG=[]
Tcap05deg_SG=[]
Tcap80deg_TQM=[]
Tcap60deg_TQM=[]
Tcap45deg_TQM=[]
Tcap30deg_TQM=[]
Tcap15deg_TQM=[]
Tcap05deg_TQM=[]
for j in range(len(amrange_SG)):
    Tcap80deg_SG.append(Tcap_estim_BHL(irange[5],amrange_SG[j],hint_SG,density_SG))
    Tcap60deg_SG.append(Tcap_estim_BHL(irange[4],amrange_SG[j],hint_SG,density_SG))
    Tcap45deg_SG.append(Tcap_estim_BHL(irange[3],amrange_SG[j],hint_SG,density_SG))
    Tcap30deg_SG.append(Tcap_estim_BHL(irange[2],amrange_SG[j],hint_SG,density_SG))
    Tcap15deg_SG.append(Tcap_estim_BHL(irange[1],amrange_SG[j],hint_SG,density_SG))
    Tcap05deg_SG.append(Tcap_estim_BHL(irange[0],amrange_SG[j],hint_SG,density_SG))
for j in range(len(amrange_TQM)):
    Tcap80deg_TQM.append(Tcap_estim_BHL(irange[5],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap60deg_TQM.append(Tcap_estim_BHL(irange[4],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap45deg_TQM.append(Tcap_estim_BHL(irange[3],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap30deg_TQM.append(Tcap_estim_BHL(irange[2],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap15deg_TQM.append(Tcap_estim_BHL(irange[1],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap05deg_TQM.append(Tcap_estim_BHL(irange[0],amrange_TQM[j],hint_TQM,density_TQM))

Tcap2Rg_SG=[]
Tcap3Rg_SG=[]
Tcap4Rg_SG=[]
Tcap5Rg_SG=[]
Tcap6Rg_SG=[]
Tcap7Rg_SG=[]
Tcap2Rg_TQM=[]
Tcap3Rg_TQM=[]
Tcap4Rg_TQM=[]
Tcap5Rg_TQM=[]
Tcap6Rg_TQM=[]
Tcap7Rg_TQM=[]
for j in range(len(irange4_SG)):
    Tcap2Rg_SG.append(Tcap_estim_BHL(irange2_SG[j],amrange[0],hint_SG,density_SG))
    Tcap3Rg_SG.append(Tcap_estim_BHL(irange3_SG[j],amrange[1],hint_SG,density_SG))
    Tcap4Rg_SG.append(Tcap_estim_BHL(irange4_SG[j],amrange[2],hint_SG,density_SG))
    Tcap5Rg_SG.append(Tcap_estim_BHL(irange5_SG[j],amrange[3],hint_SG,density_SG))
    Tcap6Rg_SG.append(Tcap_estim_BHL(irange6_SG[j],amrange[4],hint_SG,density_SG))
    Tcap7Rg_SG.append(Tcap_estim_BHL(irange7_SG[j],amrange[5],hint_SG,density_SG))
for j in range(len(irange4_TQM)):
    Tcap2Rg_TQM.append(Tcap_estim_BHL(irange2_TQM[j],amrange[0],hint_TQM,density_TQM))
    Tcap3Rg_TQM.append(Tcap_estim_BHL(irange3_TQM[j],amrange[1],hint_TQM,density_TQM))
    Tcap4Rg_TQM.append(Tcap_estim_BHL(irange4_TQM[j],amrange[2],hint_TQM,density_TQM))
    Tcap5Rg_TQM.append(Tcap_estim_BHL(irange5_TQM[j],amrange[3],hint_TQM,density_TQM))
    Tcap6Rg_TQM.append(Tcap_estim_BHL(irange6_TQM[j],amrange[4],hint_TQM,density_TQM))
    Tcap7Rg_TQM.append(Tcap_estim_BHL(irange7_TQM[j],amrange[5],hint_TQM,density_TQM))

#template=loadtxt("capturedata/capturedataMODEL/OBJECT/CONDITIONS.txt")

#Plot with CONDITIONS,  define CONDITIONS in "if" loop, depending on STO vs BHL
#def capturedata(CONDITIONS,output)
#    # (ai,tcap), (af, tcap), (i,tcap)
#    CONDITIONS_i_i=CONDITIONS[1][0]*(180/pi)
#    CONDITIONS_a_i=CONDITIONS[0][0]/Rg
#    CONDITIONS_a_f=CONDITIONS[0][len(CONDITIONS[0])-1]/Rg
#    CONDITIONS_t_f=CONDITIONS[3][len(CONDITIONS[3])-1]
    #CONDITIONS_n_orb=t_f=CONDITIONS[2][len(CONDITIONS[2])-1]
    #WILL NEED TO PLOT (t,a) and (t,i)
    #CONDITIONS_a=CONDITIONS[0]/Rg
    #CONDITIONS_i=CONDITIONS[1]*(180/pi)
    #CONDITIONS_t=CONDITIONS[3]
#    return output

#Waste of computation, but perhaps easier on the eyes and brain
#capturedata_sBH_SG_ao=capturedata_sBH_SG[0]
#capturedata_sBH_SG_af=capturedata_sBH_SG[1]
#capturedata_sBH_SG_io=capturedata_sBH_SG[2]
#capturedata_sBH_SG_tf=capturedata_sBH_SG[3]

#A[0] I[1] N[2] T[3] ALL LOADED DATA FOLLOW THIS FORMAT

########################################################################################################

#sBH, SG
capturedata_1e2_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e2_5_sBH_SG.txt")
capturedata_1e3_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e3_5_sBH_SG.txt")
capturedata_2e3_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_2e3_5_sBH_SG.txt")
capturedata_5e3_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_5e3_5_sBH_SG.txt")
capturedata_1e4_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e4_5_sBH_SG.txt")
capturedata_1e5_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e5_5_sBH_SG.txt")
capturedata_5e5_5_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_5e5_5_sBH_SG.txt")

capturedata_1e3_15_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e3_15_sBH_SG.txt")
capturedata_1e4_15_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e4_15_sBH_SG.txt")
capturedata_1e5_15_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e5_15_sBH_SG.txt")
capturedata_5e5_15_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_5e5_15_sBH_SG.txt")
capturedata_1e6_15_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e6_15_sBH_SG.txt")

capturedata_1e5_30_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e5_30_sBH_SG.txt")
capturedata_5e5_30_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_5e5_30_sBH_SG.txt")
capturedata_1e6_30_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e6_30_sBH_SG.txt")
capturedata_1e7_30_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e7_30_sBH_SG.txt")

capturedata_5e5_45_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_5e5_45_sBH_SG.txt")
capturedata_1e6_45_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e6_45_sBH_SG.txt")
capturedata_1e7_45_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e7_45_sBH_SG.txt")

capturedata_1e6_60_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e6_60_sBH_SG.txt")
capturedata_1e7_60_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e7_60_sBH_SG.txt")

capturedata_1e6_80_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e6_80_sBH_SG.txt")
capturedata_1e7_80_sBH_SG=loadtxt("capturedata/capturedataSG/sBH/capturedata_1e7_80_sBH_SG.txt")

####################################################

capturedata_5_sBH_SG=[[],[],[]] #A0 Af I0 Tf format for relavant plotting

capturedata_5_sBH_SG[0].append(capturedata_1e2_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_1e2_5_sBH_SG[0][len(capturedata_1e2_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_1e2_5_sBH_SG[3][len(capturedata_1e2_5_sBH_SG[3])-1])

capturedata_5_sBH_SG[0].append(capturedata_1e3_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_1e3_5_sBH_SG[0][len(capturedata_1e3_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_1e3_5_sBH_SG[3][len(capturedata_1e3_5_sBH_SG[3])-1])

capturedata_5_sBH_SG[0].append(capturedata_2e3_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_2e3_5_sBH_SG[0][len(capturedata_2e3_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_2e3_5_sBH_SG[3][len(capturedata_2e3_5_sBH_SG[3])-1])

capturedata_5_sBH_SG[0].append(capturedata_5e3_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_5e3_5_sBH_SG[0][len(capturedata_5e3_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_5e3_5_sBH_SG[3][len(capturedata_5e3_5_sBH_SG[3])-1])

capturedata_5_sBH_SG[0].append(capturedata_1e4_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_1e4_5_sBH_SG[0][len(capturedata_1e4_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_1e4_5_sBH_SG[3][len(capturedata_1e4_5_sBH_SG[3])-1])

capturedata_5_sBH_SG[0].append(capturedata_1e5_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_1e5_5_sBH_SG[0][len(capturedata_1e5_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_1e5_5_sBH_SG[3][len(capturedata_1e5_5_sBH_SG[3])-1])

capturedata_5_sBH_SG[0].append(capturedata_5e5_5_sBH_SG[0][0]/Rg)
capturedata_5_sBH_SG[1].append(capturedata_5e5_5_sBH_SG[0][len(capturedata_5e5_5_sBH_SG[0])-1]/Rg)
capturedata_5_sBH_SG[2].append(capturedata_5e5_5_sBH_SG[3][len(capturedata_5e5_5_sBH_SG[3])-1])

capturedata_15_sBH_SG=[[],[],[]]

capturedata_15_sBH_SG[0].append(capturedata_1e3_15_sBH_SG[0][0]/Rg)
capturedata_15_sBH_SG[1].append(capturedata_1e3_15_sBH_SG[0][len(capturedata_1e3_15_sBH_SG[0])-1]/Rg)
capturedata_15_sBH_SG[2].append(capturedata_1e3_15_sBH_SG[3][len(capturedata_1e3_15_sBH_SG[3])-1])

capturedata_15_sBH_SG[0].append(capturedata_1e4_15_sBH_SG[0][0]/Rg)
capturedata_15_sBH_SG[1].append(capturedata_1e4_15_sBH_SG[0][len(capturedata_1e4_15_sBH_SG[0])-1]/Rg)
capturedata_15_sBH_SG[2].append(capturedata_1e4_15_sBH_SG[3][len(capturedata_1e4_15_sBH_SG[3])-1])

capturedata_15_sBH_SG[0].append(capturedata_1e5_15_sBH_SG[0][0]/Rg)
capturedata_15_sBH_SG[1].append(capturedata_1e5_15_sBH_SG[0][len(capturedata_1e5_15_sBH_SG[0])-1]/Rg)
capturedata_15_sBH_SG[2].append(capturedata_1e5_15_sBH_SG[3][len(capturedata_1e5_15_sBH_SG[3])-1])

capturedata_15_sBH_SG[0].append(capturedata_5e5_15_sBH_SG[0][0]/Rg)
capturedata_15_sBH_SG[1].append(capturedata_5e5_15_sBH_SG[0][len(capturedata_5e5_15_sBH_SG[0])-1]/Rg)
capturedata_15_sBH_SG[2].append(capturedata_5e5_15_sBH_SG[3][len(capturedata_5e5_15_sBH_SG[3])-1])

capturedata_15_sBH_SG[0].append(capturedata_1e6_15_sBH_SG[0][0]/Rg)
capturedata_15_sBH_SG[1].append(capturedata_1e6_15_sBH_SG[0][len(capturedata_1e6_15_sBH_SG[0])-1]/Rg)
capturedata_15_sBH_SG[2].append(capturedata_1e6_15_sBH_SG[3][len(capturedata_1e6_15_sBH_SG[3])-1])

capturedata_30_sBH_SG=[[],[],[]]

capturedata_30_sBH_SG[0].append(capturedata_1e5_30_sBH_SG[0][0]/Rg)
capturedata_30_sBH_SG[1].append(capturedata_1e5_30_sBH_SG[0][len(capturedata_1e5_30_sBH_SG[0])-1]/Rg)
capturedata_30_sBH_SG[2].append(capturedata_1e5_30_sBH_SG[3][len(capturedata_1e5_30_sBH_SG[3])-1])

capturedata_30_sBH_SG[0].append(capturedata_5e5_30_sBH_SG[0][0]/Rg)
capturedata_30_sBH_SG[1].append(capturedata_5e5_30_sBH_SG[0][len(capturedata_5e5_30_sBH_SG[0])-1]/Rg)
capturedata_30_sBH_SG[2].append(capturedata_5e5_30_sBH_SG[3][len(capturedata_5e5_30_sBH_SG[3])-1])

capturedata_30_sBH_SG[0].append(capturedata_1e6_30_sBH_SG[0][0]/Rg)
capturedata_30_sBH_SG[1].append(capturedata_1e6_30_sBH_SG[0][len(capturedata_1e6_30_sBH_SG[0])-1]/Rg)
capturedata_30_sBH_SG[2].append(capturedata_1e6_30_sBH_SG[3][len(capturedata_1e6_30_sBH_SG[3])-1])

capturedata_30_sBH_SG[0].append(capturedata_1e7_30_sBH_SG[0][0]/Rg)
capturedata_30_sBH_SG[1].append(capturedata_1e7_30_sBH_SG[0][len(capturedata_1e7_30_sBH_SG[0])-1]/Rg)
capturedata_30_sBH_SG[2].append(capturedata_1e7_30_sBH_SG[3][len(capturedata_1e7_30_sBH_SG[3])-1])

capturedata_45_sBH_SG=[[],[],[]]

capturedata_45_sBH_SG[0].append(capturedata_5e5_45_sBH_SG[0][0]/Rg)
capturedata_45_sBH_SG[1].append(capturedata_5e5_45_sBH_SG[0][len(capturedata_5e5_45_sBH_SG[0])-1]/Rg)
capturedata_45_sBH_SG[2].append(capturedata_5e5_45_sBH_SG[3][len(capturedata_5e5_45_sBH_SG[3])-1])

capturedata_45_sBH_SG[0].append(capturedata_1e6_45_sBH_SG[0][0]/Rg)
capturedata_45_sBH_SG[1].append(capturedata_1e6_45_sBH_SG[0][len(capturedata_1e6_45_sBH_SG[0])-1]/Rg)
capturedata_45_sBH_SG[2].append(capturedata_1e6_45_sBH_SG[3][len(capturedata_1e6_45_sBH_SG[3])-1])

capturedata_45_sBH_SG[0].append(capturedata_1e7_45_sBH_SG[0][0]/Rg)
capturedata_45_sBH_SG[1].append(capturedata_1e7_45_sBH_SG[0][len(capturedata_1e7_45_sBH_SG[0])-1]/Rg)
capturedata_45_sBH_SG[2].append(capturedata_1e7_45_sBH_SG[3][len(capturedata_1e7_45_sBH_SG[3])-1])

capturedata_60_sBH_SG=[[],[],[]]

capturedata_60_sBH_SG[0].append(capturedata_1e6_60_sBH_SG[0][0]/Rg)
capturedata_60_sBH_SG[1].append(capturedata_1e6_60_sBH_SG[0][len(capturedata_1e6_60_sBH_SG[0])-1]/Rg)
capturedata_60_sBH_SG[2].append(capturedata_1e6_60_sBH_SG[3][len(capturedata_1e6_60_sBH_SG[3])-1])

capturedata_60_sBH_SG[0].append(capturedata_1e7_60_sBH_SG[0][0]/Rg)
capturedata_60_sBH_SG[1].append(capturedata_1e7_60_sBH_SG[0][len(capturedata_1e7_60_sBH_SG[0])-1]/Rg)
capturedata_60_sBH_SG[2].append(capturedata_1e7_60_sBH_SG[3][len(capturedata_1e7_60_sBH_SG[3])-1])

capturedata_80_sBH_SG=[[],[],[]]

capturedata_80_sBH_SG[0].append(capturedata_1e6_80_sBH_SG[0][0]/Rg)
capturedata_80_sBH_SG[1].append(capturedata_1e6_80_sBH_SG[0][len(capturedata_1e6_80_sBH_SG[0])-1]/Rg)
capturedata_80_sBH_SG[2].append(capturedata_1e6_80_sBH_SG[3][len(capturedata_1e6_80_sBH_SG[3])-1])

capturedata_80_sBH_SG[0].append(capturedata_1e7_80_sBH_SG[0][0]/Rg)
capturedata_80_sBH_SG[1].append(capturedata_1e7_80_sBH_SG[0][len(capturedata_1e7_80_sBH_SG[0])-1]/Rg)
capturedata_80_sBH_SG[2].append(capturedata_1e7_80_sBH_SG[3][len(capturedata_1e7_80_sBH_SG[3])-1])

####################################################

capturedata_1e2_sBH_SG=[[],[]]

capturedata_1e2_sBH_SG[0].append(capturedata_1e2_5_sBH_SG[1][0])
capturedata_1e2_sBH_SG[1].append(capturedata_1e2_5_sBH_SG[3][len(capturedata_1e2_5_sBH_SG[3])-1])

capturedata_1e3_sBH_SG=[[],[]]

capturedata_1e3_sBH_SG[0].append(capturedata_1e3_5_sBH_SG[1][0])
capturedata_1e3_sBH_SG[1].append(capturedata_1e3_5_sBH_SG[3][len(capturedata_1e3_5_sBH_SG[3])-1])

capturedata_1e3_sBH_SG[0].append(capturedata_1e3_15_sBH_SG[1][0])
capturedata_1e3_sBH_SG[1].append(capturedata_1e3_15_sBH_SG[3][len(capturedata_1e3_15_sBH_SG[3])-1])

capturedata_2e3_sBH_SG=[[],[]]

capturedata_2e3_sBH_SG[0].append(capturedata_2e3_5_sBH_SG[1][0])
capturedata_2e3_sBH_SG[1].append(capturedata_2e3_5_sBH_SG[3][len(capturedata_2e3_5_sBH_SG[3])-1])

capturedata_5e3_sBH_SG=[[],[]]

capturedata_5e3_sBH_SG[0].append(capturedata_5e3_5_sBH_SG[1][0])
capturedata_5e3_sBH_SG[1].append(capturedata_5e3_5_sBH_SG[3][len(capturedata_5e3_5_sBH_SG[3])-1])

capturedata_1e4_sBH_SG=[[],[]]

capturedata_1e4_sBH_SG[0].append(capturedata_1e4_5_sBH_SG[1][0])
capturedata_1e4_sBH_SG[1].append(capturedata_1e4_5_sBH_SG[3][len(capturedata_1e4_5_sBH_SG[3])-1])

capturedata_1e4_sBH_SG[0].append(capturedata_1e4_15_sBH_SG[1][0])
capturedata_1e4_sBH_SG[1].append(capturedata_1e4_15_sBH_SG[3][len(capturedata_1e4_15_sBH_SG[3])-1])

capturedata_1e5_sBH_SG=[[],[]]

capturedata_1e5_sBH_SG[0].append(capturedata_1e5_5_sBH_SG[1][0])
capturedata_1e5_sBH_SG[1].append(capturedata_1e5_5_sBH_SG[3][len(capturedata_1e5_5_sBH_SG[3])-1])

capturedata_1e5_sBH_SG[0].append(capturedata_1e5_15_sBH_SG[1][0])
capturedata_1e5_sBH_SG[1].append(capturedata_1e5_15_sBH_SG[3][len(capturedata_1e5_15_sBH_SG[3])-1])

capturedata_1e5_sBH_SG[0].append(capturedata_1e5_30_sBH_SG[1][0])
capturedata_1e5_sBH_SG[1].append(capturedata_1e5_30_sBH_SG[3][len(capturedata_1e5_30_sBH_SG[3])-1])

capturedata_5e5_sBH_SG=[[],[]]

capturedata_5e5_sBH_SG[0].append(capturedata_5e5_5_sBH_SG[1][0])
capturedata_5e5_sBH_SG[1].append(capturedata_5e5_5_sBH_SG[3][len(capturedata_5e5_5_sBH_SG[3])-1])

capturedata_5e5_sBH_SG[0].append(capturedata_5e5_15_sBH_SG[1][0])
capturedata_5e5_sBH_SG[1].append(capturedata_5e5_15_sBH_SG[3][len(capturedata_5e5_15_sBH_SG[3])-1])

capturedata_5e5_sBH_SG[0].append(capturedata_5e5_30_sBH_SG[1][0])
capturedata_5e5_sBH_SG[1].append(capturedata_5e5_30_sBH_SG[3][len(capturedata_5e5_30_sBH_SG[3])-1])

capturedata_5e5_sBH_SG[0].append(capturedata_5e5_45_sBH_SG[1][0])
capturedata_5e5_sBH_SG[1].append(capturedata_5e5_45_sBH_SG[3][len(capturedata_5e5_45_sBH_SG[3])-1])

capturedata_1e6_sBH_SG=[[],[]]

capturedata_1e6_sBH_SG[0].append(capturedata_1e6_15_sBH_SG[1][0])
capturedata_1e6_sBH_SG[1].append(capturedata_1e6_15_sBH_SG[3][len(capturedata_1e6_15_sBH_SG[3])-1])

capturedata_1e6_sBH_SG[0].append(capturedata_1e6_30_sBH_SG[1][0])
capturedata_1e6_sBH_SG[1].append(capturedata_1e6_30_sBH_SG[3][len(capturedata_1e6_30_sBH_SG[3])-1])

capturedata_1e6_sBH_SG[0].append(capturedata_1e6_45_sBH_SG[1][0])
capturedata_1e6_sBH_SG[1].append(capturedata_1e6_45_sBH_SG[3][len(capturedata_1e6_45_sBH_SG[3])-1])

capturedata_1e6_sBH_SG[0].append(capturedata_1e6_60_sBH_SG[1][0])
capturedata_1e6_sBH_SG[1].append(capturedata_1e6_60_sBH_SG[3][len(capturedata_1e6_60_sBH_SG[3])-1])

capturedata_1e6_sBH_SG[0].append(capturedata_1e6_80_sBH_SG[1][0])
capturedata_1e6_sBH_SG[1].append(capturedata_1e6_80_sBH_SG[3][len(capturedata_1e6_80_sBH_SG[3])-1])

capturedata_1e7_sBH_SG=[[],[]]

capturedata_1e7_sBH_SG[0].append(capturedata_1e7_30_sBH_SG[1][0])
capturedata_1e7_sBH_SG[1].append(capturedata_1e7_30_sBH_SG[3][len(capturedata_1e7_30_sBH_SG[3])-1])

capturedata_1e7_sBH_SG[0].append(capturedata_1e7_45_sBH_SG[1][0])
capturedata_1e7_sBH_SG[1].append(capturedata_1e7_45_sBH_SG[3][len(capturedata_1e7_45_sBH_SG[3])-1])

capturedata_1e7_sBH_SG[0].append(capturedata_1e7_60_sBH_SG[1][0])
capturedata_1e7_sBH_SG[1].append(capturedata_1e7_60_sBH_SG[3][len(capturedata_1e7_60_sBH_SG[3])-1])

capturedata_1e7_sBH_SG[0].append(capturedata_1e7_80_sBH_SG[1][0])
capturedata_1e7_sBH_SG[1].append(capturedata_1e7_80_sBH_SG[3][len(capturedata_1e7_80_sBH_SG[3])-1])

########################################################################################################
########################################################################################################

#sBH, TQM
capturedata_1e3_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e3_5_sBH_TQM.txt")
capturedata_2e3_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_2e3_5_sBH_TQM.txt")
capturedata_1e4_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e4_5_sBH_TQM.txt")
capturedata_2e4_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_2e4_5_sBH_TQM.txt")
capturedata_3e4_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_3e4_5_sBH_TQM.txt")
capturedata_4e4_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_4e4_5_sBH_TQM.txt")
capturedata_5e4_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e4_5_sBH_TQM.txt")
capturedata_1e5_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e5_5_sBH_TQM.txt")
capturedata_2e5_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_2e5_5_sBH_TQM.txt")
capturedata_5e5_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e5_5_sBH_TQM.txt")
capturedata_1e6_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e6_5_sBH_TQM.txt")
capturedata_5e6_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e6_5_sBH_TQM.txt")
capturedata_8e6_5_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_8e6_5_sBH_TQM.txt")

#capturedata_1e3_15_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e3_15_sBH_TQM.txt")
capturedata_1e4_15_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e4_15_sBH_TQM.txt")
capturedata_1e5_15_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e5_15_sBH_TQM.txt")
capturedata_1e6_15_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e6_15_sBH_TQM.txt")
capturedata_5e6_15_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e6_15_sBH_TQM.txt")
capturedata_1e7_15_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e7_15_sBH_TQM.txt")

capturedata_1e5_30_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e5_30_sBH_TQM.txt")
capturedata_1e6_30_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e6_30_sBH_TQM.txt")
capturedata_5e6_30_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e6_30_sBH_TQM.txt")
capturedata_1e7_30_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e7_30_sBH_TQM.txt")

capturedata_1e6_45_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e6_45_sBH_TQM.txt")
capturedata_5e6_45_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e6_45_sBH_TQM.txt")
capturedata_1e7_45_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e7_45_sBH_TQM.txt")

capturedata_1e6_60_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e6_60_sBH_TQM.txt")
capturedata_5e6_60_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e6_60_sBH_TQM.txt")
capturedata_1e7_60_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e7_60_sBH_TQM.txt")

capturedata_1e6_80_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e6_80_sBH_TQM.txt")
capturedata_5e6_80_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_5e6_80_sBH_TQM.txt")
capturedata_1e7_80_sBH_TQM=loadtxt("capturedata/capturedataTQM/sBH/capturedata_1e7_80_sBH_TQM.txt")

####################################################

capturedata_5_sBH_TQM=[[],[],[]]

capturedata_5_sBH_TQM[0].append(capturedata_1e3_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_1e3_5_sBH_TQM[0][len(capturedata_1e3_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_1e3_5_sBH_TQM[3][len(capturedata_1e3_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_2e3_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_2e3_5_sBH_TQM[0][len(capturedata_2e3_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_2e3_5_sBH_TQM[3][len(capturedata_2e3_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_1e4_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_1e4_5_sBH_TQM[0][len(capturedata_1e4_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_1e4_5_sBH_TQM[3][len(capturedata_1e4_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_2e4_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_2e4_5_sBH_TQM[0][len(capturedata_2e4_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_2e4_5_sBH_TQM[3][len(capturedata_2e4_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_3e4_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_3e4_5_sBH_TQM[0][len(capturedata_3e4_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_3e4_5_sBH_TQM[3][len(capturedata_3e4_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_4e4_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_4e4_5_sBH_TQM[0][len(capturedata_4e4_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_4e4_5_sBH_TQM[3][len(capturedata_4e4_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_5e4_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_5e4_5_sBH_TQM[0][len(capturedata_5e4_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_5e4_5_sBH_TQM[3][len(capturedata_5e4_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_1e5_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_1e5_5_sBH_TQM[0][len(capturedata_1e5_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_1e5_5_sBH_TQM[3][len(capturedata_1e5_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_2e5_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_2e5_5_sBH_TQM[0][len(capturedata_2e5_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_2e5_5_sBH_TQM[3][len(capturedata_2e5_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_5e5_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_5e5_5_sBH_TQM[0][len(capturedata_5e5_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_5e5_5_sBH_TQM[3][len(capturedata_5e5_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_1e6_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_1e6_5_sBH_TQM[0][len(capturedata_1e6_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_1e6_5_sBH_TQM[3][len(capturedata_1e6_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_5e6_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_5e6_5_sBH_TQM[0][len(capturedata_5e6_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_5e6_5_sBH_TQM[3][len(capturedata_5e6_5_sBH_TQM[3])-1])

capturedata_5_sBH_TQM[0].append(capturedata_8e6_5_sBH_TQM[0][0]/Rg)
capturedata_5_sBH_TQM[1].append(capturedata_8e6_5_sBH_TQM[0][len(capturedata_8e6_5_sBH_TQM[0])-1]/Rg)
capturedata_5_sBH_TQM[2].append(capturedata_8e6_5_sBH_TQM[3][len(capturedata_8e6_5_sBH_TQM[3])-1])

capturedata_15_sBH_TQM=[[],[],[]]

#capturedata_15_sBH_TQM[0].append(capturedata_1e3_15_sBH_TQM[0][0]/Rg)
#capturedata_15_sBH_TQM[1].append(capturedata_1e3_15_sBH_TQM[0][len(capturedata_1e3_15_sBH_TQM[0])-1]/Rg)
#capturedata_15_sBH_TQM[2].append(capturedata_1e3_15_sBH_TQM[3][len(capturedata_1e3_15_sBH_TQM[3])-1])

capturedata_15_sBH_TQM[0].append(capturedata_1e4_15_sBH_TQM[0][0]/Rg)
capturedata_15_sBH_TQM[1].append(capturedata_1e4_15_sBH_TQM[0][len(capturedata_1e4_15_sBH_TQM[0])-1]/Rg)
capturedata_15_sBH_TQM[2].append(capturedata_1e4_15_sBH_TQM[3][len(capturedata_1e4_15_sBH_TQM[3])-1])

capturedata_15_sBH_TQM[0].append(capturedata_1e5_15_sBH_TQM[0][0]/Rg)
capturedata_15_sBH_TQM[1].append(capturedata_1e5_15_sBH_TQM[0][len(capturedata_1e5_15_sBH_TQM[0])-1]/Rg)
capturedata_15_sBH_TQM[2].append(capturedata_1e5_15_sBH_TQM[3][len(capturedata_1e5_15_sBH_TQM[3])-1])

capturedata_15_sBH_TQM[0].append(capturedata_1e6_15_sBH_TQM[0][0]/Rg)
capturedata_15_sBH_TQM[1].append(capturedata_1e6_15_sBH_TQM[0][len(capturedata_1e6_15_sBH_TQM[0])-1]/Rg)
capturedata_15_sBH_TQM[2].append(capturedata_1e6_15_sBH_TQM[3][len(capturedata_1e6_15_sBH_TQM[3])-1])

capturedata_15_sBH_TQM[0].append(capturedata_5e6_15_sBH_TQM[0][0]/Rg)
capturedata_15_sBH_TQM[1].append(capturedata_5e6_15_sBH_TQM[0][len(capturedata_5e6_15_sBH_TQM[0])-1]/Rg)
capturedata_15_sBH_TQM[2].append(capturedata_5e6_15_sBH_TQM[3][len(capturedata_5e6_15_sBH_TQM[3])-1])

capturedata_15_sBH_TQM[0].append(capturedata_1e7_15_sBH_TQM[0][0]/Rg)
capturedata_15_sBH_TQM[1].append(capturedata_1e7_15_sBH_TQM[0][len(capturedata_1e7_15_sBH_TQM[0])-1]/Rg)
capturedata_15_sBH_TQM[2].append(capturedata_1e7_15_sBH_TQM[3][len(capturedata_1e7_15_sBH_TQM[3])-1])

capturedata_30_sBH_TQM=[[],[],[]]

capturedata_30_sBH_TQM[0].append(capturedata_1e5_30_sBH_TQM[0][0]/Rg)
capturedata_30_sBH_TQM[1].append(capturedata_1e5_30_sBH_TQM[0][len(capturedata_1e5_30_sBH_TQM[0])-1]/Rg)
capturedata_30_sBH_TQM[2].append(capturedata_1e5_30_sBH_TQM[3][len(capturedata_1e5_30_sBH_TQM[3])-1])

capturedata_30_sBH_TQM[0].append(capturedata_1e6_30_sBH_TQM[0][0]/Rg)
capturedata_30_sBH_TQM[1].append(capturedata_1e6_30_sBH_TQM[0][len(capturedata_1e6_30_sBH_TQM[0])-1]/Rg)
capturedata_30_sBH_TQM[2].append(capturedata_1e6_30_sBH_TQM[3][len(capturedata_1e6_30_sBH_TQM[3])-1])

capturedata_30_sBH_TQM[0].append(capturedata_5e6_30_sBH_TQM[0][0]/Rg)
capturedata_30_sBH_TQM[1].append(capturedata_5e6_30_sBH_TQM[0][len(capturedata_5e6_30_sBH_TQM[0])-1]/Rg)
capturedata_30_sBH_TQM[2].append(capturedata_5e6_30_sBH_TQM[3][len(capturedata_5e6_30_sBH_TQM[3])-1])

capturedata_30_sBH_TQM[0].append(capturedata_1e7_30_sBH_TQM[0][0]/Rg)
capturedata_30_sBH_TQM[1].append(capturedata_1e7_30_sBH_TQM[0][len(capturedata_1e7_30_sBH_TQM[0])-1]/Rg)
capturedata_30_sBH_TQM[2].append(capturedata_1e7_30_sBH_TQM[3][len(capturedata_1e7_30_sBH_TQM[3])-1])

capturedata_45_sBH_TQM=[[],[],[]]

capturedata_45_sBH_TQM[0].append(capturedata_1e6_45_sBH_TQM[0][0]/Rg)
capturedata_45_sBH_TQM[1].append(capturedata_1e6_45_sBH_TQM[0][len(capturedata_1e6_45_sBH_TQM[0])-1]/Rg)
capturedata_45_sBH_TQM[2].append(capturedata_1e6_45_sBH_TQM[3][len(capturedata_1e6_45_sBH_TQM[3])-1])

capturedata_45_sBH_TQM[0].append(capturedata_5e6_45_sBH_TQM[0][0]/Rg)
capturedata_45_sBH_TQM[1].append(capturedata_5e6_45_sBH_TQM[0][len(capturedata_5e6_45_sBH_TQM[0])-1]/Rg)
capturedata_45_sBH_TQM[2].append(capturedata_5e6_45_sBH_TQM[3][len(capturedata_5e6_45_sBH_TQM[3])-1])

capturedata_45_sBH_TQM[0].append(capturedata_1e7_45_sBH_TQM[0][0]/Rg)
capturedata_45_sBH_TQM[1].append(capturedata_1e7_45_sBH_TQM[0][len(capturedata_1e7_45_sBH_TQM[0])-1]/Rg)
capturedata_45_sBH_TQM[2].append(capturedata_1e7_45_sBH_TQM[3][len(capturedata_1e7_45_sBH_TQM[3])-1])

capturedata_60_sBH_TQM=[[],[],[]]

capturedata_60_sBH_TQM[0].append(capturedata_1e6_60_sBH_TQM[0][0]/Rg)
capturedata_60_sBH_TQM[1].append(capturedata_1e6_60_sBH_TQM[0][len(capturedata_1e6_60_sBH_TQM[0])-1]/Rg)
capturedata_60_sBH_TQM[2].append(capturedata_1e6_60_sBH_TQM[3][len(capturedata_1e6_60_sBH_TQM[3])-1])

capturedata_60_sBH_TQM[0].append(capturedata_5e6_60_sBH_TQM[0][0]/Rg)
capturedata_60_sBH_TQM[1].append(capturedata_5e6_60_sBH_TQM[0][len(capturedata_5e6_60_sBH_TQM[0])-1]/Rg)
capturedata_60_sBH_TQM[2].append(capturedata_5e6_60_sBH_TQM[3][len(capturedata_5e6_60_sBH_TQM[3])-1])

capturedata_60_sBH_TQM[0].append(capturedata_1e7_60_sBH_TQM[0][0]/Rg)
capturedata_60_sBH_TQM[1].append(capturedata_1e7_60_sBH_TQM[0][len(capturedata_1e7_60_sBH_TQM[0])-1]/Rg)
capturedata_60_sBH_TQM[2].append(capturedata_1e7_60_sBH_TQM[3][len(capturedata_1e7_60_sBH_TQM[3])-1])

capturedata_80_sBH_TQM=[[],[],[]]

capturedata_80_sBH_TQM[0].append(capturedata_1e6_80_sBH_TQM[0][0]/Rg)
capturedata_80_sBH_TQM[1].append(capturedata_1e6_80_sBH_TQM[0][len(capturedata_1e6_80_sBH_TQM[0])-1]/Rg)
capturedata_80_sBH_TQM[2].append(capturedata_1e6_80_sBH_TQM[3][len(capturedata_1e6_80_sBH_TQM[3])-1])

capturedata_80_sBH_TQM[0].append(capturedata_5e6_80_sBH_TQM[0][0]/Rg)
capturedata_80_sBH_TQM[1].append(capturedata_5e6_80_sBH_TQM[0][len(capturedata_5e6_80_sBH_TQM[0])-1]/Rg)
capturedata_80_sBH_TQM[2].append(capturedata_5e6_80_sBH_TQM[3][len(capturedata_5e6_80_sBH_TQM[3])-1])

capturedata_80_sBH_TQM[0].append(capturedata_1e7_80_sBH_TQM[0][0]/Rg)
capturedata_80_sBH_TQM[1].append(capturedata_1e7_80_sBH_TQM[0][len(capturedata_1e7_80_sBH_TQM[0])-1]/Rg)
capturedata_80_sBH_TQM[2].append(capturedata_1e7_80_sBH_TQM[3][len(capturedata_1e7_80_sBH_TQM[3])-1])

####################################################

capturedata_1e2_sBH_TQM=[[],[]]

capturedata_1e3_sBH_TQM=[[],[]]

capturedata_1e3_sBH_TQM[0].append(capturedata_1e3_5_sBH_TQM[1][0])
capturedata_1e3_sBH_TQM[1].append(capturedata_1e3_5_sBH_TQM[3][len(capturedata_1e3_5_sBH_TQM[3])-1])

#capturedata_1e3_sBH_TQM[0].append(capturedata_1e3_15_sBH_TQM[1][0])
#capturedata_1e3_sBH_TQM[1].append(capturedata_1e3_15_sBH_TQM[3][len(capturedata_1e3_15_sBH_TQM[3])-1])

#capturedata_2e3_sBH_TQM=[[],[]]

#capturedata_2e3_sBH_TQM[0].append(capturedata_2e3_5_sBH_TQM[1][0])
#capturedata_2e3_sBH_TQM[1].append(capturedata_2e3_5_sBH_TQM[3][len(capturedata_2e3_5_sBH_TQM[3])-1])

capturedata_1e4_sBH_TQM=[[],[]]

capturedata_1e4_sBH_TQM[0].append(capturedata_1e4_5_sBH_TQM[1][0])
capturedata_1e4_sBH_TQM[1].append(capturedata_1e4_5_sBH_TQM[3][len(capturedata_1e4_5_sBH_TQM[3])-1])

capturedata_1e4_sBH_TQM[0].append(capturedata_1e4_15_sBH_TQM[1][0])
capturedata_1e4_sBH_TQM[1].append(capturedata_1e4_15_sBH_TQM[3][len(capturedata_1e4_15_sBH_TQM[3])-1])

#capturedata_2e4_sBH_TQM=[[],[]]

#capturedata_2e4_sBH_TQM[0].append(capturedata_2e4_5_sBH_TQM[1][0])
#capturedata_2e4_sBH_TQM[1].append(capturedata_2e4_5_sBH_TQM[3][len(capturedata_2e4_5_sBH_TQM[3])-1])

#capturedata_3e4_sBH_TQM=[[],[]]

#capturedata_3e4_sBH_TQM[0].append(capturedata_3e4_5_sBH_TQM[1][0])
#capturedata_3e4_sBH_TQM[1].append(capturedata_3e4_5_sBH_TQM[3][len(capturedata_3e4_5_sBH_TQM[3])-1])

#capturedata_4e4_sBH_TQM=[[],[]]

#capturedata_4e4_sBH_TQM[0].append(capturedata_4e4_5_sBH_TQM[1][0])
#capturedata_4e4_sBH_TQM[1].append(capturedata_4e4_5_sBH_TQM[3][len(capturedata_4e4_5_sBH_TQM[3])-1])

#capturedata_5e4_sBH_TQM=[[],[]]

#capturedata_5e4_sBH_TQM[0].append(capturedata_5e4_5_sBH_TQM[1][0])
#capturedata_5e4_sBH_TQM[1].append(capturedata_5e4_5_sBH_TQM[3][len(capturedata_5e4_5_sBH_TQM[3])-1])

capturedata_1e5_sBH_TQM=[[],[]]

capturedata_1e5_sBH_TQM[0].append(capturedata_1e5_5_sBH_TQM[1][0])
capturedata_1e5_sBH_TQM[1].append(capturedata_1e5_5_sBH_TQM[3][len(capturedata_1e5_5_sBH_TQM[3])-1])

capturedata_1e5_sBH_TQM[0].append(capturedata_1e5_15_sBH_TQM[1][0])
capturedata_1e5_sBH_TQM[1].append(capturedata_1e5_15_sBH_TQM[3][len(capturedata_1e5_15_sBH_TQM[3])-1])

capturedata_1e5_sBH_TQM[0].append(capturedata_1e5_30_sBH_TQM[1][0])
capturedata_1e5_sBH_TQM[1].append(capturedata_1e5_30_sBH_TQM[3][len(capturedata_1e5_30_sBH_TQM[3])-1])

#capturedata_2e5_sBH_TQM=[[],[]]

#capturedata_2e5_sBH_TQM[0].append(capturedata_2e5_5_sBH_TQM[1][0])
#capturedata_2e5_sBH_TQM[1].append(capturedata_2e5_5_sBH_TQM[3][len(capturedata_2e5_5_sBH_TQM[3])-1])

#capturedata_5e5_sBH_TQM=[[],[]]

#capturedata_5e5_sBH_TQM[0].append(capturedata_5e5_5_sBH_TQM[1][0])
#capturedata_5e5_sBH_TQM[1].append(capturedata_5e5_5_sBH_TQM[3][len(capturedata_5e5_5_sBH_TQM[3])-1])

capturedata_1e6_sBH_TQM=[[],[]]

capturedata_1e6_sBH_TQM[0].append(capturedata_1e6_5_sBH_TQM[1][0])
capturedata_1e6_sBH_TQM[1].append(capturedata_1e6_5_sBH_TQM[3][len(capturedata_1e6_5_sBH_TQM[3])-1])

capturedata_1e6_sBH_TQM[0].append(capturedata_1e6_15_sBH_TQM[1][0])
capturedata_1e6_sBH_TQM[1].append(capturedata_1e6_15_sBH_TQM[3][len(capturedata_1e6_15_sBH_TQM[3])-1])

capturedata_1e6_sBH_TQM[0].append(capturedata_1e6_30_sBH_TQM[1][0])
capturedata_1e6_sBH_TQM[1].append(capturedata_1e6_30_sBH_TQM[3][len(capturedata_1e6_30_sBH_TQM[3])-1])

capturedata_1e6_sBH_TQM[0].append(capturedata_1e6_45_sBH_TQM[1][0])
capturedata_1e6_sBH_TQM[1].append(capturedata_1e6_45_sBH_TQM[3][len(capturedata_1e6_45_sBH_TQM[3])-1])

capturedata_1e6_sBH_TQM[0].append(capturedata_1e6_60_sBH_TQM[1][0])
capturedata_1e6_sBH_TQM[1].append(capturedata_1e6_60_sBH_TQM[3][len(capturedata_1e6_60_sBH_TQM[3])-1])

capturedata_1e6_sBH_TQM[0].append(capturedata_1e6_80_sBH_TQM[1][0])
capturedata_1e6_sBH_TQM[1].append(capturedata_1e6_80_sBH_TQM[3][len(capturedata_1e6_80_sBH_TQM[3])-1])

capturedata_5e6_sBH_TQM=[[],[]]

capturedata_5e6_sBH_TQM[0].append(capturedata_5e6_5_sBH_TQM[1][0])
capturedata_5e6_sBH_TQM[1].append(capturedata_5e6_5_sBH_TQM[3][len(capturedata_5e6_5_sBH_TQM[3])-1])

capturedata_5e6_sBH_TQM[0].append(capturedata_5e6_15_sBH_TQM[1][0])
capturedata_5e6_sBH_TQM[1].append(capturedata_5e6_15_sBH_TQM[3][len(capturedata_5e6_15_sBH_TQM[3])-1])

capturedata_5e6_sBH_TQM[0].append(capturedata_5e6_30_sBH_TQM[1][0])
capturedata_5e6_sBH_TQM[1].append(capturedata_5e6_30_sBH_TQM[3][len(capturedata_5e6_30_sBH_TQM[3])-1])

capturedata_5e6_sBH_TQM[0].append(capturedata_5e6_45_sBH_TQM[1][0])
capturedata_5e6_sBH_TQM[1].append(capturedata_5e6_45_sBH_TQM[3][len(capturedata_5e6_45_sBH_TQM[3])-1])

capturedata_5e6_sBH_TQM[0].append(capturedata_5e6_60_sBH_TQM[1][0])
capturedata_5e6_sBH_TQM[1].append(capturedata_5e6_60_sBH_TQM[3][len(capturedata_5e6_60_sBH_TQM[3])-1])

capturedata_5e6_sBH_TQM[0].append(capturedata_5e6_80_sBH_TQM[1][0])
capturedata_5e6_sBH_TQM[1].append(capturedata_5e6_80_sBH_TQM[3][len(capturedata_5e6_80_sBH_TQM[3])-1])

capturedata_8e6_sBH_TQM=[[],[]]

capturedata_8e6_sBH_TQM[0].append(capturedata_8e6_5_sBH_TQM[1][0])
capturedata_8e6_sBH_TQM[1].append(capturedata_8e6_5_sBH_TQM[3][len(capturedata_8e6_5_sBH_TQM[3])-1])

capturedata_1e7_sBH_TQM=[[],[]]

capturedata_1e7_sBH_TQM[0].append(capturedata_1e7_15_sBH_TQM[1][0])
capturedata_1e7_sBH_TQM[1].append(capturedata_1e7_15_sBH_TQM[3][len(capturedata_1e7_15_sBH_TQM[3])-1])

capturedata_1e7_sBH_TQM[0].append(capturedata_1e7_30_sBH_TQM[1][0])
capturedata_1e7_sBH_TQM[1].append(capturedata_1e7_30_sBH_TQM[3][len(capturedata_1e7_30_sBH_TQM[3])-1])

capturedata_1e7_sBH_TQM[0].append(capturedata_1e7_45_sBH_TQM[1][0])
capturedata_1e7_sBH_TQM[1].append(capturedata_1e7_45_sBH_TQM[3][len(capturedata_1e7_45_sBH_TQM[3])-1])

capturedata_1e7_sBH_TQM[0].append(capturedata_1e7_60_sBH_TQM[1][0])
capturedata_1e7_sBH_TQM[1].append(capturedata_1e7_60_sBH_TQM[3][len(capturedata_1e7_60_sBH_TQM[3])-1])

capturedata_1e7_sBH_TQM[0].append(capturedata_1e7_80_sBH_TQM[1][0])
capturedata_1e7_sBH_TQM[1].append(capturedata_1e7_80_sBH_TQM[3][len(capturedata_1e7_80_sBH_TQM[3])-1])

########################################################################################################
########################################################################################################

#rgiant, SG
capturedata_1e1_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e1_45_rgiant_SG.txt")
capturedata_1e2_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e2_45_rgiant_SG.txt")
capturedata_1e3_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e3_45_rgiant_SG.txt")
capturedata_1e4_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e4_45_rgiant_SG.txt")
capturedata_1e5_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e5_45_rgiant_SG.txt")
capturedata_1e6_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e6_45_rgiant_SG.txt")
capturedata_1e7_45_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e7_45_rgiant_SG.txt")

capturedata_1e4_5_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e4_5_rgiant_SG.txt")
capturedata_1e4_15_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e4_15_rgiant_SG.txt")
capturedata_1e4_30_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e4_30_rgiant_SG.txt")
capturedata_1e4_60_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e4_60_rgiant_SG.txt")
capturedata_1e4_80_rgiant_SG=loadtxt("capturedata/capturedataSG/rgiant/capturedata_1e4_80_rgiant_SG.txt")

####################################################

capturedata_a_rgiant_SG=[[],[],[]]

capturedata_a_rgiant_SG[0].append(capturedata_1e1_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e1_45_rgiant_SG[0][len(capturedata_1e1_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e1_45_rgiant_SG[3][len(capturedata_1e1_45_rgiant_SG[3])-1])

capturedata_a_rgiant_SG[0].append(capturedata_1e2_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e2_45_rgiant_SG[0][len(capturedata_1e2_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e2_45_rgiant_SG[3][len(capturedata_1e2_45_rgiant_SG[3])-1])

capturedata_a_rgiant_SG[0].append(capturedata_1e3_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e3_45_rgiant_SG[0][len(capturedata_1e3_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e3_45_rgiant_SG[3][len(capturedata_1e3_45_rgiant_SG[3])-1])

capturedata_a_rgiant_SG[0].append(capturedata_1e4_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e4_45_rgiant_SG[0][len(capturedata_1e4_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e4_45_rgiant_SG[3][len(capturedata_1e4_45_rgiant_SG[3])-1])

capturedata_a_rgiant_SG[0].append(capturedata_1e5_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e5_45_rgiant_SG[0][len(capturedata_1e5_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e5_45_rgiant_SG[3][len(capturedata_1e5_45_rgiant_SG[3])-1])

capturedata_a_rgiant_SG[0].append(capturedata_1e6_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e6_45_rgiant_SG[0][len(capturedata_1e6_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e6_45_rgiant_SG[3][len(capturedata_1e6_45_rgiant_SG[3])-1])

capturedata_a_rgiant_SG[0].append(capturedata_1e7_45_rgiant_SG[0][0]/Rg)
capturedata_a_rgiant_SG[1].append(capturedata_1e7_45_rgiant_SG[0][len(capturedata_1e7_45_rgiant_SG[0])-1]/Rg)
capturedata_a_rgiant_SG[2].append(capturedata_1e7_45_rgiant_SG[3][len(capturedata_1e7_45_rgiant_SG[3])-1])

####################################################

capturedata_i_rgiant_SG=[[],[]]

capturedata_i_rgiant_SG[0].append(capturedata_1e4_5_rgiant_SG[1][0])
capturedata_i_rgiant_SG[1].append(capturedata_1e4_5_rgiant_SG[3][len(capturedata_1e4_5_rgiant_SG[3])-1])

capturedata_i_rgiant_SG[0].append(capturedata_1e4_15_rgiant_SG[1][0])
capturedata_i_rgiant_SG[1].append(capturedata_1e4_15_rgiant_SG[3][len(capturedata_1e4_15_rgiant_SG[3])-1])

capturedata_i_rgiant_SG[0].append(capturedata_1e4_30_rgiant_SG[1][0])
capturedata_i_rgiant_SG[1].append(capturedata_1e4_30_rgiant_SG[3][len(capturedata_1e4_30_rgiant_SG[3])-1])

capturedata_i_rgiant_SG[0].append(capturedata_1e4_45_rgiant_SG[1][0])
capturedata_i_rgiant_SG[1].append(capturedata_1e4_45_rgiant_SG[3][len(capturedata_1e4_45_rgiant_SG[3])-1])

capturedata_i_rgiant_SG[0].append(capturedata_1e4_60_rgiant_SG[1][0])
capturedata_i_rgiant_SG[1].append(capturedata_1e4_60_rgiant_SG[3][len(capturedata_1e4_60_rgiant_SG[3])-1])

capturedata_i_rgiant_SG[0].append(capturedata_1e4_80_rgiant_SG[1][0])
capturedata_i_rgiant_SG[1].append(capturedata_1e4_80_rgiant_SG[3][len(capturedata_1e4_80_rgiant_SG[3])-1])

########################################################################################################

#ostar, SG
#capturedata_1e1_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e1_45_ostar_SG.txt")
capturedata_1e2_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e2_45_ostar_SG.txt")
capturedata_1e3_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e3_45_ostar_SG.txt")
capturedata_1e4_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e4_45_ostar_SG.txt")
capturedata_1e5_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e5_45_ostar_SG.txt")
capturedata_1e6_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e6_45_ostar_SG.txt")
#capturedata_1e7_45_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e7_45_ostar_SG.txt")

capturedata_1e4_5_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e4_5_ostar_SG.txt")
capturedata_1e4_15_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e4_15_ostar_SG.txt")
capturedata_1e4_30_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e4_30_ostar_SG.txt")
capturedata_1e4_60_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e4_60_ostar_SG.txt")
capturedata_1e4_80_ostar_SG=loadtxt("capturedata/capturedataSG/ostar/capturedata_1e4_80_ostar_SG.txt")

####################################################

capturedata_a_ostar_SG=[[],[],[]]

#capturedata_a_ostar_SG[0].append(capturedata_1e1_45_ostar_SG[0][0]/Rg)
#capturedata_a_ostar_SG[1].append(capturedata_1e1_45_ostar_SG[0][len(capturedata_1e1_45_ostar_SG[0])-1]/Rg)
#capturedata_a_ostar_SG[2].append(capturedata_1e1_45_ostar_SG[3][len(capturedata_1e1_45_ostar_SG[3])-1])

capturedata_a_ostar_SG[0].append(capturedata_1e2_45_ostar_SG[0][0]/Rg)
capturedata_a_ostar_SG[1].append(capturedata_1e2_45_ostar_SG[0][len(capturedata_1e2_45_ostar_SG[0])-1]/Rg)
capturedata_a_ostar_SG[2].append(capturedata_1e2_45_ostar_SG[3][len(capturedata_1e2_45_ostar_SG[3])-1])

capturedata_a_ostar_SG[0].append(capturedata_1e3_45_ostar_SG[0][0]/Rg)
capturedata_a_ostar_SG[1].append(capturedata_1e3_45_ostar_SG[0][len(capturedata_1e3_45_ostar_SG[0])-1]/Rg)
capturedata_a_ostar_SG[2].append(capturedata_1e3_45_ostar_SG[3][len(capturedata_1e3_45_ostar_SG[3])-1])

capturedata_a_ostar_SG[0].append(capturedata_1e4_45_ostar_SG[0][0]/Rg)
capturedata_a_ostar_SG[1].append(capturedata_1e4_45_ostar_SG[0][len(capturedata_1e4_45_ostar_SG[0])-1]/Rg)
capturedata_a_ostar_SG[2].append(capturedata_1e4_45_ostar_SG[3][len(capturedata_1e4_45_ostar_SG[3])-1])

capturedata_a_ostar_SG[0].append(capturedata_1e5_45_ostar_SG[0][0]/Rg)
capturedata_a_ostar_SG[1].append(capturedata_1e5_45_ostar_SG[0][len(capturedata_1e5_45_ostar_SG[0])-1]/Rg)
capturedata_a_ostar_SG[2].append(capturedata_1e5_45_ostar_SG[3][len(capturedata_1e5_45_ostar_SG[3])-1])

capturedata_a_ostar_SG[0].append(capturedata_1e6_45_ostar_SG[0][0]/Rg)
capturedata_a_ostar_SG[1].append(capturedata_1e6_45_ostar_SG[0][len(capturedata_1e6_45_ostar_SG[0])-1]/Rg)
capturedata_a_ostar_SG[2].append(capturedata_1e6_45_ostar_SG[3][len(capturedata_1e6_45_ostar_SG[3])-1])

#capturedata_a_ostar_SG[0].append(capturedata_1e7_45_ostar_SG[0][0]/Rg)
#capturedata_a_ostar_SG[1].append(capturedata_1e7_45_ostar_SG[0][len(capturedata_1e7_45_ostar_SG[0])-1]/Rg)
#capturedata_a_ostar_SG[2].append(capturedata_1e7_45_ostar_SG[3][len(capturedata_1e7_45_ostar_SG[3])-1])

####################################################

capturedata_i_ostar_SG=[[],[]]

capturedata_i_ostar_SG[0].append(capturedata_1e4_5_ostar_SG[1][0])
capturedata_i_ostar_SG[1].append(capturedata_1e4_5_ostar_SG[3][len(capturedata_1e4_5_ostar_SG[3])-1])

capturedata_i_ostar_SG[0].append(capturedata_1e4_15_ostar_SG[1][0])
capturedata_i_ostar_SG[1].append(capturedata_1e4_15_ostar_SG[3][len(capturedata_1e4_15_ostar_SG[3])-1])

capturedata_i_ostar_SG[0].append(capturedata_1e4_30_ostar_SG[1][0])
capturedata_i_ostar_SG[1].append(capturedata_1e4_30_ostar_SG[3][len(capturedata_1e4_30_ostar_SG[3])-1])

capturedata_i_ostar_SG[0].append(capturedata_1e4_45_ostar_SG[1][0])
capturedata_i_ostar_SG[1].append(capturedata_1e4_45_ostar_SG[3][len(capturedata_1e4_45_ostar_SG[3])-1])

capturedata_i_ostar_SG[0].append(capturedata_1e4_60_ostar_SG[1][0])
capturedata_i_ostar_SG[1].append(capturedata_1e4_60_ostar_SG[3][len(capturedata_1e4_60_ostar_SG[3])-1])

capturedata_i_ostar_SG[0].append(capturedata_1e4_80_ostar_SG[1][0])
capturedata_i_ostar_SG[1].append(capturedata_1e4_80_ostar_SG[3][len(capturedata_1e4_80_ostar_SG[3])-1])

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

#rgiant, TQM
capturedata_1e2_45_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e2_45_rgiant_TQM.txt")
capturedata_1e3_45_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e3_45_rgiant_TQM.txt")
capturedata_1e4_45_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e4_45_rgiant_TQM.txt")
capturedata_1e5_45_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e5_45_rgiant_TQM.txt")
capturedata_1e6_45_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e6_45_rgiant_TQM.txt")
capturedata_1e7_45_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e7_45_rgiant_TQM.txt")

capturedata_1e4_5_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e4_5_rgiant_TQM.txt")
capturedata_1e4_15_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e4_15_rgiant_TQM.txt")
capturedata_1e4_30_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e4_30_rgiant_TQM.txt")
capturedata_1e4_60_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e4_60_rgiant_TQM.txt")
capturedata_1e4_80_rgiant_TQM=loadtxt("capturedata/capturedataTQM/rgiant/capturedata_1e4_80_rgiant_TQM.txt")

####################################################

capturedata_a_rgiant_TQM=[[],[],[]]

capturedata_a_rgiant_TQM[0].append(capturedata_1e2_45_rgiant_TQM[0][0]/Rg)
capturedata_a_rgiant_TQM[1].append(capturedata_1e2_45_rgiant_TQM[0][len(capturedata_1e2_45_rgiant_TQM[0])-1]/Rg)
capturedata_a_rgiant_TQM[2].append(capturedata_1e2_45_rgiant_TQM[3][len(capturedata_1e2_45_rgiant_TQM[3])-1])

capturedata_a_rgiant_TQM[0].append(capturedata_1e3_45_rgiant_TQM[0][0]/Rg)
capturedata_a_rgiant_TQM[1].append(capturedata_1e3_45_rgiant_TQM[0][len(capturedata_1e3_45_rgiant_TQM[0])-1]/Rg)
capturedata_a_rgiant_TQM[2].append(capturedata_1e3_45_rgiant_TQM[3][len(capturedata_1e3_45_rgiant_TQM[3])-1])

capturedata_a_rgiant_TQM[0].append(capturedata_1e4_45_rgiant_TQM[0][0]/Rg)
capturedata_a_rgiant_TQM[1].append(capturedata_1e4_45_rgiant_TQM[0][len(capturedata_1e4_45_rgiant_TQM[0])-1]/Rg)
capturedata_a_rgiant_TQM[2].append(capturedata_1e4_45_rgiant_TQM[3][len(capturedata_1e4_45_rgiant_TQM[3])-1])

capturedata_a_rgiant_TQM[0].append(capturedata_1e5_45_rgiant_TQM[0][0]/Rg)
capturedata_a_rgiant_TQM[1].append(capturedata_1e5_45_rgiant_TQM[0][len(capturedata_1e5_45_rgiant_TQM[0])-1]/Rg)
capturedata_a_rgiant_TQM[2].append(capturedata_1e5_45_rgiant_TQM[3][len(capturedata_1e5_45_rgiant_TQM[3])-1])

capturedata_a_rgiant_TQM[0].append(capturedata_1e6_45_rgiant_TQM[0][0]/Rg)
capturedata_a_rgiant_TQM[1].append(capturedata_1e6_45_rgiant_TQM[0][len(capturedata_1e6_45_rgiant_TQM[0])-1]/Rg)
capturedata_a_rgiant_TQM[2].append(capturedata_1e6_45_rgiant_TQM[3][len(capturedata_1e6_45_rgiant_TQM[3])-1])

capturedata_a_rgiant_TQM[0].append(capturedata_1e7_45_rgiant_TQM[0][0]/Rg)
capturedata_a_rgiant_TQM[1].append(capturedata_1e7_45_rgiant_TQM[0][len(capturedata_1e7_45_rgiant_TQM[0])-1]/Rg)
capturedata_a_rgiant_TQM[2].append(capturedata_1e7_45_rgiant_TQM[3][len(capturedata_1e7_45_rgiant_TQM[3])-1])

####################################################

capturedata_i_rgiant_TQM=[[],[]]

capturedata_i_rgiant_TQM[0].append(capturedata_1e4_5_rgiant_TQM[1][0])
capturedata_i_rgiant_TQM[1].append(capturedata_1e4_5_rgiant_TQM[3][len(capturedata_1e4_5_rgiant_TQM[3])-1])

capturedata_i_rgiant_TQM[0].append(capturedata_1e4_15_rgiant_TQM[1][0])
capturedata_i_rgiant_TQM[1].append(capturedata_1e4_15_rgiant_TQM[3][len(capturedata_1e4_15_rgiant_TQM[3])-1])

capturedata_i_rgiant_TQM[0].append(capturedata_1e4_30_rgiant_TQM[1][0])
capturedata_i_rgiant_TQM[1].append(capturedata_1e4_30_rgiant_TQM[3][len(capturedata_1e4_30_rgiant_TQM[3])-1])

capturedata_i_rgiant_TQM[0].append(capturedata_1e4_45_rgiant_TQM[1][0])
capturedata_i_rgiant_TQM[1].append(capturedata_1e4_45_rgiant_TQM[3][len(capturedata_1e4_45_rgiant_TQM[3])-1])

capturedata_i_rgiant_TQM[0].append(capturedata_1e4_60_rgiant_TQM[1][0])
capturedata_i_rgiant_TQM[1].append(capturedata_1e4_60_rgiant_TQM[3][len(capturedata_1e4_60_rgiant_TQM[3])-1])

capturedata_i_rgiant_TQM[0].append(capturedata_1e4_80_rgiant_TQM[1][0])
capturedata_i_rgiant_TQM[1].append(capturedata_1e4_80_rgiant_TQM[3][len(capturedata_1e4_80_rgiant_TQM[3])-1])

########################################################################################################

#ostar, TQM
#capturedata_1e2_45_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e2_45_ostar_TQM.txt")
capturedata_1e3_45_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e3_45_ostar_TQM.txt")
capturedata_1e4_45_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e4_45_ostar_TQM.txt")
capturedata_1e5_45_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e5_45_ostar_TQM.txt")
#capturedata_1e6_45_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e6_45_ostar_TQM.txt")
#capturedata_1e7_45_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e7_45_ostar_TQM.txt")

#capturedata_1e4_5_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e4_5_ostar_TQM.txt")
#capturedata_1e4_15_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e4_15_ostar_TQM.txt")
capturedata_1e4_30_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e4_30_ostar_TQM.txt")
capturedata_1e4_60_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e4_60_ostar_TQM.txt")
#capturedata_1e4_80_ostar_TQM=loadtxt("capturedata/capturedataTQM/ostar/capturedata_1e4_80_ostar_TQM.txt")

####################################################

capturedata_a_ostar_TQM=[[],[],[]]

#capturedata_a_ostar_TQM[0].append(capturedata_1e2_45_ostar_TQM[0][0]/Rg)
#capturedata_a_ostar_TQM[1].append(capturedata_1e2_45_ostar_TQM[0][len(capturedata_1e2_45_ostar_TQM[0])-1]/Rg)
#capturedata_a_ostar_TQM[2].append(capturedata_1e2_45_ostar_TQM[3][len(capturedata_1e2_45_ostar_TQM[3])-1])

capturedata_a_ostar_TQM[0].append(capturedata_1e3_45_ostar_TQM[0][0]/Rg)
capturedata_a_ostar_TQM[1].append(capturedata_1e3_45_ostar_TQM[0][len(capturedata_1e3_45_ostar_TQM[0])-1]/Rg)
capturedata_a_ostar_TQM[2].append(capturedata_1e3_45_ostar_TQM[3][len(capturedata_1e3_45_ostar_TQM[3])-1])

capturedata_a_ostar_TQM[0].append(capturedata_1e4_45_ostar_TQM[0][0]/Rg)
capturedata_a_ostar_TQM[1].append(capturedata_1e4_45_ostar_TQM[0][len(capturedata_1e4_45_ostar_TQM[0])-1]/Rg)
capturedata_a_ostar_TQM[2].append(capturedata_1e4_45_ostar_TQM[3][len(capturedata_1e4_45_ostar_TQM[3])-1])

capturedata_a_ostar_TQM[0].append(capturedata_1e5_45_ostar_TQM[0][0]/Rg)
capturedata_a_ostar_TQM[1].append(capturedata_1e5_45_ostar_TQM[0][len(capturedata_1e5_45_ostar_TQM[0])-1]/Rg)
capturedata_a_ostar_TQM[2].append(capturedata_1e5_45_ostar_TQM[3][len(capturedata_1e5_45_ostar_TQM[3])-1])

#capturedata_a_ostar_TQM[0].append(capturedata_1e6_45_ostar_TQM[0][0]/Rg)
#capturedata_a_ostar_TQM[1].append(capturedata_1e6_45_ostar_TQM[0][len(capturedata_1e6_45_ostar_TQM[0])-1]/Rg)
#capturedata_a_ostar_TQM[2].append(capturedata_1e6_45_ostar_TQM[3][len(capturedata_1e6_45_ostar_TQM[3])-1])

#capturedata_a_ostar_TQM[0].append(capturedata_1e7_45_ostar_TQM[0][0]/Rg)
#capturedata_a_ostar_TQM[1].append(capturedata_1e7_45_ostar_TQM[0][len(capturedata_1e7_45_ostar_TQM[0])-1]/Rg)
#capturedata_a_ostar_TQM[2].append(capturedata_1e7_45_ostar_TQM[3][len(capturedata_1e7_45_ostar_TQM[3])-1])

####################################################

capturedata_i_ostar_TQM=[[],[]]

#capturedata_i_ostar_TQM[0].append(capturedata_1e4_5_ostar_TQM[1][0])
#capturedata_i_ostar_TQM[1].append(capturedata_1e4_5_ostar_TQM[3][len(capturedata_1e4_5_ostar_TQM[3])-1])

#capturedata_i_ostar_TQM[0].append(capturedata_1e4_15_ostar_TQM[1][0])
#capturedata_i_ostar_TQM[1].append(capturedata_1e4_15_ostar_TQM[3][len(capturedata_1e4_15_ostar_TQM[3])-1])

capturedata_i_ostar_TQM[0].append(capturedata_1e4_30_ostar_TQM[1][0])
capturedata_i_ostar_TQM[1].append(capturedata_1e4_30_ostar_TQM[3][len(capturedata_1e4_30_ostar_TQM[3])-1])

capturedata_i_ostar_TQM[0].append(capturedata_1e4_45_ostar_TQM[1][0])
capturedata_i_ostar_TQM[1].append(capturedata_1e4_45_ostar_TQM[3][len(capturedata_1e4_45_ostar_TQM[3])-1])

capturedata_i_ostar_TQM[0].append(capturedata_1e4_60_ostar_TQM[1][0])
capturedata_i_ostar_TQM[1].append(capturedata_1e4_60_ostar_TQM[3][len(capturedata_1e4_60_ostar_TQM[3])-1])

#capturedata_i_ostar_TQM[0].append(capturedata_1e4_80_ostar_TQM[1][0])
#capturedata_i_ostar_TQM[1].append(capturedata_1e4_80_ostar_TQM[3][len(capturedata_1e4_80_ostar_TQM[3])-1])

########################################################################################################

#gstar, TQM
#capturedata_1e2_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e2_45_gstar_TQM.txt")
capturedata_1e3_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e3_45_gstar_TQM.txt")
#capturedata_1e4_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e4_45_gstar_TQM.txt")
#capturedata_1e5_45_gstar_TQM=loadtxt("capturedata/capturedataTQM/gstar/capturedata_1e5_45_gstar_TQM.txt")
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

#capturedata_a_gstar_TQM[0].append(capturedata_1e4_45_gstar_TQM[0][0]/Rg)
#capturedata_a_gstar_TQM[1].append(capturedata_1e4_45_gstar_TQM[0][len(capturedata_1e4_45_gstar_TQM[0])-1]/Rg)
#capturedata_a_gstar_TQM[2].append(capturedata_1e4_45_gstar_TQM[3][len(capturedata_1e4_45_gstar_TQM[3])-1])

#capturedata_a_gstar_TQM[0].append(capturedata_1e5_45_gstar_TQM[0][0]/Rg)
#capturedata_a_gstar_TQM[1].append(capturedata_1e5_45_gstar_TQM[0][len(capturedata_1e5_45_gstar_TQM[0])-1]/Rg)
#capturedata_a_gstar_TQM[2].append(capturedata_1e5_45_gstar_TQM[3][len(capturedata_1e5_45_gstar_TQM[3])-1])

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

#capturedata_i_gstar_TQM[0].append(capturedata_1e4_45_gstar_TQM[1][0])
#capturedata_i_gstar_TQM[1].append(capturedata_1e4_45_gstar_TQM[3][len(capturedata_1e4_45_gstar_TQM[3])-1])

capturedata_i_gstar_TQM[0].append(capturedata_1e4_60_gstar_TQM[1][0])
capturedata_i_gstar_TQM[1].append(capturedata_1e4_60_gstar_TQM[3][len(capturedata_1e4_60_gstar_TQM[3])-1])

#capturedata_i_gstar_TQM[0].append(capturedata_1e4_80_gstar_TQM[1][0])
#capturedata_i_gstar_TQM[1].append(capturedata_1e4_80_gstar_TQM[3][len(capturedata_1e4_80_gstar_TQM[3])-1])

########################################################################################################

#mstar, TQM
#capturedata_1e2_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e2_45_mstar_TQM.txt")
#capturedata_1e3_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e3_45_mstar_TQM.txt")
#capturedata_1e4_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_45_mstar_TQM.txt")
#capturedata_1e5_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e5_45_mstar_TQM.txt")
#capturedata_1e6_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e6_45_mstar_TQM.txt")
#capturedata_1e7_45_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e7_45_mstar_TQM.txt")

#capturedata_1e4_5_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_5_mstar_TQM.txt")
#capturedata_1e4_15_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_15_mstar_TQM.txt")
capturedata_1e4_30_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_30_mstar_TQM.txt")
#capturedata_1e4_60_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_60_mstar_TQM.txt")
#capturedata_1e4_80_mstar_TQM=loadtxt("capturedata/capturedataTQM/mstar/capturedata_1e4_80_mstar_TQM.txt")

####################################################

capturedata_a_mstar_TQM=[[],[],[]]

#capturedata_a_mstar_TQM[0].append(capturedata_1e2_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e2_45_mstar_TQM[0][len(capturedata_1e2_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e2_45_mstar_TQM[3][len(capturedata_1e2_45_mstar_TQM[3])-1])

#capturedata_a_mstar_TQM[0].append(capturedata_1e3_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e3_45_mstar_TQM[0][len(capturedata_1e3_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e3_45_mstar_TQM[3][len(capturedata_1e3_45_mstar_TQM[3])-1])

#capturedata_a_mstar_TQM[0].append(capturedata_1e4_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e4_45_mstar_TQM[0][len(capturedata_1e4_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e4_45_mstar_TQM[3][len(capturedata_1e4_45_mstar_TQM[3])-1])

#capturedata_a_mstar_TQM[0].append(capturedata_1e5_45_mstar_TQM[0][0]/Rg)
#capturedata_a_mstar_TQM[1].append(capturedata_1e5_45_mstar_TQM[0][len(capturedata_1e5_45_mstar_TQM[0])-1]/Rg)
#capturedata_a_mstar_TQM[2].append(capturedata_1e5_45_mstar_TQM[3][len(capturedata_1e5_45_mstar_TQM[3])-1])

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

#capturedata_i_mstar_TQM[0].append(capturedata_1e4_45_mstar_TQM[1][0])
#capturedata_i_mstar_TQM[1].append(capturedata_1e4_45_mstar_TQM[3][len(capturedata_1e4_45_mstar_TQM[3])-1])

#capturedata_i_mstar_TQM[0].append(capturedata_1e4_60_mstar_TQM[1][0])
#capturedata_i_mstar_TQM[1].append(capturedata_1e4_60_mstar_TQM[3][len(capturedata_1e4_60_mstar_TQM[3])-1])

#capturedata_i_mstar_TQM[0].append(capturedata_1e4_80_mstar_TQM[1][0])
#capturedata_i_mstar_TQM[1].append(capturedata_1e4_80_mstar_TQM[3][len(capturedata_1e4_80_mstar_TQM[3])-1])

########################################################################################################