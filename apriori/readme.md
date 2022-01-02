1. 数据处理

   import pandas as pd
   all_data=pd.read_csv("final_all_data.csv")
   del all_data['Unnamed: 0']
   all_data.head()
   all_data.to_csv("final.csv",encoding='utf_8_sig')

   import numpy as np
   from pandas import Series
   all_data=pd.read_csv("final.csv")
   del all_data['Unnamed: 0']
   all_data.index=Series(np.arange(all_data.shape[0])).index
   all_data.head()
   all_data.to_csv("final.csv",encoding='utf_8_sig')

   import pandas as pd
   import numpy as np
   from pandas import Series
   all_data=pd.read_csv("final.csv")
   all_data.head()
   from efficient_apriori import apriori
   drop_same=all_data.drop_duplicates(['用户的id'])
   print(drop_same.head())
   sign=[i for i in drop_same['用户的签名（0,1）']]
   for i in range(len(sign)):
       if sign[i]==1:
           sign[i]="有签名"
       else:
           sign[i]="无签名"
   medal=[i for i in drop_same['有没有佩戴粉丝牌']]
   for i in range(len(medal)):
       if medal[i]==1:
           medal[i]="有佩戴粉丝牌"
       else:
           medal[i]="没佩戴粉丝牌"    
   # medal
   vip=[i for i in drop_same['vip']]
   for i in range(len(vip)):
       if vip[i]==1:
           vip[i]="是会员"
       else:
           vip[i]="不是会员" 
   # vip
   level=[i for i in drop_same['用户的等级']]
   for i in range(len(level)):
       if level[i]==-8.573938131:
           level[i]="等级是1"
       elif level[i]==-5.437075136:
           level[i]="等级是2"
       elif level[i]==-3.868643638:
           level[i]="等级是3"
       elif level[i]==-2.300212141:
           level[i]="等级是4"
       elif level[i]==-0.731780643:
           level[i]="等级是5"
       else :
           level[i]="等级是6"

   sex=[i for i in drop_same['男']]
   for i in range(len(sex)):
       if sex[i]==1:
           sex[i]="男"
       else:
           sex[i]="性别保密"
   print(sex)
   sex0=[i for i in drop_same['女']]
   for i in range(len(sex0)):
       if sex0[i]==1:
           sex[i]="女"
       elif sex[i]=="男":
           pass
       else:
           sex[i]="性别保密"   

2. 算法测试

   ![image-20220102213810905](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20220102213810905.png)

3. 调参方法
   ![image-20220102213849587](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20220102213849587.png)

4. 输出多个结果
   ![image-20220102214012450](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20220102214012450.png)

5. 三维图展示
   ![image-20220102214154768](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20220102214154768.png)
   