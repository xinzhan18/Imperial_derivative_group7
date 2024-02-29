# Derivates





## Individual Writeups



## Basic Understanding

In this game, our core objective is to acquire the card with the highest probability of winning at the lowest cost possible. Given that the final payoff can only be either 1 (indicating a win) or 0 (indicating a loss), this represents the payoff of a call option. When users calculate win probabilities using the data at hand, they are essentially estimating a fair value based on personal information. However, the real fair value or risk-neutral value in the market should be a result that aggregates the information and expectations of all players. Therefore, while individual probability calculations provide a basis for trading decisions, the ultimate market price (or fair value) is influenced by the shared information and expectations of all market participants.

The basic probability formula is: 13−target disclosed number52−number of cards disclosed52−number of cards disclosed13−target disclosed number

Here, the disclosed number includes both public and private information.

Additionally, in this market, users can achieve significant gains through short selling. However, short selling also introduces considerable risk exposure. The most reasonable approach is to retain short positions for the first two contracts to end but maintain no short positions for the last two contracts, reducing the risk to zero.

###  

### Pricing Strategy

1. **Adjust Pricing**: Determine pricing based on the probability, calculated using both private and public information.
2. **Dynamic Adjustment of Trading Volume**: Monitor market trading volume and respond to abnormal trading activities. If unusual buying or selling behavior is detected, adjust your pricing strategy accordingly to protect yourself from potential market manipulation.



### Buying and Selling Strategy

1. **Exploiting Market Anomalies**: If a significant deviation is observed in the sum of all buying or selling prices from 1 in the market, this situation can be leveraged for arbitrage trading. If the market's buying price is less than 1, then all cards should be bought, where the expected profit in this scenario is greater than 0 (1 - buying price). If the market's selling price is greater than 1, short sell every card. The expected profit is (selling price - 1).
2. **Spread Arbitrage and Risk Management**: Identify opportunities for buying and selling by analyzing the difference between market prices and your calculated "fair price" in real-time. Pay attention to position management in the later stages of the game to avoid holding too many short positions.
3. **Early Closing Strategy**: Close positions in a timely manner, especially for short positions, to avoid last-minute risk exposure when the game is nearing its end and if you are not among the last two players.
4. **Profit from Short Selling**: On top of spread arbitrage, appropriately increase short exposure to the two suits with the lowest probabilities, expecting to gain above-average profits.



### Information strategy：

If the number of suits in hand is concentrated, it's strategic to disclose the suits with dispersed quantities first and delay the disclosure of suits with larger quantities until later.



### Position Management

1. **Endgame Strategy**: In the final stages of the game, especially when only two suits remain, closely monitor market dynamics and the behavior of the remaining players. If possible, maintain flexibility to quickly respond to market changes and adjust positions.
2. **Short Position Management**: After the game is narrowed down to the last two participants, ensure to close out short positions in the remaining two suits to zero. This guarantees no negative risk exposure.



## 基本认知



在这个游戏中，我们的核心目标是以最低的成本获取最高概率胜出的那张牌。考虑到最终的收益只有两种可能：要么是1（代表获胜），要么是0（代表失败）。所以这是一个看涨期权的payoff。当用户使用手中的数据计算胜率时，他们实际上是在尝试估计一个基于个人信息的公允价值。然而，市场上的真正公允价值或风险中性价值应该是集合了所有玩家信息和市场预期的结果。因此，虽然个人的概率计算为交易决策提供了基础，但最终的市场价格（或公允价值）会受到所有市场参与者共有信息和预期的影响。

基本的概率公式为： 13 - target 公布数量 / （52 - 已公布的数量）

其中公布数量包含了公共以及自己的私有信息。

同时在这个市场上，用户可以通过做空获得大量收益。但是做空同时带来了大量的风险暴露。最合理的方式是，对于最先结束的两个合约，可以保留做空仓位，但是对于最后两个合约，要保持没有空头仓位，将风险降低为0。



### 定价策略

1. **动态概率调整**：玩家应根据私有信息和公共信息来动态调整对每种花色被抽中的概率估计。
2. **交易量动态调整**：观察市场交易量，对异常的交易活动作出反应。如果发现异常买入或卖出行为，可以适当调整自己的报价策略，以保护自己免受潜在的市场操纵影响。



### 买卖策略

