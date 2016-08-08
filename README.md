# HeuristicAlgorithm
Some useful heuristic algorithm

## GA
运算流程

1. 
2.
3.



## FOA

运算流程

1. 随机生成versionsize个种群中心
2. 每个种群中心进行smellsize次嗅觉搜索，搜索方法采用mutation突变方法
3. evaluate
4. 每个种群当中选择evaluation最高的那个解，然后将这个解作为新的种群中心。
5. 重复操作步骤3,4直到达到设置的代数。

注：这种为原始的FOA，忽略了种群之间的信息交流。