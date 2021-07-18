#! /usr/bin/env python
# -*- coding:utf-8 -*-


# port = 'https://www.wmxz.wang/video.php?url='
resolve_address = [
{"name":"线路一", "url":"https://www.h8jx.com/jiexi.php?url="},
{"name":"线路二", "url":"https://z1.m1907.cn/?jx="},
{"name":"线路三", "url":"https://api.tv920.com/jx/?url="},
{"name":"线路四", "url":"https://api.bingdou.net/?url="},
{"name":"线路五", "url":"https://jsap.attakids.com/?url="},
{"name":"线路六", "url":"https://jx.m3u8.tv/jiexi/?url="},
{"name":"线路七", "url":"https://www.41478.net/?url="},
{"name":"线路八", "url":"https://jx.yparse.com/index.php?url="},
{"name":"线路九", "url":"https://jiexi.q-q.wang/?url="},
{"name":"线路十", "url":"https://jx.youyitv.com/?url="},
# --------------------------------------------------------------------------------------
{"name":"B站解析一", "url":"https://api.tv920.com/vip/?url="},
{"name":"B站解析二", "url":"https://jx.116kan.com/?url="},
{"name":"B站解析三", "url":"https://jiexi.380k.com/?url="},
{"name":"B站解析四", "url":"https://jx.yparse.com/index.php?url="},
{"name":"B站解析六", "url":"https://www.cuan.la/m3u8.php?url="},
{"name":"B站解析七", "url":"https://jx.973973.xyz/?url="},
{"name":"B站解析八", "url":"https://jx.popo520.cn/jiexi/?url="},
{"name":"B站解析九", "url":"https://vip.parwix.com:4433/player/?url="},
{"name":"B站解析十", "url":"https://www.ckplayer.vip/jiexi/?url="},
{"name":"B站解析11", "url":"https://api.10dy.net/?url="},
{"name":"B站解析12 ", "url":"https://www.8090g.cn/?url="},
{"name":"B站解析13", "url":"https://vip.ikjiexi.top/?url="},
{"name":"B站解析14", "url":"https://www.h8jx.com/jiexi.php?url="},
# --------------------------------------------------------------------------------------
{"name":"B站弹窗", "url":"http://jx.rdhk.net/?v="},
{"name":"B站弹窗", "url":"http://api.myzch.cn/?url="},
{"name":"1907", "url":"https://z1.m1907.cn/?jx="},
{"name":"52", "url":"https://vip.52jiexi.top/?url="},
{"name":"17云", "url":"https://www.1717yun.com/jx/ty.php?url="},
{"name":"618G", "url":"https://jx.618g.com/?url="},
{"name":"明日", "url":"https://jx.yingxiangbao.cn/vip.php?url="},
{"name":"千叶", "url":"https://yi29f.cn/vip.php?url="},
{"name":"思古", "url":"https://jx.quanmingjiexi.com/?url="},
{"name":"大幕", "url":"https://jx.52damu.com/dmjx/jiexi.php?url="},

{"name":"纯净线路1", "url":"https://z1.m1907.cn/?jx="},
{"name":"纯净线路2", "url":"https://jx.618g.com/?url="},
{"name":"B站", "url":"https://vip.parwix.com:4433/player/?url="},
{"name":"B站2", "url":"https://jx.yingxiangbao.cn/vip.php?url="},
{"name":"B站3", "url":"https://vip.52jiexi.top/?url="},
{"name":"B站4", "url":"https://jx.yparse.com/index.php?url="},
{"name":"B站5", "url":"https://jx.116kan.com/?url="},
{"name":"B站7", "url":"https://www.cuan.la/m3u8.php?url="},
{"name":"bl解析", "url":"https://vip.bljiex.com/?v="},
{"name":"冰豆", "url":"https://api.bingdou.net/?url="},
{"name":"八八", "url":"https://jiexi.q-q.wang/?url="},
{"name":"爸比云", "url":"https://jx.1ff1.cn/?url="},
{"name":"百域", "url":"https://jx.618g.com/?url="},
{"name":"clouse6", "url":"http://jx.clousx6.cn/player/?url="},
{"name":"ckmov", "url":"https://www.ckmov.vip/api.php?url="},
{"name":"初心", "url":"http://jx.bwcxy.com/?v="},
{"name":"大幕", "url":"https://jx.52damu.com/dmjx/jiexi.php?url="},
{"name":"二度", "url":"https://jx.du2.cc/?url="},
{"name":"凡凡", "url":"https://jx.wslmf.com/?url="},
{"name":"福星", "url":"https://jx.popo520.cn/jiexi/?url="},
{"name":"跟剧", "url":"https://www.5igen.com/dmplayer/player/?url="},
{"name":"ha12", "url":"https://py.ha12.xyz/sos/index.php?url="},
{"name":"Hk", "url":"https://jx.rdhk.net/?v="},
{"name":"H8", "url":"https://www.h8jx.com/jiexi.php?url="},
{"name":"豪华啦", "url":"https://api.lhh.la/vip/?url="},
{"name":"黑米", "url":"https://www.myxin.top/jx/api/?url="},
{"name":"黑云", "url":"https://jiexi.380k.com/?url="},
{"name":"蝴蝶", "url":"https://api.hdworking.top/?url="},
{"name":"IDC", "url":"https://jx.idc126.net/jx/?url="},
{"name":"IK解析", "url":"https://vip.ikjiexi.top/?url="},
{"name":"金桥", "url":"https://jqaaa.com/jx.php?url="},
{"name":"解析S", "url":"https://jx.jiexis.com/?url="},
{"name":"久播(明日)", "url":"https://jx.jiubojx.com/vip.php?url="},
{"name":"九八看", "url":"https://jx.youyitv.com/?url="},
{"name":"凉城", "url":"https://jx.mw0.cc/?url="},
{"name":"蓝影", "url":"http://huiwanka.xyz/jx/?url="},
{"name":"流氓凡", "url":"https://jx.wslmf.com/?url="},
{"name":"m3u8", "url":"https://jx.m3u8.tv/jiexi/?url="},
{"name":"m3u8tv", "url":"https://jiexi.janan.net/jiexi/?url="},
{"name":"Mao", "url":"https://titan.mgtv.com.kunlanys.com/m3u8.php?url="},
{"name":"磨菇", "url":"https://jx.wzslw.cn/?url="},
{"name":"诺诺", "url":"https://www.ckmov.com/?url="},
{"name":"诺讯", "url":"https://www.nxflv.com/?url="},
{"name":"OK", "url":"https://okjx.cc/?url="},
{"name":"千忆", "url":"https://v.qianyicp.com/v.php?url="},
{"name":"穷二代", "url":"https://jx.ejiafarm.com/dy.php?url="},
{"name":"千叶", "url":"https://yi29f.cn/vip.php?url="},
{"name":"思云", "url":"https://jx.ap2p.cn/?url="},
{"name":"思古", "url":"https://api.sigujx.com/?url="},
{"name":"思古2", "url":"https://api.bbbbbb.me/jx/?url="},
{"name":"思古3", "url":"https://jsap.attakids.com/?url="},
{"name":"宿命", "url":"https://api.sumingys.com/index.php?url="},
{"name":"时光", "url":"http://timeys.maosp.me/jx/?url="},
{"name":"石云", "url":"https://jiexi.071811.cc/jx.php?url="},
{"name":"tv920", "url":"https://api.tv920.com/vip/?url="},
{"name":"通用", "url":"https://jx.598110.com/index.php?url="},
{"name":"维多", "url":"https://jx.ivito.cn/?url="},
{"name":"无名", "url":"https://www.administratorw.com/video.php?url="},
{"name":"xx", "url":"https://chkkk.top/jiexi/ys?url="},
{"name":"小蒋极致", "url":"https://www.kpezp.cn/jlexi.php?url="},
{"name":"小狼", "url":"https://jx.yaohuaxuan.com/?url="},
{"name":"新线路", "url":"https://vip.kurumit3.top/?v="},
{"name":"新线路2", "url":"https://jx.hnhsn.com/api/?url="},
{"name":"星驰", "url":"https://vip.cjys.top/?url="},
{"name":"星空", "url":"http://60jx.com/?url="},
{"name":"要搜", "url":"https://www.yaosou.cc/jiexi/?v="},
{"name":"云端", "url":"https://jx.ergan.top/?url="},
{"name":"用心", "url":"https://yi29f.cn/vip.php?url="},
{"name":"一起走吧", "url":"http://jiexi.yiqizouba.top/?url="},
{"name":"8B", "url":"https://api.8bjx.cn/?url="},
{"name":"17云", "url":"https://www.1717yun.com/jx/ty.php?url="},
{"name":"33t", "url":"https://www.33tn.cn/?url="},
{"name":"41", "url":"https://jx.f41.cc/?url="},
{"name":"69", "url":"https://api.69ne.com/?url="},
{"name":"89", "url":"https://www.ka61b.cn/jx.php?url="},
{"name":"180", "url":"https://jx.000180.top/jx/?url="},
{"name":"200", "url":"https://vip.66parse.club/?url="},
{"name":"517", "url":"https://cn.bjbanshan.cn/jx.php?url="},
{"name":"973", "url":"https://jx.973973.xyz/?url="},
{"name":"8090", "url":"https://www.8090g.cn/?url="}
]
resolve_address_information = []
for i in range(len(resolve_address)):
    resolve_address_information += ['%s %s' % (resolve_address[i]["name"], resolve_address[i]["url"] )]
