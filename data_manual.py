
Fdrag_BHL_SG=[]
Fdrag_BHL_TQM=[]
Fdrag_STO_SG=[]
Fdrag_STO_TQM=[]
for i in range(len(capturedata_1e6_45_sBH_SG[0])):
    Fdrag_BHL_SG.append(F_BHL(capturedata_1e6_45_sBH_SG[1][i],capturedata_1e6_45_sBH_SG[0][i],
        rBH(capturedata_1e6_45_sBH_SG[1][i],capturedata_1e6_45_sBH_SG[0][i]),density_SG))
for i in range(len(capturedata_1e6_45_sBH_TQM[0])):
    Fdrag_BHL_TQM.append(F_BHL(capturedata_1e6_45_sBH_TQM[1][i],capturedata_1e6_45_sBH_TQM[0][i],
        rBH(capturedata_1e6_45_sBH_TQM[1][i],capturedata_1e6_45_sBH_TQM[0][i]),density_TQM))
for j in range(len(capturedata_1e6_45_rgiant_SG[0])):
    Fdrag_STO_SG.append(F_STO(capturedata_1e6_45_rgiant_SG[1][j],capturedata_1e6_45_rgiant_SG[0][j],
        rrgiant,density_SG))
for j in range(len(capturedata_1e6_45_rgiant_TQM[0])):
    Fdrag_STO_TQM.append(F_STO(capturedata_1e6_45_rgiant_TQM[1][j],capturedata_1e6_45_rgiant_TQM[0][j],
        rrgiant,density_TQM))

Wdrag_BHL_SG=[]
Wdrag_BHL_TQM=[]
Wdrag_STO_SG=[]
Wdrag_STO_TQM=[]
for i in range(len(capturedata_1e6_45_sBH_SG[0])):
    Wdrag_BHL_SG.append(Worb_BHL(capturedata_1e6_45_sBH_SG[1][i],capturedata_1e6_45_sBH_SG[0][i],
        rBH(capturedata_1e6_45_sBH_SG[1][i],capturedata_1e6_45_sBH_SG[0][i]),density_SG,hint_SG))
for i in range(len(capturedata_1e6_45_sBH_TQM[0])):
    Wdrag_BHL_TQM.append(Worb_BHL(capturedata_1e6_45_sBH_TQM[1][i],capturedata_1e6_45_sBH_TQM[0][i],
        rBH(capturedata_1e6_45_sBH_TQM[1][i],capturedata_1e6_45_sBH_TQM[0][i]),density_TQM,hint_TQM))
for j in range(len(capturedata_1e6_45_rgiant_SG[0])):
    Wdrag_STO_SG.append(Worb_STO(capturedata_1e6_45_rgiant_SG[1][j],capturedata_1e6_45_rgiant_SG[0][j],
        rrgiant,density_SG,hint_SG))
for j in range(len(capturedata_1e6_45_rgiant_TQM[0])):
    Wdrag_STO_TQM.append(Worb_STO(capturedata_1e6_45_rgiant_TQM[1][j],capturedata_1e6_45_rgiant_TQM[0][j],
        rrgiant,density_TQM,hint_TQM))

E_BHL_SG=[]
E_BHL_TQM=[]
E_STO_SG=[]
E_STO_TQM=[]
for i in range(len(capturedata_1e6_45_sBH_SG[0])):
    E_BHL_SG.append(Eorb(capturedata_1e6_45_sBH_SG[0][i],m_sBH))
for i in range(len(capturedata_1e6_45_sBH_TQM[0])):
    E_BHL_TQM.append(Eorb(capturedata_1e6_45_sBH_TQM[0][i],m_sBH))
for i in range(len(capturedata_1e6_45_rgiant_SG[0])):
    E_STO_SG.append(Eorb(capturedata_1e6_45_rgiant_SG[0][i],mrgiant))
for i in range(len(capturedata_1e6_45_rgiant_TQM[0])):
    E_STO_TQM.append(Eorb(capturedata_1e6_45_rgiant_TQM[0][i],mrgiant))

dens_BHL_SG=[]
dens_BHL_TQM=[]
dens_STO_SG=[]
dens_STO_TQM=[]
for i in range(len(capturedata_1e6_45_sBH_SG[0])):
    dens_BHL_SG.append(density_SG(capturedata_1e6_45_sBH_SG[0][i])/1e3)
for i in range(len(capturedata_1e6_45_sBH_TQM[0])):
    dens_BHL_TQM.append(density_TQM(capturedata_1e6_45_sBH_TQM[0][i])/1e3)
for i in range(len(capturedata_1e6_45_rgiant_SG[0])):
    dens_STO_SG.append(density_SG(capturedata_1e6_45_rgiant_SG[0][i])/1e3)
for i in range(len(capturedata_1e6_45_rgiant_TQM[0])):
    dens_STO_TQM.append(density_TQM(capturedata_1e6_45_rgiant_TQM[0][i])/1e3)

hrat_BHL_SG=[]
hrat_BHL_TQM=[]
hrat_STO_SG=[]
hrat_STO_TQM=[]
for i in range(len(capturedata_1e6_45_sBH_SG[0])):
    hrat_BHL_SG.append(hint_SG(capturedata_1e6_45_sBH_SG[0][i])/Rg)
for i in range(len(capturedata_1e6_45_sBH_TQM[0])):
    hrat_BHL_TQM.append(hint_TQM(capturedata_1e6_45_sBH_TQM[0][i])/Rg)
for i in range(len(capturedata_1e6_45_rgiant_SG[0])):
    hrat_STO_SG.append(hint_SG(capturedata_1e6_45_rgiant_SG[0][i])/Rg)
for i in range(len(capturedata_1e6_45_rgiant_TQM[0])):
    hrat_STO_TQM.append(hint_TQM(capturedata_1e6_45_rgiant_TQM[0][i])/Rg)