1. **市场异常行为的利用**：如果观察到市场上所有买入或卖出价格之和与1有显著偏差，可以利用这种情况进行套利交易。如果市场的买入价格小于1，则需要买入所有卡片，在这种情况下的期望收益是大于0(1- 买入价格)。如果市场的卖出价格大于1，每一个卡片进行同时做空。期望收益是(卖出价格-1)。
2. **价差套利与风险管理**：通过实时分析市场价格与自己计算的"fair price"之间的差异，寻找买入和卖出的机会。在游戏的后期，注意管理仓位，避免持有过多的空头仓位。
3. **提前平仓策略**：在游戏即将结束时，如果不在最后两位的玩家，应及时平仓，尤其是对于空头仓位，以避免最后的风险暴露。
4. 空头获利：在价差套利的基础上，适当增加对与概率最低的两个花色的空头暴漏，期望获得超额利润



### 信息策略：

1. 如果手中的花色数量比较集中，应该先公布数量比较分散的花色，较晚公布数量较多的花色。



### 仓位管理

1. **风险分散**：通过在不同花色上建立多仓和空仓，分散风险。注意不要过度集中在某一花色上，特别是在游戏的早期阶段。
2. **最终阶段的策略**：在游戏的最终阶段，特别是只剩下两种花色时，密切关注市场动态和剩余玩家的行为。如果可能，保持灵活性，以便快速响应市场变化并进行仓位调整。
3. 空头管理：当场上只剩两个人之后，需要将自己剩余两个人的空头仓位平为0.保证没有负的风险暴露。





## 策略回顾

![image-20240228213920775](D:\学校\Term2\Derivatives\coursework1\assets\image-20240228213920775.png)

紫线是基于信息计算出来的公允价值。

定价：基于公允价值，clubs早期定价偏低，后期定价回归合理范围。

信息策略：私有信息持有两个clubs，4个spades。基于信息策略，首先公布了两个clubs，保留了大量的spades最后公布。基于计算的公允价值，spades是一个被overprice的。所以为了获得超额利润，我们加大了空头暴漏。

diamonds是处于under price的状态，所以进行了持续购买。

对于hearts，其定价在公允价值附近，定价比较合理。

![image-20240228214441153](D:\学校\Term2\Derivatives\coursework1\assets\image-20240228214441153.png)

position management：

可以看出，对于spades空头持仓250手，同时在做空过程中，根据其概率波动，进行平仓。最终由于提前较早被展示，最终空头风险暴漏转为获利获得巨额利润。

在游戏中后期，对于hearts持有的空头仓位，逐渐进行了平仓。最终只剩两个花色，分别是diamonds和hearts。结合风险管理策略，两者没有持有任何空头头寸，保证了收益的同时，进行了合理的风险管理。









下面是盈利分析

| 方向     | 收益  |
| -------- | ----- |
| spades   | 65.42 |
| hearts   | 0.42  |
| diamonds | 9.24  |
| clubs    | 15.52 |
| 总收益   | 90.60 |
| bonus    | 103.6 |



收益来源分为几部分：空头暴露收益，价差收益，以及最终奖励。

其中主要的盈利

盈利主要来源于 spades的空头仓位的风险暴漏。因为持有较多的spade的私人信息，所以得到了更为精确的fair price。同时由于其获胜的概率比较低，以及一致处于over prices状态，因此加大了做空的仓位到达了200手。最终由于其较早的被揭露最后一张，获得了较大的收益(65.42)

价差收益主要来自于，通过对于低于fair price的产品进行买入，对高于fair price的价格进行卖出。同时注意风险管理，这一部分的收益很少，只有25.18 ( hearts:0.42,diamonds 9.24, clubs:15.52)。其中hearts的收益最少，说明其定价比较符合fair prices。

最终持有13手的diamonds，获得了13的payoff收益





反思：

如果市场定价合理，那么是没有办法可以获得较高的价差套利。同时价差套利获得收益比较稳定，无法获得较高的超额利润

如果想要获得较高的超额利润，需要加大风险暴漏，对于获胜概率最低的花色进行sell，最终才可以获利

仓位管理很重要，尤其是游戏的后半程，当只有两个玩家的时候，还持有空头仓位很容陷亏损的情况，因此要及时降低空头暴漏









定价策略

定价策略 根据手中已知的私有信息以及共有信息，依据概率调整定价策略

1. 基本准则 根据概率计算

2. 调整与市场价格进行匹配，如果市场上存在一样的公开信息，则调整到相应的价格范围

3. 如果存在有人疯狂的买入卖出，则根据交易量动态调整价格，但是在fair price上下进行变动

   