# print(resolve_address_information)

'''https://www.wmxz.wang/video.php?url=
http://jx.618g.com/?url=
http://api.baiyug.vip/index.PHP?url=
https://z1.m1907.cn/?jx=
https://jx.618g.com/?url=
https://www.1717yun.com/jx/ty.php?url=
https://cdn.yangju.vip/k/?url=
https://api.sigujx.com/?url=
https://vip.jaoyun.com/index.php?url=
https://jx.618g.com/?url=
https://api.bbbbbb.me/jx/?url=
https://www.myxin.top/jx/api/?url=
https://jiexi.071811.cc/jx.php?url=
https://jx.wslmf.com/?url=
https://jx.dy-jx.com/?url=
https://vip.mpos.ren/v/?url=
https://jqaaa.com/jx.php?url=
https://jx.598110.com/index.php?url=
https://jx.bwcxy.com/?v=
https://jx.rdhk.net/?v=
https://jx.fo97.cn/?url=
https://www.kpezp.cn/jlexi.php?url=
https://jx.ivito.cn/?url=
https://api.927jx.com/vip/?url=
https://api.tv920.com/vip/?url=
https://www.ka61b.cn/jx.php?url=
https://api.lhh.la/vip/?url=
https://api.sumingys.com/index.php?url=
https://api.8bjx.cn/?url=
https://v.qianyicp.com/v.php?url=
https://mcncn.cn/?url=
https://jx.f41.cc/?url=
https://www.ckmov.vip/api.php?url=
https://cn.bjbanshan.cn/jx.php?url=
https://jx.mw0.cc/?url=
https://www.33tn.cn/?url=
https://jx.1ff1.cn/?url=
https://jx.000180.top/jx/?url=
https://py.ha12.xyz/sos/index.php?url=
https://www.administratorw.com/video.php?url=
https://jq.qq.com/?_wv=1027&k=5MnmeT8
https://jiexi.380k.com/?url=
https://jx.wslmf.com/?url=
https://okjx.cc/?url=
http://jx.ejiafarm.com/dy.php?url='''

