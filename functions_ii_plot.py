def stitch_plot_stellar_i():
    #fig=plt.figure(figsize=(12,12))
    fig=plt.figure(figsize=(12,6))
    plt.subplots_adjust(left=0.06, right=0.95, top=0.85, bottom=0.1, wspace=0, hspace=0.15)
    
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-10,10**5]
    f=[-10,10**8]
    g=[190,(10**5)]
    h=[190,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimei2=matplotlib.patches.Rectangle((-10,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei4=matplotlib.patches.Rectangle((-10,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    
    ax2=plt.subplot(121)
    ax2.plot(ideg4_SG,Tcaprgianti_SG,'r:',lw=uplimw, label='Red Giant',c='crimson')
    ax2.plot(capturedata_i_rgiant_SG[0],capturedata_i_rgiant_SG[1],'*',label='Red Giant',
        markersize=12, markerfacecolor='crimson', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcapostari_SG,'r-.',lw=uplimw,label='O Star',c='royalblue')
    ax2.plot(capturedata_i_ostar_SG[0], capturedata_i_ostar_SG[1],'*',label='O Star',
        markersize=12, markerfacecolor='royalblue', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcapgstari_SG,'r--',lw=uplimw, label='G Star',c='gold')
    ax2.plot(capturedata_i_gstar_SG[0], capturedata_i_gstar_SG[1],'*',label='G Star',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcapmstari_SG,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
    ax2.plot(capturedata_i_mstar_SG[0], capturedata_i_mstar_SG[1],'*',label='M Dwarf',
        markersize=12, markerfacecolor='darkorange', markeredgewidth=0.1, markeredgecolor='k')
    matplotlib.pyplot.annotate('$a_{0} = 10^{4}~R_g$', (3,7e9))
    matplotlib.pyplot.annotate('AGN lifetime', (73,3e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    ax2.add_patch(lifetimei2)
    ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=4, columnspacing=7, loc='center left', bbox_to_anchor=(-0.013,1.08))
    plt.yscale('log')
    ax2.set_xlabel('$i$ [$deg$]', fontsize=12)
    ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax2.set_xlim([-2,182])
    ax2.set_ylim([3e1,3e10])
    
    ax4=plt.subplot(122) 
    ax4.plot(ideg4_TQM,Tcaprgianti_TQM,'r:',lw=uplimw, label='Red Giant',c='crimson')
    ax4.plot(capturedata_i_rgiant_TQM[0],capturedata_i_rgiant_TQM[1],'*',label='Red Giant',
        markersize=12, markerfacecolor='crimson', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM,Tcapostari_TQM,'r-.',lw=uplimw,label='O Star',c='royalblue')
    ax4.plot(capturedata_i_ostar_TQM[0], capturedata_i_ostar_TQM[1],'*',label='O Star',
        markersize=12, markerfacecolor='royalblue', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM,Tcapgstari_TQM,'r--',lw=uplimw, label='G Star',c='gold')
    ax4.plot(capturedata_i_gstar_TQM[0], capturedata_i_gstar_TQM[1],'*',label='G Star',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM,Tcapmstari_TQM,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
    ax4.plot(capturedata_i_mstar_TQM[0], capturedata_i_mstar_TQM[1],'*',label='M Dwarf',
        markersize=12, markerfacecolor='darkorange', markeredgewidth=0.1, markeredgecolor='k')
    #
    ax4.plot(capturedata_i_gstar_TQM[0], capturedata_i_gstar_TQM[1],'*',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
    #
    #matplotlib.pyplot.annotate('$a_{0} = 10^{4}~R_g$', (0,1e5))
    matplotlib.pyplot.annotate('AGN lifetime', (73,3.5e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    ax4.add_patch(lifetimei4)
    #ax4.legend(fontsize=9.5, framealpha=1, edgecolor= 'k', handlelength=2.7,
    #    ncol=4, columnspacing=2.7, loc='center left', bbox_to_anchor=(-0.012,1.08))
    plt.yscale('log')
    ax4.set_xlabel('$i$ [$deg$]', fontsize=12)
    #ax4.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax4.set_xlim([-2,182])
    ax4.set_ylim([3e1,3e10])
    ax4.yaxis.tick_right()
    
    plt.savefig('plots/capturetimeplots/stellar-Tcap_i.pdf')
    plt.savefig('plots/paperplots/stellar-Tcap_i.pdf')

def it_acolor_plot_proretro(): #this one
    fig=plt.figure(figsize=(12,6))
    vmin=1e1; vmax=1e4; norm=matplotlib.colors.LogNorm(vmax=vmax, vmin=vmin)
    #norm=plt.Normalize(vmax=vmax, vmin=vmin)
    plt.subplots_adjust(left=0.05, right=0.96, top=0.98, bottom=0.25, wspace=0.0)
    
    ax1=plt.subplot(121)
    ax1.scatter(capturedata_1e4_5_rgiant_SG[3],capturedata_1e4_5_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_5_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_15_rgiant_SG[3],capturedata_1e4_15_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_15_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_30_rgiant_SG[3],capturedata_1e4_30_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_30_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_45_rgiant_SG[3],capturedata_1e4_45_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_45_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_60_rgiant_SG[3],capturedata_1e4_60_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_60_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_80_rgiant_SG[3],capturedata_1e4_80_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_80_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_90_rgiant_SG[3],capturedata_1e4_90_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_90_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_100_rgiant_SG[3],capturedata_1e4_100_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_100_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_120_rgiant_SG[3],capturedata_1e4_120_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_120_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_135_rgiant_SG[3],capturedata_1e4_135_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_135_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_150_rgiant_SG[3],capturedata_1e4_150_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_150_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    ax1.scatter(capturedata_1e4_165_rgiant_SG[3],capturedata_1e4_165_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_165_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    delta=ax1.scatter(capturedata_1e4_175_rgiant_SG[3],capturedata_1e4_175_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_175_rgiant_SG[0]/Rg, cmap='inferno_r', norm=norm)
    
    matplotlib.pyplot.annotate('SG', (4.5e3,175))
    #ax1.set_xlim([0,5.5e3])
    plt.xscale('log')
    #ax1.set_xscale('symlog')
    ax1.set_xlabel('$t$ [$yr$]')
    ax1.set_ylabel('$i$ [$deg$]')
    
    ax2=plt.subplot(122)
    ax2.scatter(capturedata_1e4_5_rgiant_TQM[3],capturedata_1e4_5_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_5_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_15_rgiant_TQM[3],capturedata_1e4_15_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_15_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_30_rgiant_TQM[3],capturedata_1e4_30_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_30_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_45_rgiant_TQM[3],capturedata_1e4_45_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_45_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_60_rgiant_TQM[3],capturedata_1e4_60_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_60_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_80_rgiant_TQM[3],capturedata_1e4_80_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_80_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_90_rgiant_TQM[3],capturedata_1e4_90_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_90_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_100_rgiant_TQM[3],capturedata_1e4_100_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_100_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_120_rgiant_TQM[3],capturedata_1e4_120_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_120_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_135_rgiant_TQM[3],capturedata_1e4_135_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_135_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_150_rgiant_TQM[3],capturedata_1e4_150_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_150_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    ax2.scatter(capturedata_1e4_165_rgiant_TQM[3],capturedata_1e4_165_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_165_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)    
    delta=ax2.scatter(capturedata_1e4_175_rgiant_TQM[3],capturedata_1e4_175_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_175_rgiant_TQM[0]/Rg, cmap='inferno_r', norm=norm)
    
    matplotlib.pyplot.annotate('TQM', (3e5,175))
    #ax2.set_xlim([0,4e5])
    plt.xscale('log') 
    #ax2.set_xscale('symlog')
    ax2.set_xlabel('$t$ [$yr$]')
    #ax2.set_ylabel('$i$ [$deg$]')
    ax2.yaxis.tick_right()
    
    cbaxes = fig.add_axes([0.05, 0.1, 0.917, 0.03]) 
    cb = plt.colorbar(delta, cax = cbaxes, orientation='horizontal') 
    cb.set_label('a [Rg]')
    cb.ax.invert_xaxis()
    cb.ax.set_xscale('log')
    #ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
    #    ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    
    plt.savefig('plots/propertyplots/it_proretro.pdf')
    plt.savefig('plots/propertyplots/it_proretro.jpeg')

def it_acolor_plot_45135(): #this one
    fig=plt.figure(figsize=(12,6))
    vmin=1e1; vmax=1e4; norm=matplotlib.colors.LogNorm(vmax=vmax, vmin=vmin)
    #norm=plt.Normalize(vmax=vmax, vmin=vmin)
    plt.subplots_adjust(left=0.06, right=0.96, top=0.98, bottom=0.25, wspace=0.0)
    
    ax1=plt.subplot(121)
    delta=ax1.scatter(capturedata_1e4_135_rgiant_SG[3],capturedata_1e4_135_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_135_rgiant_SG[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax1.scatter(capturedata_1e4_n135_rgiant_SG[3],capturedata_1e4_n135_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_n135_rgiant_SG[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax1.scatter(capturedata_1e4_n45_rgiant_SG[3],capturedata_1e4_n45_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_n45_rgiant_SG[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax1.scatter(capturedata_1e4_45_rgiant_SG[3],capturedata_1e4_45_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e4_45_rgiant_SG[0]/Rg, cmap='inferno_r',
        norm=norm)
    matplotlib.pyplot.annotate('SG', (1e4,175))
    plt.xscale('log')
    ax1.set_xlabel('$t$ [$yr$]')
    ax1.set_ylabel('$i$ [$deg$]')
    
    ax2=plt.subplot(122)
    delta=ax2.scatter(capturedata_1e4_135_rgiant_TQM[3],capturedata_1e4_135_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_135_rgiant_TQM[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax2.scatter(capturedata_1e4_n135_rgiant_TQM[3],capturedata_1e4_n135_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_n135_rgiant_TQM[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax2.scatter(capturedata_1e4_n45_rgiant_TQM[3],capturedata_1e4_n45_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_n45_rgiant_TQM[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax2.scatter(capturedata_1e4_45_rgiant_TQM[3],capturedata_1e4_45_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e4_45_rgiant_TQM[0]/Rg, cmap='inferno_r',
        norm=norm)
    matplotlib.pyplot.annotate('TQM', (7e5,175))
    plt.xscale('log') 
    ax2.set_xlabel('$t$ [$yr$]')
    #ax2.set_ylabel('$i$ [$deg$]')
    ax2.yaxis.tick_right()
    
    cbaxes = fig.add_axes([0.05, 0.1, 0.917, 0.03]) 
    cb = plt.colorbar(delta, cax = cbaxes, orientation='horizontal') 
    cb.set_label('a [Rg]')
    cb.ax.invert_xaxis()
    cb.ax.set_xscale('log')
    #ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
    #    ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    
    plt.savefig('plots/propertyplots/it_45135.pdf')
    plt.savefig('plots/propertyplots/it_45135.jpeg')

def fig2_plot():
    fig=plt.figure(figsize=(8,12)) #9.6
    plt.subplots_adjust(left=0.09, right=0.99, top=0.955, bottom=0.08, wspace=0.2, hspace=0.2)
    
    uplimw=2.5
    delaw=0.75
    acapw=0.2
    
    i_0=pi/4
    am_0=1e4*Rg
    irange=[pi/36,pi/12,pi/6,pi/4,pi/3,4*pi/9]
    amrange=[1e2*Rg,1e3*Rg,1e4*Rg,1e5*Rg,1e6*Rg,1e7*Rg]
    amrange_SG=surfacedensityam_SG
    amrange_TQM=surfacedensityam_TQM
    vc_ratio_a5_SG=[]
    vc_ratio_a10_SG=[]
    vc_ratio_a15_SG=[]
    vc_ratio_a45_SG=[]
    vc_ratio_a80_SG=[]
    vc_ratio_a5_TQM=[]
    vc_ratio_a10_TQM=[]
    vc_ratio_a15_TQM=[]
    vc_ratio_a45_TQM=[]
    vc_ratio_a80_TQM=[]
    vc_ratio_i=[]
    moc_SG=[]
    moc_TQM=[]
    
    uplimw=2.5
    amrange_SG=surfacedensityam_SG
    amrange_TQM=surfacedensityam_TQM
    icrit_TQM=[]
    icrit_SG=[]
    
    for i in range(len(amrange_SG)):
        icrit_SG.append(imin(amrange_SG[i],hint_SG)*degrees)
    for i in range(len(amrange_TQM)):
        icrit_TQM.append(imin(amrange_TQM[i],hint_TQM)*degrees) 
    
    for i in range(len(amrange_SG)):
        vc_ratio_a5_SG.append(vrel(5/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a10_SG.append(vrel(10/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a15_SG.append(vrel(15/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a45_SG.append(vrel(45/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a80_SG.append(vrel(80/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        moc_SG.append(4)
        
    for i in range(len(amrange_TQM)):
        vc_ratio_a5_TQM.append(vrel(5/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a10_TQM.append(vrel(10/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a15_TQM.append(vrel(15/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a45_TQM.append(vrel(45/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a80_TQM.append(vrel(80/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        moc_TQM.append(4)        
    
    ax3=plt.subplot(311)
    ax3.plot(amrange_SG/Rg,icrit_SG,'r-',lw=uplimw,label='SG',c='b')
    ax3.plot(amrange_TQM/Rg,icrit_TQM,'r-',lw=uplimw,label='TQM',c='r')
    ax3.plot(amrange_SG/Rg,icrit_SG,'r-',lw=uplimw,c='b')
    ax3.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=7, columnspacing=0.6, loc='center left', bbox_to_anchor=(-0.015,1.1))
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax3.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax3.set_ylabel('$i_{critcal}$ [$deg$]', fontsize=12)   
    
    ax1=plt.subplot(312)
    ax1.plot(amrange_SG/Rg,vc_ratio_a5_SG,'r-',lw=uplimw,label='5',c='lavender')
    ax1.plot(amrange_SG/Rg,vc_ratio_a10_SG,'r-',lw=uplimw,label='10',c='lightsteelblue')
    ax1.plot(amrange_SG/Rg,vc_ratio_a15_SG,'r-',lw=uplimw,label='15',c='slategrey')
    ax1.plot(amrange_SG/Rg,vc_ratio_a45_SG,'r-',lw=uplimw,label='45',c='slateblue')
    ax1.plot(amrange_SG/Rg,vc_ratio_a80_SG,'r-',lw=uplimw,label='80',c='navy')
    ax1.plot(amrange_SG/Rg,moc_SG,'r--',lw=delaw,c='k')
    #ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
    #    ncol=7, columnspacing=0.6, loc='center left', bbox_to_anchor=(-0.015,1.1))
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax1.set_ylabel('$v_{rel}/c_{s}$', fontsize=12)
    #ax1.set_xlim([3e0,3e7])
    #ax1.set_ylim([1e3,3e14])
    
    ax2=plt.subplot(313)
    ax2.plot(amrange_TQM/Rg,vc_ratio_a5_TQM,'r-',lw=uplimw,label='5',c='lavender')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a10_TQM,'r-',lw=uplimw,label='10',c='lightsteelblue')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a15_TQM,'r-',lw=uplimw,label='15',c='slategrey')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a45_TQM,'r-',lw=uplimw,label='45',c='slateblue')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a80_TQM,'r-',lw=uplimw,label='80',c='navy')
    ax2.plot(amrange_TQM/Rg,moc_TQM,'r--',lw=delaw,c='k')
    ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=7, columnspacing=0.6, loc='center left', bbox_to_anchor=(-0.015,-0.25))
    matplotlib.pyplot.annotate('$i = 45^{\circ}s$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax2.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax2.set_ylabel('$v_{rel}/c_{s}$', fontsize=12)
    #ax1.set_xlim([3e0,3e7])
        
    #ax2=plt.subplot(212)
    #ax2.plot(irange,vc_ratio_i,'r-',lw=uplimw,label='vrel/cs',c='k')
    #ax2.plot(irange,vc_ratio_i,'r-',lw=uplimw,label='DYN',c='rebeccapurple')
    #ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
    #    ncol=6, columnspacing=0.55, loc='center left', bbox_to_anchor=(-0.015,1.11))    
    #matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,1e5))
    #plt.yscale('log')
    #ax2.set_xlabel('$i$ [$deg$]', fontsize=12)
    #ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    #ax2.set_xlim([-2,92])
    #ax2.set_ylim([1e2,3e14])
    
    plt.savefig('plots/paperplots/fig2.pdf')


def icrit_plot():
    fig=plt.figure(figsize=(8,4.5)) #9.6
    plt.subplots_adjust(left=0.08, right=0.99, top=0.93, bottom=0.06, wspace=0.2, hspace=0.2)
    
    uplimw=2.5
    amrange_SG=surfacedensityam_SG
    amrange_TQM=surfacedensityam_TQM
    icrit_TQM=[]
    icrit_SG=[]
    
    for i in range(len(amrange_SG)):
        icrit_SG.append(imin(amrange_SG[i],hint_SG)*degrees)
    for i in range(len(amrange_TQM)):
        icrit_TQM.append(imin(amrange_TQM[i],hint_TQM)*degrees)
        
    ax1=plt.subplot(111)
    ax1.plot(amrange_SG/Rg,icrit_SG,'r-',lw=uplimw,label='SG',c='b')
    ax1.plot(amrange_TQM/Rg,icrit_TQM,'r-',lw=uplimw,label='TQM',c='r')
    ax1.plot(amrange_SG/Rg,icrit_SG,'r-',lw=uplimw,c='b')
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=7, columnspacing=0.6, loc='center left', bbox_to_anchor=(-0.015,1.1))
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax1.set_ylabel('$i_{critcal}$ [$deg$]', fontsize=12)    
    
    plt.savefig('plots/paperplots/icrit_plot.pdf')

def vrel_cs_ratio_plot():
    fig=plt.figure(figsize=(12,6)) #9.6
    plt.subplots_adjust(left=0.075, right=0.95, top=0.93, bottom=0.085, wspace=0, hspace=0.2)
    
    uplimw=2.5
    delaw=0.75
    acapw=0.2
    
    i_0=pi/4
    am_0=1e4*Rg
    irange=[pi/36,pi/12,pi/6,pi/4,pi/3,4*pi/9]
    amrange=[1e2*Rg,1e3*Rg,1e4*Rg,1e5*Rg,1e6*Rg,1e7*Rg]
    amrange_SG=surfacedensityam_SG
    amrange_TQM=surfacedensityam_TQM
    vc_ratio_a5_SG=[]
    vc_ratio_a10_SG=[]
    vc_ratio_a15_SG=[]
    vc_ratio_a45_SG=[]
    vc_ratio_a80_SG=[]
    vc_ratio_a5_TQM=[]
    vc_ratio_a10_TQM=[]
    vc_ratio_a15_TQM=[]
    vc_ratio_a45_TQM=[]
    vc_ratio_a80_TQM=[]
    vc_ratio_i=[]
    moc_SG=[]
    moc_TQM=[]
    
    for i in range(len(amrange_SG)):
        vc_ratio_a5_SG.append(vrel(5/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a10_SG.append(vrel(10/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a15_SG.append(vrel(15/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a45_SG.append(vrel(45/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        vc_ratio_a80_SG.append(vrel(80/degrees,amrange_SG[i])/csound(amrange_SG[i],hint_SG))
        moc_SG.append(4)
        
    for i in range(len(amrange_TQM)):
        vc_ratio_a5_TQM.append(vrel(5/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a10_TQM.append(vrel(10/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a15_TQM.append(vrel(15/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a45_TQM.append(vrel(45/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        vc_ratio_a80_TQM.append(vrel(80/degrees,amrange_TQM[i])/csound(amrange_TQM[i],hint_TQM))
        moc_TQM.append(4)
    
    ax1=plt.subplot(121)
    ax1.plot(amrange_SG/Rg,vc_ratio_a5_SG,'r-',lw=uplimw,label='5',c='lavender')
    ax1.plot(amrange_SG/Rg,vc_ratio_a10_SG,'r-',lw=uplimw,label='10',c='lightsteelblue')
    ax1.plot(amrange_SG/Rg,vc_ratio_a15_SG,'r-',lw=uplimw,label='15',c='slategrey')
    ax1.plot(amrange_SG/Rg,vc_ratio_a45_SG,'r-',lw=uplimw,label='45',c='slateblue')
    ax1.plot(amrange_SG/Rg,vc_ratio_a80_SG,'r-',lw=uplimw,label='80',c='navy')
    ax1.plot(amrange_SG/Rg,moc_SG,'r--',lw=delaw,c='k')
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=8,
        ncol=7, columnspacing=3.1, loc='center left', bbox_to_anchor=(-0.015,1.05))
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax1.set_ylabel('$v_{rel}/c_{s}$', fontsize=12)
    #ax1.set_xlim([3e0,3e7])
    ax1.set_ylim([1e-1,5e3])
    
    ax2=plt.subplot(122)
    ax2.plot(amrange_TQM/Rg,vc_ratio_a5_TQM,'r-',lw=uplimw,label='5',c='lavender')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a10_TQM,'r-',lw=uplimw,label='10',c='lightsteelblue')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a15_TQM,'r-',lw=uplimw,label='15',c='slategrey')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a45_TQM,'r-',lw=uplimw,label='45',c='slateblue')
    ax2.plot(amrange_TQM/Rg,vc_ratio_a80_TQM,'r-',lw=uplimw,label='80',c='navy')
    ax2.plot(amrange_TQM/Rg,moc_TQM,'r--',lw=delaw,c='k')
    matplotlib.pyplot.annotate('$i = 45^{\circ}s$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax2.set_xlabel('$a$ [$R_g$]', fontsize=12)
    #ax2.set_ylabel('$v_{rel}/c_{s}$', fontsize=12)
    #ax1.set_xlim([3e0,3e7])
    ax2.set_ylim([1e-1,5e3])
    ax2.yaxis.tick_right()
        
    #ax2=plt.subplot(212)
    #ax2.plot(irange,vc_ratio_i,'r-',lw=uplimw,label='vrel/cs',c='k')
    #ax2.plot(irange,vc_ratio_i,'r-',lw=uplimw,label='DYN',c='rebeccapurple')
    #ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
    #    ncol=6, columnspacing=0.55, loc='center left', bbox_to_anchor=(-0.015,1.11))    
    #matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,1e5))
    #plt.yscale('log')
    #ax2.set_xlabel('$i$ [$deg$]', fontsize=12)
    #ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    #ax2.set_xlim([-2,92])
    #ax2.set_ylim([1e2,3e14])
    
    plt.savefig('plots/paperplots/vrel_cs_ratio_plot.pdf')

def stitch_plot_sBH_COMP():
    fig=plt.figure(figsize=(6,12)) #9.6
    #plt.subplots_adjust(left=0.06, right=0.99, top=0.94, bottom=0.06, wspace=0.2, hspace=0.3)
    plt.subplots_adjust(left=0.06, right=0.95, top=0.9, bottom=0.06, wspace=0, hspace=0.4)
    
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-180,10**5]
    f=[-180,10**8]
    g=[180,(10**5)]
    h=[180,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimea1=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei2=matplotlib.patches.Rectangle((-180,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimea3=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei4=matplotlib.patches.Rectangle((-180,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    
    ax1=plt.subplot(211)
    ax1.plot(amrange_SG/Rg,Tcap45deg_SG,'r-',lw=uplimw,label='BHL',c='k')
    ax1.plot(amrange_SG/Rg,Tcap645_DYNa,'r-',lw=uplimw,label='DYN',c='rebeccapurple')
    matplotlib.pyplot.annotate('AGN lifetime', (1.5e6,1e7))
    ax1.add_patch(lifetimea1)
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=7, columnspacing=0.6, loc='center left', bbox_to_anchor=(-0.015,1.1))
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e5))
    plt.xscale('log')
    plt.yscale('log')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax1.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax1.set_xlim([3e0,3e7])
    #ax1.set_ylim([1e3,3e14])
        
    ax2=plt.subplot(212)
    ax2.plot(ideg6_SG,Tcap6Rg_SG,'r-',lw=uplimw,label='BHL',c='k')
    ax2.plot(ideg6_SG,Tcap645_DYNi,'r-',lw=uplimw,label='DYN',c='rebeccapurple')
    matplotlib.pyplot.annotate('AGN lifetime', (73,1e7))
    ax2.add_patch(lifetimei2)
    ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=6, columnspacing=0.55, loc='center left', bbox_to_anchor=(-0.015,1.11))    
    matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,1e5))
    plt.yscale('log')
    ax2.set_xlabel('$i$ [$deg$]', fontsize=12)
    ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax2.set_xlim([-2,92])
    #ax2.set_ylim([1e2,3e14])
    
    #plt.savefig('plots/capturetimeplots/sBH-Tcap-COMP.pdf')
    plt.savefig('plots/paperplots/sBH-Tcap-COMP.pdf')

def fig1_plot():    
    densityden_TQM=[]
    for i in range(len(surfacedensityam_TQM)):
        densityden_TQM.append(density_TQM(surfacedensityam_TQM[i])/1e3)
    densityden_SG=[]
    for i in range(len(surfacedensityam_SG)):
        densityden_SG.append(density_SG(surfacedensityam_SG[i])/1e3)
    
    fig=plt.figure(figsize=(16,8))
    #fig=plt.figure(figsize=(7,8))
    plt.subplots_adjust(left=0.06, right=0.94, top=0.95, bottom=0.075, wspace=-0.275, hspace=0.0)  

    ax1 = plt.subplot(121)
    ax2 = plt.subplot(233)
    ax3 = plt.subplot(236)
    #ax2 = plt.subplot(244)
    #ax3 = plt.subplot(248)
    lwid=2
    
    ax1.plot(harg_SG,h_SG/Rg/2,label='SG',lw=lwid,c='b')
    ax1.plot(harg_TQM,h_TQM/Rg/2,label='TQM',lw=lwid,c='r')
    ax1.plot(-harg_TQM,-h_TQM/Rg/2,lw=lwid,c='r')
    ax1.plot(-harg_TQM,h_TQM/Rg/2,lw=lwid,c='r')
    ax1.plot(harg_TQM,-h_TQM/Rg/2,lw=lwid,c='r')
    ax1.plot(harg_SG,h_SG/Rg/2,lw=lwid,c='b') #,label='SG'
    ax1.plot(-harg_SG,-h_SG/Rg/2,lw=lwid,c='b')
    ax1.plot(-harg_SG,h_SG/Rg/2,lw=lwid,c='b')
    ax1.plot(harg_SG,-h_SG/Rg/2,lw=lwid,c='b')
    ax1.axhline(y=0,lw=1,linestyle="--",c='black')
    ax1.plot([0,10**4],[0,10**5],'r:',lw=1,c='black')
    ax1.plot(0,0,'o',markersize=20,c='black')
    ax1.plot(10**4,10**5,'*',markersize=15, markeredgewidth=0.1, markeredgecolor='k', c='black')
    #matplotlib.pyplot.annotate('$a$', (1e2,1e3),fontsize=12) #labeling orbital radius
    #matplotlib.pyplot.annotate('$i$', (1e1,1e1),fontsize=12) #labeling orbital inclination
    ax1.set_xlabel('$a$ [$R_g$]',fontsize=16)
    ax1.set_ylabel('$H$ [$R_g$]',fontsize=16)
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=4,
               ncol=2, columnspacing=2, loc='center left', bbox_to_anchor=(-0.009,1.03))
    ax1.set_yscale('symlog')
    ax1.set_xscale('symlog')
    ax1.xaxis.set_tick_params(labelsize=12)
    ax1.yaxis.set_tick_params(labelsize=12)
    ax1.xaxis.set_ticks([-1e8, -1e7, -1e6, -1e5, -1e4, -1e3, -1e2, -1e1, 0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8])
    ax1.yaxis.set_ticks([-1e7, -1e6, -1e5, -1e4, -1e3, -1e2, -1e1, 0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7])
#    ax1.set_xlim([-1e8,1e8])
    
    ax2.loglog(harg_TQM,hovera_TQM,lw=lwid,label='TQM',c='r')
    ax2.loglog(harg_SG,hovera_SG,lw=lwid,label='SG',c='b')
    #ax2.set_xlabel('$a$ [$R_g$]',fontsize=16)
    ax2.set_ylabel('$H$ / $a$',fontsize=16)
    ax2.xaxis.set_tick_params(labelsize=12)
    ax2.yaxis.set_tick_params(labelsize=12)
#    ax2.xaxis.set_ticks([1e1, 1e3, 1e5, 1e7])
#    ax2.yaxis.set_ticks([1e-3, 1e-2, 1e-1, 1e0])
    ax2.yaxis.set_label_position("right")
    ax2.yaxis.tick_right()
    ax2.xaxis.set_label_position("top")
    ax2.xaxis.tick_top()
    
    ax3.loglog(surfacedensityam_TQM/Rg,densityden_TQM,lw=lwid,label='TQM',c='r')
    ax3.loglog(surfacedensityam_SG/Rg,densityden_SG,lw=lwid,c='b')
    ax3.set_xlabel('$a$ [$R_g$]',fontsize=16)
    ax3.set_ylabel('$ρ$ [$g/cm^{3}$]',fontsize=16)
    ax3.xaxis.set_tick_params(labelsize=12)
    ax3.yaxis.set_tick_params(labelsize=12)
#    ax3.xaxis.set_ticks([1e1, 1e3, 1e5, 1e7])
#    ax3.yaxis.set_ticks([1e-20, 1e-17, 1e-14, 1e-11, 1e-8])
    ax3.yaxis.set_label_position("right")
    ax3.yaxis.tick_right()
    
    plt.savefig('plots/propertyplots/Disk-Profile.pdf')
    plt.savefig('plots/paperplots/Disk-Profile.pdf')

#####################################################
def stitch_plot_stellar():
    fig=plt.figure(figsize=(12,12))
    #fig=plt.figure(figsize=(12,6))
    plt.subplots_adjust(left=0.06, right=0.95, top=0.9, bottom=0.06, wspace=0, hspace=0.15)
    
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-10,10**5]
    f=[-10,10**8]
    g=[190,(10**5)]
    h=[190,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimea1=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei2=matplotlib.patches.Rectangle((-10,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimea3=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei4=matplotlib.patches.Rectangle((-10,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
        
    ax1=plt.subplot(221)
    ax1.plot(amrange_SG/Rg,Tcaprgianta_SG,'r:',lw=uplimw,label='Red Giant',c='crimson')
    ax1.plot([capturedata_a_rgiant_SG[0],capturedata_a_rgiant_SG[1]],
        [capturedata_a_rgiant_SG[2],capturedata_a_rgiant_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_a_rgiant_SG[0], capturedata_a_rgiant_SG[2],'*',label='Red Giant',
        markersize=12,markerfacecolor='crimson',markeredgewidth=0.1,markeredgecolor='k')
    ax1.plot(capturedata_a_rgiant_SG[1], capturedata_a_rgiant_SG[2],'*',
        markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='crimson')
    ax1.plot(amrange_SG/Rg,Tcapostara_SG,'r-.',lw=uplimw,label='O Star',c='royalblue')
    ax1.plot([capturedata_a_ostar_SG[0],capturedata_a_ostar_SG[1]],
        [capturedata_a_ostar_SG[2],capturedata_a_ostar_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_a_ostar_SG[0], capturedata_a_ostar_SG[2],'*',label='O Star',
        markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
    ax1.plot(capturedata_a_ostar_SG[1], capturedata_a_ostar_SG[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
    ax1.plot(amrange_SG/Rg,Tcapgstara_SG,'r--',lw=uplimw,label='G Star',c='gold')
    ax1.plot([capturedata_a_gstar_SG[0],capturedata_a_gstar_SG[1]],
        [capturedata_a_gstar_SG[2],capturedata_a_gstar_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_a_gstar_SG[0], capturedata_a_gstar_SG[2],'*',label='G Star',
        markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
    ax1.plot(capturedata_a_gstar_SG[1], capturedata_a_gstar_SG[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
    ax1.plot(amrange_SG/Rg,Tcapmstara_SG,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
    ax1.plot([capturedata_a_mstar_SG[0],capturedata_a_mstar_SG[1]],
        [capturedata_a_mstar_SG[2],capturedata_a_mstar_SG[2]],'r:',lw=delaw, c='k')
    ax1.plot(capturedata_a_mstar_SG[0],capturedata_a_mstar_SG[2],'*',label='M Dwarf',
        markersize=12,markerfacecolor='darkorange',markeredgewidth=0.1,markeredgecolor='k')
    ax1.plot(capturedata_a_mstar_SG[1][0],capturedata_a_mstar_SG[2][0],'r:',lw=delaw,label='Δ a',c='k')
    ax1.plot(capturedata_a_mstar_SG[1],capturedata_a_mstar_SG[2],'*',label='$a_{cap}$',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='k')
    ax1.plot(capturedata_a_mstar_SG[1],capturedata_a_mstar_SG[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='darkorange')
    #
    ax1.plot([capturedata_a_gstar_SG[0],capturedata_a_gstar_SG[1]],
        [capturedata_a_gstar_SG[2],capturedata_a_gstar_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_a_gstar_SG[0], capturedata_a_gstar_SG[2],'*',
        markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
    ax1.plot(capturedata_a_gstar_SG[1], capturedata_a_gstar_SG[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
    ax1.plot([capturedata_a_ostar_SG[0],capturedata_a_ostar_SG[1]],
        [capturedata_a_ostar_SG[2],capturedata_a_ostar_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_a_ostar_SG[0], capturedata_a_ostar_SG[2],'*',
        markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
    ax1.plot(capturedata_a_ostar_SG[1], capturedata_a_ostar_SG[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
    #
    matplotlib.pyplot.annotate('$i_{0} = 45^{\circ}$', (5e0,5e17))
    matplotlib.pyplot.annotate('AGN lifetime', (1*10**6,1e7))
    ax1.add_patch(lifetimea1)
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=5, columnspacing=3, loc='center left', bbox_to_anchor=(-0.015,1.1))
    plt.xscale('log')
    plt.yscale('log')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax1.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax1.set_xlim([3e0,3e7])
    ax1.set_ylim([2e-1,1e19])
    
    ax3=plt.subplot(222)
    ax3.plot(amrange_TQM/Rg,Tcaprgianta_TQM,'r:',lw=uplimw,label='Red Giant',c='crimson')
    ax3.plot([capturedata_a_rgiant_TQM[0],capturedata_a_rgiant_TQM[1]],
        [capturedata_a_rgiant_TQM[2],capturedata_a_rgiant_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_a_rgiant_TQM[0], capturedata_a_rgiant_TQM[2],'*',label='Red Giant',
        markersize=12,markerfacecolor='crimson',markeredgewidth=0.1,markeredgecolor='k')
    ax3.plot(capturedata_a_rgiant_TQM[1], capturedata_a_rgiant_TQM[2],'*',
        markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='crimson')
    ax3.plot(amrange_TQM/Rg,Tcapostara_TQM,'r-.',lw=uplimw,label='O Star',c='royalblue')
    ax3.plot([capturedata_a_ostar_TQM[0],capturedata_a_ostar_TQM[1]],
        [capturedata_a_ostar_TQM[2],capturedata_a_ostar_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_a_ostar_TQM[0], capturedata_a_ostar_TQM[2],'*',label='O Star',
        markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
    ax3.plot(capturedata_a_ostar_TQM[1], capturedata_a_ostar_TQM[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
    ax3.plot(amrange_TQM/Rg,Tcapgstara_TQM,'r--',lw=uplimw,label='G Star',c='gold')
    ax3.plot([capturedata_a_gstar_TQM[0],capturedata_a_gstar_TQM[1]],
        [capturedata_a_gstar_TQM[2],capturedata_a_gstar_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_a_gstar_TQM[0], capturedata_a_gstar_TQM[2],'*',label='G Star',
        markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
    ax3.plot(capturedata_a_gstar_TQM[1], capturedata_a_gstar_TQM[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
    ax3.plot(amrange_TQM/Rg,Tcapmstara_TQM,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
    ax3.plot([capturedata_a_mstar_TQM[0],capturedata_a_mstar_TQM[1]],
        [capturedata_a_mstar_TQM[2],capturedata_a_mstar_TQM[2]],'r:',lw=delaw, c='k')
    ax3.plot(capturedata_a_mstar_TQM[0],capturedata_a_mstar_TQM[2],'*',label='M Dwarf',
        markersize=12,markerfacecolor='darkorange',markeredgewidth=0.1,markeredgecolor='k')
    #ax3.plot(capturedata_a_mstar_TQM[1][0],capturedata_a_mstar_TQM[2][0],'r:',lw=delaw,label='Δ a',c='k')
    ax3.plot(capturedata_a_mstar_TQM[1],capturedata_a_mstar_TQM[2],'*',label='$a_{cap}$',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='k')
    ax3.plot(capturedata_a_mstar_TQM[1],capturedata_a_mstar_TQM[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='darkorange')
    
    ax3.plot([capturedata_a_gstar_TQM[0],capturedata_a_gstar_TQM[1]],
        [capturedata_a_gstar_TQM[2],capturedata_a_gstar_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_a_gstar_TQM[0], capturedata_a_gstar_TQM[2],'*',
        markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
    ax3.plot(capturedata_a_gstar_TQM[1], capturedata_a_gstar_TQM[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
    ax3.plot([capturedata_a_ostar_TQM[0],capturedata_a_ostar_TQM[1]],
        [capturedata_a_ostar_TQM[2],capturedata_a_ostar_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_a_ostar_TQM[0], capturedata_a_ostar_TQM[2],'*',
        markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
    ax3.plot(capturedata_a_ostar_TQM[1], capturedata_a_ostar_TQM[2],'*',
        markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
    
    #matplotlib.pyplot.annotate('$i_{0} = 45^{\circ}$', (6e1,5e17))
    matplotlib.pyplot.annotate('AGN lifetime', (3*10**6,1e7))
    ax3.add_patch(lifetimea3)
    #ax3.legend(fontsize=9.5, framealpha=1, edgecolor= 'k', handlelength=2.7,
    #    ncol=5, columnspacing=0.65, loc='center left', bbox_to_anchor=(-0.012,1.08))
    plt.xscale('log')
    plt.yscale('log')
    ax3.set_xlabel('$a$ [$R_g$]', fontsize=12)
    #ax3.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax3.set_xlim([4e1,6e7])
    ax3.set_ylim([2e-1,1e19])
    ax3.yaxis.tick_right()
    
    ax2=plt.subplot(223)
    #ax2=plt.subplot(121)
    ax2.plot(ideg4_SG,Tcaprgianti_SG,'r:',lw=uplimw, label='Red Giant',c='crimson')
    ax2.plot(capturedata_i_rgiant_SG[0],capturedata_i_rgiant_SG[1],'*',label='Red Giant',
        markersize=12, markerfacecolor='crimson', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcapostari_SG,'r-.',lw=uplimw,label='O Star',c='royalblue')
    ax2.plot(capturedata_i_ostar_SG[0], capturedata_i_ostar_SG[1],'*',label='O Star',
        markersize=12, markerfacecolor='royalblue', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcapgstari_SG,'r--',lw=uplimw, label='G Star',c='gold')
    ax2.plot(capturedata_i_gstar_SG[0], capturedata_i_gstar_SG[1],'*',label='G Star',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcapmstari_SG,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
    ax2.plot(capturedata_i_mstar_SG[0], capturedata_i_mstar_SG[1],'*',label='M Dwarf',
        markersize=12, markerfacecolor='darkorange', markeredgewidth=0.1, markeredgecolor='k')
    matplotlib.pyplot.annotate('$a_{0} = 10^{4}~R_g$', (3,7e9))
    matplotlib.pyplot.annotate('AGN lifetime', (73,3e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    ax2.add_patch(lifetimei2)
    #ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
    #    ncol=4, columnspacing=7.8, loc='center left', bbox_to_anchor=(-0.013,1.08))
    plt.yscale('log')
    ax2.set_xlabel('$i$ [$deg$]', fontsize=12)
    ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax2.set_xlim([-2,182])
    ax2.set_ylim([3e1,3e10])
    
    ax4=plt.subplot(224)
    #ax4=plt.subplot(122) 
    ax4.plot(ideg4_TQM,Tcaprgianti_TQM,'r:',lw=uplimw, label='Red Giant',c='crimson')
    ax4.plot(capturedata_i_rgiant_TQM[0],capturedata_i_rgiant_TQM[1],'*',label='Red Giant',
        markersize=12, markerfacecolor='crimson', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM,Tcapostari_TQM,'r-.',lw=uplimw,label='O Star',c='royalblue')
    ax4.plot(capturedata_i_ostar_TQM[0], capturedata_i_ostar_TQM[1],'*',label='O Star',
        markersize=12, markerfacecolor='royalblue', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM,Tcapgstari_TQM,'r--',lw=uplimw, label='G Star',c='gold')
    ax4.plot(capturedata_i_gstar_TQM[0], capturedata_i_gstar_TQM[1],'*',label='G Star',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM,Tcapmstari_TQM,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
    ax4.plot(capturedata_i_mstar_TQM[0], capturedata_i_mstar_TQM[1],'*',label='M Dwarf',
        markersize=12, markerfacecolor='darkorange', markeredgewidth=0.1, markeredgecolor='k')
    #
    ax4.plot(capturedata_i_gstar_TQM[0], capturedata_i_gstar_TQM[1],'*',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
    #
    #matplotlib.pyplot.annotate('$a_{0} = 10^{4}~R_g$', (0,1e5))
    matplotlib.pyplot.annotate('AGN lifetime', (73,3.5e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    ax4.add_patch(lifetimei4)
    #ax4.legend(fontsize=9.5, framealpha=1, edgecolor= 'k', handlelength=2.7,
    #    ncol=4, columnspacing=2.7, loc='center left', bbox_to_anchor=(-0.012,1.08))
    plt.yscale('log')
    ax4.set_xlabel('$i$ [$deg$]', fontsize=12)
    #ax4.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax4.set_xlim([-2,182])
    ax4.set_ylim([3e1,3e10])
    ax4.yaxis.tick_right()
    
    plt.savefig('plots/capturetimeplots/stellar-Tcap.pdf')
    plt.savefig('plots/paperplots/stellar-Tcap.pdf')

def stitch_plot_sBH():
    fig=plt.figure(figsize=(12,12)) #9.6
    #plt.subplots_adjust(left=0.06, right=0.99, top=0.94, bottom=0.06, wspace=0.2, hspace=0.3)
    plt.subplots_adjust(left=0.06, right=0.95, top=0.9, bottom=0.06, wspace=0, hspace=0.4)
    
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-180,10**5]
    f=[-180,10**8]
    g=[180,(10**5)]
    h=[180,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimea1=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei2=matplotlib.patches.Rectangle((-180,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimea3=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei4=matplotlib.patches.Rectangle((-180,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
        
    ax1=plt.subplot(221)
    ax1.plot(amrange_SG/Rg,Tcap05deg_SG,'r-',lw=uplimw,label='$5^{\circ}$',c='darkgreen')
    ax1.plot([capturedata_5_sBH_SG[0],capturedata_5_sBH_SG[1]],
        [capturedata_5_sBH_SG[2],capturedata_5_sBH_SG[2]],'r:', lw=delaw,c='k')
    ax1.plot(capturedata_5_sBH_SG[0],capturedata_5_sBH_SG[2],'*',label='$5^{\circ}$',
        markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
    ax1.plot(capturedata_5_sBH_SG[1],capturedata_5_sBH_SG[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkgreen')
    ax1.plot(amrange_SG/Rg,Tcap15deg_SG,'r--',lw=uplimw,label='$15^{\circ}$',c='navy')
    ax1.plot([capturedata_15_sBH_SG[0],capturedata_15_sBH_SG[1]],
        [capturedata_15_sBH_SG[2],capturedata_15_sBH_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_15_sBH_SG[0],capturedata_15_sBH_SG[2],'*',label='$15^{\circ}$',
        markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
    ax1.plot(capturedata_15_sBH_SG[1],capturedata_15_sBH_SG[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='navy')
    ax1.plot(amrange_SG/Rg,Tcap30deg_SG,'r-.',lw=uplimw,label='$30^{\circ}$',c='palevioletred')
    ax1.plot([capturedata_30_sBH_SG[0],capturedata_30_sBH_SG[1]],
        [capturedata_30_sBH_SG[2],capturedata_30_sBH_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_30_sBH_SG[0],capturedata_30_sBH_SG[2],'*',label='$30^{\circ}$',
        markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
    ax1.plot(capturedata_30_sBH_SG[1],capturedata_30_sBH_SG[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='palevioletred')
    ax1.plot(amrange_SG/Rg,Tcap45deg_SG,'r:',lw=uplimw,label='$45^{\circ}$',c='darkmagenta')
    ax1.plot([capturedata_45_sBH_SG[0],capturedata_45_sBH_SG[1]],
        [capturedata_45_sBH_SG[2],capturedata_45_sBH_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_45_sBH_SG[0],capturedata_45_sBH_SG[2],'*',label='$45^{\circ}$',
        markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
    ax1.plot(capturedata_45_sBH_SG[1],capturedata_45_sBH_SG[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkmagenta')
    ax1.plot(amrange_SG/Rg,Tcap60deg_SG,'r-',lw=uplimw,label='$60^{\circ}$',c='steelblue')
    ax1.plot([capturedata_60_sBH_SG[0],capturedata_60_sBH_SG[1]],
        [capturedata_60_sBH_SG[2],capturedata_60_sBH_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_60_sBH_SG[0],capturedata_60_sBH_SG[2],'*',label='$60^{\circ}$',
        markersize=12,markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
    ax1.plot(capturedata_60_sBH_SG[1],capturedata_60_sBH_SG[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='steelblue')
    ax1.plot(amrange_SG/Rg,Tcap80deg_SG,'r-.',lw=uplimw,label='$80^{\circ}$',c='brown')
    ax1.plot([capturedata_80_sBH_SG[0],capturedata_80_sBH_SG[1]],
        [capturedata_80_sBH_SG[2],capturedata_80_sBH_SG[2]],'r:',lw=delaw,c='k')
    ax1.plot(capturedata_80_sBH_SG[0],capturedata_80_sBH_SG[2],'*',label='$80^{\circ}$',
        markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
    ax1.plot(capturedata_80_sBH_SG[1][0],capturedata_80_sBH_SG[2][0],'r:',lw=1,label='Δ a',c='k')
    ax1.plot(capturedata_80_sBH_SG[1],capturedata_80_sBH_SG[2],'*',label='$a_{cap}$',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='k')
    ax1.plot(capturedata_80_sBH_SG[1],capturedata_80_sBH_SG[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=0.1, markeredgecolor='brown')
    
    ax1.plot(capturedata_45_sBH_SG[1],capturedata_45_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkmagenta')
    
    matplotlib.pyplot.annotate('AGN lifetime', (1.5e6,1e7))
    ax1.add_patch(lifetimea1)
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=7, columnspacing=0.6, loc='center left', bbox_to_anchor=(-0.015,1.1))
    plt.xscale('log')
    plt.yscale('log')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=12)
    ax1.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax1.set_xlim([3e0,3e7])
    ax1.set_ylim([1e3,3e14])
    
    ax3=plt.subplot(222)        
    ax3.plot(amrange_TQM/Rg,Tcap05deg_TQM,'r-',lw=uplimw,label='$5^{\circ}$',c='darkgreen')
    ax3.plot([capturedata_5_sBH_TQM[0],capturedata_5_sBH_TQM[1]],
        [capturedata_5_sBH_TQM[2],capturedata_5_sBH_TQM[2]],'r:', lw=delaw,c='k')
    ax3.plot(capturedata_5_sBH_TQM[0],capturedata_5_sBH_TQM[2],'*',label='$5^{\circ}$',
        markersize=12, markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
    ax3.plot(capturedata_5_sBH_TQM[1],capturedata_5_sBH_TQM[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkgreen')
    ax3.plot(amrange_TQM/Rg,Tcap15deg_TQM,'r--',lw=uplimw,label='$15^{\circ}$',c='navy')
    ax3.plot([capturedata_15_sBH_TQM[0],capturedata_15_sBH_TQM[1]],
        [capturedata_15_sBH_TQM[2],capturedata_15_sBH_TQM[2]],'r:', lw=delaw,c='k')
    ax3.plot(capturedata_15_sBH_TQM[0],capturedata_15_sBH_TQM[2],'*',label='$15^{\circ}$',
        markersize=12, markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
    ax3.plot(capturedata_15_sBH_TQM[1],capturedata_15_sBH_TQM[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='navy')
    ax3.plot(amrange_TQM/Rg,Tcap30deg_TQM,'r-.',lw=uplimw,label='$30^{\circ}$',c='palevioletred')
    ax3.plot([capturedata_30_sBH_TQM[0],capturedata_30_sBH_TQM[1]],
        [capturedata_30_sBH_TQM[2],capturedata_30_sBH_TQM[2]],'r:', lw=delaw,c='k')
    ax3.plot(capturedata_30_sBH_TQM[0],capturedata_30_sBH_TQM[2],'*',label='$30^{\circ}$',
        markersize=12, markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
    ax3.plot(capturedata_30_sBH_TQM[1],capturedata_30_sBH_TQM[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='palevioletred')
    ax3.plot(amrange_TQM/Rg,Tcap45deg_TQM,'r:',lw=uplimw,label='$45^{\circ}$',c='darkmagenta')
    ax3.plot([capturedata_45_sBH_TQM[0],capturedata_45_sBH_TQM[1]],
        [capturedata_45_sBH_TQM[2],capturedata_45_sBH_TQM[2]],'r:', lw=delaw,c='k')
    ax3.plot(capturedata_45_sBH_TQM[0],capturedata_45_sBH_TQM[2],'*',label='$45^{\circ}$',
        markersize=12, markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
    ax3.plot(capturedata_45_sBH_TQM[1],capturedata_45_sBH_TQM[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkmagenta')
    ax3.plot(amrange_TQM/Rg,Tcap60deg_TQM,'r-',lw=uplimw,label='$60^{\circ}$',c='steelblue')
    ax3.plot([capturedata_60_sBH_TQM[0],capturedata_60_sBH_TQM[1]],
        [capturedata_60_sBH_TQM[2],capturedata_60_sBH_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_60_sBH_TQM[0],capturedata_60_sBH_TQM[2],'*',label='$60^{\circ}$',
        markersize=12, markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
    ax3.plot(capturedata_60_sBH_TQM[1],capturedata_60_sBH_TQM[2],'*',
        markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='steelblue')
    ax3.plot(amrange_TQM/Rg,Tcap80deg_TQM,'r-.',lw=uplimw,label='$80^{\circ}$',c='brown')
    ax3.plot([capturedata_80_sBH_TQM[0],capturedata_80_sBH_TQM[1]],
        [capturedata_80_sBH_TQM[2],capturedata_80_sBH_TQM[2]],'r:',lw=delaw,c='k')
    ax3.plot(capturedata_80_sBH_TQM[0],capturedata_80_sBH_TQM[2],'*',label='$80^{\circ}$',
        markersize=12, markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
    ax3.plot(capturedata_80_sBH_TQM[1][0],capturedata_80_sBH_TQM[2][0],'r:',lw=1,label='Δ a',c='k')
    ax3.plot(capturedata_80_sBH_TQM[1],capturedata_80_sBH_TQM[2],'*',label='$a_{cap}$',
        markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='k')
    ax3.plot(capturedata_80_sBH_TQM[1],capturedata_80_sBH_TQM[2],'*',
        markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='brown')
    matplotlib.pyplot.annotate('AGN lifetime', (4e6,1e7))
    ax3.add_patch(lifetimea3)
    #ax3.legend(fontsize=8.5, framealpha=1, edgecolor= 'k', handlelength=2.8,
    #    ncol=7, columnspacing=0.8, loc='center left', bbox_to_anchor=(-0.012,1.08))
    plt.xscale('log')
    plt.yscale('log')
    ax3.set_xlabel('$a$ [$R_g$]', fontsize=12)
    #ax3.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax3.set_xlim([4e1,6e7])
    ax3.set_ylim([1e3,3e14])
    ax3.yaxis.tick_right()
    
    ax2=plt.subplot(223)
    ax2.plot(ideg2_SG,Tcap2Rg_SG,'r--',lw=uplimw,label='$10^{2}~R_g$',c='darkgreen')
    ax2.plot(capturedata_1e2_sBH_SG[0], capturedata_1e2_sBH_SG[1],'*',label='$10^{2}~R_g$', 
        markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg3_SG,Tcap3Rg_SG,'r-.',lw=uplimw,label='$10^{3}~R_g$',c='navy')
    ax2.plot(capturedata_1e3_sBH_SG[0], capturedata_1e3_sBH_SG[1],'*',label='$10^{3}~R_g$', 
        markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg4_SG,Tcap4Rg_SG,'r:',lw=uplimw,label='$10^{4}~R_g$',c='darkmagenta')
    ax2.plot(capturedata_1e4_sBH_SG[0], capturedata_1e4_sBH_SG[1],'*',label='$10^{4}~R_g$', 
        markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg5_SG,Tcap5Rg_SG,'r-',lw=uplimw,label='$10^{5}~R_g$',c='palevioletred')
    ax2.plot(capturedata_1e5_sBH_SG[0], capturedata_1e5_sBH_SG[1],'*',label='$10^{5}~R_g$', 
        markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg6_SG,Tcap6Rg_SG,'r--',lw=uplimw,label='$10^{6}~R_g$',c='brown')
    ax2.plot(capturedata_1e6_sBH_SG[0], capturedata_1e6_sBH_SG[1],'*',label='$10^{6}~R_g$', 
        markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(ideg7_SG,Tcap7Rg_SG,'r-.',lw=uplimw,label='$10^{7}~R_g$',c='steelblue')
    ax2.plot(capturedata_1e7_sBH_SG[0], capturedata_1e7_sBH_SG[1],'*',label='$10^{7}~R_g$', 
        markersize=12,markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
    matplotlib.pyplot.annotate('AGN lifetime', (73,1e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    
    ax2.plot(capturedata_1e2_sBH_SG[0], capturedata_1e2_sBH_SG[1],'*',
        markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(capturedata_1e5_sBH_SG[0], capturedata_1e5_sBH_SG[1],'*',
        markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(capturedata_1e3_sBH_SG[0], capturedata_1e3_sBH_SG[1],'*',
        markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
    ax2.plot(capturedata_1e4_sBH_SG[0], capturedata_1e4_sBH_SG[1],'*',
        markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
    ax2.add_patch(lifetimei2)
    ax2.legend(fontsize=12, framealpha=1, edgecolor= 'k', handlelength=6,
        ncol=6, columnspacing=0.55, loc='center left', bbox_to_anchor=(-0.015,1.11))    
    plt.yscale('log')
    ax2.set_xlabel('$i$ [$deg$]', fontsize=12)
    ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax2.set_xlim([-2,92])
    ax2.set_ylim([1e2,3e14])
    
    ax4=plt.subplot(224)    
    ax4.plot(ideg2_TQM,Tcap2Rg_TQM,'r--',lw=uplimw,label='$10^{2}~R_g$',c='darkgreen')
    ax4.plot(capturedata_1e2_sBH_TQM[0], capturedata_1e2_sBH_TQM[1],'*',label='$10^{2}~R_g$', 
        markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg3_TQM,Tcap3Rg_TQM,'r-.',lw=uplimw,label='$10^{3}~R_g$',c='navy')
    ax4.plot(capturedata_1e3_sBH_TQM[0], capturedata_1e3_sBH_TQM[1],'*',label='$10^{3}~R_g$', 
        markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg4_TQM[1:],Tcap4Rg_TQM[1:],'r:',lw=uplimw,label='$10^{4}~R_g$',c='darkmagenta')
    ax4.plot(capturedata_1e4_sBH_TQM[0], capturedata_1e4_sBH_TQM[1],'*',label='$10^{4}~R_g$', 
        markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg5_TQM[1:],Tcap5Rg_TQM[1:],'r-',lw=uplimw,label='$10^{5}~R_g$',c='palevioletred')
    ax4.plot(capturedata_1e5_sBH_TQM[0], capturedata_1e5_sBH_TQM[1],'*',label='$10^{5}~R_g$', 
        markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg6_TQM,Tcap6Rg_TQM,'r--',lw=uplimw,label='$10^{6}~R_g$',c='brown')
    ax4.plot(capturedata_1e6_sBH_TQM[0], capturedata_1e6_sBH_TQM[1],'*',label='$10^{6}~R_g$', 
        markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(ideg7_TQM,Tcap7Rg_TQM,'r-.',lw=uplimw,label='$10^{7}~R_g$',c='steelblue')
    ax4.plot(capturedata_1e7_sBH_TQM[0], capturedata_1e7_sBH_TQM[1],'*',label='$10^{7}~R_g$', 
        markersize=12,markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
    
    ax4.plot(capturedata_1e3_sBH_TQM[0], capturedata_1e3_sBH_TQM[1],'*', 
        markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(capturedata_1e6_sBH_TQM[0], capturedata_1e6_sBH_TQM[1],'*',
        markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
    ax4.plot(capturedata_1e5_sBH_TQM[0], capturedata_1e5_sBH_TQM[1],'*',
        markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
    matplotlib.pyplot.annotate('AGN lifetime', (73,1e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    ax4.add_patch(lifetimei4)
    #ax4.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=3.2,
    #    ncol=6, columnspacing=0.25, loc='center left', bbox_to_anchor=(-0.012,1.08))
    plt.yscale('log')
    ax4.set_xlabel('$i$ [$deg$]', fontsize=12)
    #ax4.set_ylabel('$T_{cap}$ [$yr$]', fontsize=12)
    ax4.set_xlim([-2,92])
    ax4.set_ylim([1e2,3e14])
    ax4.yaxis.tick_right()
    
    plt.savefig('plots/capturetimeplots/sBH-Tcap.pdf')
    plt.savefig('plots/paperplots/sBH-Tcap.pdf')
#########################################################   


'''defining plotting functions, etc, for characteristics of each model'''
'''Everything depends soley on the model'''
#########################################################
def hprofile_plot():
    lwid=2
    fig=plt.figure(figsize=(6,4.5))
    plt.subplots_adjust(left=0.15, right=0.99, top=0.935, bottom=0.12)
    
    ax1 = plt.subplot(111)
    ax1.plot(harg_SG,h_SG/Rg/2,label='SG',lw=lwid,c='b')
    ax1.plot(harg_TQM,h_TQM/Rg/2,label='TQM',lw=lwid,c='r')
    ax1.plot(-harg_TQM,-h_TQM/Rg/2,lw=lwid,c='r')
    ax1.plot(-harg_TQM,h_TQM/Rg/2,lw=lwid,c='r')
    ax1.plot(harg_TQM,-h_TQM/Rg/2,lw=lwid,c='r')
    ax1.plot(harg_SG,h_SG/Rg/2,lw=lwid,c='b') #,label='SG'
    ax1.plot(-harg_SG,-h_SG/Rg/2,lw=lwid,c='b')
    ax1.plot(-harg_SG,h_SG/Rg/2,lw=lwid,c='b')
    ax1.plot(harg_SG,-h_SG/Rg/2,lw=lwid,c='b')
    ax1.axhline(y=0,lw=1,linestyle="--",c='black')
    ax1.plot([0,10**4],[0,10**5],'r:',lw=1,c='black')
    ax1.plot(0,0,'o',markersize=15,c='black')
    ax1.plot(10**4,10**5,'*',markersize=8, markeredgewidth=0.1, markeredgecolor='k', c='black')
    #matplotlib.pyplot.annotate('$a$', (1e2,1e3),fontsize=12) #labeling orbital radius
    #matplotlib.pyplot.annotate('$i$', (1e1,1e1),fontsize=12) #labeling orbital inclination
    ax1.set_xlabel('$a$ [$R_g$]',fontsize=14)
    ax1.set_ylabel('$H$ [$R_g$]',fontsize=14)
    ax1.legend(fontsize=10, framealpha=1, edgecolor= 'k', handlelength=4, 
               ncol=2, columnspacing=2, loc='center left', bbox_to_anchor=(-0.015,1.04))
    ax1.set_yscale('symlog')
    ax1.set_xscale('symlog')
    #ax1.xaxis.set_tick_params(labelsize=12)
    #ax1.yaxis.set_tick_params(labelsize=12)
    ax1.xaxis.set_ticks([-1e7, -1e5, -1e3, -1e1, 0, 1e1, 1e3, 1e5, 1e7])
    ax1.yaxis.set_ticks([-1e7, -1e5, -1e3, -1e1, 0, 1e1, 1e3, 1e5, 1e7])
    ax1.set_xlim([-1e8,1e8])
    plt.savefig('plots/propertyplots/disk-heightprofile.pdf')
    
#(a,h/a) 
#(h/a) ratio of distances plot function
def hovera_plot(): 
    lwid=2
    fig=plt.figure(figsize=(6,3.6))
    plt.subplots_adjust(left=0.15, right=0.99, top=0.98, bottom=0.15)
    
    ax1 = plt.subplot(111)    
    ax1.plot(harg_TQM,hovera_TQM,lw=lwid,label='TQM',c='r')
    ax1.plot(harg_SG,hovera_SG,lw=lwid,label='SG',c='b')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=14)
    ax1.set_ylabel('$H$ / $a$', fontsize=14) # [$m/m$]
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    plt.savefig('plots/propertyplots/disk-heightratio.pdf')
    
#(a,density) 
#(density) disk density plot function
def density_plot(): 
    lwid=2
    fig=plt.figure(figsize=(6,3.6))
    plt.subplots_adjust(left=0.15, right=0.99, top=0.98, bottom=0.15)
    
    densityden_TQM=[]
    densityden_SG=[]
    for i in range(len(surfacedensityam_TQM)):
        densityden_TQM.append(density_TQM(surfacedensityam_TQM[i])/1e3)
    for i in range(len(surfacedensityam_SG)):
        densityden_SG.append(density_SG(surfacedensityam_SG[i])/1e3)
    
    ax1 = plt.subplot(111)    
    ax1.plot(surfacedensityam_TQM/Rg,densityden_TQM,lw=lwid,label='TQM',c='r')
    ax1.plot(surfacedensityam_SG/Rg,densityden_SG,lw=lwid,label='SG',c='b')
    ax1.set_xlabel('$a$ [$R_g$]', fontsize=14)
    ax1.set_ylabel('$ρ$ [$g/cm^{3}$]', fontsize=14) # $density$ [$kg/m^3$]
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    plt.savefig('plots/propertyplots/disk-densityprofile.pdf')
#########################################################   
#(a,h)
#(h) disk thickness plot function
def h_plot(): 
    logPlot=plt.gca()
    logPlot.loglog(harg_SG,h_SG,lw=2,label='SG',c='b')
    logPlot.loglog(harg_TQM,h_TQM,lw=2,label='TQM',c='r')
    plt.title('Height')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$H$ [$m$]')
    logPlot.legend()
    ax = plt.subplot(111)
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
              ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.68,0.05))
    plt.savefig('plots/propertyplots/Height.pdf')

#(a,h)
#(h) interpolated disk thickness plot function
def hint_plot(): # (a,h) & (a,hint) comparison
    #creating a list of values for interpolated thickness hint
    h_int_TQM=[]
    for i in range(len(am_TQM)):
        h_int_TQM.append(hint_TQM(am_TQM[i]))
    h_int_SG=[]
    for i in range(len(am_SG)):
        h_int_SG.append(hint_SG(am_SG[i]))
    logPlot=plt.gca()
    logPlot.loglog(am_SG/Rg,h_int_SG,'r:',lw=3,label='SG',c='b')
    logPlot.loglog(arg_SG,h_SG_interpolated(am_SG),'r:',lw=2,label='SG$_{int}$',c='darkblue')
    logPlot.loglog(am_TQM/Rg,h_int_TQM,'r:',lw=3,label='TQM',c='r')
    logPlot.loglog(arg_TQM,h_TQM_interpolated(am_TQM),'r:',lw=2,label='TQM$_{int}$',c='darkred')
    plt.title('Interpolated Height')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$H_{interpolated}$ [$m$]')
    logPlot.legend()
    ax = plt.subplot(111)
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
              ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.63,0.1))
    plt.savefig('plots/propertyplots/Height interpolated.pdf')
#########################################################
#(a,surfacedensity)
#(surfacedensity) disk surface density plot function
def surfacedensity_plot(): 
    logPlot=plt.gca()
    logPlot.loglog(surfacedensityarg_SG,surfacedensity_SG,lw=2,label='SG',c='b')
    logPlot.loglog(surfacedensityarg_TQM,surfacedensity_TQM,lw=2,label='TQM',c='r')
    plt.title('Surface Density')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$σ$ [$g/cm^2$]')
    logPlot.legend()
    ax = plt.subplot(111)
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
              ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.68,0.95))
    plt.savefig('plots/propertyplots/Surface Density.pdf')

#(a,surfacedensity)
#(surfacedensity) interpolated disk surface density plot function
def surfacedensityint_plot(): # (a,surfacedensity) & (a,surfacedensityint) comparison
    #creating lists of values for interpolated surface density surfacedensityint
    surfacedensitydenint_TQM=[]
    for i in range(len(am_TQM)):
        surfacedensitydenint_TQM.append(surfacedensityint_TQM(am_TQM[i]))
    surfacedensitydenint_SG=[]
    for i in range(len(am_SG)):
        surfacedensitydenint_SG.append(surfacedensityint_SG(am_SG[i]))
    logPlot=plt.gca()
    logPlot.loglog(am_SG/Rg,surfacedensitydenint_SG,'r:',lw=3,label='SG',c='b')
    logPlot.loglog(arg_SG,surfacedensity_SG_interpolated(am_SG),'r:',lw=2,label='SG$_{int}$',c='darkblue')
    logPlot.loglog(am_TQM/Rg,surfacedensitydenint_TQM,'r:',lw=3,label='TQM',c='r')
    logPlot.loglog(arg_TQM,surfacedensity_TQM_interpolated(am_TQM),'r:',lw=2,label='TQM$_{int}$',c='darkred')
    plt.title('Interpolated Surface Density')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$σ_{interpolated}$ [$g/cm^2$]')
    logPlot.legend()
    ax = plt.subplot(111)
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
              ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.63,0.9))
    plt.savefig('plots/propertyplots/Surface Density interpolated.pdf')
#########################################################

#########################################################
def vel_plot(): # (a,vel) for i=0 (i.e. no inclination)
    logPlot=plt.gca()
    logPlot.loglog(surfacedensityarg_SG,vel(surfacedensityam_SG)/1000,lw=2,label='$v_{Keplerian}$; i=0')
    plt.title('Keplerian Velocity')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$v_{keplerian}$ [$km/s$]')
    #logPlot.legend()
    #ax = plt.subplot(111)
    #ax.legend(loc='center left', bbox_to_anchor=(0.6,0.8))
    plt.savefig('plots/propertyplots/Keplerian Velocity.pdf')
    
def Torb_plot(): # (a,Torb)
    #31,557,600 s/yr
    #a=10**4 -> Torb=100yr
    logPlot=plt.gca()
    logPlot.loglog(arg_SG,Torb(am_SG),lw=2,label='$T_{orbit}$')
    plt.title('Time per Orbit')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$T_{orbit}$ [$s$]')
    #logPlot.legend()
    #ax = plt.subplot(111)
    #ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig('plots/propertyplots/Time per Orbit.pdf')
    
def Tdisk_plot(i): # (a,Tdisk)
    #creating a list of values for Tdisk
    Tdisk_TQM=[]
    for j in range(len(am_TQM)):
        Tdisk_TQM.append(Tdisk(i,am_TQM[j],hint_TQM))
    Tdisk_SG=[]
    for j in range(len(am_SG)):
        Tdisk_SG.append(Tdisk(i,am_SG[j],hint_SG))
    logPlot=plt.gca()
    logPlot.loglog(arg_SG,Tdisk_SG,lw=2,label='SG $T_{disk}$',c='b')
    logPlot.loglog(harg_SG,h_SG,'r:',lw=2,label='SG $H$',c='b')
    logPlot.loglog(arg_TQM,Tdisk_TQM,lw=2,label='TQM $T_{disk}$',c='r')
    logPlot.loglog(harg_TQM,h_TQM,'r:',lw=2,label='TQM $H$',c='r')
    plt.title('Time in Disk')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$T_{disk}$ [$s$]')
    logPlot.legend()
    ax = plt.subplot(111)
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
              ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.55,0.1))
    plt.savefig('plots/propertyplots/Time in Disk.pdf')
    
def Tratio_plot(i): # (a,Tdisk/Torb)
    #creating a list of values for Tratio
    Tratio_TQM=[]
    for j in range(len(am_TQM)):
        Tratio_TQM.append(Tratio(i,am_TQM[j],hint_TQM))
    Tratio_SG=[]
    for j in range(len(am_SG)):
        Tratio_SG.append(Tratio(i,am_SG[j],hint_SG))
    logPlot=plt.gca()
    logPlot.loglog(arg_SG,Tratio_SG,lw=2,label='SG $Time_{ratio}$',c='b')
    logPlot.loglog(harg_SG,hovera_SG,'r:',lw=2,label='SG $Height_{ratio}$',c='b')
    logPlot.loglog(arg_TQM,Tratio_TQM,lw=2,label='TQM $Time_{ratio}$',c='r')
    logPlot.loglog(harg_TQM,hovera_TQM,'r:',lw=2,label='TQM $Height_{ratio}$',c='r')
    plt.title('Time Ratio')
    logPlot.set_xlabel('$a$ [$R_g$]')
    logPlot.set_ylabel('$T_{disk}$ / $T_{orbit}$ [$s/s$]')
    logPlot.legend()
    ax = plt.subplot(111)
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
              ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.1))
    plt.savefig('plots/propertyplots/Time Ratio.pdf')
#########################################################
'''H profiles of disk'''
#(a,h)
#(h) disk thickness plot function
def hprofile_color_plot():
    den_TQM=[]
    den_SG=[]
    for i in range(len(ham_TQM)):
        den_TQM.append(density_TQM(ham_TQM[i])/1e3)
    for i in range(len(ham_SG)):
        den_SG.append(density_SG(ham_SG[i])/1e3)
    
    fig=plt.figure(figsize=(10,8))
    vmin=1e-20; vmax=1e-8; norm=matplotlib.colors.LogNorm(vmax=vmax, vmin=vmin)
    
    ax = plt.subplot(111)
    ax.plot(harg_TQM,h_TQM/Rg,label='TQM',lw=2,c='r')
    ax.plot(-harg_TQM,-h_TQM/Rg,lw=2,c='r')
    ax.plot(-harg_TQM,h_TQM/Rg,lw=2,c='r')
    ax.plot(harg_TQM,-h_TQM/Rg,lw=2,c='r')
    ax.plot(harg_SG,h_SG/Rg,label='SG',lw=2,c='b')
    ax.plot(-harg_SG,-h_SG/Rg,lw=2,c='b')
    ax.plot(-harg_SG,h_SG/Rg,lw=2,c='b')
    ax.plot(harg_SG,-h_SG/Rg,lw=2,c='b')
    
    #deltaTQM=ax.scatter(harg_TQM,h_TQM/Rg,marker='.',c=den_TQM, cmap='magma',norm=norm)
    #ax.scatter(-harg_TQM,-h_TQM/Rg,marker='.',c=den_TQM, cmap='magma',norm=norm)
    #ax.scatter(-harg_TQM,h_TQM/Rg,marker='.',c=den_TQM, cmap='magma',norm=norm)
    #ax.scatter(harg_TQM,-h_TQM/Rg,marker='.',c=den_TQM, cmap='magma',norm=norm)
    
    #deltaSG=ax.scatter(harg_SG,h_SG/Rg,marker='.',c=den_SG, cmap='magma',norm=norm)
    #ax.scatter(-harg_SG,-h_SG/Rg,marker='.',c=den_SG, cmap='magma',norm=norm)
    #ax.scatter(-harg_SG,h_SG/Rg,marker='.',c=den_SG, cmap='magma',norm=norm)
    #ax.scatter(harg_SG,-h_SG/Rg,marker='.',c=den_SG, cmap='magma',norm=norm)
    
    #cb=plt.colorbar(deltaSG)
    #cb.set_label('Δ ρ [$g/cm^{3}$]')
    #cb.ax.set_yscale('log')
    
    ax.axhline(y=0,lw=1,linestyle="--",c='black')
    #ax.plot([0,10**4],[0,10**5],'r:',lw=1.5,c='black')
    ax.plot(0,0,'o',markersize=20,c='black')
    #ax.plot(10**4,10**5,'*',markersize=12,c='black')
    
    #matplotlib.pyplot.annotate('$a$', (20,500)) #labeling orbital radius
    #matplotlib.pyplot.annotate('$i$', (1.5,0.3)) #labeling orbital inclination
    
    #ax.set_title('Disk Height ($H$) vs Semi-Major Axis ($a$)')
    ax.set_xlabel('$a$ [$R_g$]')
    ax.set_ylabel('$H$ [$R_g$]')
    ax.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, 
               ncol=2, columnspacing=2, loc='center left', bbox_to_anchor=(-0.007,1.03))
    ax.set_yscale('symlog')
    ax.set_xscale('symlog')
    plt.savefig('plots/propertyplots/disk-heightprofile.pdf')
    
    
    

#########################################################      
 
def fig6():
    fig=plt.figure(figsize=(6,4))
    plt.subplots_adjust(left=0.09, right=0.99, top=0.97, bottom=0.125)
    vmin=6e1; vmax=1e6; norm=matplotlib.colors.LogNorm(vmax=vmax, vmin=vmin)
    #norm=plt.Normalize(vmax=vmax, vmin=vmin)
    
    ax1=plt.subplot(111)
    ax1.scatter(capturedata_1e5_5_sBH_SG[3],capturedata_1e5_5_sBH_SG[1],
        marker='.',label='sBH', c=capturedata_1e5_5_sBH_SG[0]/Rg, cmap='seismic', #'seismic',PuOr
        norm=norm)
    ax1.scatter(capturedata_1e5_15_sBH_SG[3],capturedata_1e5_15_sBH_SG[1],
        marker='.',label='sBH', c=capturedata_1e5_15_sBH_SG[0]/Rg, cmap='seismic', 
        norm=norm)
    delta=ax1.scatter(capturedata_1e6_15_sBH_SG[3],capturedata_1e6_15_sBH_SG[1],
        marker='.',label='sBH', c=capturedata_1e6_15_sBH_SG[0]/Rg, cmap='seismic', 
        norm=norm)
    plt.xscale('log')
    ax1.set_xlabel('$t$ [$yr$]', fontsize=14)
    ax1.set_ylabel('$i$ [$deg$]', fontsize=14)
    ax1.set_xlim([1e3,1e8])
    #ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
    #    ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    cb = plt.colorbar(delta)
    cb.set_label('$a$ [$R_g$]', fontsize=14)
    cb.ax.set_yscale('log')
    plt.savefig('plots/propertyplots/sBH-i_t_SG.pdf')

def it_acolor_plot(): #this one
    fig=plt.figure(figsize=(12,5))
    vmin=1.5e1; vmax=1e6; norm=matplotlib.colors.LogNorm(vmax=vmax, vmin=vmin)
    #norm=plt.Normalize(vmax=vmax, vmin=vmin)
    plt.subplots_adjust(left=0.05, right=0.96, top=0.98, bottom=0.25, wspace=0)
    
    ax1=plt.subplot(121)
    ax1.scatter(capturedata_1e6_45_rgiant_SG[3],capturedata_1e6_45_rgiant_SG[1],
        marker='.',label='r giant', c=capturedata_1e6_45_rgiant_SG[0]/Rg, cmap='inferno_r',
        norm=norm)
    delta=ax1.scatter(capturedata_1e6_45_sBH_SG[3],capturedata_1e6_45_sBH_SG[1],
        marker='.',label='sBH', c=capturedata_1e6_45_sBH_SG[0]/Rg, cmap='inferno_r', #plasma_r
        norm=norm)
    matplotlib.pyplot.annotate('rgiant', (2e8,10))
    matplotlib.pyplot.annotate('sBH', (4e9,10))
    plt.xscale('log')
    
    ax2=plt.subplot(122)
    ax2.scatter(capturedata_1e6_45_rgiant_TQM[3],capturedata_1e6_45_rgiant_TQM[1],
        marker='.',label='r giant', c=capturedata_1e6_45_rgiant_TQM[0]/Rg, cmap='inferno_r',
        norm=norm)
    ax2.scatter(capturedata_1e6_45_sBH_TQM[3],capturedata_1e6_45_sBH_TQM[1],
        marker='.',label='sBH', c=capturedata_1e6_45_sBH_TQM[0]/Rg, cmap='inferno_r',
        norm=norm)
    matplotlib.pyplot.annotate('rgiant', (2e8,10))
    matplotlib.pyplot.annotate('sBH', (4e9,10))
    plt.xscale('log')
    
    ax1.set_xlim([3e6,2e10])
    ax2.set_xlim([3e6,2e10])
    ax1.set_xlabel('$t$ [$yr$]')
    ax2.set_xlabel('$t$ [$yr$]')
    ax1.set_ylabel('$i$ [$deg$]')
    ax2.yaxis.tick_right()
    
    cbaxes = fig.add_axes([0.05, 0.1, 0.917, 0.03]) 
    cb = plt.colorbar(delta, cax = cbaxes, orientation='horizontal') 
    cb.set_label('a [Rg]')
    cb.ax.invert_xaxis()
    cb.ax.set_xscale('log')
    #ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
    #    ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    
    plt.savefig('plots/propertyplots/it.pdf')
    plt.savefig('plots/propertyplots/it.jpeg')
    
def at_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_SG[3],capturedata_1e6_45_sBH_SG[0]/Rg,'r:',label='sBH, SG',c='b')
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],capturedata_1e6_45_sBH_TQM[0]/Rg,'r:',label='sBH, TQM',c='r')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],capturedata_1e6_45_rgiant_SG[0]/Rg,'r-',label='rgiant, SG',c='b')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],capturedata_1e6_45_rgiant_TQM[0]/Rg,'r-',label='rgiant, TQM',c='r')
    ax1.set_title('Δ a')
    ax1.set_xlabel('$t$ [$yr$]')
    ax1.set_ylabel('$a$ [$Rg$]')
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/at.pdf')
    
def it_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_SG[3],capturedata_1e6_45_sBH_SG[1],'r:',label='sBH, SG',c='b')
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],capturedata_1e6_45_sBH_TQM[1],'r:',label='sBH, TQM',c='r')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],capturedata_1e6_45_rgiant_SG[1],'r-',label='rgiant, SG',c='b')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],capturedata_1e6_45_rgiant_TQM[1],'r-',label='rgiant, TQM',c='r')
    ax1.set_title('Δ i')
    ax1.set_xlabel('$t$ [$yr$]')
    ax1.set_ylabel('$i$ [$deg$]')
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    plt.xscale('log')
    plt.savefig('plots/propertyplots/it.pdf')
    
def fa_plot():
    Fdrag_BHL_SG=[]
    Fdrag_BHL_TQM=[]
    Fdrag_STO_SG=[]
    Fdrag_STO_TQM=[]
    for i in range(len(surfacedensityam_SG)):
            Fdrag_BHL_SG.append(F_BHL(45/degrees,surfacedensityam_SG[i],rBH(45/degrees,surfacedensityam_SG[i]),density_SG))
            Fdrag_STO_SG.append(F_STO(45/degrees,surfacedensityam_SG[i],rrgiant,density_SG))
    for j in range(len(surfacedensityam_TQM)):        
            Fdrag_BHL_TQM.append(F_BHL(45/degrees,surfacedensityam_TQM[j],rBH(45/degrees,surfacedensityam_TQM[j]),density_TQM))
            Fdrag_STO_TQM.append(F_STO(45/degrees,surfacedensityam_TQM[j],rrgiant,density_TQM))
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e31))
    ax1.plot(surfacedensityam_TQM/Rg,Fdrag_BHL_TQM,'r:',label='BHL, TQM',c='k')
    ax1.plot(surfacedensityam_SG/Rg,Fdrag_BHL_SG,'r-',label='BHL, SG',c='k')
    ax1.plot(surfacedensityam_TQM/Rg,Fdrag_STO_TQM,'r:',label='STO, TQM',c='r')
    ax1.plot(surfacedensityam_SG/Rg,Fdrag_STO_SG,'r-',label='STO, SG',c='r')
    ax1.set_title('F')
    ax1.set_xlabel('$a$ [$Rg$]')
    ax1.set_ylabel('$F$ [$N$]')
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/fa.pdf')

def fi_plot():
    irange=ivals(1e6*Rg,hint_SG)
    Fdrag_BHL_SG=[]
    Fdrag_BHL_TQM=[]
    Fdrag_STO_SG=[]
    Fdrag_STO_TQM=[]
    for i in range(len(irange)):
            Fdrag_BHL_SG.append(F_BHL(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_SG))
            Fdrag_BHL_TQM.append(F_BHL(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_TQM))
            Fdrag_STO_SG.append(F_STO(irange[i],1e6*Rg,rrgiant,density_SG))
            Fdrag_STO_TQM.append(F_STO(irange[i],1e6*Rg,rrgiant,density_TQM))
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,5e22))
    ax1.plot(irange*degrees,Fdrag_BHL_TQM,'r:',label='BHL, TQM',c='k')
    ax1.plot(irange*degrees,Fdrag_BHL_SG,'r-',label='BHL, SG,',c='k')
    ax1.plot(irange*degrees,Fdrag_STO_TQM,'r:',label='STO, TQM',c='r')
    ax1.plot(irange*degrees,Fdrag_STO_SG,'r-',label='STO, SG,',c='r')
    ax1.set_title('F')
    ax1.set_xlabel('$i$ [$deg$]')
    ax1.set_ylabel('$F$ [$N$]')
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.7,0.05))
    plt.yscale('log')
    plt.savefig('plots/propertyplots/fi.pdf')

def wa_plot():
    irange=ivals(1e6*Rg,hint_SG)
    Wdrag_BHL_SG=[]
    Wdrag_BHL_TQM=[]
    Wdrag_STO_SG=[]
    Wdrag_STO_TQM=[]
    for i in range(len(surfacedensityam_SG)):
            Wdrag_BHL_SG.append(Worb_BHL(45/degrees,surfacedensityam_SG[i],rBH(45/degrees,surfacedensityam_SG[i]),density_SG,hint_SG))
            Wdrag_STO_SG.append(Worb_STO(45/degrees,surfacedensityam_SG[i],rrgiant,density_SG,hint_SG))
    for i in range(len(surfacedensityam_TQM)):
            Wdrag_BHL_TQM.append(Worb_BHL(45/degrees,surfacedensityam_TQM[i],rBH(45/degrees,surfacedensityam_SG[i]),density_TQM,hint_TQM))
            Wdrag_STO_TQM.append(Worb_STO(45/degrees,surfacedensityam_TQM[i],rrgiant,density_TQM,hint_TQM))
    
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e43))
    ax1.plot(surfacedensityam_TQM/Rg,Wdrag_BHL_TQM,'r:',label='BHL, TQM',c='k')
    ax1.plot(surfacedensityam_SG/Rg,Wdrag_BHL_SG,'r-',label='BHL, SG,',c='k')
    ax1.plot(surfacedensityam_TQM/Rg,Wdrag_STO_TQM,'r:',label='STO, TQM',c='r')
    ax1.plot(surfacedensityam_SG/Rg,Wdrag_STO_SG,'r-',label='STO, SG,',c='r')
    ax1.set_title('W')
    ax1.set_xlabel('$a$ [$Rg$]')
    ax1.set_ylabel('$W$ [$J$]')
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.7,0.05))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/wa.pdf')
    
def ea_plot():
    energy=[]
    for i in range(len(am)):
            energy.append(Eorb(am[i],m_sBH))
    
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(am/Rg,energy,'r-',c='k')
    ax1.set_title('E', fontsize=12)
    ax1.set_xlabel('$a$ [$Rg$]', fontsize=12)
    ax1.set_ylabel('$E$ [$J$]', fontsize=12)
    #ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
    #           ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.7,0.05))
    plt.xscale('log')
    plt.savefig('plots/propertyplots/ea.pdf')
    
def wi_plot():
    irange=ivals(1e6*Rg,hint_SG)
    Wdrag_BHL_SG=[]
    Wdrag_BHL_TQM=[]
    Wdrag_STO_SG=[]
    Wdrag_STO_TQM=[]
    for i in range(len(irange)):
            Wdrag_BHL_SG.append(Worb_BHL(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_SG,hint_SG))
            Wdrag_BHL_TQM.append(Worb_BHL(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_TQM,hint_TQM))
            Wdrag_STO_SG.append(Worb_STO(irange[i],1e6*Rg,rrgiant,density_SG,hint_SG))
            Wdrag_STO_TQM.append(Worb_STO(irange[i],1e6*Rg,rrgiant,density_TQM,hint_TQM))
    
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,3e40))
    ax1.plot(irange*degrees,Wdrag_BHL_TQM,'r:',label='BHL, TQM',c='k')
    ax1.plot(irange*degrees,Wdrag_BHL_SG,'r-',label='BHL, SG,',c='k')
    ax1.plot(irange*degrees,Wdrag_STO_TQM,'r:',label='STO, TQM',c='r')
    ax1.plot(irange*degrees,Wdrag_STO_SG,'r-',label='STO, SG,',c='r')
    ax1.set_title('W', fontsize=12)
    ax1.set_xlabel('$i$ [$deg$]', fontsize=12)
    ax1.set_ylabel('$W$ [$J$]', fontsize=12)
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
               ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0.7,0.05))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/wi.pdf')

    
def stitch_plot_fw():
    fig=plt.figure(figsize=(16,10))
    plt.subplots_adjust(left=0.06, right=0.94, top=0.95, bottom=0.06, wspace=0, hspace=0.2)
    
    irange=ivals(1e6*Rg,hint_SG)
    a_Fdrag_BHL_SG=[]
    a_Fdrag_BHL_TQM=[]
    a_Fdrag_STO_SG=[]
    a_Fdrag_STO_TQM=[]
    i_Fdrag_BHL_SG=[]
    i_Fdrag_BHL_TQM=[]
    i_Fdrag_STO_SG=[]
    i_Fdrag_STO_TQM=[]
    a_Wdrag_BHL_SG=[]
    a_Wdrag_BHL_TQM=[]
    a_Wdrag_STO_SG=[]
    a_Wdrag_STO_TQM=[]
    i_Wdrag_BHL_SG=[]
    i_Wdrag_BHL_TQM=[]
    i_Wdrag_STO_SG=[]
    i_Wdrag_STO_TQM=[]
    a_Fdrag_DYN_SG=[]
    a_Fdrag_DYN_TQM=[]
    i_Fdrag_DYN_SG=[]
    i_Fdrag_DYN_TQM=[]
    a_Wdrag_DYN_SG=[]
    a_Wdrag_DYN_TQM=[]
    i_Wdrag_DYN_SG=[]
    i_Wdrag_DYN_TQM=[]
    
    for i in range(len(surfacedensityam_SG)):
            a_Fdrag_DYN_SG.append(F_DYN(45/degrees,surfacedensityam_SG[i],
                                      rBH(45/degrees,surfacedensityam_SG[i]),density_SG,hint_SG))
            a_Fdrag_BHL_SG.append(F_BHL(45/degrees,surfacedensityam_SG[i],
                                      rBH(45/degrees,surfacedensityam_SG[i]),density_SG))
            a_Fdrag_STO_SG.append(F_STO(45/degrees,surfacedensityam_SG[i],rsun,density_SG))
    for j in range(len(surfacedensityam_TQM)):        
            a_Fdrag_DYN_TQM.append(F_DYN(45/degrees,surfacedensityam_TQM[j],
                                       rBH(45/degrees,surfacedensityam_TQM[j]),density_TQM,hint_TQM))
            a_Fdrag_BHL_TQM.append(F_BHL(45/degrees,surfacedensityam_TQM[j],
                                       rBH(45/degrees,surfacedensityam_TQM[j]),density_TQM))
            a_Fdrag_STO_TQM.append(F_STO(45/degrees,surfacedensityam_TQM[j],rsun,density_TQM))
    for i in range(len(irange)):
            i_Fdrag_DYN_SG.append(F_DYN(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_SG,hint_SG))
            i_Fdrag_DYN_TQM.append(F_DYN(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_TQM,hint_TQM))
            i_Fdrag_BHL_SG.append(F_BHL(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_SG))
            i_Fdrag_BHL_TQM.append(F_BHL(irange[i],1e6*Rg,rBH(irange[i],1e6*Rg),density_TQM))
            i_Fdrag_STO_SG.append(F_STO(irange[i],1e6*Rg,rsun,density_SG))
            i_Fdrag_STO_TQM.append(F_STO(irange[i],1e6*Rg,rsun,density_TQM))
    for i in range(len(surfacedensityam_SG)):
            a_Wdrag_DYN_SG.append(Worb_DYN(45/degrees,surfacedensityam_SG[i],
                                         rBH(45/degrees,surfacedensityam_SG[i]),density_SG,hint_SG))
            a_Wdrag_BHL_SG.append(Worb_BHL(45/degrees,surfacedensityam_SG[i],
                                         rBH(45/degrees,surfacedensityam_SG[i]),density_SG,hint_SG))
            a_Wdrag_STO_SG.append(Worb_STO(45/degrees,surfacedensityam_SG[i],
                                         rsun,density_SG,hint_SG))
    for i in range(len(surfacedensityam_TQM)):
            a_Wdrag_DYN_TQM.append(Worb_DYN(45/degrees,surfacedensityam_TQM[i],
                                          rBH(45/degrees,surfacedensityam_SG[i]),density_TQM,hint_TQM))
            a_Wdrag_BHL_TQM.append(Worb_BHL(45/degrees,surfacedensityam_TQM[i],
                                          rBH(45/degrees,surfacedensityam_SG[i]),density_TQM,hint_TQM))
            a_Wdrag_STO_TQM.append(Worb_STO(45/degrees,surfacedensityam_TQM[i],
                                          rsun,density_TQM,hint_TQM))
    for i in range(len(irange)):
            i_Wdrag_DYN_SG.append(Worb_DYN(irange[i],1e6*Rg,
                                         rBH(irange[i],1e6*Rg),density_SG,hint_SG))
            i_Wdrag_DYN_TQM.append(Worb_DYN(irange[i],1e6*Rg,
                                          rBH(irange[i],1e6*Rg),density_TQM,hint_TQM))
            i_Wdrag_BHL_SG.append(Worb_BHL(irange[i],1e6*Rg,
                                         rBH(irange[i],1e6*Rg),density_SG,hint_SG))
            i_Wdrag_BHL_TQM.append(Worb_BHL(irange[i],1e6*Rg,
                                          rBH(irange[i],1e6*Rg),density_TQM,hint_TQM))
            i_Wdrag_STO_SG.append(Worb_STO(irange[i],1e6*Rg,rsun,density_SG,hint_SG))
            i_Wdrag_STO_TQM.append(Worb_STO(irange[i],1e6*Rg,rsun,density_TQM,hint_TQM))
    ax1=plt.subplot(221)
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e26))
    #ax1.plot(surfacedensityam_TQM/Rg,a_Fdrag_STO_TQM,'r:',label='$F_{GEO}$, TQM',c='khaki')
    #ax1.plot(surfacedensityam_SG/Rg,a_Fdrag_STO_SG,'r-',label='$F_{GEO}$, SG',c='khaki')
    ax1.plot(surfacedensityam_TQM/Rg,a_Fdrag_BHL_TQM,'r:',label='$F_{BHL}$, TQM',c='k')
    ax1.plot(surfacedensityam_SG/Rg,a_Fdrag_BHL_SG,'r-',label='$F_{BHL}$, SG',c='k')
    ax1.plot(surfacedensityam_TQM/Rg,a_Fdrag_DYN_TQM,'r:',label='$F_{DYN}$, TQM',c='rebeccapurple')
    ax1.plot(surfacedensityam_SG/Rg,a_Fdrag_DYN_SG,'r-',label='$F_{DYN}$, SG',c='rebeccapurple')
    #ax1.set_title('F')
    ax1.set_xlabel('$a$ [$Rg$]',fontsize=16)
    ax1.set_ylabel('$F$ [$N$]',fontsize=16)
    ax1.xaxis.set_tick_params(labelsize=12)
    ax1.yaxis.set_tick_params(labelsize=12)
    #ax1.xaxis.tick_top()
    plt.xscale('log')
    plt.yscale('log')
    
    ax2=plt.subplot(223)
    matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,1e24))
    #ax2.plot(irange*degrees,i_Fdrag_STO_TQM,'r:',label='$F_{GEO}$, TQM',c='khaki')
    #ax2.plot(irange*degrees,i_Fdrag_STO_SG,'r-',label='$F_{GEO}$, SG,',c='khaki')
    ax2.plot(irange*degrees,i_Fdrag_BHL_TQM,'r:',label='$F_{BHL}$, TQM',c='k')
    ax2.plot(irange*degrees,i_Fdrag_BHL_SG,'r-',label='$F_{BHL}$, SG,',c='k')
    ax2.plot(irange*degrees,i_Fdrag_DYN_TQM,'r:',label='$F_{DYN}$, TQM',c='rebeccapurple')
    ax2.plot(irange*degrees,i_Fdrag_DYN_SG,'r-',label='$F_{DYN}$, SG,',c='rebeccapurple')
    #ax2.set_title('F')
    ax2.set_xlabel('$i$ [$deg$]',fontsize=16)
    ax2.set_ylabel('$F$ [$N$]',fontsize=16)
    ax2.xaxis.set_tick_params(labelsize=12)
    ax2.yaxis.set_tick_params(labelsize=12)
    #ax2.yaxis.set_label_position("right")
    plt.yscale('log')
    
    ax3=plt.subplot(222)
    matplotlib.pyplot.annotate('$i = 45^{\circ}$', (5e6,1e38))
    #ax3.plot(surfacedensityam_TQM/Rg,a_Wdrag_STO_TQM,'r:',label='$F_{GEO}$, TQM',c='khaki')
    #ax3.plot(surfacedensityam_SG/Rg,a_Wdrag_STO_SG,'r-',label='$F_{GEO}$, SG,',c='khaki')
    ax3.plot(surfacedensityam_TQM/Rg,a_Wdrag_BHL_TQM,'r:',label='$F_{BHL}$, TQM',c='k')
    ax3.plot(surfacedensityam_SG/Rg,a_Wdrag_BHL_SG,'r-',label='$F_{BHL}$, SG,',c='k')
    ax3.plot(surfacedensityam_TQM/Rg,a_Wdrag_DYN_TQM,'r:',label='$F_{DYN}$, TQM',c='rebeccapurple')
    ax3.plot(surfacedensityam_SG/Rg,a_Wdrag_DYN_SG,'r-',label='$F_{DYN}$, SG,',c='rebeccapurple')
    #ax3.set_title('W')
    #ax3.xaxis.tick_top()
    ax3.yaxis.tick_right()
    ax3.yaxis.set_label_position("right")
    ax3.set_xlabel('$a$ [$Rg$]',fontsize=16)
    ax3.set_ylabel('$W$ [$J$]',fontsize=16)
    ax3.xaxis.set_tick_params(labelsize=12)
    ax3.yaxis.set_tick_params(labelsize=12)
    plt.xscale('log')
    plt.yscale('log')
    
    ax4=plt.subplot(224)
    matplotlib.pyplot.annotate('$a = 10^{6}~R_g$', (77,3e40))
    #ax4.plot(irange*degrees,i_Wdrag_STO_TQM,'r:',label='$F_{GEO}$, TQM',c='khaki')
    #ax4.plot(irange*degrees,i_Wdrag_STO_SG,'r-',label='$F_{GEO}$, SG,',c='khaki')
    ax4.plot(irange*degrees,i_Wdrag_BHL_TQM,'r:',label='$F_{BHL}$, TQM',c='k')
    ax4.plot(irange*degrees,i_Wdrag_BHL_SG,'r-',label='$F_{BHL}$, SG,',c='k')
    ax4.plot(irange*degrees,i_Wdrag_DYN_TQM,'r:',label='$F_{DYN}$, TQM',c='rebeccapurple')
    ax4.plot(irange*degrees,i_Wdrag_DYN_SG,'r-',label='$F_{DYN}$, SG,',c='rebeccapurple')
    #ax4.set_title('W', fontsize=12)
    ax4.set_xlabel('$i$ [$deg$]', fontsize=16)
    ax4.set_ylabel('$W$ [$J$]', fontsize=16)
    ax4.xaxis.set_tick_params(labelsize=12)
    ax4.yaxis.set_tick_params(labelsize=12)
    ax4.yaxis.tick_right()
    ax4.yaxis.set_label_position("right")
    plt.yscale('log')
    ax1.legend(fontsize=12, framealpha=1, edgecolor= 'k', 
               ncol=6, columnspacing=0.5, loc='center left', bbox_to_anchor=(-0.015,1.05))
    
    plt.savefig('plots/propertyplots/fw.pdf')
    plt.savefig('plots/paperplots/fw.pdf')
    
    
def fwt_plot():
    fig=plt.figure(figsize=(10,16))
    plt.subplots_adjust(left=0.13, right=0.98, top=0.92, bottom=0.06, hspace=0)
    
    ax1=plt.subplot(211)
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],Fdrag_BHL_TQM,'r:',label='$F_{BHL}$, TQM',c='k')
    ax1.plot(capturedata_1e6_45_sBH_SG[3],Fdrag_BHL_SG,'r-',label='$F_{BHL}$, SG',c='k')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],Fdrag_STO_TQM,'r:',label='$F_{GEO}$, TQM',c='r')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],Fdrag_STO_SG,'r-',label='$F_{GEO}$, SG',c='r')
    ax1.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax1.set_ylabel('$F$ [$N$]', fontsize=12)
    ax1.xaxis.tick_top()
    #ax1.xaxis.set_label_position("top")
    plt.xscale('log')
    plt.yscale('log')
    ax1.legend(fontsize=10, framealpha=1, edgecolor= 'k', 
                   ncol=4, columnspacing=2.1, loc='center left', bbox_to_anchor=(-0.01,1.13))
    
    ax2=plt.subplot(212)
    ax2.plot(capturedata_1e6_45_sBH_TQM[3],Wdrag_BHL_TQM,'r:',label='$F_{BHL}$, TQM',c='k')
    ax2.plot(capturedata_1e6_45_sBH_SG[3],Wdrag_BHL_SG,'r-',label='$F_{BHL}$, SG',c='k')
    ax2.plot(capturedata_1e6_45_rgiant_TQM[3],Wdrag_STO_TQM,'r:',label='$F_{GEO}$, TQM',c='r')
    ax2.plot(capturedata_1e6_45_rgiant_SG[3],Wdrag_STO_SG,'r-',label='$F_{GEO}$, SG',c='r')
    ax2.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax2.set_ylabel('$W$ [$J$]', fontsize=12)
    #ax2.yaxis.set_label_position("right")
    #ax2.yaxis.tick_right()
    plt.xscale('log')
    plt.yscale('log')
    #ax2.legend(fontsize=10, framealpha=1, edgecolor= 'k', 
    #               ncol=4, columnspacing=2.1, loc='center left', bbox_to_anchor=(-0.01,-0.25))
    
    plt.savefig('plots/propertyplots/fwt.pdf')
    
def ft_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],Fdrag_BHL_TQM,'r-',label='BHL, TQM',c='b')
    ax1.plot(capturedata_1e6_45_sBH_SG[3],Fdrag_BHL_SG,'r-',label='BHL, SG',c='k')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],Fdrag_STO_TQM,'r-',label='STO, TQM',c='g')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],Fdrag_STO_SG,'r-',label='STO, SG',c='r')
    ax1.set_title('$Δ F$ ($a_0 = 1e6 R_g$, $i_0 = 45^{\circ})$', fontsize=12)
    ax1.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax1.set_ylabel('$F$ [$N$]', fontsize=12)
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.95))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/ft.pdf')
    
def wt_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],Wdrag_BHL_TQM,'r-',label='BHL, TQM',c='b')
    ax1.plot(capturedata_1e6_45_sBH_SG[3],Wdrag_BHL_SG,'r-',label='BHL, SG',c='k')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],Wdrag_STO_TQM,'r-',label='STO, TQM',c='g')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],Wdrag_STO_SG,'r-',label='STO, SG',c='r')
    
    ax1.set_title('$Δ W$ ($a_0 = 1e6 R_g$, $i_0 = 45^{\circ})$', fontsize=12)
    ax1.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax1.set_ylabel('$W$ [$J$]', fontsize=12)
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.95))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/wt.pdf')
    
    
def et_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],E_BHL_TQM,'r-',label='BHL, TQM',c='b')
    ax1.plot(capturedata_1e6_45_sBH_SG[3],E_BHL_SG,'r-',label='BHL, SG',c='k')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],E_STO_TQM,'r-',label='STO, TQM',c='g')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],E_STO_SG,'r-',label='STO, SG',c='r')
    
    ax1.set_title('$Δ E$ ($a_0 = 1e6 R_g$, $i_0 = 45^{\circ})$', fontsize=12)
    ax1.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax1.set_ylabel('$E$ [$J$]', fontsize=12)
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    plt.xscale('log')
    plt.savefig('plots/propertyplots/et.pdf')
    
def densityt_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],dens_BHL_TQM,'r-',label='BHL, TQM',c='b')
    ax1.plot(capturedata_1e6_45_sBH_SG[3],dens_BHL_SG,'r-',label='BHL, SG',c='k')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],dens_STO_TQM,'r-',label='STO, TQM',c='g')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],dens_STO_SG,'r-',label='STO, SG',c='r')
    
    ax1.set_title('$Δ ρ$ ($a_0 = 1e6 R_g$, $i_0 = 45^{\circ})$', fontsize=12)
    ax1.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax1.set_ylabel('$ρ$ [$g/cm^{3}$]', fontsize=12)
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.95))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/density_t.pdf')
    
def hratiot_plot():
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(capturedata_1e6_45_sBH_TQM[3],hrat_BHL_TQM,'r-',label='BHL, TQM',c='b')
    ax1.plot(capturedata_1e6_45_sBH_SG[3],hrat_BHL_SG,'r-',label='BHL, SG',c='k')
    ax1.plot(capturedata_1e6_45_rgiant_TQM[3],hrat_STO_TQM,'r-',label='STO, TQM',c='g')
    ax1.plot(capturedata_1e6_45_rgiant_SG[3],hrat_STO_SG,'r-',label='STO, SG',c='r')   
    
    ax1.set_title('$Δ H$ ($a_0 = 1e6 R_g$, $i_0 = 45^{\circ})$', fontsize=12)
    ax1.set_xlabel('$t$ [$yr$]', fontsize=12)
    ax1.set_ylabel('$H$', fontsize=12)
    ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', 
                   ncol=2, columnspacing=0.5, loc='center left', bbox_to_anchor=(0,0.05))
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('plots/propertyplots/h_t.pdf')
    
def plot_vrel_t(x,y,label):
    fig=plt.figure(figsize=(10,8))
    
    ax1=plt.subplot(111)
    ax1.plot(x,y,lw=2.5,label=label)
    ax1.set_xlabel('$t$ [$yr$]')
    ax1.set_ylabel('$v_{rel}$ [$m/s$]')
    ax1.legend(fontsize=8, framealpha=1, handlelength=4.9, loc='center left', bbox_to_anchor=(0,0.05))
    plt.xscale('log')
    plt.yscale('log')
#########################################################

#####################################################
#####################################################
def plot_Tcap_a_stellar(name): # (a,Tcap)
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-180,10**5]
    f=[-180,10**8]
    g=[180,(10**5)]
    h=[180,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimea1=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimea3=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    
    if (name in SG) == True: 
        fig=plt.figure(figsize=(6,4))
        plt.subplots_adjust(right=0.99, top=0.89, bottom=0.13)
    
        ax1=plt.subplot(111)
        ax1.plot(amrange_SG/Rg,Tcaprgianta_SG,'r:',lw=uplimw,label='Red Giant',c='crimson')
        ax1.plot([capturedata_a_rgiant_SG[0],capturedata_a_rgiant_SG[1]],
            [capturedata_a_rgiant_SG[2],capturedata_a_rgiant_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_a_rgiant_SG[0], capturedata_a_rgiant_SG[2],'*',label='Red Giant',
            markersize=12,markerfacecolor='crimson',markeredgewidth=0.1,markeredgecolor='k')
        ax1.plot(capturedata_a_rgiant_SG[1], capturedata_a_rgiant_SG[2],'*',
            markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='crimson')
        ax1.plot(amrange_SG/Rg,Tcapostara_SG,'r-.',lw=uplimw,label='O Star',c='royalblue')
        ax1.plot([capturedata_a_ostar_SG[0],capturedata_a_ostar_SG[1]],
            [capturedata_a_ostar_SG[2],capturedata_a_ostar_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_a_ostar_SG[0], capturedata_a_ostar_SG[2],'*',label='O Star',
            markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
        ax1.plot(capturedata_a_ostar_SG[1], capturedata_a_ostar_SG[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
        ax1.plot(amrange_SG/Rg,Tcapgstara_SG,'r--',lw=uplimw,label='G Star',c='gold')
        ax1.plot([capturedata_a_gstar_SG[0],capturedata_a_gstar_SG[1]],
            [capturedata_a_gstar_SG[2],capturedata_a_gstar_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_a_gstar_SG[0], capturedata_a_gstar_SG[2],'*',label='G Star',
            markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
        ax1.plot(capturedata_a_gstar_SG[1], capturedata_a_gstar_SG[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
        ax1.plot(amrange_SG/Rg,Tcapmstara_SG,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
        ax1.plot([capturedata_a_mstar_SG[0],capturedata_a_mstar_SG[1]],
            [capturedata_a_mstar_SG[2],capturedata_a_mstar_SG[2]],'r:',lw=delaw, c='k')
        ax1.plot(capturedata_a_mstar_SG[0],capturedata_a_mstar_SG[2],'*',label='M Dwarf',
            markersize=12,markerfacecolor='darkorange',markeredgewidth=0.1,markeredgecolor='k')
        ax1.plot(capturedata_a_mstar_SG[1][0],capturedata_a_mstar_SG[2][0],'r:',lw=delaw,label='Δ a',c='k')
        ax1.plot(capturedata_a_mstar_SG[1],capturedata_a_mstar_SG[2],'*',label='$a_{cap}$',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='k')
        ax1.plot(capturedata_a_mstar_SG[1],capturedata_a_mstar_SG[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='darkorange')
        
        ax1.plot([capturedata_a_gstar_SG[0],capturedata_a_gstar_SG[1]],
            [capturedata_a_gstar_SG[2],capturedata_a_gstar_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_a_gstar_SG[0], capturedata_a_gstar_SG[2],'*',
            markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
        ax1.plot(capturedata_a_gstar_SG[1], capturedata_a_gstar_SG[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
        ax1.plot([capturedata_a_ostar_SG[0],capturedata_a_ostar_SG[1]],
            [capturedata_a_ostar_SG[2],capturedata_a_ostar_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_a_ostar_SG[0], capturedata_a_ostar_SG[2],'*',
            markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
        ax1.plot(capturedata_a_ostar_SG[1], capturedata_a_ostar_SG[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
    
        matplotlib.pyplot.annotate('$i_{0} = 45^{\circ}$', (5e0,5e17))
        matplotlib.pyplot.annotate('AGN lifetime', (1*10**6,1e7))
        ax1.add_patch(lifetimea1)
        ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, handletextpad=1,
            ncol=5, columnspacing=2.4, loc='center left', bbox_to_anchor=(-0.012,1.07))
        plt.xscale('log')
        plt.yscale('log')
        ax1.set_xlabel('$a$ [$R_g$]', fontsize=14)
        ax1.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax1.set_xlim([3e0,3e7])
        #ax1.set_ylim([1e2,1e14])

    if (name in TQM) == True:
        fig=plt.figure(figsize=(6,3.6))
        plt.subplots_adjust(right=0.99, top=0.99, bottom=0.15)
        
        ax3=plt.subplot(111)
        ax3.plot(amrange_TQM/Rg,Tcaprgianta_TQM,'r:',lw=uplimw,label='Red Giant',c='crimson')
        ax3.plot([capturedata_a_rgiant_TQM[0],capturedata_a_rgiant_TQM[1]],
            [capturedata_a_rgiant_TQM[2],capturedata_a_rgiant_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_a_rgiant_TQM[0], capturedata_a_rgiant_TQM[2],'*',label='Red Giant',
            markersize=12,markerfacecolor='crimson',markeredgewidth=0.1,markeredgecolor='k')
        ax3.plot(capturedata_a_rgiant_TQM[1], capturedata_a_rgiant_TQM[2],'*',
            markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='crimson')
        ax3.plot(amrange_TQM/Rg,Tcapostara_TQM,'r-.',lw=uplimw,label='O Star',c='royalblue')
        ax3.plot([capturedata_a_ostar_TQM[0],capturedata_a_ostar_TQM[1]],
            [capturedata_a_ostar_TQM[2],capturedata_a_ostar_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_a_ostar_TQM[0], capturedata_a_ostar_TQM[2],'*',label='O Star',
            markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
        ax3.plot(capturedata_a_ostar_TQM[1], capturedata_a_ostar_TQM[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
        ax3.plot(amrange_TQM/Rg,Tcapgstara_TQM,'r--',lw=uplimw,label='G Star',c='gold')
        ax3.plot([capturedata_a_gstar_TQM[0],capturedata_a_gstar_TQM[1]],
            [capturedata_a_gstar_TQM[2],capturedata_a_gstar_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_a_gstar_TQM[0], capturedata_a_gstar_TQM[2],'*',label='G Star',
            markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
        ax3.plot(capturedata_a_gstar_TQM[1], capturedata_a_gstar_TQM[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
        ax3.plot(amrange_TQM/Rg,Tcapmstara_TQM,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
        ax3.plot([capturedata_a_mstar_TQM[0],capturedata_a_mstar_TQM[1]],
            [capturedata_a_mstar_TQM[2],capturedata_a_mstar_TQM[2]],'r:',lw=delaw, c='k')
        ax3.plot(capturedata_a_mstar_TQM[0],capturedata_a_mstar_TQM[2],'*',label='M Dwarf',
            markersize=12,markerfacecolor='darkorange',markeredgewidth=0.1,markeredgecolor='k')
        #ax3.plot(capturedata_a_mstar_TQM[1][0],capturedata_a_mstar_TQM[2][0],'r:',lw=delaw,label='Δ a',c='k')
        ax3.plot(capturedata_a_mstar_TQM[1],capturedata_a_mstar_TQM[2],'*',label='$a_{cap}$',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='k')
        ax3.plot(capturedata_a_mstar_TQM[1],capturedata_a_mstar_TQM[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='darkorange')
        
        ax3.plot([capturedata_a_gstar_TQM[0],capturedata_a_gstar_TQM[1]],
            [capturedata_a_gstar_TQM[2],capturedata_a_gstar_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_a_gstar_TQM[0], capturedata_a_gstar_TQM[2],'*',
            markersize=12,markerfacecolor='gold',markeredgewidth=0.1,markeredgecolor='k')
        ax3.plot(capturedata_a_gstar_TQM[1], capturedata_a_gstar_TQM[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='gold')
        ax3.plot([capturedata_a_ostar_TQM[0],capturedata_a_ostar_TQM[1]],
            [capturedata_a_ostar_TQM[2],capturedata_a_ostar_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_a_ostar_TQM[0], capturedata_a_ostar_TQM[2],'*',
            markersize=12,markerfacecolor='royalblue',markeredgewidth=0.1,markeredgecolor='k')
        ax3.plot(capturedata_a_ostar_TQM[1], capturedata_a_ostar_TQM[2],'*',
            markersize=7,markerfacecolor='k',markeredgewidth=acapw,markeredgecolor='royalblue')
        
        #matplotlib.pyplot.annotate('$i_{0} = 45^{\circ}$', (6e1,5e17))
        matplotlib.pyplot.annotate('AGN lifetime', (3*10**6,1e7))
        ax3.add_patch(lifetimea3)
        plt.xscale('log')
        plt.yscale('log')
        ax3.set_xlabel('$a$ [$R_g$]', fontsize=14)
        ax3.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax3.set_xlim([4e1,6e7])
        #ax3.set_ylim([1e2,1e14])

    plt.savefig('plots/capturetimeplots/stellar-Tcap_a_'+name+'.pdf')
    plt.savefig('plots/paperplots/stellar-Tcap_a_'+name+'.pdf')
#####################################################
def plot_Tcap_i_stellar(name): # (i,Tcap)
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-10,10**5]
    f=[-10,10**8]
    g=[190,(10**5)]
    h=[190,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimei2=matplotlib.patches.Rectangle((-10,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei4=matplotlib.patches.Rectangle((-10,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    
    if (name in SG) == True:
        fig=plt.figure(figsize=(6,4))
        plt.subplots_adjust(right=0.99, top=0.89, bottom=0.135)
        
        ax2=plt.subplot(111)
        ax2.plot(ideg4_SG,Tcaprgianti_SG,'r:',lw=uplimw, label='Red Giant',c='crimson')
        ax2.plot(capturedata_i_rgiant_SG[0],capturedata_i_rgiant_SG[1],'*',label='Red Giant',
            markersize=12, markerfacecolor='crimson', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg4_SG,Tcapostari_SG,'r-.',lw=uplimw,label='O Star',c='royalblue')
        ax2.plot(capturedata_i_ostar_SG[0], capturedata_i_ostar_SG[1],'*',label='O Star',
            markersize=12, markerfacecolor='royalblue', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg4_SG,Tcapgstari_SG,'r--',lw=uplimw, label='G Star',c='gold')
        ax2.plot(capturedata_i_gstar_SG[0], capturedata_i_gstar_SG[1],'*',label='G Star',
            markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg4_SG,Tcapmstari_SG,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
        ax2.plot(capturedata_i_mstar_SG[0], capturedata_i_mstar_SG[1],'*',label='M Dwarf',
            markersize=12, markerfacecolor='darkorange', markeredgewidth=0.1, markeredgecolor='k')
        matplotlib.pyplot.annotate('$a_{0} = 10^{4}~R_g$', (0,5e2))
        matplotlib.pyplot.annotate('AGN lifetime', (150,3e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
        ax2.add_patch(lifetimei2)
        ax2.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, handletextpad=1,
        ncol=4, columnspacing=5.1, loc='center left', bbox_to_anchor=(-0.012,1.07))
        plt.yscale('log')
        ax2.set_xlabel('$i$ [$deg$]', fontsize=14)
        ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax2.set_xlim([-2,182])
        #    ax2.set_ylim([1e0,1e14])
        
    if (name in TQM) == True:
        fig=plt.figure(figsize=(6,3.6))
        plt.subplots_adjust(right=0.99, top=0.98, bottom=0.15)
        
        ax4=plt.subplot(111)    
        ax4.plot(ideg4_TQM,Tcaprgianti_TQM,'r:',lw=uplimw, label='Red Giant',c='crimson')
        ax4.plot(capturedata_i_rgiant_TQM[0],capturedata_i_rgiant_TQM[1],'*',label='Red Giant',
            markersize=12, markerfacecolor='crimson', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg4_TQM,Tcapostari_TQM,'r-.',lw=uplimw,label='O Star',c='royalblue')
        ax4.plot(capturedata_i_ostar_TQM[0], capturedata_i_ostar_TQM[1],'*',label='O Star',
            markersize=12, markerfacecolor='royalblue', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg4_TQM,Tcapgstari_TQM,'r--',lw=uplimw, label='G Star',c='gold')
        ax4.plot(capturedata_i_gstar_TQM[0], capturedata_i_gstar_TQM[1],'*',label='G Star',
            markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg4_TQM,Tcapmstari_TQM,'r-',lw=uplimw, label='M Dwarf',c='darkorange')
        ax4.plot(capturedata_i_mstar_TQM[0], capturedata_i_mstar_TQM[1],'*',label='M Dwarf',
            markersize=12, markerfacecolor='darkorange', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(capturedata_i_gstar_TQM[0], capturedata_i_gstar_TQM[1],'*',
        markersize=12, markerfacecolor='gold', markeredgewidth=0.1, markeredgecolor='k')
        #matplotlib.pyplot.annotate('$a_{0} = 10^{4}~R_g$', (0,1e5))
        matplotlib.pyplot.annotate('AGN lifetime', (73,3.5e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
        ax4.add_patch(lifetimei4)
        plt.yscale('log')
        ax4.set_xlabel('$i$ [$deg$]', fontsize=14)
        ax4.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax4.set_xlim([-2,182])
        #    ax4.set_ylim([1e0,1e14])
    
    plt.savefig('plots/capturetimeplots/stellar-Tcap_i_'+name+'.pdf')
    plt.savefig('plots/paperplots/stellar-Tcap_i_'+name+'.pdf')
#########################################################
    
#########################################################
def plot_Tcap_a_sBH(name): # (a,Tcap)
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-180,10**5]
    f=[-180,10**8]
    g=[180,(10**5)]
    h=[180,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimea1=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimea3=matplotlib.patches.Rectangle((0,10**5), widtha, heighta, angle=0.0, facecolor='lightgrey',alpha=0.5)
    
    if (name in SG) == True:
        fig=plt.figure(figsize=(6,4))
        plt.subplots_adjust(right=0.99, top=0.89, bottom=0.13)
    
        ax1=plt.subplot(111)
        ax1.plot(amrange_SG/Rg,Tcap05deg_SG,'r-',lw=uplimw,label='$5^{\circ}$',c='darkgreen')
        ax1.plot([capturedata_5_sBH_SG[0],capturedata_5_sBH_SG[1]],
        [capturedata_5_sBH_SG[2],capturedata_5_sBH_SG[2]],'r:', lw=delaw,c='k')
        ax1.plot(capturedata_5_sBH_SG[0],capturedata_5_sBH_SG[2],'*',label='$5^{\circ}$',
            markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
        ax1.plot(capturedata_5_sBH_SG[1],capturedata_5_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkgreen')
        ax1.plot(amrange_SG/Rg,Tcap15deg_SG,'r--',lw=uplimw,label='$15^{\circ}$',c='navy')
        ax1.plot([capturedata_15_sBH_SG[0],capturedata_15_sBH_SG[1]],
        [capturedata_15_sBH_SG[2],capturedata_15_sBH_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_15_sBH_SG[0],capturedata_15_sBH_SG[2],'*',label='$15^{\circ}$',
            markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
        ax1.plot(capturedata_15_sBH_SG[1],capturedata_15_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='navy')
        ax1.plot(amrange_SG/Rg,Tcap30deg_SG,'r-.',lw=uplimw,label='$30^{\circ}$',c='palevioletred')
        ax1.plot([capturedata_30_sBH_SG[0],capturedata_30_sBH_SG[1]],
        [capturedata_30_sBH_SG[2],capturedata_30_sBH_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_30_sBH_SG[0],capturedata_30_sBH_SG[2],'*',label='$30^{\circ}$',
            markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
        ax1.plot(capturedata_30_sBH_SG[1],capturedata_30_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='palevioletred')
        ax1.plot(amrange_SG/Rg,Tcap45deg_SG,'r:',lw=uplimw,label='$45^{\circ}$',c='darkmagenta')
        ax1.plot([capturedata_45_sBH_SG[0],capturedata_45_sBH_SG[1]],
        [capturedata_45_sBH_SG[2],capturedata_45_sBH_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_45_sBH_SG[0],capturedata_45_sBH_SG[2],'*',label='$45^{\circ}$',
            markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
        ax1.plot(capturedata_45_sBH_SG[1],capturedata_45_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkmagenta')
        ax1.plot(amrange_SG/Rg,Tcap60deg_SG,'r-',lw=uplimw,label='$60^{\circ}$',c='steelblue')
        ax1.plot([capturedata_60_sBH_SG[0],capturedata_60_sBH_SG[1]],
        [capturedata_60_sBH_SG[2],capturedata_60_sBH_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_60_sBH_SG[0],capturedata_60_sBH_SG[2],'*',label='$60^{\circ}$',
            markersize=12,markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
        ax1.plot(capturedata_60_sBH_SG[1],capturedata_60_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='steelblue')
        ax1.plot(amrange_SG/Rg,Tcap80deg_SG,'r-.',lw=uplimw,label='$80^{\circ}$',c='brown')
        ax1.plot([capturedata_80_sBH_SG[0],capturedata_80_sBH_SG[1]],
        [capturedata_80_sBH_SG[2],capturedata_80_sBH_SG[2]],'r:',lw=delaw,c='k')
        ax1.plot(capturedata_80_sBH_SG[0],capturedata_80_sBH_SG[2],'*',label='$80^{\circ}$',
            markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
        ax1.plot(capturedata_80_sBH_SG[1][0],capturedata_80_sBH_SG[2][0],'r:',lw=1,label='Δ a',c='k')
        ax1.plot(capturedata_80_sBH_SG[1],capturedata_80_sBH_SG[2],'*',label='$a_{cap}$',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='k')
        ax1.plot(capturedata_80_sBH_SG[1],capturedata_80_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=0.1, markeredgecolor='brown')
        
        ax1.plot(capturedata_45_sBH_SG[1],capturedata_45_sBH_SG[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkmagenta')
        
        matplotlib.pyplot.annotate('AGN lifetime', (1*10**6,1e7))
        ax1.add_patch(lifetimea1)
        ax1.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=2.8, handletextpad=0.4,
        ncol=7, columnspacing=1.95, loc='center left', bbox_to_anchor=(-0.012,1.07))
        plt.xscale('log')
        plt.yscale('log')
        ax1.set_xlabel('$a$ [$R_g$]', fontsize=14)
        ax1.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax1.set_xlim([3e0,3e7])
        #    ax1.set_ylim([1e2,1e14])
    if (name in TQM) == True:
        fig=plt.figure(figsize=(6,3.6))
        plt.subplots_adjust(right=0.99, top=0.99, bottom=0.15)
        
        ax3=plt.subplot(111)
        ax3.plot(amrange_TQM/Rg,Tcap05deg_TQM,'r-',lw=uplimw,label='$5^{\circ}$',c='darkgreen')
        ax3.plot([capturedata_5_sBH_TQM[0],capturedata_5_sBH_TQM[1]],
        [capturedata_5_sBH_TQM[2],capturedata_5_sBH_TQM[2]],'r:', lw=delaw,c='k')
        ax3.plot(capturedata_5_sBH_TQM[0],capturedata_5_sBH_TQM[2],'*',label='$5^{\circ}$',
            markersize=12, markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
        ax3.plot(capturedata_5_sBH_TQM[1],capturedata_5_sBH_TQM[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkgreen')
        ax3.plot(amrange_TQM/Rg,Tcap15deg_TQM,'r--',lw=uplimw,label='$15^{\circ}$',c='navy')
        ax3.plot([capturedata_15_sBH_TQM[0],capturedata_15_sBH_TQM[1]],
        [capturedata_15_sBH_TQM[2],capturedata_15_sBH_TQM[2]],'r:', lw=delaw,c='k')
        ax3.plot(capturedata_15_sBH_TQM[0],capturedata_15_sBH_TQM[2],'*',label='$15^{\circ}$',
            markersize=12, markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
        ax3.plot(capturedata_15_sBH_TQM[1],capturedata_15_sBH_TQM[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='navy')
        ax3.plot(amrange_TQM/Rg,Tcap30deg_TQM,'r-.',lw=uplimw,label='$30^{\circ}$',c='palevioletred')
        ax3.plot([capturedata_30_sBH_TQM[0],capturedata_30_sBH_TQM[1]],
        [capturedata_30_sBH_TQM[2],capturedata_30_sBH_TQM[2]],'r:', lw=delaw,c='k')
        ax3.plot(capturedata_30_sBH_TQM[0],capturedata_30_sBH_TQM[2],'*',label='$30^{\circ}$',
            markersize=12, markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
        ax3.plot(capturedata_30_sBH_TQM[1],capturedata_30_sBH_TQM[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='palevioletred')
        ax3.plot(amrange_TQM/Rg,Tcap45deg_TQM,'r:',lw=uplimw,label='$45^{\circ}$',c='darkmagenta')
        ax3.plot([capturedata_45_sBH_TQM[0],capturedata_45_sBH_TQM[1]],
        [capturedata_45_sBH_TQM[2],capturedata_45_sBH_TQM[2]],'r:', lw=delaw,c='k')
        ax3.plot(capturedata_45_sBH_TQM[0],capturedata_45_sBH_TQM[2],'*',label='$45^{\circ}$',
            markersize=12, markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
        ax3.plot(capturedata_45_sBH_TQM[1],capturedata_45_sBH_TQM[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='darkmagenta')
        ax3.plot(amrange_TQM/Rg,Tcap60deg_TQM,'r-',lw=uplimw,label='$60^{\circ}$',c='steelblue')
        ax3.plot([capturedata_60_sBH_TQM[0],capturedata_60_sBH_TQM[1]],
        [capturedata_60_sBH_TQM[2],capturedata_60_sBH_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_60_sBH_TQM[0],capturedata_60_sBH_TQM[2],'*',label='$60^{\circ}$',
            markersize=12, markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
        ax3.plot(capturedata_60_sBH_TQM[1],capturedata_60_sBH_TQM[2],'*',
            markersize=7,markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='steelblue')
        ax3.plot(amrange_TQM/Rg,Tcap80deg_TQM,'r-.',lw=uplimw,label='$80^{\circ}$',c='brown')
        ax3.plot([capturedata_80_sBH_TQM[0],capturedata_80_sBH_TQM[1]],
        [capturedata_80_sBH_TQM[2],capturedata_80_sBH_TQM[2]],'r:',lw=delaw,c='k')
        ax3.plot(capturedata_80_sBH_TQM[0],capturedata_80_sBH_TQM[2],'*',label='$80^{\circ}$',
            markersize=12, markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
        ax3.plot(capturedata_80_sBH_TQM[1][0],capturedata_80_sBH_TQM[2][0],'r:',lw=1,label='Δ a',c='k')
        ax3.plot(capturedata_80_sBH_TQM[1],capturedata_80_sBH_TQM[2],'*',label='$a_{cap}$',
            markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='k')
        ax3.plot(capturedata_80_sBH_TQM[1],capturedata_80_sBH_TQM[2],'*',
            markersize=7, markerfacecolor='k', markeredgewidth=acapw, markeredgecolor='brown')
        matplotlib.pyplot.annotate('AGN lifetime', (3*10**6,1e7))
        ax3.add_patch(lifetimea3)
        plt.xscale('log')
        plt.yscale('log')
        ax3.set_xlabel('$a$ [$R_g$]', fontsize=14)
        ax3.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax3.set_xlim([4e1,6e7])
        #    ax3.set_ylim([1e2,1e14])
    
    plt.savefig('plots/capturetimeplots/sBH-Tcap_a_'+name+'.pdf')
    plt.savefig('plots/paperplots/sBH-Tcap_a_'+name+'.pdf')
#########################################################
def plot_Tcap_i_sBH(name): # (i,Tcap) #(am,hint,density,name)
    uplimw=2.5
    delaw=0.75
    acapw=0.2
        
    a=[0,10**5]
    b=[0,10**8]
    c=[10**8,(10**5)]
    d=[10**8,(10**8)]
    widtha = c[0] - a[0]
    heighta = d[1] - a[1]
    e=[-180,10**5]
    f=[-180,10**8]
    g=[180,(10**5)]
    h=[180,(10**8)]
    widthi = g[0] - e[0]
    heighti = h[1] - e[1]
    lifetimei2=matplotlib.patches.Rectangle((-180,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    lifetimei4=matplotlib.patches.Rectangle((-180,10**5), widthi, heighti, angle=0.0, facecolor='lightgrey',alpha=0.5)
    
    if (name in SG) == True:
        fig=plt.figure(figsize=(6,4))
        plt.subplots_adjust(right=0.99, top=0.875, bottom=0.13)
        
        ax2=plt.subplot(111)
        ax2.plot(ideg2_SG,Tcap2Rg_SG,'r--',lw=uplimw,label='$10^{2}~R_g$',c='darkgreen')
        ax2.plot(capturedata_1e2_sBH_SG[0], capturedata_1e2_sBH_SG[1],'*',label='$10^{2}~R_g$', 
            markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg3_SG,Tcap3Rg_SG,'r-.',lw=uplimw,label='$10^{3}~R_g$',c='navy')
        ax2.plot(capturedata_1e3_sBH_SG[0], capturedata_1e3_sBH_SG[1],'*',label='$10^{3}~R_g$', 
            markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg4_SG,Tcap4Rg_SG,'r:',lw=uplimw,label='$10^{4}~R_g$',c='darkmagenta')
        ax2.plot(capturedata_1e4_sBH_SG[0], capturedata_1e4_sBH_SG[1],'*',label='$10^{4}~R_g$', 
            markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg5_SG,Tcap5Rg_SG,'r-',lw=uplimw,label='$10^{5}~R_g$',c='palevioletred')
        ax2.plot(capturedata_1e5_sBH_SG[0], capturedata_1e5_sBH_SG[1],'*',label='$10^{5}~R_g$', 
            markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg6_SG,Tcap6Rg_SG,'r--',lw=uplimw,label='$10^{6}~R_g$',c='brown')
        ax2.plot(capturedata_1e6_sBH_SG[0], capturedata_1e6_sBH_SG[1],'*',label='$10^{6}~R_g$', 
            markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(ideg7_SG,Tcap7Rg_SG,'r-.',lw=uplimw,label='$10^{7}~R_g$',c='steelblue')
        ax2.plot(capturedata_1e7_sBH_SG[0], capturedata_1e7_sBH_SG[1],'*',label='$10^{7}~R_g$', 
            markersize=12,markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
        matplotlib.pyplot.annotate('AGN lifetime', (73,1e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
    
        ax2.plot(capturedata_1e2_sBH_SG[0], capturedata_1e2_sBH_SG[1],'*',
            markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(capturedata_1e5_sBH_SG[0], capturedata_1e5_sBH_SG[1],'*',
            markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(capturedata_1e3_sBH_SG[0], capturedata_1e3_sBH_SG[1],'*',
            markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
        ax2.plot(capturedata_1e4_sBH_SG[0], capturedata_1e4_sBH_SG[1],'*',
            markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
        ax2.add_patch(lifetimei2)
        ax2.legend(fontsize=8, framealpha=1, edgecolor= 'k', handlelength=3.2, handletextpad=0.5,
        ncol=6, columnspacing=0.85, loc='center left', bbox_to_anchor=(-0.012,1.085))    
        plt.yscale('log')
        ax2.set_xlabel('$i$ [$deg$]', fontsize=14)
        ax2.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax2.set_xlim([-2,92])
        #    ax2.set_ylim([1e-1,1e14])
    
    if (name in TQM) == True:
        fig=plt.figure(figsize=(6,3.55))
        plt.subplots_adjust(right=0.99, top=0.99, bottom=0.15)
        
        ax4=plt.subplot(111)
        ax4.plot(ideg2_TQM,Tcap2Rg_TQM,'r--',lw=uplimw,label='$10^{2}~R_g$',c='darkgreen')
        ax4.plot(capturedata_1e2_sBH_TQM[0], capturedata_1e2_sBH_TQM[1],'*',label='$10^{2}~R_g$', 
            markersize=12,markerfacecolor='darkgreen', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg3_TQM,Tcap3Rg_TQM,'r-.',lw=uplimw,label='$10^{3}~R_g$',c='navy')
        ax4.plot(capturedata_1e3_sBH_TQM[0], capturedata_1e3_sBH_TQM[1],'*',label='$10^{3}~R_g$', 
            markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg4_TQM[1:],Tcap4Rg_TQM[1:],'r:',lw=uplimw,label='$10^{4}~R_g$',c='darkmagenta')
        ax4.plot(capturedata_1e4_sBH_TQM[0], capturedata_1e4_sBH_TQM[1],'*',label='$10^{4}~R_g$', 
            markersize=12,markerfacecolor='darkmagenta', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg5_TQM[1:],Tcap5Rg_TQM[1:],'r-',lw=uplimw,label='$10^{5}~R_g$',c='palevioletred')
        ax4.plot(capturedata_1e5_sBH_TQM[0], capturedata_1e5_sBH_TQM[1],'*',label='$10^{5}~R_g$', 
            markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg6_TQM,Tcap6Rg_TQM,'r--',lw=uplimw,label='$10^{6}~R_g$',c='brown')
        ax4.plot(capturedata_1e6_sBH_TQM[0], capturedata_1e6_sBH_TQM[1],'*',label='$10^{6}~R_g$', 
            markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(ideg7_TQM,Tcap7Rg_TQM,'r-.',lw=uplimw,label='$10^{7}~R_g$',c='steelblue')
        ax4.plot(capturedata_1e7_sBH_TQM[0], capturedata_1e7_sBH_TQM[1],'*',label='$10^{7}~R_g$', 
            markersize=12,markerfacecolor='steelblue', markeredgewidth=0.1, markeredgecolor='k')
    
        ax4.plot(capturedata_1e3_sBH_TQM[0], capturedata_1e3_sBH_TQM[1],'*', 
            markersize=12,markerfacecolor='navy', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(capturedata_1e6_sBH_TQM[0], capturedata_1e6_sBH_TQM[1],'*',
            markersize=12,markerfacecolor='brown', markeredgewidth=0.1, markeredgecolor='k')
        ax4.plot(capturedata_1e5_sBH_TQM[0], capturedata_1e5_sBH_TQM[1],'*',
            markersize=12,markerfacecolor='palevioletred', markeredgewidth=0.1, markeredgecolor='k')
        matplotlib.pyplot.annotate('AGN lifetime', (73,1e7)) # rad: (1.3,2*10**5)  deg: (73,2*10**5)
        ax4.add_patch(lifetimei4)
        plt.yscale('log')
        ax4.set_xlabel('$i$ [$deg$]', fontsize=14)
        ax4.set_ylabel('$T_{cap}$ [$yr$]', fontsize=14)
        ax4.set_xlim([-2,92])
        #    ax4.set_ylim([1e-1,1e14])
    
    plt.savefig('plots/capturetimeplots/sBH-Tcap_i_'+name+'.pdf')
    plt.savefig('plots/paperplots/sBH-Tcap_i_'+name+'.pdf')
#########################################################

#########################################################