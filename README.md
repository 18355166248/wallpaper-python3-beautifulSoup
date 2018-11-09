# 用scrapy爬取中关村壁纸

## 用到的模块看代码找

### 用pycharm运行begin.py即可

#### 爬取的保存地址 在pipelines.py里面修改

#### 遇到的坑
- beautifulSoup获取不到id元素,最后不得不用xpath获取
- 保存图片的时候报错, 是ssl安全验证问题, 通过下列代码解决

```
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```
- mac和window不一样 转移到window  OSx文件夹不能删除, 可能会出问题
- 多次回调 Request 不能回调 需要添加 dont_filter=True 让scrapy不要过滤掉 因为名字过于相似,scrapy会将请求过滤掉
```
    yield Request('http://desk.zol.com.cn%s'%url2, dont_filter=True, callback=self.getImgUrl)
```