import numpy as np
import matplotlib.pyplot as plt
import sys
from cycler import cycler 
from matplotlib import cm

H = 128
W = 256
O = 24
def alpha_5p3(K,I,S, H=H, W=W, O=O):
    P = (np.ceil((W-K)/S)+1)*(np.ceil((H-K)/S)+1)
    return 2*O*P*I*K**2 / (I*K**2*(O+P) + O*P)

if __name__=='__main__':
    
    #with open('output.txt', r) as file:
    #    content = file.read()

    N = np.array([2,4,8,16,32,64,128,256,512,1024,2048])
    inner_prod_times = np.array([253, 640, 1449, 3506, 37320, 314281, 2997486, 29738131, 304454335, 3047277003, 120637131254])
    outer_prod_times = np.array([325, 591, 1119, 1537, 8804, 60072, 542379, 3372533, 26729370, 235291168, 2829761328])
    
    plt.rcParams.update({'font.size':14})
    fig, ax = plt.subplots(1, figsize=(16.0,9.0))


    ax.plot(N, inner_prod_times*1e-3, '*-', label='inner product times')
    ax.plot(N, outer_prod_times*1e-3, '.-', label='outer product times')
    ax.set(xlabel='matrix size N', ylabel=r'execution time  $[\mu s]$', 
            title='MMM execution times vs matrix size')
    ax.set_xscale('log', basex=2)
    ax.set_yscale('log', basey=10)
    ax.grid()
    ax.legend()
    
    ############################
    fig2, ax2 = plt.subplots(4,4, figsize=(16,9), sharey=True)
    fig2.suptitle(r'$\alpha$ vs K,I,S with H={:d}, W={:d}, O={:d}'.format(H,W,O))
    cmap = cm.get_cmap('viridis')

    I = 256
    S = 1
    new_cycler = cycler(color=cmap(np.linspace(0,1, 8)))
    for idx, s in enumerate(np.linspace(1,64,16, dtype=int)):
        row = idx//4
        col = idx%4
        ax2[row,col].set_prop_cycle(new_cycler)
        for i in np.linspace(1,I,8, dtype=int):
            max_K = int(min(H,W)*7/8)
            K = np.linspace(1, max_K, max_K, dtype=int)
            ax2[row,col].plot(K, alpha_5p3(K,i,s), '.-', label='I={:d}'.format(i) )
            
        if row==3:
            ax2[row,col].set_xlabel('K')
        if col==0:
            ax2[row,col].set_ylabel(r'$\alpha$')
        x = max(ax2[row,col].get_xlim())*0.8
        y = max(ax2[row,col].get_ylim())*0.8
        ax2[row,col].text(x,y,'S={:d}'.format(s),fontsize=14) 
        ax2[row,col].grid()

    handles, labels = ax2[row,col].get_legend_handles_labels() 
    fig2.legend(handles, labels, fontsize=14)
    
    if(len(sys.argv)>=2):
        if(sys.argv[1]=='save1'):
            print('Saving time_vs_size.png ...')
            fig.savefig('../figures/time_vs_size.png', bbox_inches='tight')
            print('done.')
        if(sys.argv[1]=='save2'):
            print('Saving alpha.png ...')
            fig2.savefig('../figures/alpha.png', bbox_inches='tight')
            print('done.')

    plt.show()
