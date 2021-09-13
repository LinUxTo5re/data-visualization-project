# coding: utf-8
plt.plot(x,y,'x--r',lw=1,ms=10,mfc='g',mec='k',mew=2,fillstyle='left',label='cross_data')

plt.title('Normal plot',fontdict={'fontsize':20,'color':'green','verticalalignment':'center'},loc='center')

plt.xlabel('x-label',fontdict={'fontsize':14,'color':'k','verticalalignment':'top'},loc='center',labelpad=10)

plt.ylabel('y-label',fontdict={'fontsize':14,'color':'black','horizontalalignment':'right',},loc='center',labelpad=5)

x_t=x[1]+5
y_t=np.max(y)
s='high-A'

plt.text(x=x_t,y=y_t,s=s,fontdict={'fontsize':15,'verticalalignment':'bottom','horizontalalignment':'right'},backgroundcolor='yellow',color='black',fontstyle='italic',rotation=45,
        visible=True,weight='bold')
