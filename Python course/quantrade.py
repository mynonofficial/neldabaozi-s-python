enable_profile()

from kuanke.user_space_api import *
from jqlib.technical_analysis import *

def initialize(context):
    g.stocksnum = 5 # 持有最小市值股票数
    g.period = 10 # 轮动频率
    g.days = 1 # 记录策略进行到第几天，初始为1

    log.set_level("order", "error")
    run_daily(daily,time='every_bar')# 周期循环daily
    run_daily(mktopen, time = "every_bar")
    g.holdpct = 1

def mktopen(context):
    stop (context)

def daily(context):
    if g.days % g.period == 1:
        buylist = pick(context)
        g.holdpct = mkt_index(context)
        trade(context, buylist)
    else:
        pass
    g.days = g.days + 1

def mkt_index(context):
    #获取大盘指数
    mktindex = history(count = 1, field = "close", security_list = ["000300.XSHG"])
    print "first\n%s" % mktindex
    mktindex = mktindex.ix[-1, "000300.XSHG"]
    print "second\n%s" % mktindex
    #获取大盘指数20日均值
    date = context.current_dt.strftime("%Y-%m-%d")
    ma20 = MA(["000300.XSHG"], check_date = date, timeperiod = 20)
    print "first\n%s" % ma20
    ma20 = ma20["000300.XSHG"]
    print "second\n%s" % ma20
    #判断大盘状况并返回信号
    if mktindex > ma20:
        return 1
    else:
        return 0.5

def pick(context):
    date=context.current_dt.strftime("%Y-%m-%d")

    scu = get_industry_stocks("HY007") + get_industry_stocks("801180") + get_concept_stocks("399106")
    # 选出在scu内的股票的股票代码，并按照当前时间市值从小到大排序
    df = get_fundamentals(query(
            valuation.code,valuation.market_cap
        ).filter(
            valuation.code.in_(scu)
        ).order_by(
            valuation.market_cap.asc()
        ), date=date
        )
    # 取出前g.stocksnum名的股票代码，并转成list类型，buylist为选中的股票
    buylist = list(df['code'][:g.stocksnum])
    return buylist

        # 对于每个当下持有的股票进行判断：现在是否已经不在buylist里，如果是则卖出
def trade(context, buylist):
    for stock in context.portfolio.positions:
        if stock not in buylist: #如果stock不在buylist
            order_target(stock, 0) #调整stock的持仓为0，即卖出
    # 将资金分成g.stocksnum份
    position_per_stk = context.portfolio.total_value * g.holdpct/g.stocksnum
    # 用position_per_stk大小的g.stocksnum份资金去买buylist中的股票
    for stock in buylist:
        order_value(stock, position_per_stk)

def stop(context):
    for stock in context.portfolio.positions:
        if context.portfolio.positions[stock].price < 0.8 * context.portfolio.positions[stock].avg_cost :
            order_target(stock, 0)
            print "\n%s stop loss" % stock
        else:
            pass
