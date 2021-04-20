i_0=pi/4
#irange=[pi/36,pi/12,pi/6,pi/4,pi/3,4*pi/9]
irange=[5/degrees,15/degrees,30/degrees,45/degrees,60/degrees,80/degrees,
        90/degrees,100/degrees,120/degrees,135/degrees,150/degrees,165/degrees,175/degrees]
irangedeg=[5*degrees,15*degrees,30*degrees,45*degrees,60*degrees,80*degrees,
           90*degrees,100*degrees,120*degrees,135*degrees,150*degrees,165*degrees,175*degrees]
ideg=[pi/36*degrees,pi/12*degrees,pi/6*degrees,pi/4*degrees,pi/3*degrees,4*pi/9*degrees]
am_0=1e4*Rg
amrange=[1e2*Rg,1e3*Rg,1e4*Rg,1e5*Rg,1e6*Rg,1e7*Rg]
amrange_SG=surfacedensityam_SG
amrange_TQM=surfacedensityam_TQM

irange2_SG=ivals_alli(amrange[0],hint_SG)
irange3_SG=ivals_alli(amrange[1],hint_SG)
irange4_SG=ivals_alli(amrange[2],hint_SG)
irange5_SG=ivals_alli(amrange[3],hint_SG)
irange6_SG=ivals_alli(amrange[4],hint_SG)
irange7_SG=ivals_alli(amrange[5],hint_SG)
ideg2_SG=ivals_alli(amrange[0],hint_SG)*(180/pi)
ideg3_SG=ivals_alli(amrange[1],hint_SG)*(180/pi)
ideg4_SG=ivals_alli(amrange[2],hint_SG)*(180/pi)
ideg5_SG=ivals_alli(amrange[3],hint_SG)*(180/pi)
ideg6_SG=ivals_alli(amrange[4],hint_SG)*(180/pi)
ideg7_SG=ivals_alli(amrange[5],hint_SG)*(180/pi)
irange2_TQM=ivals_alli(amrange[0],hint_TQM)
irange3_TQM=ivals_alli(amrange[1],hint_TQM)
irange4_TQM=ivals_alli(amrange[2],hint_TQM)
irange5_TQM=ivals_alli(amrange[3],hint_TQM)
irange6_TQM=ivals_alli(amrange[4],hint_TQM)
irange7_TQM=ivals_alli(amrange[5],hint_TQM)
ideg2_TQM=ivals_alli(amrange[0],hint_TQM)*(180/pi)
ideg3_TQM=ivals_alli(amrange[1],hint_TQM)*(180/pi)
ideg4_TQM=ivals_alli(amrange[2],hint_TQM)*(180/pi)
ideg5_TQM=ivals_alli(amrange[3],hint_TQM)*(180/pi)
ideg6_TQM=ivals_alli(amrange[4],hint_TQM)*(180/pi)
ideg7_TQM=ivals_alli(amrange[5],hint_TQM)*(180/pi)

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
        Tcaprgianta_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rrgiant,densityrgiant,hint_TQM,density_TQM))
        Tcapostara_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rostar,densityostar,hint_TQM,density_TQM))
        Tcapgstara_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rsun,densitysun,hint_TQM,density_TQM))
        Tcapmstara_TQM.append(Tcap_estim_STO(i_0,amrange_TQM[j],rmstar,densitymstar,hint_TQM,density_TQM))

Tcaprgianta_SG_135=[]
Tcapostara_SG_135=[]
Tcapgstara_SG_135=[]
Tcapmstara_SG_135=[]
Tcaprgianta_TQM_135=[]
Tcapostara_TQM_135=[]
Tcapgstara_TQM_135=[]
Tcapmstara_TQM_135=[]

for j in range(len(amrange_SG)):
        Tcaprgianta_SG_135.append(Tcap_estim_STO(135/degrees,amrange_SG[j],rrgiant,densityrgiant,hint_SG,density_SG))
        Tcapostara_SG_135.append(Tcap_estim_STO(135/degrees,amrange_SG[j],rostar,densityostar,hint_SG,density_SG))
        Tcapgstara_SG_135.append(Tcap_estim_STO(135/degrees,amrange_SG[j],rsun,densitysun,hint_SG,density_SG))
        Tcapmstara_SG_135.append(Tcap_estim_STO(135/degrees,amrange_SG[j],rmstar,densitymstar,hint_SG,density_SG))       
