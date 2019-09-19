import os

from .ydm_client import YDMHttp

def ydm_api(filename):
    username = 'l19930417'

    # 密码
    password = 'l19930417'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 8974

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '13319b3ac68cc944c498c0abb6f1549e'

    # 图片文件
    # filename = 'code.png'

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 1004

    # 超时时间，秒
    timeout = 60

    # 初始化
    yundama = YDMHttp(username, password, appid, appkey)

    # 登陆云打码
    uid = yundama.login();
    # print('uid: %s' % uid)

    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(filename, codetype, timeout);
    # print('cid: %s, result: %s' % (cid, result))

    #删除验证码图片文件
    # os.remove(filename)

    return result


