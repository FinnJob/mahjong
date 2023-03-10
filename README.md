### mahjong

博弈论麻将作业，简单实现基于规则的麻将博弈算法，核心思想是关注手中的牌，尽量碰、杠、吃，尽量保留顺子，按优先级打出有利于和牌的手牌。

##### 使用方法

安装棋牌类强化学习工具平台rlcard（如果缺其他包自行安装即可）

```bash
pip3 install rlcard
```

具体使用方法见[rlcard官网](https://rlcard.org/)

##### 官网关于麻将游戏的表格说明

麻将牌一共有34种牌，每种牌一共四张，所以每一种牌可以拥有的牌数最多四张，麻将牌编码为一个34\*4的矩阵，然后将当前玩家手牌，当前桌面的牌，当前四个玩家的幅露，上述每一个都用一个34\*4的二维数组表示，然后将这6个二维数组组织成一个大的数组作为每个玩家的状态信息，即state，shape为[6, 34, 4]，第一维表示6个二维数组，所代表的意义如表1所示，第二维表示麻将有34种牌，编码id如表2所示，第三维表示每种牌有4张。上述算法只关注玩家手里的牌，将手里的牌尽可能打好，故只取state第一个34\*4的矩阵即可，同时需要用到state提供的合法出牌动作(legal actions)，合法动作id如表2所示。RLCard平台还封装好了洗牌发牌，判断碰，杠，吃，和牌、判断出牌次序等操作。

|  Plane   | Feature  |
|  :----:  | :----:  |
| 0  | 表示当前玩家的手牌 |
| 1  | 当前桌面上打出的牌 |
| 2-5  | 四个玩家的幅露（碰、杠、吃放在公共位置的牌） |
<center>表1</center>


|  Action ID   | Action  |
|  :----:  | :----:  |
| 0 ~ 8  | Bamboo-1 ~ Bamboo-9（1-9条） |
| 9 ~ 17  | Characters-1 ~ Character-9（1-9万） |
| 18 ~ 26  | Dots-1 ~ Dots-9（1-9筒） |
| 27  | Dragons-green（发财） |
| 28  | Dragons-red（红中） |
| 29  | Dragons-white（白板） |
| 30  | Winds-east（东风） |
| 31  | Winds-west（西风） |
| 32  | Winds-north（北风） |
| 33  | Winds-south（南风） |
| 34  | Pong（碰） |
| 35  | Chow（吃） |
| 36  | Gong（杠） |
| 37  | Stand（停牌，不碰，不杠） |
<center>表2</center>
	
	
	
	
	
	
	
	
	
	
	
	
	