for j in range(len(amrange_TQM)):
        Tcaprgianta_TQM_135.append(Tcap_estim_STO(135/degrees,amrange_TQM[j],rrgiant,densityrgiant,hint_TQM,density_TQM))
        Tcapostara_TQM_135.append(Tcap_estim_STO(135/degrees,amrange_TQM[j],rostar,densityostar,hint_TQM,density_TQM))
        Tcapgstara_TQM_135.append(Tcap_estim_STO(135/degrees,amrange_TQM[j],rsun,densitysun,hint_TQM,density_TQM))
        Tcapmstara_TQM_135.append(Tcap_estim_STO(135/degrees,amrange_TQM[j],rmstar,densitymstar,hint_TQM,density_TQM))

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

Tcap175deg_SG=[]
Tcap165deg_SG=[]
Tcap150deg_SG=[]
Tcap135deg_SG=[]
Tcap120deg_SG=[]
Tcap100deg_SG=[]
Tcap90deg_SG=[]
Tcap80deg_SG=[]
Tcap60deg_SG=[]
Tcap45deg_SG=[]
Tcap30deg_SG=[]
Tcap15deg_SG=[]
Tcap05deg_SG=[]
Tcap175deg_TQM=[]
Tcap165deg_TQM=[]
Tcap150deg_TQM=[]
Tcap135deg_TQM=[]
Tcap120deg_TQM=[]
Tcap100deg_TQM=[]
Tcap90deg_TQM=[]
Tcap80deg_TQM=[]
Tcap60deg_TQM=[]
Tcap45deg_TQM=[]
Tcap30deg_TQM=[]
Tcap15deg_TQM=[]
Tcap05deg_TQM=[]
for j in range(len(amrange_SG)):
    Tcap175deg_SG.append(Tcap_estim_BHL(irange[12],amrange_SG[j],hint_SG,density_SG))
    Tcap165deg_SG.append(Tcap_estim_BHL(irange[11],amrange_SG[j],hint_SG,density_SG))
    Tcap150deg_SG.append(Tcap_estim_BHL(irange[10],amrange_SG[j],hint_SG,density_SG))
    Tcap135deg_SG.append(Tcap_estim_BHL(irange[9],amrange_SG[j],hint_SG,density_SG))
    Tcap120deg_SG.append(Tcap_estim_BHL(irange[8],amrange_SG[j],hint_SG,density_SG))
    Tcap100deg_SG.append(Tcap_estim_BHL(irange[7],amrange_SG[j],hint_SG,density_SG))
    Tcap90deg_SG.append(Tcap_estim_BHL(irange[6],amrange_SG[j],hint_SG,density_SG))
    Tcap80deg_SG.append(Tcap_estim_BHL(irange[5],amrange_SG[j],hint_SG,density_SG))
    Tcap60deg_SG.append(Tcap_estim_BHL(irange[4],amrange_SG[j],hint_SG,density_SG))
    Tcap45deg_SG.append(Tcap_estim_BHL(irange[3],amrange_SG[j],hint_SG,density_SG))
    Tcap30deg_SG.append(Tcap_estim_BHL(irange[2],amrange_SG[j],hint_SG,density_SG))
    Tcap15deg_SG.append(Tcap_estim_BHL(irange[1],amrange_SG[j],hint_SG,density_SG))
    Tcap05deg_SG.append(Tcap_estim_BHL(irange[0],amrange_SG[j],hint_SG,density_SG))
for j in range(len(amrange_TQM)):
    Tcap175deg_TQM.append(Tcap_estim_BHL(irange[12],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap165deg_TQM.append(Tcap_estim_BHL(irange[11],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap150deg_TQM.append(Tcap_estim_BHL(irange[10],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap135deg_TQM.append(Tcap_estim_BHL(irange[9],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap120deg_TQM.append(Tcap_estim_BHL(irange[8],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap100deg_TQM.append(Tcap_estim_BHL(irange[7],amrange_TQM[j],hint_TQM,density_TQM))
    Tcap90deg_TQM.append(Tcap_estim_BHL(irange[6],amrange_TQM[j],hint_TQM,density_TQM))
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

Tcap645_DYNa=[]
Tcap645_DYNi=[]
for j in range(len(amrange_SG)):
    Tcap645_DYNa.append(abs(Tcap_estim_DYN(irange[3],amrange_SG[j],hint_SG,density_SG)))
for j in range(len(irange6_SG)):
    Tcap645_DYNi.append(abs(Tcap_estim_DYN(irange2_SG[j],amrange[4],hint_SG,density_SG)))

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