买卖策略

	1. 基础准则：如果市场上所有的买入价格小于1，则无脑买入所有的仓位。等权买入所有产品，直到市场回归正常
	1. 如果市场上所有卖出价格大于1，则无脑卖出所有的仓位，等权sell所有产品，直到市场回归正常。

核心策略逻辑：

低买高卖 进行价差套利 但是这样的操作收益并不客观

如果想要获取大量的利润，必须要对于相应产品进行sell

sell 会产生分析风险暴漏，所以如果到达最后只剩两个产品存在场上，那么场上仍然存在的产品 那么我们必须要进行平仓 使得持有的sell仓位为0

最后只剩两位在场上：

1. 如果自己不在场上：
   1. 对于自己的空头仓位进行平仓，保证没有负的风险暴露
   2. 同时依据期望，不断购买产品 保证持有



	1. 根据fair price 进行操作，如果相应的产品价格大于fair price则大量卖出产品，如果相应的产品价格低于fair price 则无脑买入产品

4. 如果出现价格异样



仓位管理

保证自己在最后两个人的时候，不要持有sell仓位





如果一个 



个人的策略是什么？

通过



定价策略：

1. 基于公布的卡片的概率来计算公允价值？

   如何计算fair price？

   几个guide line，例如 如果一个厂





购买策略：

1. 基本准则：如果市场中buy的price小于1，则无脑买入，如果sell的价格大于1，则无脑卖出
   1. 原因：如果市场上所有的buy价格小于1，这就意味着，我们的如果每一个都买一样的数量，最终一定会有一个花色是被选中，所以我们的成本是<1,最终的预期收益一定是E[X]  > 1，最终收益是E[X]>0
   2. 等权购买的情况并不存在。

1. 如果市场上存在两者是一致的信息（公开+非公开），如果有两者存在价格偏移 则说明卖定价高的， 买定价低的





首先存在两个内容

第一个内容是 是通过物理概率或者实际概率 来计算的期望收益 在这里等于由于最终的收益永远是1，所以期望收益直接等于是这张卡牌的概率



计算物理概率

计算风险中性概率



如果真实概率 小于 物理概率 则买入

如果 真实概率小于物理概率 则卖出







### 私有信息如何影响市场



下面是一个案例解释，私有信息是如何影响市场的。 在本次市场中，clubs market maker持有4个spades的私有信息，并且选择了在最后4轮才公布所有信息。其他的market  maker并没有持有任何spades的私有信息。因此我们分别计算了两条fair price曲线。第一个是基于市场上公开信息来计算的public fair prices，因为对于其他三个market maker 并没有人持有spades，所以他们的获取的信息是一致的都是灰色线 public infomation。而对于 club market marker，根据其持有的消息计算出来的private fair price.

通过这个图片可以看出，基于spades market maker的定价符合基于公开信息的定价。而对于拥有更多消息的clubes market maker来说，spades的定价是overprice的，所以可以通过不断做空其使其回归正常的价格范围。随着公开信息的不断增加，private fairprice 开始逐渐于public fair price一致，这说明私有信息再也无法影响市场了



![image-20240229023213329](D:\学校\Term2\Derivatives\coursework1\assets\image-20240229023213329.png)

另一个比较有意思的点是，由于私人信息的对于spades交易量的影响。由于其他的用户基于公开信息判断，spades的概率最高，所以疯狂的买入sapdes 进一步提高了spades的价格。而club market maker 发现价格的进一步升高，导致更被over prices，所以增加了空头的数量。我们可以从下图可以看到spades的交易量随着时间的变化。spades的库存从21轮前，库存波动变化非常激烈，说明市场存在激烈的交易，两者无法达成明确的共识。随着私有信息被逐渐公布，对于spades的概率认知逐渐趋于一致，可以看出21轮后，spades库存运作方向趋于一致，说明市场基本达成了形成了共识

![image-20240229030242131](D:\学校\Term2\Derivatives\coursework1\assets\image-20240229030242131.png)





### 价差会影响市场流动性



|        | 平均价差 | 交易量 | max_spread |
| ------ | -------- | ------ | ---------- |
| trade1 | 6.8788   | 1981   | 10         |
| trade2 | 3.312·   | 2525   | 4          |
|        |          |        |            |



价差影响了市场的流动性。我们进行了两次价差对比，发现价差越大，用户的交易量变得很低，而较低的价差可以更好的促进流动性。

因为如果价差过大，那么ask于bid之间的区间便会变得更宽，这就意味者更有可能击中fair price。而价差更小则促进了流动性

