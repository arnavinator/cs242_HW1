import numpy as np
import matplotlib.pyplot as plt


if __name__=='__main__':
    
    #with open('output.txt', r) as file:
    #    content = file.read()

    N = np.array([2,4,8,16,32,64,128,256,512,1024,2048,4096,8192])
    inner_prod_times = np.array([ , , , 3506, 37320, 314281, 2997486, 29738131, 304454335, 3047277003, , , ])
    outer_prod_times = np.array([ , , , 1537, 8804, 60072, 542379, 3372533, 26729370, 235291168, , , ])
    
    plt.rcParams.update({'font.size':15})
    fig, ax = plt.subplots(1, figsize=(16.0,9.0))

    ax.plot(N, inner_prod_times*1e-3, '*-', label='inner product times')
    ax.plot(N, outer_prod_times*1e-3, '.-', label='outer product times')
    ax.set(xlabel='matrix size N', ylabel=r'execution time  $[\mu s]$', 
            title='MMM execution times vs matrix size')
    ax.set_xscale('log', basex=2)
    ax.set_yscale('log', basey=10)
    ax.grid()
    ax.legend()
    fig.savefig('time_vs_size.png', bbox_inches='tight')
    plt.show()