import tkinter.messagebox as msgbox
from urllib import parse
import tkinter as tk
from tkinter import ttk  # 导入ttk模块，因为下拉菜单控件在ttk中
import webbrowser
import re  # 正则表达式

# 定义一个类
class APP:
    def __init__(self, width=500, hight=300):  # 穿花衣
        self.w = width
        self.h = hight
        self.title = "vip视频解析V0.0.2  Ctrl+V粘贴  QQ:3434623263"
        # self.root = tk.Tk(className=self.title)
        self.root = tk.Tk()
        self.root.title(self.title)
        # self.root.resizable(0,0)# 禁止调节窗口大小
        # 地址变量
        self.url = tk.StringVar()
        # 小型框架(小组件)
        frame_1 = tk.Frame(self.root)
        label_1 = tk.Label(frame_1, text='视频地址:')
        entry = tk.Entry(frame_1, textvariable=self.url, width=45)
        paste_button = tk.Button(frame_1, text='粘贴', width=4, heigh=1, command=self.paste)
        play_1 = tk.Button(frame_1, text='播放1', width=5, heigh=1, command=lambda : self.video_play(True))
        frame_1.pack()
        # 小组件关系如何控制？
        label_1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        paste_button.grid(row=0, column=2)
        play_1.grid(
            row=0, column=3, 
            # ipadx=12, ipady=12  # x、y轴扩大12倍
            )
        
        
        frame_2 = tk.Frame(self.root)
        label_2 = tk.Label(frame_2, text='解析地址:')
        self.choose_port = ttk.Combobox(frame_2, width=48)
        # 设置下拉菜单中的值
        # self.choose_port['value'] = tuple(resolve_address.split('\n'))
        self.choose_port['value'] = resolve_address_information
        # 设置默认值，即默认下拉框中的内容
        self.choose_port.current(0)
        
        play_2 = tk.Button(frame_2, text='播放2', width=5, heigh=1, command=lambda : self.video_play(False))  # font=('楷体', 10),
        frame_2.pack()
        label_2.grid(row=0, column=0)
        self.choose_port.grid(row=0, column=1)
        play_2.grid(
            row=0, column=2, 
            # ipadx=12, ipady=12  # x、y轴扩大12倍
            )
    
    def paste(self):
        try:
            self.url.set(self.root.clipboard_get())
        except:
            msgbox.showerror(title='警告错误', message='获取剪贴板内容失败！')
    
    def video_play(self, quote):  # 核心
        # port = 'http://www.wmxz.wang/video.php?url='
        port = self.choose_port.get().split(' ')[-1]
        # 怎么获取？
        # 拦截
        # https://v.qq.com/x/cover/68otu5em7wil239.html
        regx = '^https?:/{2}\w.+$'  # 重点
        ips = self.url.get()
        if re.match(regx, ips):
            if quote:
                # 包装
                ip = parse.quote_plus(ips)
            else:
                ip = ips
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='警告错误', message='视频地址无效，请重新输入！')
    
    def loop(self):
        self.root.resizable(True, True)
        self.root.mainloop()
        


if __name__ == '__main__':
    app = APP()
    app.loop()
    pass
